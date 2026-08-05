#!/usr/bin/env python3
# enum4linux - Windows enumeration tool for Linux (Python version)
# Copyright (C) 2011  Mark Lowe (Original Perl version)
# Python conversion based on enum4linux v0.9.1
# 
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool.  The author accepts no liability
# for damage caused by this tool.  If these terms are not acceptable to you, then
# you are not permitted to use this tool.
#
# In all other respects the GPL version 2 applies:
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# You are encouraged to send comments, improvements or suggestions to
# me at mrl@portcullis-security.com
#
# TODO
#
# * Search RID space intelligently.  Samba starts accounts at 0, but
#   Windows starts at 500.  We don't want to search 0-500 on all
#   hosts.  Maybe check 0-10 and abort if nothing is found.  Some SIDs
#   on samba servers start RIDs much higher (3000+).  How do we make
#   sure we get all these.
#
# * Multiple SIDs can be found on some hosts (samba).  
#
# * Output Group Memberships in a more parsable format.
#

import subprocess
import sys
import re
import os
import argparse
import random
import string
from typing import Dict, List, Tuple, Optional, Any

VERSION = "0.9.1"

# Global variables
verbose = False
debug = False
aggressive = False
global_fail_limit = 1000      # no command line option yet
global_search_until_fail = False  # no command line option yet
heighest_rid = 999999
global_workgroup = ''
global_username = ''
global_password = ''
global_dictionary = False
global_filename = ''
global_share_file = ''
global_detailed = False
global_passpol = False
global_rid_range = "500-550,1000-1050"
global_known_username_string = "administrator,guest,krbtgt,domain admins,root,bin,none"
dependent_programs = ['nmblookup', 'net', 'rpcclient', 'smbclient']
optional_dependent_programs = ['polenum', 'ldapsearch']
odp_present = {}  # dict to track which optional programs are present
null_session_test = False

###############################################################################
# The following mappings for nmblookup (nbtstat) status codes to human readable
# format is taken from nbtscan 1.5.1 "statusq.c".  This file in turn
# was derived from the Samba package which contains the following
# license:
#    Unix SMB/Netbios implementation
#    Version 1.9
#    Main SMB server routine
#    Copyright (C) Andrew Tridgell 1992-199
# 
#    This program is free software; you can redistribute it and/or modif
#    it under the terms of the GNU General Public License as published b
#    the Free Software Foundation; either version 2 of the License, o
#    (at your option) any later version
# 
#    This program is distributed in the hope that it will be useful
#    but WITHOUT ANY WARRANTY; without even the implied warranty o
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See th
#    GNU General Public License for more details
# 
#    You should have received a copy of the GNU General Public Licens
#    along with this program; if not, write to the Free Softwar
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA

nbt_info = [
    ("__MSBROWSE__", "01", 0, "Master Browser"),
    ("INet~Services", "1C", 0, "IIS"),
    ("IS~", "00", 1, "IIS"),
    ("", "00", 1, "Workstation Service"),
    ("", "01", 1, "Messenger Service"),
    ("", "03", 1, "Messenger Service"),
    ("", "06", 1, "RAS Server Service"),
    ("", "1F", 1, "NetDDE Service"),
    ("", "20", 1, "File Server Service"),
    ("", "21", 1, "RAS Client Service"),
    ("", "22", 1, "Microsoft Exchange Interchange(MSMail Connector)"),
    ("", "23", 1, "Microsoft Exchange Store"),
    ("", "24", 1, "Microsoft Exchange Directory"),
    ("", "30", 1, "Modem Sharing Server Service"),
    ("", "31", 1, "Modem Sharing Client Service"),
    ("", "43", 1, "SMS Clients Remote Control"),
    ("", "44", 1, "SMS Administrators Remote Control Tool"),
    ("", "45", 1, "SMS Clients Remote Chat"),
    ("", "46", 1, "SMS Clients Remote Transfer"),
    ("", "4C", 1, "DEC Pathworks TCPIP service on Windows NT"),
    ("", "52", 1, "DEC Pathworks TCPIP service on Windows NT"),
    ("", "87", 1, "Microsoft Exchange MTA"),
    ("", "6A", 1, "Microsoft Exchange IMC"),
    ("", "BE", 1, "Network Monitor Agent"),
    ("", "BF", 1, "Network Monitor Application"),
    ("", "03", 1, "Messenger Service"),
    ("", "00", 0, "Domain/Workgroup Name"),
    ("", "1B", 1, "Domain Master Browser"),
    ("", "1C", 0, "Domain Controllers"),
    ("", "1D", 1, "Master Browser"),
    ("", "1E", 0, "Browser Service Elections"),
    ("", "2B", 1, "Lotus Notes Server Service"),
    ("IRISMULTICAST", "2F", 0, "Lotus Notes"),
    ("IRISNAMESERVER", "33", 0, "Lotus Notes"),
    ('Forte_$ND800ZA', "20", 1, "DCA IrmaLan Gateway Server Service")
]
####################### end of nbtscan-derrived code ############################


def get_usage():
    return f"""enum4linux v{VERSION} (http://labs.portcullis.co.uk/application/enum4linux/)
Copyright (C) 2011 Mark Lowe (mrl@portcullis-security.com)

Simple wrapper around the tools in the samba package to provide similar 
functionality to enum.exe (formerly from www.bindview.com).  Some additional 
features such as RID cycling have also been added for convenience.

Usage: {sys.argv[0]} [options] ip

Options are (like "enum"):
    -U        get userlist
    -M        get machine list*
    -S        get sharelist
    -P        get password policy information
    -G        get group and member list
    -d        be detailed, applies to -U and -S
    -u user   specify username to use (default "")  
    -p pass   specify password to use (default "")   

The following options from enum.exe aren't implemented: -L, -N, -D, -f

Additional options:
    -a        Do all simple enumeration (-U -S -G -P -r -o -n -i).
              This option is enabled if you don't provide any other options.
    -h        Display this help message and exit
    -r        enumerate users via RID cycling
    -R range  RID ranges to enumerate (default: {global_rid_range}, implies -r)
    -K n      Keep searching RIDs until n consective RIDs don't correspond to
              a username.  Impies RID range ends at {heighest_rid}. Useful 
              against DCs.
    -l        Get some (limited) info via LDAP 389/TCP (for DCs only)
    -s file   brute force guessing for share names
    -k user   User(s) that exists on remote system (default: {global_known_username_string})
              Used to get sid with "lookupsid known_username"
              Use commas to try several users: "-k admin,user1,user2"
    -o        Get OS information
    -i        Get printer information
    -w wrkg   Specify workgroup manually (usually found automatically)
    -n        Do an nmblookup (similar to nbtstat)
    -v        Verbose.  Shows full commands being run (net, rpcclient, etc.)
    -A        Aggressive. Do write checks on shares etc

RID cycling should extract a list of users from Windows (or Samba) hosts 
which have RestrictAnonymous set to 1 (Windows NT and 2000), or "Network 
access: Allow anonymous SID/Name translation" enabled (XP, 2003).

NB: Samba servers often seem to have RIDs in the range 3000-3050.

Dependancy info: You will need to have the samba package installed as this 
script is basically just a wrapper around rpcclient, net, nmblookup and 
smbclient.  Polenum from http://labs.portcullis.co.uk/application/polenum/ 
is required to get Password Policy info.
"""


def run_command(command: str) -> str:
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        return ""


def print_heading(text: str):
    """Print a section heading."""
    output = text
    maxlen = 100
    length = maxlen - len(output)
    print()
    print(f"\033[34m {'=' * (length // 2)}(\033[0m", end='')
    print(f"\033[32m{output}\033[0m", end='')
    print(f"\033[34m){'=' * (length // 2)}\n\033[0m")


def print_verbose(text: str):
    """Print verbose output."""
    print(f"\033[33m\n[V] \033[0m\033[35m{text}\033[0m")


def print_plus(text: str):
    """Print positive/success output."""
    print(f"\033[33m\n[+] \033[0m\033[32m{text}\033[0m")


def print_info(text: str):
    """Print informational output."""
    print(f"\033[33m\n[I] \033[0m\033[36m{text}\033[0m")


def print_error(text: str):
    """Print error output."""
    print(f"\033[33m\n[E] \033[0m\033[31m{text}\033[0m")


def check_dependencies():
    """Check that dependent programs are present on the system."""
    dependency_error = False
    
    for prog in dependent_programs:
        which_output = run_command(f"which {prog} 2>&1").strip()
        if not re.match(r'^/.*\/' + prog + r'$', which_output):
            print(f"ERROR: {prog} is not in your path.  Check that samba package is installed")
            dependency_error = True
        else:
            if verbose:
                print_verbose(f'Dependent program "{prog}" found in {which_output}')
    
    for prog in optional_dependent_programs:
        which_output = run_command(f"which {prog} 2>&1").strip()
        if not re.match(r'^/.*\/' + prog + r'$', which_output):
            print(f"WARNING: {prog} is not in your path.  Check that package is installed and your PATH is sane.")
            odp_present[prog] = False
        else:
            if verbose:
                print_verbose(f'Dependent program "{prog}" found in {which_output}')
            odp_present[prog] = True
    
    if dependency_error:
        print('For Gentoo, you need to install the "samba" package')
        print('For Debian, you need to install the "smbclient" package')
        sys.exit(1)


def sanitize_for_shell(s: str) -> str:
    """Sanitize a string for safe use in shell commands."""
    s = s.replace("'", "'\\''")
    # Remove any potentially dangerous characters
    s = re.sub(r'[;&|`$(){}]', '', s)
    return s


def nbt_to_human(nbt_in: str) -> str:
    """Convert nbtstat output to human-readable format."""
    nbt_lines = nbt_in.split('\n')
    nbt_out = []
    
    for line in nbt_lines:
        match = re.match(r'\s+(\S+)\s+<(..)>\s+-\s+?(<GROUP>)?\s+?[A-Z]', line)
        if match:
            line_val = match.group(1)
            line_code = match.group(2).upper()
            line_group = 0 if match.group(3) else 1  # opposite
            
            for pattern, code, group, desc in nbt_info:
                if pattern:
                    if re.search(pattern, line_val) and line_code == code and line_group == group:
                        nbt_out.append(f"{line} {desc}")
                        break
                else:
                    if line_code == code and line_group == group:
                        nbt_out.append(f"{line} {desc}")
                        break
            else:
                nbt_out.append(line)
        else:
            nbt_out.append(line)
    
    return '\n'.join(nbt_out)


def get_nbtstat(target: str):
    """Get NBTSTAT information for target."""
    print_heading(f"Nbtstat Information for {target}")
    output = run_command(f"nmblookup -A '{target}' 2>&1")
    output = nbt_to_human(output)
    print(f"{output}\n")


def get_domain_sid(target: str, workgroup: str, username: str, password: str):
    """Get domain SID for target."""
    print_heading(f"Getting domain SID for {target}")
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' {target} -c 'lsaquery' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get domain SID with command: {command}")
    
    domain_sid_text = run_command(command).strip()
    print(domain_sid_text)
    print()
    
    if re.search(r'Domain Sid: S-0-0', domain_sid_text):
        print_plus("Host is part of a workgroup (not a domain)")
    elif re.search(r'Domain Sid: S-\d+-\d+-\d+-\d+-\d+-\d+', domain_sid_text):
        print_plus("Host is part of a domain (not a workgroup)")
    else:
        print_plus("Can't determine if host is part of domain or part of a workgroup")


def get_workgroup(target: str):
    """Get workgroup from nbtstat info - needed for lots of rpcclient calls."""
    global global_workgroup
    
    print_heading(f"Enumerating Workgroup/Domain on {target}")
    if verbose:
        print_verbose(f"Attempting to get domain name with command: nmblookup -A '{target}'")
    
    # Workgroup might already be known - e.g. from command line or from get_os_info()
    if not global_workgroup:
        global_workgroup = run_command(f"nmblookup -A '{target}'")
        match = re.search(r'\s+(\S+)\s+<00> - <GROUP>', global_workgroup, re.DOTALL)
        if match:
            global_workgroup = match.group(1)
        
        if not global_workgroup:
            # dc.example.org. hostmaster.example.org. 1 900 600 86400 3600
            global_workgroup = run_command("dig +short 0.in-addr.arpa")
            match = re.search(r'.*\. hostmaster\.(.*?)\. .*', global_workgroup, re.DOTALL)
            if match:
                global_workgroup = match.group(1)
                print(f"[+] Domain guessed: {global_workgroup}")
            else:
                global_workgroup = "WORKGROUP"
                print_error("Can't find workgroup/domain")
                print()
                return
        
        if not global_workgroup or not re.match(r'^[A-Za-z0-9_\.\-]+$', global_workgroup):
            print_error(f'Workgroup "{global_workgroup}"contains some illegal characters')
            sys.exit(1)
    
    print_plus(f"Got domain/workgroup name: {global_workgroup}")


def get_ldapinfo(target: str):
    """Get long domain name via LDAP.
    We don't do this by default because LDAP ports might not be present, or firewalled.
    """
    print_heading(f"Getting information via LDAP for {target}")
    command = f"ldapsearch -x -h '{target}' -p 389 -s base namingContexts 2>&1"
    if verbose:
        print_verbose(f"Attempting to long domain name: {command}")
    
    if not odp_present.get("ldapsearch", False):
        print_error('Dependent program "ldapsearch" not present.  Skipping this check.  Install ldapsearch to fix.\n')
        return False
    
    output = run_command(command)
    
    if re.search(r'ldap_sasl_bind', output):
        print_error("Connection error")
        return False
    
    parent = False
    for line in output.split('\n'):
        if re.search(r'namingContexts: DC=DomainDnsZones', line) or re.search(r'namingContexts: DC=ForestDnsZones', line):
            parent = True
        elif re.search(r'namingContexts:\s+(DC=[^,]+,DC=.*)', line):
            match = re.search(r'namingContexts:\s+(DC=[^,]+,DC=.*)', line)
            if match:
                long_domain = match.group(1)
                long_domain = long_domain.replace('DC=', '')
                long_domain = long_domain.replace(',', '.')
                print_plus(f"Long domain name for {target}: {long_domain}")
    
    if parent:
        print_plus(f"{target} appears to be a root/parent DC")
    else:
        print_plus(f"{target} appears to be a child DC")


def make_session(target: str, workgroup: str, username: str, password: str):
    """See if we can connect using a null session or supplied credentials."""
    print_heading(f"Session Check on {target}")
    command = f"smbclient -W '{workgroup}' //'{target}'/ipc$ -U'{username}'%'{password}' -c 'help' 2>&1"
    if verbose:
        print_verbose(f"Attempting to make null session using command: {command}")
    
    os_info = run_command(command).strip()
    
    if re.search(r'protocol negotiation failed: NT_STATUS_CONNECTION_RESET', os_info):
        print_error("Protocol mismatch.  smbclient doesn't support the same protocol versions as the server.  You likely need to install a later version of Samba.")
    
    if re.search(r'case_sensitive', os_info):
        print_plus(f"Server {target} allows sessions using username '{username}', password '{password}'")
    else:
        print_error(f"Server doesn't allow session using username '{username}', password '{password}'.  Aborting remainder of tests.")
        sys.exit(1)
    
    # Use this info to set workgroup if possible
    if not workgroup:
        match = re.search(r'Domain=\[([^\]]*)\]', os_info)
        if match:
            global global_workgroup
            global_workgroup = match.group(1)
            print_plus(f"Got domain/workgroup name: {global_workgroup}")


def get_os_info(target: str, workgroup: str, username: str, password: str):
    """Get OS information."""
    print_heading(f"OS information on {target}")
    
    command = f"smbclient -W '{workgroup}' //'{target}'/ipc$ -U'{username}'%'{password}' -c 'q' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get OS info with command: {command}")
    
    os_info = run_command(command).strip()
    
    if os_info:
        match = re.search(r'(Domain=[^\n]+)', os_info, re.DOTALL)
        if match:
            os_info_str = match.group(1)
            print_plus(f"Got OS info for {target} from smbclient: ")
            print(os_info_str)
        else:
            print_error("Can't get OS info with smbclient")
    
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' -c 'srvinfo' '{target}' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get OS info with command: {command}")
    
    os_info = run_command(command)
    if os_info:
        if re.search(r'error: NT_STATUS_ACCESS_DENIED', os_info):
            print_error("Can't get OS info with srvinfo")
        else:
            print_plus(f"Got OS info for {target} from srvinfo: ")
            print(os_info)


def enum_password_policy(target: str, username: str, password: str, workgroup: str):
    """Enumerate password policy information."""
    print_heading(f"Password Policy Information for {target}")
    command = f"polenum '{username}':'{password}'@'{target}' 2>&1"
    
    if not odp_present.get("polenum", False):
        print_error('Dependent program "polenum" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/\n')
        return False
    
    if verbose:
        print_verbose(f"Attempting to get Password Policy info with command: {command}")
    
    passpol_info = run_command(command).strip()
    
    if passpol_info:
        if re.search(r'Account Lockout Threshold', passpol_info):
            print(passpol_info)
        elif re.search(r'Error Getting Password Policy: Connect error', passpol_info):
            print_error("Can't connect to host with supplied credentials.")
        else:
            print_error("Unexpected error from polenum:")
            print(passpol_info)
    else:
        print_error("polenum gave no output.")
    
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' '{target}' -c \"getdompwinfo\" 2>&1"
    if verbose:
        print_verbose(f"Attempting to get Password Policy info with command: {command}")
    
    passpol_info = run_command(command).strip()
    print()
    
    if passpol_info and not re.search(r'ACCESS_DENIED', passpol_info):
        print_plus("Retieved partial password policy with rpcclient:\n")
        if re.search(r'password_properties: 0x[0-9a-fA-F]{7}0', passpol_info):
            print("Password Complexity: Disabled")
        elif re.search(r'password_properties: 0x[0-9a-fA-F]{7}1', passpol_info):
            print("Password Complexity: Enabled")
        
        match = re.search(r'min_password_length: (\d+)', passpol_info)
        if match:
            minlen = match.group(1)
            print(f"Minimum Password Length: {minlen}")
    else:
        print_error("Failed to get password policy with rpcclient")
    
    print()


def enum_lsa_policy(target: str):
    """Enumerate LSA policy information."""
    print_heading(f"LSA Policy Information on {target}")
    print_error("Not implemented in this version of enum4linux.")


def enum_machines(target: str):
    """Enumerate machines."""
    print_heading(f"Machine Enumeration on {target}")
    print_error("Not implemented in this version of enum4linux.")


def enum_names(target: str):
    """Enumerate names."""
    print_heading(f"Name Enumeration on {target}")
    print_error("Not implemented in this version of enum4linux.")


def get_group_details_from_rid(target: str, workgroup: str, username: str, password: str, rid: int, detailed: bool):
    """Get detailed group information from RID."""
    if invalid_rid(rid):
        print_error(f"Invalid RID passed: {rid}")
        return False
    
    if not detailed:
        return
    
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' -c 'querygroup {rid}' '{target}' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get detailed group info with command: {command}")
    
    group_info = run_command(command)
    match = re.search(r'([^\n]*Group Name.*Num Members[^\n]*)', group_info, re.DOTALL)
    if match:
        group_info = match.group(1)
        print(f"{group_info}\n")
    else:
        print_error("No info found\n")


def get_user_details_from_rid(target: str, workgroup: str, username: str, password: str, rid: int, detailed: bool):
    """Get detailed user information from RID."""
    if invalid_rid(rid):
        print_error(f"Invalid RID passed: {rid}")
        return False
    
    if not detailed:
        return
    
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' -c 'queryuser {rid}' '{target}' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get detailed user info with command: {command}")
    
    user_info = run_command(command)
    match = re.search(r'([^\n]*User Name.*logon_hrs[^\n]*)', user_info, re.DOTALL)
    if match:
        user_info = match.group(1)
        print(user_info)
    
    acb_match = re.search(r'acb_info\s+:\s+0x([0-9a-fA-F]+)', user_info)
    if acb_match:
        acb_info = acb_match.group(1)
        acb_int = int(acb_info, 16)
        pad = "\t"
        
        if acb_int & 0x00000001:
            print(f"{pad}{'Account Disabled':<25}: True")
        else:
            print(f"{pad}{'Account Disabled':<25}: False")
        
        if acb_int & 0x00000200:
            print(f"{pad}{'Password does not expire':<25}: True")
        else:
            print(f"{pad}{'Password does not expire':<25}: False")
        
        if acb_int & 0x00000400:
            print(f"{pad}{'Account locked out':<25}: True")
        else:
            print(f"{pad}{'Account locked out':<25}: False")
        
        if acb_int & 0x00020000:
            print(f"{pad}{'Password expired':<25}: True")
        else:
            print(f"{pad}{'Password expired':<25}: False")
        
        if acb_int & 0x00000040:
            print(f"{pad}{'Interdomain trust account':<25}: True")
        else:
            print(f"{pad}{'Interdomain trust account':<25}: False")
        
        if acb_int & 0x00000080:
            print(f"{pad}{'Workstation trust account':<25}: True")
        else:
            print(f"{pad}{'Workstation trust account':<25}: False")
        
        if acb_int & 0x00000100:
            print(f"{pad}{'Server trust account':<25}: True")
        else:
            print(f"{pad}{'Server trust account':<25}: False")
        
        if acb_int & 0x00002000:
            print(f"{pad}{'Trusted for delegation':<25}: True")
        else:
            print(f"{pad}{'Trusted for delegation':<25}: False")
    
    print()


def invalid_rid(rid: int) -> bool:
    """Check if RID is invalid."""
    if re.match(r'^\d+$', str(rid)):
        return False
    else:
        return True


def enum_groups(target: str, workgroup: str, username: str, password: str, detailed: bool):
    """Enumerate groups on target."""
    print_heading(f"Groups on {target}")
    
    for grouptype in ["builtin", "domain"]:
        # Get list of groups
        command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' '{target}' -c 'enumalsgroups {grouptype}' 2>&1"
        if grouptype == "domain":
            if verbose:
                print_verbose("Getting local groups with command: {command}")
            print_plus(" Getting local groups:")
        else:
            if verbose:
                print_verbose(f"Getting {grouptype} groups with command: {command}")
            print_plus(f"Getting {grouptype} groups:")
        
        groups_string = run_command(command)
        if re.search(r'error: NT_STATUS_ACCESS_DENIED', groups_string):
            if grouptype == "domain":
                print_error("Can't get local groups: NT_STATUS_ACCESS_DENIED")
            else:
                print_error(f"Can't get {grouptype} groups: NT_STATUS_ACCESS_DENIED")
        else:
            match = re.search(r'(group:.*)', groups_string, re.DOTALL)
            if match:
                groups_string = match.group(1)
            else:
                groups_string = ""
            print(groups_string)
        
        # Get group members
        rid_of_group = dict(re.findall(r'\[([^\]]+)\]', groups_string))
        if grouptype == "domain":
            print_plus(" Getting local group memberships:")
        else:
            print_plus(f" Getting {grouptype} group memberships:")
        
        for groupname in rid_of_group.keys():
            groupname_safe = groupname.replace("'", "'\\''")
            rid_hex = rid_of_group[groupname].replace('0x', '')
            rid_int = int(rid_hex, 16)
            command = f"net rpc group members '{groupname_safe}' -W '{workgroup}' -I '{target}' -U'{username}'%'{password}' 2>&1\n"
            if verbose:
                print_verbose(f"Running command: {command}")
            
            members = run_command(command)
            member_list = members.split('\n')
            for m in member_list:
                print(f"\033[35mGroup: \033[0m{groupname}' (RID: {rid_int}) has member: {m}")
        
        if detailed:
            for groupname in rid_of_group.keys():
                rid_hex = rid_of_group[groupname].replace('0x', '')
                rid_int = int(rid_hex, 16)
                print_plus(f"Getting detailed info for group {groupname} (RID: {rid_int})")
                get_group_details_from_rid(target, workgroup, username, password, rid_int, detailed)


def enum_dom_groups(target: str, workgroup: str, username: str, password: str, detailed: bool):
    """Enumerate domain groups on target."""
    # Get list of groups
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' '{target}' -c \"enumdomgroups\" 2>&1"
    if verbose:
        print_verbose(f"Getting domain groups with command: {command}")
    print_plus(" Getting domain groups:")
    
    groups_string = run_command(command)
    if re.search(r'error: NT_STATUS_ACCESS_DENIED', groups_string):
        print_error("Can't get domain groups: NT_STATUS_ACCESS_DENIED")
    else:
        match = re.search(r'(group:.*)', groups_string, re.DOTALL)
        if match:
            groups_string = match.group(1)
        else:
            groups_string = ""
        print(groups_string)
    
    # Get group members
    rid_of_group = dict(re.findall(r'\[([^\]]+)\]', groups_string))
    print_plus(" Getting domain group memberships:")
    
    for groupname in rid_of_group.keys():
        groupname_safe = groupname.replace("'", "'\\''")
        rid_hex = rid_of_group[groupname].replace('0x', '')
        rid_int = int(rid_hex, 16)
        command = f"net rpc group members '{groupname_safe}' -W '{workgroup}' -I '{target}' -U'{username}'%'{password}' 2>&1\n"
        if verbose:
            print_verbose(f"Running command: {command}")
        
        members = run_command(command)
        member_list = members.split('\n')
        for m in member_list:
            print(f"\033[35mGroup: \033[0m'{groupname}' (RID: {rid_int}) has member: {m}")
    
    if detailed:
        for groupname in rid_of_group.keys():
            rid_hex = rid_of_group[groupname].replace('0x', '')
            rid_int = int(rid_hex, 16)
            print_plus(f"Getting detailed info for group {groupname} (RID: {rid_int})")
            get_group_details_from_rid(target, workgroup, username, password, rid_int, detailed)


def enum_groups_unauth(target: str):
    """Enumerate groups via RID cycling (unauthenticated)."""
    print_heading(f"Groups on {target} via RID cycling")
    print_error("Not implemented in this version of enum4linux.")


def enum_shares(target: str, workgroup: str, username: str, password: str, aggressive_mode: bool, detailed: bool):
    """Enumerate shares on target."""
    # Share enumeration
    print_heading(f"Share Enumeration on {target}")
    if verbose:
        print_verbose("Attempting to get share list using authentication")
    
    command = f"smbclient -W '{workgroup}' -L //'{target}' -U'{username}'%'{password}' 2>&1"
    shares = run_command(command)
    
    if shares:
        if re.search(r'NT_STATUS_ACCESS_DENIED', shares):
            print_error("Can't list shares: NT_STATUS_ACCESS_DENIED")
        else:
            print(shares)
    
    print_plus(f"Attempting to map shares on {target}")
    share_matches = re.findall(r'^[\t ]*?([ \S]+?)[\t ]*?(?:Disk|IPC|Printer)[^\n]*', shares, re.MULTILINE | re.DOTALL)
    
    for share in share_matches:
        mapping_result = "N/A"
        listing_result = "N/A"
        writing_result = "N/A"
        
        share_safe = share.replace("'", "'\\''")
        command = f"smbclient -W '{workgroup}' //'{target}'/'{share_safe}' -U'{username}'%'{password}' -c dir 2>&1"
        if verbose:
            print_verbose(f"Attempting map to share //{target}/{share_safe} with command: {command}")
        
        output = run_command(command)
        
        if re.search(r'NT_STATUS_ACCESS_DENIED listing', output) or re.search(r'do_list:.*NT_STATUS_ACCESS_DENIED', output):
            mapping_result = "OK"
            listing_result = "DENIED"
        elif re.search(r'tree connect failed: NT_STATUS_ACCESS_DENIED', output):
            mapping_result = "DENIED"
            listing_result = "N/A"
        elif re.search(r'\n\s+\.\.\s+D.*\d{4}\n', output):
            mapping_result = "OK"
            listing_result = "OK"
        else:
            print_error("Can't understand response:")
            print(output)
        
        if mapping_result == "OK":
            if aggressive_mode:
                print(f"testing write access {share}")
                # check for write access
                chars = string.ascii_letters + string.digits
                random_string = ''.join(random.choice(chars) for _ in range(8))
                
                command = f"smbclient -W '{workgroup}' //'{target}'/'{share_safe}' -U'{username}'%'{password}' -c 'mkdir {random_string}' 2>&1"
                if verbose:
                    print_verbose(f"Checking write access to share //{target}/{share_safe} with command: {command}")
                
                output = run_command(command)
                if re.search(r'NT_STATUS_ACCESS_DENIED making', output):
                    writing_result = "DENIED"
                elif len(output):
                    # the command should not give any output, if something was output maybe it's a failure
                    command2 = f"smbclient -W '{workgroup}' //'{target}'/'{share_safe}' -U'{username}'%'{password}' -c dir 2>&1"
                    if verbose:
                        print_verbose(f"Attempting check for directory {random_string} on //{target}/{share_safe} with command: {command2}")
                    
                    output2 = run_command(command2)
                    if re.search(rf'.*{random_string}.*', output2):
                        writing_result = "OK"
                    else:
                        print_error("Can't understand initial response:")
                        print(output)
                        print_error("Can't understand second response:")
                        print(output2)
                else:
                    writing_result = "OK"
                
                if writing_result != "DENIED":
                    # remove the directory we created
                    command = f"smbclient -W '{workgroup}' //'{target}'/'{share_safe}' -U'{username}'%'{password}' -c 'rmdir {random_string}' 2>&1"
                    if verbose:
                        print_verbose(f"Removing created directory on share //{target}/{share_safe} with command: {command}")
                    
                    output = run_command(command)
                    if len(output):
                        print_error("rmdir command returned the following:")
                        print(output)
        
        # print results
        print(f"//{target}/{share}\t", end='')
        print(f"\033[35mMapping: \033[0m{mapping_result}", end='')
        print(f"\033[35m Listing: \033[0m{listing_result}", end='')
        print(f"\033[35m Writing: \033[0m{writing_result}")


def enum_shares_unauth(target: str, workgroup: str, username: str, password: str, share_file: str):
    """Brute force share enumeration."""
    print_heading(f"Brute Force Share Enumeration on {target}")
    if verbose:
        print_verbose("Attempting to get share list using bruteforcing")
    
    try:
        with open(share_file, 'r') as f:
            shares = [line.strip() for line in f.readlines()]
    except IOError as e:
        print_error(f"Can't open share list file {share_file}: {e}")
        sys.exit(1)
    
    for share in shares:
        # Validate share name
        if not re.match(r'^[a-zA-Z0-9._$-]+$', share):
            print_error(f"Share name {share} contains some illegal characters")
            sys.exit(1)
        
        result = run_command(f"smbclient -W '{workgroup}' //'{target}'/'{share}' -c dir -U'{username}'%'{password}' 2>&1")
        if re.search(r'blocks of size .* blocks available', result):
            print(f"{share} EXISTS, Allows access using username: '{username}', password: '{password}'")
        elif re.search(r'NT_STATUS_BAD_NETWORK_NAME', result):
            if debug:
                print(f"{share} doesn't exist")
        elif re.search(r'NT_STATUS_ACCESS_DENIED', result):
            print(f"{share} EXISTS")
        else:
            print(result)


def enum_users_rids(target: str, workgroup: str, username: str, password: str, rid_range: str, 
                    known_usernames: List[str], search_until_fail: bool, fail_limit: int, 
                    heighest_rid: int, detailed: bool):
    """Enumerate users via RID cycling."""
    print_heading(f"Users on {target} via RID cycling (RIDS: {rid_range})")
    
    sid = None
    sids = {}
    logon = None
    cleansid = None
    
    # Get SID - try other known usernames if necessary
    for known_username in known_usernames:
        command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' '{target}' -c 'lookupnames {known_username}' 2>&1"
        if verbose:
            print_verbose(f"Attempting to get SID from {target} with command: {command}")
            print_verbose(f'Assuming that user "{known_username}" exists')
        
        logon = f"username '{username}', password '{password}'"
        sid = run_command(command)
        
        if re.search(r'NT_STATUS_ACCESS_DENIED', sid):
            print_error("Couldn't get SID: NT_STATUS_ACCESS_DENIED.  RID cycling not possible.")
            break
        elif re.search(r'NT_STATUS_NONE_MAPPED', sid):
            if verbose:
                print_verbose(f'User "{known_username}" doesn\'t exist.  User enumeration should be possible, but SID needed...')
            continue
        elif re.search(r'S-1-5-21-[\d-]+-\d+\s+', sid):
            match = re.search(r'(S-1-5-21-[\d-]+)-\d+\s+', sid)
            if match:
                cleansid = match.group(1)
                if cleansid in sids:
                    print_info("Found new SID: ")
                    print(cleansid)
                sids[cleansid] = True
                continue
        elif re.search(r'S-1-5-[\d-]+-\d+\s+', sid):
            match = re.search(r'(S-1-5-[\d-]+)-\d+\s+', sid)
            if match:
                cleansid = match.group(1)
                if cleansid in sids:
                    print_info("Found new SID: ")
                    print(cleansid)
                sids[cleansid] = True
                continue
        elif re.search(r'S-1-22-[\d-]+-\d+\s+', sid):
            match = re.search(r'(S-1-22-[\d-]+)-\d+\s+', sid)
            if match:
                cleansid = match.group(1)
                if cleansid in sids:
                    print_info("Found new SID: ")
                    print(cleansid)
                sids[cleansid] = True
                continue
    
    # Get some more SIDs (hopefully)
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' '{target}' -c lsaenumsid 2>&1"
    if verbose:
        print_verbose(f"Attempting to get SIDs from {target} with command: {command}")
    
    sid_list = run_command(command)
    for sid_match in re.findall(r'(S-[0-9-]+)', sid_list):
        if verbose:
            print_verbose(f"Processing SID {sid_match}")
        
        if re.search(r'NT_STATUS_ACCESS_DENIED', sid_match):
            print_error("Couldn't get SID: NT_STATUS_ACCESS_DENIED.  RID cycling not possible.")
            continue
        elif re.search(r'S-1-5-21-[\d-]+-\d+', sid_match):
            match = re.search(r'(S-1-5-21-[\d-]+)-\d+', sid_match)
            if match:
                cleansid = match.group(1)
                if cleansid in sids:
                    print_info("Found new SID: ")
                    print(cleansid)
                sids[cleansid] = True
                continue
        elif re.search(r'S-1-5-[\d-]+-\d+', sid_match):
            match = re.search(r'(S-1-5-[\d-]+)-\d+', sid_match)
            if match:
                cleansid = match.group(1)
                if cleansid in sids:
                    print_info("Found new SID: ")
                    print(cleansid)
                sids[cleansid] = True
                continue
        elif re.search(r'S-1-22-[\d-]+-\d+', sid_match):
            match = re.search(r'(S-1-22-[\d-]+)-\d+', sid_match)
            if match:
                cleansid = match.group(1)
                if cleansid in sids:
                    print_info("Found new SID: ")
                    print(cleansid)
                sids[cleansid] = True
                continue
    
    for sid_key in sids.keys():
        if not sid_key and username:
            if verbose:
                print_verbose(f"WARNING: Can't get SID.  Maybe none of the 'known' users really exist.  Try others with -k.  Trying null session.")
            
            for known_username in known_usernames:
                command = f"rpcclient -W '{workgroup}' -U% '{target}' -c 'lookupnames {known_username}' 2>&1"
                print_info(f"Assuming that user {known_username} exists")
                if verbose:
                    print_verbose(f"Trying null username and password: {command}")
                
                sid = run_command(command)
                if re.search(r'error: NT_STATUS_ACCESS_DENIED', sid):
                    print_error("Couldn't get SID: NT_STATUS_ACCESS_DENIED")
                    continue
                else:
                    break
            
            match = re.search(r'(S-1-5-21-[\d-]+)-\d+\s+', sid)
            if match:
                sid = match.group(1)
            
            if not sid:
                print_error(f'Can\'t get SID using either a null username or the username "{username}"')
                sys.exit(1)
            
            logon = "username '', password ''"
        
        if not sid_key:
            print_error("Couldn't find SID.  Aborting RID cycling attempt.\n")
            return True
        
        print_plus(f"Enumerating users using SID {sid_key} and logon {logon}")
        
        # RID Cycle
        last_range = False
        ranges = rid_range.split(',')
        
        for i, current_range in enumerate(ranges):
            if current_range == ranges[-1]:
                last_range = True
            
            start_rid = 0
            end_rid = 0
            
            # Check range is of form n-m (n,m integers)
            if re.match(r'\d+-\d+', current_range):
                match = re.match(r'^(\d+)-(\d+)$', current_range)
                if match:
                    start_rid = int(match.group(1))
                    end_rid = int(match.group(2))
            # Check range is of form n (n integer)
            elif re.match(r'^\d+$', current_range):
                start_rid = int(current_range)
                end_rid = int(current_range)
            # Invalid range
            else:
                print(f"WARNING: RID range {current_range} isn't valid.  Should be like 10-20 or 1199.  Ignoring this range")
                continue
            
            # Check we have an ascending range
            if start_rid > end_rid:
                print(f"WARNING: RID range {current_range} seems to be reversed.  Automatically reversing.")
                start_rid, end_rid = end_rid, start_rid
            
            if search_until_fail:
                end_rid = 500000
            
            fail_count = 0
            if search_until_fail and last_range:
                end_rid = heighest_rid
            
            for rid in range(start_rid, end_rid + 1):
                output = run_command(f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' '{target}' -c 'lookupsids {sid_key}-{rid}' 2>&1")
                match = re.search(r'(S-\d+-\d+-\d+-[\d-]+\s+[^\)]+\))', output)
                
                if match:
                    sid_and_user = match.group(1)
                    sid_and_user = sid_and_user.replace('(1)', '(Local User)')
                    sid_and_user = sid_and_user.replace('(2)', '(Domain Group)')
                    sid_and_user = sid_and_user.replace('(4)', '(Local Group)')
                    
                    # Samba servers sometimes claim to have user accounts
                    # with the same name as the UID/RID.  We don't report these.
                    rid_match = re.search(r'-(\d+) .*\\\1 \(', sid_and_user)
                    if rid_match:
                        fail_count += 1
                    else:
                        if re.search(r'\((Local|Domain) User\)', sid_and_user):
                            print(sid_and_user)
                        if re.search(r'\((Local|Domain) Group\)', sid_and_user):
                            print(sid_and_user)
                        
                        fail_count = 0
                        
                        if re.search(r'\((Local|Domain) User\)', sid_and_user):
                            get_user_details_from_rid(target, workgroup, username, password, rid, detailed)
                        if re.search(r'\((Local|Domain) Group\)', sid_and_user):
                            get_group_details_from_rid(target, workgroup, username, password, rid, detailed)
                else:
                    fail_count += 1
                
                if search_until_fail:
                    if fail_count > fail_limit:
                        break


def enum_users(target: str, workgroup: str, username: str, password: str, detailed: bool):
    """Enumerate users on target."""
    print_heading(f"Users on {target}")
    
    command = f"rpcclient -W '{workgroup}' -c querydispinfo -U'{username}'%'{password}' '{target}' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get userlist with command: {command}")
    
    users = run_command(command)
    continue_search = True
    
    if re.search(r'NT_STATUS_ACCESS_DENIED', users):
        print_error("Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED")
    else:
        match = re.search(r'(index:.*)', users, re.DOTALL)
        if match:
            users = match.group(1)
            print(users)
            continue_search = False
    
    rids_hex = re.findall(r'RID:\s+0x([a-fA-F0-9]+)\s', users, re.DOTALL)
    rids = [int(rid, 16) for rid in rids_hex]
    
    print()
    
    command = f"rpcclient -W '{workgroup}' -c enumdomusers -U'{username}'%'{password}' '{target}' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get userlist with command: {command}")
    
    users = run_command(command)
    if re.search(r'NT_STATUS_ACCESS_DENIED', users):
        print_error("Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED")
    else:
        match = re.search(r'(user:.*)', users, re.DOTALL)
        if match:
            users = match.group(1)
            print(users)
    
    rids_hex2 = re.findall(r'rid:\[0x([A-Fa-f0-9]+)\]', users)
    rids2 = [int(rid, 16) for rid in rids_hex2]
    
    rids_dict = {}
    for rid in rids + rids2:
        rids_dict[rid] = True
    
    for rid in rids_dict.keys():
        get_user_details_from_rid(target, workgroup, username, password, rid, detailed)


def get_printer_info(target: str, workgroup: str, username: str, password: str):
    """Get printer information."""
    print_heading(f"Getting printer info for {target}")
    command = f"rpcclient -W '{workgroup}' -U'{username}'%'{password}' -c 'enumprinters' '{target}' 2>&1"
    if verbose:
        print_verbose(f"Attempting to get printer info with command: {command}")
    
    printer_info = run_command(command)
    if printer_info:
        print(f"{printer_info}\n")
    else:
        print_error("No info found\n")


def main():
    global verbose, debug, aggressive, global_workgroup, global_username, global_password
    global global_detailed, global_passpol, global_rid_range, global_known_username_string
    global global_share_file, global_fail_limit, global_search_until_fail
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-U', action='store_true', help='get userlist')
    parser.add_argument('-M', action='store_true', help='get machine list')
    parser.add_argument('-S', action='store_true', help='get sharelist')
    parser.add_argument('-P', action='store_true', help='get password policy information')
    parser.add_argument('-G', action='store_true', help='get group and member list')
    parser.add_argument('-d', action='store_true', help='be detailed, applies to -U and -S')
    parser.add_argument('-u', dest='username', default='', help='specify username to use')
    parser.add_argument('-p', dest='password', default='', help='specify password to use')
    parser.add_argument('-a', action='store_true', help='Do all simple enumeration')
    parser.add_argument('-h', action='store_true', help='Display this help message and exit')
    parser.add_argument('-r', action='store_true', help='enumerate users via RID cycling')
    parser.add_argument('-R', dest='rid_range', help='RID ranges to enumerate')
    parser.add_argument('-K', dest='fail_limit', type=int, help='Keep searching RIDs until n consecutive RIDs fail')
    parser.add_argument('-l', action='store_true', help='Get info via LDAP 389/TCP')
    parser.add_argument('-s', dest='share_file', help='brute force guessing for share names')
    parser.add_argument('-k', dest='known_usernames', help='User(s) that exists on remote system')
    parser.add_argument('-o', action='store_true', help='Get OS information')
    parser.add_argument('-i', action='store_true', help='Get printer information')
    parser.add_argument('-w', dest='workgroup', help='Specify workgroup manually')
    parser.add_argument('-n', action='store_true', help='Do an nmblookup')
    parser.add_argument('-v', action='store_true', help='Verbose output')
    parser.add_argument('-A', action='store_true', help='Aggressive mode')
    parser.add_argument('target', nargs='?', help='Target IP or hostname')
    
    args = parser.parse_args()
    
    # Print help message if required
    if args.h:
        print(get_usage())
        sys.exit(0)
    
    # Read host and validate
    if not args.target:
        print(get_usage())
        sys.exit(1)
    
    global_target = args.target
    if not re.match(r'^[a-zA-Z0-9._-]+$', global_target):
        print(f'ERROR: Target hostname "{global_target}" contains some illegal characters')
        sys.exit(1)
    
    # Enable -a if no other options (apart from -v) are given
    opts = vars(args)
    other_opts = {k: v for k, v in opts.items() if k not in ['v', 'target']}
    if not any(other_opts.values()):
        args.a = True
    
    # Turn on some other options if -a given
    if args.a:
        args.U = True
        args.S = True
        args.G = True
        args.r = True
        args.P = True
        args.o = True
        args.n = True
        args.i = True
    
    # Set global variables
    global_username = args.username if args.username else ''
    global_password = args.password if args.password else ''
    global_detailed = args.d if args.d else False
    global_rid_range = args.rid_range if args.rid_range else global_rid_range
    global_passpol = args.P if args.P else False
    global_fail_limit = args.fail_limit if args.fail_limit else global_fail_limit
    global_share_file = args.share_file if args.share_file else ''
    global_known_username_string = args.known_usernames if args.known_usernames else global_known_username_string
    global_workgroup = args.workgroup if args.workgroup else ''
    verbose = args.v if args.v else False
    aggressive = args.A if args.A else False
    
    if args.R:
        args.r = True
    
    global_search_until_fail = args.K is not None
    
    global_known_usernames = global_known_username_string.split(',')
    
    # Sanitize known usernames for shell
    global_known_usernames = [sanitize_for_shell(u) for u in global_known_usernames]
    global_username = sanitize_for_shell(global_username)
    global_password = sanitize_for_shell(global_password)
    
    # Validate workgroup if supplied
    if global_workgroup:
        if not re.match(r'^[a-zA-Z0-9.\-_]*$', global_workgroup):
            print(f'ERROR: Workgroup "{global_workgroup}" contains some illegal characters')
            sys.exit(1)
    
    # Check dependencies
    check_dependencies()
    
    # Output message about options used
    print(f"Starting enum4linux v{VERSION} ( http://labs.portcullis.co.uk/application/enum4linux/ ) on {subprocess.getoutput('date')}")
    print_heading("Target Information")
    print(f"Target ........... {global_target}")
    print(f"RID Range ........ {global_rid_range}")
    print(f"Username ......... '{global_username}'")
    print(f"Password ......... '{global_password}'")
    print(f"Known Usernames .. {', '.join(global_known_usernames)}")
    print()
    
    # Basic enumeration, check session
    get_workgroup(global_target)
    get_nbtstat(global_target) if args.n else None
    make_session(global_target, global_workgroup, global_username, global_password)
    get_ldapinfo(global_target) if args.l else None
    get_domain_sid(global_target, global_workgroup, global_username, global_password)
    get_os_info(global_target, global_workgroup, global_username, global_password) if args.o else None
    
    # enum-compatible functions
    enum_users(global_target, global_workgroup, global_username, global_password, global_detailed) if args.U else None
    enum_machines(global_target) if args.M else None
    enum_names(global_target) if hasattr(args, 'N') and args.N else None
    enum_shares(global_target, global_workgroup, global_username, global_password, aggressive, global_detailed) if args.S else None
    enum_password_policy(global_target, global_username, global_password, global_workgroup) if args.P else None
    enum_groups(global_target, global_workgroup, global_username, global_password, global_detailed) if args.G else None
    enum_dom_groups(global_target, global_workgroup, global_username, global_password, global_detailed) if args.G else None
    enum_lsa_policy(global_target) if hasattr(args, 'L') and args.L else None
    
    # extra stuff that runs slowly
    enum_users_rids(global_target, global_workgroup, global_username, global_password, 
                    global_rid_range, global_known_usernames, global_search_until_fail, 
                    global_fail_limit, heighest_rid, global_detailed) if args.r else None
    enum_shares_unauth(global_target, global_workgroup, global_username, global_password, global_share_file) if args.s else None
    get_printer_info(global_target, global_workgroup, global_username, global_password) if args.i else None
    
    print(f"\nenum4linux complete on {subprocess.getoutput('date')}\n")


if __name__ == '__main__':
    main()
