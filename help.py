spesifikasi = 
'''
Spesifikasi Target
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `nmap <target>` | Memindai satu target (IP atau hostname) . | `nmap scanme.nmap.org`  |
| `nmap <target1 target2>` | Memindai beberapa target sekaligus . | `nmap 192.168.1.1 192.168.1.2` |
| `nmap <range>` | Memindai satu rentang IP . | `nmap 192.168.1.1-10`  |
| `nmap <subnet>` | Memindai seluruh subnet menggunakan notasi CIDR . | `nmap 192.168.1.0/24`  |
| `nmap -iL <file>` | Membaca daftar target dari sebuah file . | `nmap -iL target.txt`  |
'''

deteksi = 
'''
Deteksi Host
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-sL` | **List Scan**: Menampilkan daftar target tanpa mengirim paket . | `nmap -sL 192.168.1.0/24` |
| `-sn` | **Ping Scan**: Menemukan host yang aktif tanpa memindai port . | `nmap -sn 192.168.1.0/24`  |
| `-Pn` | **No Ping**: Melewatkan proses penemuan host, menganggap semua host aktif . | `nmap -Pn 192.168.1.1`  |
| `-n` | **No DNS**: Tidak melakukan resolusi DNS untuk mempercepat proses . | `nmap -n 192.168.1.1` |
'''

teknik = 
'''Teknik Pemindaian Port
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-sS` | **SYN Scan**: Pemindaian "stealth" yang tidak menyelesaikan jabat tangan TCP . | `sudo nmap -sS 192.168.1.1`  |
| `-sT` | **TCP Connect Scan**: Menyelesaikan jabat tangan TCP penuh (default untuk user non-root) . | `nmap -sT 192.168.1.1`  |
| `-sU` | **UDP Scan**: Memindai port UDP (biasanya lambat) . | `sudo nmap -sU 192.168.1.1`  |
| `-sF` / `-sN` / `-sX` | **FIN, NULL, Xmas Scans**: Teknik lanjutan untuk melewati firewall . | `nmap -sF 192.168.1.1` |
'''

port = 
'''Spesifikasi Port
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-p <port>` | Memindai port tertentu . | `nmap -p 22,80,443 192.168.1.1`  |
| `-p <range>` | Memindai rentang port . | `nmap -p 1-1000 192.168.1.1`  |
| `-p-` | Memindai **semua** 65535 port . | `nmap -p- 192.168.1.1`  |
| `-F` | **Fast Mode**: Memindai 100 port yang paling umum . | `nmap -F 192.168.1.1` |
| `--top-ports <n>` | Memindai `n` port yang paling umum . | `nmap --top-ports 100 192.168.1.1`  |
'''

deteksi = 
'''Deteksi Layanan & OS
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-sV` | Mendeteksi versi layanan yang berjalan pada port terbuka . | `nmap -sV 192.168.1.1`  |
| `-O` | Mendeteksi sistem operasi target . | `sudo nmap -O 192.168.1.1`  |
| `-A` | **Aggressive Scan**: Mengaktifkan `-O`, `-sV`, `-sC`, dan `--traceroute` . | `sudo nmap -A 192.168.1.1`  |

### 📜 Nmap Scripting Engine (NSE)
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-sC` | Menjalankan kumpulan script NSE default . | `nmap -sC 192.168.1.1`  |
| `--script <script>` | Menjalankan script atau kategori script tertentu . | `nmap --script=vuln 192.168.1.1`  |
'''

waktu = 
'''
Pengaturan Waktu & Performa
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-T<0-5>` | Mengatur template timing, dari yang paling lambat (0) hingga tercepat (5) . | `nmap -T4 192.168.1.1`  |
| `--max-rate <n>` | Mengirim tidak lebih dari `n` paket per detik . | `nmap --max-rate 100 192.168.1.1` |
'''

evo_spoof = 
'''Evasion & Spoofing
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-f` | Memecah-mecah paket IP untuk melewati firewall . | `sudo nmap -f 192.168.1.1`  |
| `-D <decoy1,decoy2,ME>` | Menggunakan IP umpan untuk menyembunyikan sumber pemindaian . | `nmap -D 10.0.0.1,10.0.0.2,ME 192.168.1.1` |
| `--spoof-mac <MAC>` | Memalsukan alamat MAC sumber . | `nmap --spoof-mac 00:11:22:33:44:55 192.168.1.1` |
'''

output = 
'''Format Output
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-oN <file>` | Menyimpan hasil dalam format normal (human-readable) . | `nmap -oN hasil.txt 192.168.1.1` |
| `-oX <file>` | Menyimpan hasil dalam format XML . | `nmap -oX hasil.xml 192.168.1.1` |
| `-oG <file>` | Menyimpan hasil dalam format `grepable` . | `nmap -oG hasil.gnmap 192.168.1.1` |
| `-oA <basename>` | Menyimpan hasil dalam tiga format utama sekaligus: normal, XML, dan `grepable` . | `nmap -oA hasil 192.168.1.1` |
'''