"""
Unit tests for nmap.py
"""

import unittest
from unittest.mock import patch, MagicMock
import subprocess
import os
import sys

# Import the module under test
import nmap


class TestValidateTargets(unittest.TestCase):
    """Tests for _validate_targets function"""

    def test_valid_ipv4(self):
        """Test validation of valid IPv4 addresses"""
        items = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
        result = nmap._validate_targets(items)
        self.assertEqual(result, items)

    def test_valid_ipv6(self):
        """Test validation of valid IPv6 addresses"""
        items = ["::1", "2001:db8::1", "fe80::1"]
        result = nmap._validate_targets(items)
        self.assertEqual(result, items)

    def test_valid_url_with_scheme(self):
        """Test validation of URLs with proper scheme"""
        items = ["https://example.com", "http://test.org"]
        result = nmap._validate_targets(items)
        self.assertEqual(result, items)

    def test_url_without_scheme_gets_https(self):
        """Test that URLs without scheme get https:// prepended"""
        items = ["example.com"]
        result = nmap._validate_targets(items)
        self.assertEqual(result, ["https://example.com"])

    def test_invalid_target(self):
        """Test that truly invalid targets are rejected (empty string)"""
        items = [""]
        result = nmap._validate_targets(items)
        # Empty strings get converted to https:// which is still invalid
        self.assertEqual(result, [])

    def test_mixed_valid_invalid(self):
        """Test mixed valid and invalid targets"""
        # Note: _validate_targets prepends https:// to non-IP/URL strings,
        # so most strings become "valid" URLs. Only empty strings fail.
        items = ["192.168.1.1", "", "https://example.com"]
        result = nmap._validate_targets(items)
        self.assertEqual(result, ["192.168.1.1", "https://example.com"])

    def test_empty_list(self):
        """Test empty list returns empty list"""
        result = nmap._validate_targets([])
        self.assertEqual(result, [])


class TestBuildCommand(unittest.TestCase):
    """Tests for build_command function"""

    def test_basic_command(self):
        """Test basic command building without sudo"""
        targets = ["192.168.1.1"]
        args = ["-sS", "-p22,80"]
        result = nmap.build_command(targets, args, use_sudo=False)
        expected = ["nmap", "-sS", "-p22,80", "192.168.1.1"]
        self.assertEqual(result, expected)

    def test_command_with_sudo(self):
        """Test command building with sudo"""
        targets = ["192.168.1.1"]
        args = ["-sS"]
        result = nmap.build_command(targets, args, use_sudo=True)
        expected = ["sudo", "nmap", "-sS", "192.168.1.1"]
        self.assertEqual(result, expected)

    def test_multiple_targets(self):
        """Test command with multiple targets"""
        targets = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        args = ["-sn"]
        result = nmap.build_command(targets, args, use_sudo=False)
        expected = ["nmap", "-sn", "192.168.1.1", "192.168.1.2", "192.168.1.3"]
        self.assertEqual(result, expected)

    def test_empty_args(self):
        """Test command with no additional args"""
        targets = ["192.168.1.1"]
        args = []
        result = nmap.build_command(targets, args, use_sudo=False)
        expected = ["nmap", "192.168.1.1"]
        self.assertEqual(result, expected)


class TestResolveConflicts(unittest.TestCase):
    """Tests for resolve_conflicts function"""

    @patch('nmap.get_user_choice')
    @patch('nmap.clear_screen')
    @patch('nmap.input')
    def test_sn_with_port_spec_conflict_remove_conflicting(self, mock_input, mock_clear, mock_choice):
        """Test -sn conflicts with port specification"""
        mock_choice.return_value = 1  # Remove conflicting options
        args = ["-sn", "-p22,80"]
        result = nmap.resolve_conflicts(args)
        self.assertIn("-sn", result)
        self.assertNotIn("-p22,80", result)

    @patch('nmap.get_user_choice')
    @patch('nmap.clear_screen')
    @patch('nmap.input')
    def test_sn_with_scan_technique_conflict_remove_conflicting(self, mock_input, mock_clear, mock_choice):
        """Test -sn conflicts with scan technique"""
        mock_choice.return_value = 1  # Remove conflicting options
        args = ["-sn", "-sS"]
        result = nmap.resolve_conflicts(args)
        self.assertIn("-sn", result)
        self.assertNotIn("-sS", result)

    @patch('nmap.get_user_choice')
    @patch('nmap.clear_screen')
    @patch('nmap.input')
    def test_sn_with_version_detection_conflict(self, mock_input, mock_clear, mock_choice):
        """Test -sn conflicts with version detection"""
        mock_choice.return_value = 1  # Remove conflicting options
        args = ["-sn", "-sV"]
        result = nmap.resolve_conflicts(args)
        self.assertIn("-sn", result)
        self.assertNotIn("-sV", result)

    @patch('nmap.get_user_choice')
    @patch('nmap.clear_screen')
    @patch('nmap.input')
    def test_sn_with_os_detection_conflict(self, mock_input, mock_clear, mock_choice):
        """Test -sn conflicts with OS detection"""
        mock_choice.return_value = 1  # Remove conflicting options
        args = ["-sn", "-O"]
        result = nmap.resolve_conflicts(args)
        self.assertIn("-sn", result)
        self.assertNotIn("-O", result)

    @patch('nmap.get_user_choice')
    @patch('nmap.clear_screen')
    @patch('nmap.input')
    def test_no_conflict_returns_original(self, mock_input, mock_clear, mock_choice):
        """Test that args without conflicts are returned unchanged"""
        args = ["-sS", "-p22,80", "-sV"]
        result = nmap.resolve_conflicts(args)
        self.assertEqual(result, args)


class TestClearScreen(unittest.TestCase):
    """Tests for clear_screen function"""

    @patch('nmap.os.system')
    def test_clear_screen_on_linux(self, mock_system):
        """Test clear_screen uses correct command on Linux"""
        with patch('nmap.os.name', 'posix'):
            nmap.clear_screen()
            mock_system.assert_called_once_with('clear')

    @patch('nmap.os.system')
    def test_clear_screen_on_windows(self, mock_system):
        """Test clear_screen uses correct command on Windows"""
        with patch('nmap.os.name', 'nt'):
            nmap.clear_screen()
            mock_system.assert_called_once_with('cls')


class TestDisplayMenu(unittest.TestCase):
    """Tests for display_menu function"""

    @patch('builtins.print')
    def test_display_menu_shows_options(self, mock_print):
        """Test that display_menu shows all options"""
        options = [
            ("Option 1", "-opt1", False),
            ("Option 2", "-opt2", True),
        ]
        nmap.display_menu("Test Menu", options, [])
        # Should print menu title and options
        self.assertTrue(mock_print.called)


class TestGetUserChoice(unittest.TestCase):
    """Tests for get_user_choice function"""

    @patch('builtins.input', return_value='1')
    def test_valid_choice(self, mock_input):
        """Test valid choice is returned"""
        result = nmap.get_user_choice(3)
        self.assertEqual(result, 1)

    @patch('builtins.input', return_value='0')
    def test_zero_choice(self, mock_input):
        """Test zero choice is valid"""
        result = nmap.get_user_choice(3)
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=['xyz', '2'])
    def test_invalid_then_valid(self, mock_input):
        """Test invalid input followed by valid input"""
        result = nmap.get_user_choice(3)
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['5', '1'])
    def test_out_of_range_then_valid(self, mock_input):
        """Test out of range followed by valid input"""
        result = nmap.get_user_choice(3)
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['', '3'])
    def test_empty_then_valid(self, mock_input):
        """Test empty input followed by valid input"""
        result = nmap.get_user_choice(3)
        self.assertEqual(result, 3)


class TestHandleHostDiscovery(unittest.TestCase):
    """Tests for handle_host_discovery function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_host_discovery_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test host discovery returns when user chooses 0"""
        args = ["-sn"]
        result = nmap.handle_host_discovery(args)
        self.assertEqual(result, args)


class TestHandleScanTechniques(unittest.TestCase):
    """Tests for handle_scan_techniques function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_scan_techniques_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test scan techniques returns when user chooses 0"""
        args = ["-sS"]
        result = nmap.handle_scan_techniques(args)
        self.assertEqual(result, args)

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', side_effect=[1, 0])
    @patch('nmap.input')
    def test_scan_techniques_mutually_exclusive(self, mock_input, mock_choice, mock_clear):
        """Test that only one scan technique is active at a time"""
        args = []
        result = nmap.handle_scan_techniques(args)
        # Should have exactly one technique (-sS from choice 1)
        tech_flags = ['-sS', '-sT', '-sU', '-sA', '-sW', '-sM', '-sN', '-sF', '-sX', '-sO', '-sY', '-sZ']
        count = sum(1 for arg in result if arg in tech_flags)
        self.assertEqual(count, 1)
        self.assertIn('-sS', result)


class TestHandlePortSpec(unittest.TestCase):
    """Tests for handle_port_spec function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_port_spec_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test port spec returns when user chooses 0"""
        args = ["-p22"]
        result = nmap.handle_port_spec(args)
        self.assertEqual(result, args)

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', side_effect=[2, 0])
    @patch('nmap.input')
    def test_port_spec_p_dash(self, mock_input, mock_choice, mock_clear):
        """Test -p- option (all ports)"""
        args = []
        result = nmap.handle_port_spec(args)
        self.assertIn("-p-", result)


class TestHandleServiceVersion(unittest.TestCase):
    """Tests for handle_service_version function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_service_version_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test service version returns when user chooses 0"""
        args = ["-sV"]
        result = nmap.handle_service_version(args)
        self.assertEqual(result, args)


class TestHandleOSDetection(unittest.TestCase):
    """Tests for handle_os_detection function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_os_detection_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test OS detection returns when user chooses 0"""
        args = ["-O"]
        result = nmap.handle_os_detection(args)
        self.assertEqual(result, args)


class TestHandleNSEScripts(unittest.TestCase):
    """Tests for handle_nse_scripts function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_nse_scripts_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test NSE scripts returns when user chooses 0"""
        args = ["-sC"]
        result = nmap.handle_nse_scripts(args)
        self.assertEqual(result, args)


class TestHandleTiming(unittest.TestCase):
    """Tests for handle_timing function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_timing_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test timing returns when user chooses 0"""
        args = ["-T4"]
        result = nmap.handle_timing(args)
        self.assertEqual(result, args)


class TestHandleEvasion(unittest.TestCase):
    """Tests for handle_evasion function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_evasion_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test evasion returns when user chooses 0"""
        args = ["-f"]
        result = nmap.handle_evasion(args)
        self.assertEqual(result, args)


class TestHandleOutput(unittest.TestCase):
    """Tests for handle_output function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_output_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test output returns when user chooses 0"""
        args = ["-oN", "output.txt"]
        result = nmap.handle_output(args)
        self.assertEqual(result, args)


class TestHandleMisc(unittest.TestCase):
    """Tests for handle_misc function"""

    @patch('nmap.clear_screen')
    @patch('nmap.get_user_choice', return_value=0)
    @patch('nmap.input')
    def test_misc_return_immediately(self, mock_input, mock_choice, mock_clear):
        """Test misc returns when user chooses 0"""
        args = ["--version"]
        result = nmap.handle_misc(args)
        self.assertEqual(result, args)


class TestExecuteScan(unittest.TestCase):
    """Tests for execute_scan function"""

    @patch('subprocess.Popen')
    @patch('builtins.print')
    def test_execute_scan_success(self, mock_print, mock_popen):
        """Test successful scan execution"""
        mock_process = MagicMock()
        mock_process.stdout = iter(["line1\n", "line2\n"])
        mock_process.wait.return_value = 0
        mock_popen.return_value = mock_process

        cmd = ["nmap", "-sS", "192.168.1.1"]
        nmap.execute_scan(cmd)

        mock_popen.assert_called_once()
        mock_process.wait.assert_called_once()

    @patch('subprocess.Popen', side_effect=FileNotFoundError)
    @patch('builtins.print')
    def test_execute_scan_nmap_not_found(self, mock_print, mock_popen):
        """Test error handling when nmap is not installed"""
        cmd = ["nmap", "-sS", "192.168.1.1"]
        nmap.execute_scan(cmd)

        # Should print error message
        mock_print.assert_any_call("Error: nmap tidak ditemukan. Pastikan nmap terinstal.")


class TestShowCurrentArgs(unittest.TestCase):
    """Tests for show_current_args function"""

    @patch('builtins.print')
    def test_show_current_args_with_args(self, mock_print):
        """Test showing current args when there are args"""
        args = ["-sS", "-p22"]
        nmap.show_current_args(args)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_show_current_args_empty(self, mock_print):
        """Test showing current args when empty"""
        args = []
        nmap.show_current_args(args)
        mock_print.assert_called()


class TestResetArgs(unittest.TestCase):
    """Tests for reset_args function"""

    def test_reset_args_returns_empty(self):
        """Test reset_args returns empty list"""
        result = nmap.reset_args()
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
