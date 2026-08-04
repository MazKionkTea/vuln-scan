import subprocess
import ipaddress
from urllib.parse import urlparse
import os
import re


# ctf target 172.104.202.18
# === Fungsi clear screen ===

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# === Fungsi target (sudah ada) ===

def target():
    raw = input("Masukkan IP, URL, atau path file (misal targets.txt): ").strip()
    if not raw:
        print("Input kosong.")
        return []
    if os.path.isfile(raw):
        with open(raw, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        return _validate_targets(lines)
    return _validate_targets([raw])

def _validate_targets(items):
    valid = []
    for item in items:
        try:
            ipaddress.ip_address(item)
            valid.append(item)
            continue
        except ValueError:
            pass
        if not item.startswith(("http://", "https://")):
            item = "https://" + item
        parsed = urlparse(item)
        if parsed.scheme and parsed.netloc:
            valid.append(item)
        else:
            print(f"Target tidak valid: {item}")
    return valid

def change_target(current_targets):
    """
    Meminta input target baru (IP/URL/file) tanpa mengubah opsi scan.
    current_targets: list target yang sedang aktif.
    Return: list target baru yang valid, atau current_targets jika input tidak valid.
    """
    print(f"Target saat ini: {', '.join(current_targets) if current_targets else '(kosong)'}")
    raw = input("Masukkan IP, URL, atau path file target baru: ").strip()
    if not raw:
        print("Input kosong. Target tidak diubah.")
        input("Tekan Enter...")
        return current_targets

    # Gunakan validasi yang sama dengan target()
    if os.path.isfile(raw):
        with open(raw, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        new_targets = _validate_targets(lines)
    else:
        new_targets = _validate_targets([raw])

    if not new_targets:
        print("Tidak ada target valid. Target tetap sama.")
        input("Tekan Enter...")
        return current_targets

    print(f"Target berhasil diganti: {', '.join(new_targets)}")
    input("Tekan Enter...")
    return new_targets

# === Fungsi display dan input ===

def display_menu(title, options, selected_args):
    """
    Menampilkan menu dengan opsi bernomor.
    options: list of tuples (display_text, flag, needs_value?)
    selected_args: list argumen yang sudah terkumpul.
    """
    print(f"\n--- {title} ---")
    for idx, (desc, flag, needs_value) in enumerate(options, 1):
        # Cek apakah flag sudah ada di selected_args (sederhana)
        is_selected = any(flag in arg for arg in selected_args)
        selected_mark = "  [SUDAH DIPILIH]" if is_selected else ""
        print(f"  {idx}. {desc}{selected_mark}")
    print("  0. Kembali" if title != "Menu Utama" else "  0. Keluar")

def get_user_choice(max_choice):
    while True:
        try:
            choice = input("Pilihan (0-{}): ".format(max_choice)).strip()
            if not choice:
                continue
            c = int(choice)
            if 0 <= c <= max_choice:
                return c
            else:
                print("Pilihan di luar rentang.")
        except ValueError:
            print("Masukkan angka.")

# === Handler untuk setiap kategori (masih TODO) ===

def handle_host_discovery(args):
    """
    Menu untuk memilih opsi Host Discovery.
    Mengembalikan list args yang sudah diperbarui.

    Penjelasan tambahan:

    - Deskripsi lebih jelas kegunaan tiap opsi
    - Untuk -PS, -PA, -PU, ditampilkan contoh port yang sesuai
    - Tetap ada validasi sederhana
    """
    options = [
        ("-sn    Ping scan (skip port scan, hanya deteksi host hidup)", "-sn", False),
        ("-Pn    Skip host discovery (anggap semua host up, lewati ping)", "-Pn", False),
        ("-PS    TCP SYN discovery (kirim SYN ke port tertentu, contoh: 22,80)", "-PS", True),
        ("-PA    TCP ACK discovery (kirim ACK ke port tertentu)", "-PA", True),
        ("-PU    UDP discovery (kirim UDP ke port tertentu)", "-PU", True),
        ("-PE    ICMP echo discovery (standar ping ICMP)", "-PE", False),
        ("-PR    ARP discovery (hanya untuk local network, paling akurat)", "-PR", False),
    ]

    while True:
        clear_screen()
        print("\n--- Host Discovery ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            value = input(f"Masukkan port(s) untuk {flag} (contoh: 22,80 atau 1-1000): ").strip()
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            new_arg = flag + value
        else:
            new_arg = flag
        
        args = [arg for arg in args if not arg.startswith(flag)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_scan_techniques(args):
    """
    Menu untuk memilih teknik scan.
    Hanya satu teknik yang boleh aktif (mutually exclusive).

    Penjelasan:

    - Menampilkan 12 teknik scan.
    - Tandai yang sudah dipilih.
    - Saat user memilih satu, semua teknik sebelumnya (dalam daftar tech_flags) dihapus dari args, lalu tambahkan yang baru.
    - Dengan ini, hanya satu teknik scan yang aktif.
    """
    options = [
        ("-sS    TCP SYN scan (default, stealth, port status cepat)", "-sS"),
        ("-sT    TCP connect scan (lengkap, tanpa raw socket)", "-sT"),
        ("-sU    UDP scan (lambat, sering perlu root)", "-sU"),
        ("-sA    TCP ACK scan (firewall mapping, tidak tentukan port terbuka)", "-sA"),
        ("-sW    TCP Window scan (firewall mapping, exploit window size)", "-sW"),
        ("-sM    TCP Maimon scan (packet FIN/ACK, untuk BSD)", "-sM"),
        ("-sN    Null scan (semua flag mati, evasion)", "-sN"),
        ("-sF    FIN scan (hanya FIN, evasion)", "-sF"),
        ("-sX    Xmas scan (FIN/PSH/URG, evasion)", "-sX"),
        ("-sO    IP protocol scan (tentukan protokol IP, bukan port)", "-sO"),
        ("-sY    SCTP INIT scan (SCTP protocol)", "-sY"),
        ("-sZ    SCTP COOKIE-ECHO scan (SCTP)", "-sZ"),
    ]
    # Kumpulan flag teknik untuk dihapus jika ada
    tech_flags = [flag for _, flag in options]

    while True:
        clear_screen()
        print("\n--- Scan Techniques ---")
        for idx, (desc, flag) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")

        choice = get_user_choice(len(options))
        if choice == 0:
            break

        _, flag = options[choice - 1]

        # Hapus semua teknik yang sudah ada (agar hanya satu yang aktif)
        args = [arg for arg in args if not any(arg.startswith(f) for f in tech_flags)]
        args.append(flag)
        print(f"Opsi ditambahkan: {flag}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()

    return args


def handle_port_spec(args):
    """
    Menu untuk menentukan port yang akan di-scan.

    Penjelasan:

    - 5 opsi port specification dengan deskripsi jelas
    - Validasi format untuk -p (angka, range, koma) menggunakan regex
    - Untuk -p dan --top-ports, nilai digabung dengan spasi (--top-ports 100) atau langsung (-p22,80)
    - Port spec bersifat mutually exclusive (hapus yang lama saat pilih baru)
    """
    options = [
        ("-p <port(s)>         Port tertentu (contoh: 22,80,443 atau 1-1000)", "-p", True),
        ("-p-                  Semua 65535 port", "-p-", False),
        ("--top-ports <n>      N port paling umum (contoh: 100)", "--top-ports", True),
        ("-F                   Fast scan (100 port paling umum)", "-F", False),
        ("-r                   Scan port berurutan (tanpa randomisasi)", "-r", False),
    ]
    
    while True:
        clear_screen()
        print("\n--- Port Specification ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            if flag == "-p":
                value = input("Masukkan port(s) (contoh: 22,80,443 atau 1-1000): ").strip()
            elif flag == "--top-ports":
                value = input("Masukkan jumlah port (contoh: 100): ").strip()
            else:
                value = input("Masukkan nilai: ").strip()
            
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            
            # Validasi format untuk -p
            if flag == "-p":
                if not re.match(r'^(\d+(-\d+)?)(,\d+(-\d+)?)*$', value):
                    print("Format port tidak valid. Gunakan angka, range, atau koma (contoh: 22,80,443 atau 1-1000).")
                    input("Tekan Enter...")
                    continue
            
            # Bentuk argumen: untuk -p langsung digabung (misal -p22,80), untuk --top-ports pakai spasi
            if flag == "-p":
                new_arg = flag + value
            else:
                new_arg = flag + " " + value
        else:
            new_arg = flag
        
        # Hapus semua opsi port spec yang lama (hanya satu yang aktif)
        port_flags = ["-p", "-p-", "--top-ports", "-F", "-r"]
        args = [arg for arg in args if not any(arg.startswith(f) for f in port_flags)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_service_version(args):
    """
    Menu untuk konfigurasi deteksi versi service.

    Penjelasan:

    - 4 opsi untuk deteksi versi.
    - --version-intensity meminta angka 0-9 dengan validasi.
    - --version-light dan --version-all adalah shortcut, tidak perlu nilai.
    - Hanya satu opsi versi yang aktif (mutually exclusive).
    - Menghapus opsi versi lama saat memilih baru.
    """
    options = [
        ("-sV                  Deteksi versi service", "-sV", False),
        ("--version-intensity <0-9>  Level intensitas probe (0=ringan, 9=agresif)", "--version-intensity", True),
        ("--version-light      Setara intensity 2 (lebih cepat)", "--version-light", False),
        ("--version-all        Setara intensity 9 (paling teliti)", "--version-all", False),
    ]
    
    while True:
        clear_screen()
        print("\n--- Service/Version Detection ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            value = input("Masukkan intensitas (0-9): ").strip()
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            try:
                intensity = int(value)
                if not 0 <= intensity <= 9:
                    print("Intensitas harus antara 0-9.")
                    input("Tekan Enter...")
                    continue
            except ValueError:
                print("Masukkan angka.")
                input("Tekan Enter...")
                continue
            new_arg = flag + " " + value
        else:
            new_arg = flag
        
        # Hapus opsi versi yang lama jika ada
        version_flags = ["-sV", "--version-intensity", "--version-light", "--version-all"]
        args = [arg for arg in args if not any(arg.startswith(f) for f in version_flags)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_os_detection(args):
    """
    Menu untuk konfigurasi deteksi OS.

    Penjelasan:

    - 3 opsi deteksi OS.
    - Opsi bisa di-toggle (tambah/hapus) karena tidak saling eksklusif (bisa pakai -O --osscan-guess).
    - --osscan-guess dan --osscan-limit hanya valid jika -O aktif, tapi user bebas menambahkannya.
    """
    options = [
        ("-O                  Deteksi OS", "-O", False),
        ("--osscan-guess      Tebak OS agresif walau kurang yakin", "--osscan-guess", False),
        ("--osscan-limit      Skip OS detection kalau host kurang cocok", "--osscan-limit", False),
    ]
    
    while True:
        clear_screen()
        print("\n--- OS Detection ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        new_arg = flag
        
        # Tidak mutual exclusive, bisa dikombinasikan dengan -O
        # Cek apakah flag sudah ada, jika sudah hapus dulu lalu tambah lagi (toggle)
        if flag in args:
            args = [arg for arg in args if arg != flag]
            print(f"Opsi dihapus: {flag}")
        else:
            args.append(new_arg)
            print(f"Opsi ditambahkan: {new_arg}")
        
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_nse_scripts(args):
    """
    Menu untuk NSE Scripts.
    TODO: Nanti ditambah daftar script spesifik.
    """
    options = [
        ("-sC                  Default script set (setara --script=default)", "-sC", False),
        ("--script=<name>      Script tertentu (manual, contoh: http-enum)", "--script", True),
        ("--script=vuln        Kategori vulnerability", "--script=vuln", False),
        ("--script=safe        Kategori aman/non-intrusif", "--script=safe", False),
        ("--script=auth        Kategori autentikasi", "--script=auth", False),
        ("--script=discovery   Kategori discovery", "--script=discovery", False),
        ("--script-args=<args> Argumen untuk script (contoh: http.useragent=xyz)", "--script-args", True),
        ("--script-help=<name> Bantuan untuk script tertentu", "--script-help", True),
    ]
    
    while True:
        clear_screen()
        print("\n--- NSE Scripts ---")
        print("  TODO: Daftar script spesifik akan ditambahkan nanti.")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            if flag == "--script":
                value = input("Masukkan nama script (contoh: http-enum): ").strip()
                if not value:
                    print("Input kosong, lewati.")
                    input("Tekan Enter...")
                    continue
                new_arg = "--script=" + value
            elif flag == "--script-args":
                value = input("Masukkan argumen (contoh: http.useragent=xyz): ").strip()
                if not value:
                    print("Input kosong, lewati.")
                    input("Tekan Enter...")
                    continue
                new_arg = "--script-args=" + value
            elif flag == "--script-help":
                value = input("Masukkan nama script (contoh: http-enum): ").strip()
                if not value:
                    print("Input kosong, lewati.")
                    input("Tekan Enter...")
                    continue
                new_arg = "--script-help=" + value
            else:
                continue
        else:
            new_arg = flag
        
        # Hapus opsi sejenis jika ada
        if flag == "--script" or flag == "--script=vuln" or flag == "--script=safe" or flag == "--script=auth" or flag == "--script=discovery":
            # Hapus semua --script* sebelumnya
            args = [arg for arg in args if not arg.startswith("--script")]
        if flag == "--script-args":
            args = [arg for arg in args if not arg.startswith("--script-args")]
        if flag == "--script-help":
            args = [arg for arg in args if not arg.startswith("--script-help")]
        if flag == "-sC":
            args = [arg for arg in args if arg != "-sC"]
        
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_timing(args):
    """
    Menu untuk timing & performance.

    penjelasan:

    - Untuk -T, pilih salah satu, hapus template sebelumnya.
    - Untuk opsi dengan nilai, user diminta input angka atau format waktu.
    - Hanya opsi dengan nilai yang dimasukkan akan ditambahkan; jika kosong dilewati.
    """
    options = [
        ("-T0                  Paranoid (paling lambat/stealth)", "-T0", False),
        ("-T1                  Sneaky", "-T1", False),
        ("-T2                  Polite", "-T2", False),
        ("-T3                  Normal (default)", "-T3", False),
        ("-T4                  Aggressive", "-T4", False),
        ("-T5                  Insane (tercepat, paling berisik)", "-T5", False),
        ("--min-rate <n>       Kirim minimal n paket/detik", "--min-rate", True),
        ("--max-rate <n>       Batas maksimal paket/detik", "--max-rate", True),
        ("--min-parallelism <n> Jumlah probe paralel minimal", "--min-parallelism", True),
        ("--max-parallelism <n> Jumlah probe paralel maksimal", "--max-parallelism", True),
        ("--host-timeout <time> Timeout per host (contoh: 5s, 10m)", "--host-timeout", True),
        ("--scan-delay <time>  Delay antar probe (contoh: 1s)", "--scan-delay", True),
        ("--max-retries <n>    Maksimal retransmisi", "--max-retries", True),
    ]
    
    while True:
        clear_screen()
        print("\n--- Timing & Performance ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            value = input("Masukkan nilai: ").strip()
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            new_arg = flag + " " + value
        else:
            new_arg = flag
        
        # Hapus opsi timing yang sama, kecuali -T? (timing template) hanya satu yang aktif
        if flag.startswith("-T"):
            timing_flags = ["-T0","-T1","-T2","-T3","-T4","-T5"]
            args = [arg for arg in args if not any(arg.startswith(f) for f in timing_flags)]
        else:
            args = [arg for arg in args if not arg.startswith(flag)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_evasion(args):
    """
    Menu untuk firewall/IDS evasion.

    penjelasan:

    - Semua opsi bersifat aditif (dapat dipilih bersamaan, tidak saling menghapus).
    - Untuk opsi dengan nilai, user diminta input sesuai jenisnya.
    - Tidak ada validasi ketat untuk MAC/IP agar fleksibel, tapi ada pengecekan input kosong.
    """
    options = [
        ("-f                   Fragment packet", "-f", False),
        ("-D <decoy1,decoy2,ME> Decoy scan (contoh: 192.168.1.2,192.168.1.3,ME)", "-D", True),
        ("-S <IP>              Spoof source IP", "-S", True),
        ("-e <interface>       Pilih interface (contoh: eth0)", "-e", True),
        ("-g <port>            Spoof source port", "-g", True),
        ("--data-length <n>    Tambah data random ke paket", "--data-length", True),
        ("--spoof-mac <mac>    Spoof MAC address (contoh: 00:11:22:33:44:55)", "--spoof-mac", True),
        ("--badsum             Kirim checksum salah (test firewall)", "--badsum", False),
    ]
    
    while True:
        clear_screen()
        print("\n--- Firewall/IDS Evasion ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            value = input("Masukkan nilai: ").strip()
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            new_arg = flag + " " + value
        else:
            new_arg = flag
        
        # Hapus opsi yang sama
        args = [arg for arg in args if not arg.startswith(flag)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_output(args):
    """
    Menu untuk output.

    penjelasan:

    - Output file (-oN, -oX, -oG, -oA) bisa dipilih lebih dari satu (misal -oN dan -oX bersama), kecuali -oA yang akan menghapus opsi file spesifik karena sudah mencakup semuanya.
    - Verbose dan debug bersifat mutual exclusive per level (-v vs -vv, -d vs -dd).
    - Opsi toggle (--reason, --open) bisa ditambahkan kapan saja tanpa konflik.
    """
    options = [
        ("-oN <file>           Normal output", "-oN", True),
        ("-oX <file>           XML output", "-oX", True),
        ("-oG <file>           Grepable output", "-oG", True),
        ("-oA <basename>       Semua format sekaligus", "-oA", True),
        ("-v                   Verbose", "-v", False),
        ("-vv                  Very verbose", "-vv", False),
        ("-d                   Debug", "-d", False),
        ("-dd                  Debug level 2", "-dd", False),
        ("--reason             Tampilkan alasan status port", "--reason", False),
        ("--open               Hanya tampilkan port open", "--open", False),
    ]
    
    while True:
        clear_screen()
        print("\n--- Output ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            value = input("Masukkan nama file: ").strip()
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            new_arg = flag + " " + value
        else:
            new_arg = flag
        
        # Hapus opsi output yang sama
        args = [arg for arg in args if not arg.startswith(flag)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

def handle_misc(args):
    """
    Menu untuk opsi misc.

    penjelasan:

    - -A adalah opsi besar yang otomatis mengaktifkan beberapa fitur sekaligus.
    - -n dan -R saling bertentangan; jika pilih salah satu, yang lain dihapus.
    - Opsi lain bersifat aditif.
    - --exclude meminta input daftar target yang dikecualikan (tidak divalidasi ketat, biar fleksibel).
    """
    options = [
        ("-6                   IPv6 scan", "-6", False),
        ("-A                   Aggressive (OS+version+script+traceroute)", "-A", False),
        ("--traceroute         Trace jalur ke target", "--traceroute", False),
        ("-n                   Skip DNS resolution", "-n", False),
        ("-R                   Force DNS resolution", "-R", False),
        ("--packet-trace       Tampilkan paket yang dikirim/diterima", "--packet-trace", False),
        ("--exclude <hosts>    Exclude host tertentu (contoh: 192.168.1.2)", "--exclude", True),
    ]
    
    while True:
        clear_screen()
        print("\n--- Misc ---")
        for idx, (desc, flag, needs_val) in enumerate(options, 1):
            is_selected = any(arg.startswith(flag) for arg in args)
            mark = "  [SUDAH DIPILIH]" if is_selected else ""
            print(f"  {idx}. {desc}{mark}")
        print("  0. Kembali")
        
        choice = get_user_choice(len(options))
        if choice == 0:
            break
        
        desc, flag, needs_val = options[choice - 1]
        
        if needs_val:
            value = input("Masukkan host(s) yang di-exclude: ").strip()
            if not value:
                print("Input kosong, lewati.")
                input("Tekan Enter...")
                continue
            new_arg = flag + " " + value
        else:
            new_arg = flag
        
        # Hapus opsi yang sama
        args = [arg for arg in args if not arg.startswith(flag)]
        args.append(new_arg)
        print(f"Opsi ditambahkan: {new_arg}")
        input("Tekan Enter untuk lanjut...")
        clear_screen()
    
    return args

# === Fungsi tampilan dan eksekusi ===

def show_current_args(args):
    print("\nOpsi terkumpul:", ' '.join(args) if args else "(kosong)")

def reset_args():
    return []

def build_command(targets, args, use_sudo=False):
    cmd = []
    if use_sudo:
        cmd.append("sudo")
    cmd.append("nmap")
    cmd.extend(args)
    cmd.extend(targets)
    return cmd

def execute_scan(cmd):   
    """
    - Menerima command list ["nmap"] + args + targets.
    - Menggunakan subprocess.Popen atau subprocess.run dengan stdout dan stderr dialirkan ke terminal secara real-time (agar user melihat progress scan).
    - Menangani error jika:
    - nmap tidak terinstal (FileNotFoundError).
    - Target tidak reachable (tapi ini ditangani nmap sendiri, kita hanya tampilkan output).
    - Setelah scan selesai, menampilkan ringkasan atau mengembalikan exit code.
    - Memberikan notifikasi "Scan selesai" dan kembali ke menu utama.
    """    
    print("Menjalankan:", ' '.join(cmd))
    try:
        # Jalankan nmap dengan output real-time
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')
        process.wait()
    except FileNotFoundError:
        print("Error: nmap tidak ditemukan. Pastikan nmap terinstal.")
    except Exception as e:
        print(f"Terjadi error: {e}")

def resolve_conflicts(args):
    """
    Deteksi konflik antar opsi nmap. Khususnya -sn tidak valid dengan scan teknik,
    port spec, version, OS, script, -A, --traceroute. Beri user opsi perbaiki.
    Return: list args baru atau None (batal).
    """
    # Definisikan grup konflik
    scan_tech_flags = ['-sS', '-sT', '-sU', '-sA', '-sW', '-sM', '-sN', '-sF', '-sX', '-sO', '-sY', '-sZ']
    port_spec_flags = ['-p', '-p-', '--top-ports', '-F', '-r']
    version_flags = ['-sV', '--version-intensity', '--version-light', '--version-all']
    os_flags = ['-O', '--osscan-guess', '--osscan-limit']
    script_flags = ['-sC', '--script', '--script-args', '--script-help']
    aggressive_flags = ['-A']
    traceroute_flags = ['--traceroute']

    # Opsi yang bertentangan dengan -sn dan -sL
    conflict_with_sn = scan_tech_flags + port_spec_flags + version_flags + os_flags + script_flags + aggressive_flags + traceroute_flags
    conflict_with_sL = conflict_with_sn  # sama, -sL juga tidak valid dengan semua itu

    # Cek apakah ada -sn atau -sL
    has_sn = any(arg.startswith('-sn') for arg in args)
    has_sL = any(arg.startswith('-sL') for arg in args)  # meskipun tidak di menu, antisipasi

    if not has_sn and not has_sL:
        return args  # tidak ada konflik

    # Kumpulkan opsi yang konflik
    conflicting = []
    if has_sn:
        for a in args:
            if a.startswith('-sn'):
                continue  # skip diri sendiri
            # cek apakah a termasuk dalam conflict_with_sn
            for pattern in conflict_with_sn:
                if a.startswith(pattern):
                    conflicting.append(a)
                    break
    if has_sL:
        for a in args:
            if a.startswith('-sL'):
                continue
            for pattern in conflict_with_sL:
                if a.startswith(pattern):
                    conflicting.append(a)
                    break

    # Hapus duplikat
    conflicting = list(dict.fromkeys(conflicting))

    if not conflicting:
        return args

    # Tampilkan peringatan
    clear_screen()
    print("\n" + "="*50)
    print("[!] Konflik opsi terdeteksi!")
    conflict_cause = '-sn' if has_sn else '-sL'
    print(f"Opsi {conflict_cause} (skip port scan) tidak valid bersama:")
    for opt in conflicting:
        print(f"  - {opt}")
    print("="*50)
    print("Pilih tindakan:")
    print("  1. Hapus semua opsi yang konflik (pertahankan {})".format(conflict_cause))
    print("  2. Hapus {} (pertahankan opsi lainnya)".format(conflict_cause))
    print("  3. Batalkan eksekusi")
    choice = get_user_choice(3)

    if choice == 1:
        # Hapus semua conflicting, pertahankan -sn/-sL
        new_args = [arg for arg in args if arg not in conflicting and not arg.startswith('-sL')]  # tapi kita hanya mau hapus conflict, bukan -sL
        # Tapi kita juga harus pastikan -sn tetap ada
        # Lebih simple: hapus semua yang ada di conflicting, dan pastikan -sn/-sL tetap
        new_args = []
        for arg in args:
            if arg.startswith('-sn') or arg.startswith('-sL'):
                new_args.append(arg)
            elif arg not in conflicting:
                new_args.append(arg)
        print(f"Opsi konflik dihapus. {conflict_cause} dipertahankan.")
        input("Tekan Enter...")
        return new_args
    elif choice == 2:
        # Hapus -sn atau -sL
        new_args = [arg for arg in args if not arg.startswith('-sn') and not arg.startswith('-sL')]
        print(f"{conflict_cause} dihapus.")
        input("Tekan Enter...")
        return new_args
    else:
        print("Eksekusi dibatalkan.")
        input("Tekan Enter...")
        return None
    
# === Fungsi utama ===

def main():
    clear_screen()
    print("=== Nmap Scanner Builder ===")
    targets = target()
    if not targets:
        print("Tidak ada target valid. Keluar.")
        return
    clear_screen()
    print("Target tervalidasi:", ', '.join(targets))

    args = []
    use_sudo = False

    while True:
        show_current_args(args)
        sudo_status = "ON" if use_sudo else "OFF"
        print("\nPilih kategori scan:")
        print("  1. Host Discovery")
        print("  2. Scan Techniques")
        print("  3. Port Specification")
        print("  4. Service/Version Detection")
        print("  5. OS Detection")
        print("  6. NSE Scripts")
        print("  7. Timing & Performance")
        print("  8. Firewall/IDS Evasion")
        print("  9. Output")
        print("  10. Misc")
        print("  11. Lihat opsi terkumpul")
        print("  12. Jalankan scan (subprocess)")
        print("  13. Reset opsi")
        print(f"  14. Toggle sudo (root) - current: {sudo_status}")
        print(f"  15. Ganti target (current: {', '.join(targets) if targets else '(kosong)'})")
        print("  0. Keluar")

        choice = get_user_choice(15)   # hanya satu panggilan

        if choice == 0:
            print("Keluar.")
            clear_screen()
            break
        elif choice == 11:
            show_current_args(args)
            input("Tekan Enter untuk lanjut...")
            clear_screen()
        elif choice == 12:
            if not args:
                print("Tidak ada opsi scan dipilih. Jalankan nmap default? (y/n)")
                confirm = input().strip().lower()
                if confirm != 'y':
                    continue
            else:
                # Validasi konflik
                resolved = resolve_conflicts(args)
                if resolved is None:
                    # User membatalkan karena konflik
                    input("Tekan Enter untuk lanjut...")
                    clear_screen()
                    continue
                args = resolved
            cmd = build_command(targets, args, use_sudo)
            execute_scan(cmd)
            input("Tekan Enter untuk lanjut...")
            clear_screen()        
        elif choice == 13:
            args = reset_args()
            print("Opsi di-reset.")
            input("Tekan Enter untuk lanjut...")
            clear_screen()
        elif choice == 14:
            use_sudo = not use_sudo
            print(f"Sudo {'diaktifkan' if use_sudo else 'dinonaktifkan'}.")
            input("Tekan Enter untuk lanjut...")
            clear_screen()
        elif choice == 15:
            targets = change_target(targets)
            clear_screen()
        else:
            # Panggil handler sesuai kategori (1-10)
            if choice == 1:
                args = handle_host_discovery(args)
            elif choice == 2:
                args = handle_scan_techniques(args)
            elif choice == 3:
                args = handle_port_spec(args)
            elif choice == 4:
                args = handle_service_version(args)
            elif choice == 5:
                args = handle_os_detection(args)
            elif choice == 6:
                args = handle_nse_scripts(args)
            elif choice == 7:
                args = handle_timing(args)
            elif choice == 8:
                args = handle_evasion(args)
            elif choice == 9:
                args = handle_output(args)
            elif choice == 10:
                args = handle_misc(args)
            # Setelah handler selesai, bersihkan layar sebelum menu utama
            clear_screen()

if __name__ == "__main__":
    main()
