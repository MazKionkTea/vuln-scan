```python
import subprocess

nmap = subprocess.Popen("nmap")
target = input("target : ")
teknik = input("-sS, -sT, -sU, -sF\nteknik pemindaian port: ")
port = input("spesifikasi port : ")
deteksi = input("deteksi layanan & os : ")
NSE = input()
waktu = input()
eva_spoof = input()
output = input()
```

# nmap
### 🎯 Spesifikasi Target
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `nmap <target>` | Memindai satu target (IP atau hostname) . | `nmap scanme.nmap.org`  |
| `nmap <target1 target2>` | Memindai beberapa target sekaligus . | `nmap 192.168.1.1 192.168.1.2` |
| `nmap <range>` | Memindai satu rentang IP . | `nmap 192.168.1.1-10`  |
| `nmap <subnet>` | Memindai seluruh subnet menggunakan notasi CIDR . | `nmap 192.168.1.0/24`  |
| `nmap -iL <file>` | Membaca daftar target dari sebuah file . | `nmap -iL target.txt`  |

### 🔍 Deteksi Host
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-sL` | **List Scan**: Menampilkan daftar target tanpa mengirim paket . | `nmap -sL 192.168.1.0/24` |
| `-sn` | **Ping Scan**: Menemukan host yang aktif tanpa memindai port . | `nmap -sn 192.168.1.0/24`  |
| `-Pn` | **No Ping**: Melewatkan proses penemuan host, menganggap semua host aktif . | `nmap -Pn 192.168.1.1`  |
| `-n` | **No DNS**: Tidak melakukan resolusi DNS untuk mempercepat proses . | `nmap -n 192.168.1.1` |

### 🚪 Teknik Pemindaian Port
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-sS` | **SYN Scan**: Pemindaian "stealth" yang tidak menyelesaikan jabat tangan TCP . | `sudo nmap -sS 192.168.1.1`  |
| `-sT` | **TCP Connect Scan**: Menyelesaikan jabat tangan TCP penuh (default untuk user non-root) . | `nmap -sT 192.168.1.1`  |
| `-sU` | **UDP Scan**: Memindai port UDP (biasanya lambat) . | `sudo nmap -sU 192.168.1.1`  |
| `-sF` / `-sN` / `-sX` | **FIN, NULL, Xmas Scans**: Teknik lanjutan untuk melewati firewall . | `nmap -sF 192.168.1.1` |

### ⚙️ Spesifikasi Port
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-p <port>` | Memindai port tertentu . | `nmap -p 22,80,443 192.168.1.1`  |
| `-p <range>` | Memindai rentang port . | `nmap -p 1-1000 192.168.1.1`  |
| `-p-` | Memindai **semua** 65535 port . | `nmap -p- 192.168.1.1`  |
| `-F` | **Fast Mode**: Memindai 100 port yang paling umum . | `nmap -F 192.168.1.1` |
| `--top-ports <n>` | Memindai `n` port yang paling umum . | `nmap --top-ports 100 192.168.1.1`  |

### 🧠 Deteksi Layanan & OS
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

### ⏱️ Pengaturan Waktu & Performa
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-T<0-5>` | Mengatur template timing, dari yang paling lambat (0) hingga tercepat (5) . | `nmap -T4 192.168.1.1`  |
| `--max-rate <n>` | Mengirim tidak lebih dari `n` paket per detik . | `nmap --max-rate 100 192.168.1.1` |

### 🛡️ Evasion & Spoofing
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-f` | Memecah-mecah paket IP untuk melewati firewall . | `sudo nmap -f 192.168.1.1`  |
| `-D <decoy1,decoy2,ME>` | Menggunakan IP umpan untuk menyembunyikan sumber pemindaian . | `nmap -D 10.0.0.1,10.0.0.2,ME 192.168.1.1` |
| `--spoof-mac <MAC>` | Memalsukan alamat MAC sumber . | `nmap --spoof-mac 00:11:22:33:44:55 192.168.1.1` |

### 📄 Format Output
| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `-oN <file>` | Menyimpan hasil dalam format normal (human-readable) . | `nmap -oN hasil.txt 192.168.1.1` |
| `-oX <file>` | Menyimpan hasil dalam format XML . | `nmap -oX hasil.xml 192.168.1.1` |
| `-oG <file>` | Menyimpan hasil dalam format `grepable` . | `nmap -oG hasil.gnmap 192.168.1.1` |
| `-oA <basename>` | Menyimpan hasil dalam tiga format utama sekaligus: normal, XML, dan `grepable` . | `nmap -oA hasil 192.168.1.1` |

Semoga daftar ini bermanfaat! Jika ada kategori atau opsi tertentu yang ingin Anda pahami lebih dalam, beri tahu saya.


# subprocess
--Tentu! Berikut adalah daftar perintah dan fungsi dari library `subprocess` Python yang paling umum digunakan, disusun dalam format tabel:

---

### 🔧 Fungsi Utama subprocess

| Perintah | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `subprocess.run()` | Menjalankan perintah dan menunggu hingga selesai. Fungsi utama (rekomendasi) untuk Python 3.5+. | `subprocess.run(["ls", "-l"])` |
| `subprocess.call()` | Menjalankan perintah, menunggu selesai, dan mengembalikan kode keluar (return code). | `subprocess.call(["ping", "-c", "1", "google.com"])` |
| `subprocess.check_call()` | Sama seperti `call()`, tetapi akan memunculkan exception jika return code bukan 0. | `subprocess.check_call(["mkdir", "folder_baru"])` |
| `subprocess.check_output()` | Menjalankan perintah dan mengembalikan output sebagai bytes (string biner). | `output = subprocess.check_output(["echo", "Hello"])` |
| `subprocess.Popen()` | Membuat proses baru secara lebih fleksibel; memberikan kontrol penuh atas I/O, pipa, dan komunikasi. | `proc = subprocess.Popen(["ping", "-c", "4", "google.com"], stdout=subprocess.PIPE)` |

---

### 📌 Argumen Penting (parameter)

| Parameter | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `shell=True` | Menjalankan perintah melalui shell (memungkinkan penggunaan wildcard, pipe `\|`, dll). **Hati-hati risiko keamanan!** | `subprocess.run("ls -l \| grep .txt", shell=True)` |
| `stdout=subprocess.PIPE` | Menangkap output stdout untuk diproses di Python. | `result = subprocess.run(["ls"], stdout=subprocess.PIPE)` |
| `stderr=subprocess.PIPE` | Menangkap output stderr (error) secara terpisah. | `result = subprocess.run(["cmd"], stderr=subprocess.PIPE)` |
| `stdin=subprocess.PIPE` | Mengirim input (data) ke proses yang dijalankan. | `proc = subprocess.Popen(["grep", "error"], stdin=subprocess.PIPE)` |
| `text=True` (atau `universal_newlines=True`) | Mengembalikan output sebagai string (teks), bukan bytes. | `result = subprocess.run(["echo", "Halo"], text=True, capture_output=True)` |
| `capture_output=True` | Menangkap stdout dan stderr secara bersamaan (Python 3.7+). | `result = subprocess.run(["ls"], capture_output=True)` |
| `timeout=<detik>` | Mengatur batas waktu eksekusi; akan memunculkan `TimeoutExpired` jika melebihi. | `subprocess.run(["sleep", "10"], timeout=5)` |
| `env=<dict>` | Menentukan variabel lingkungan khusus untuk proses yang dijalankan. | `subprocess.run(["printenv"], env={"MY_VAR": "nilai"})` |
| `cwd=<path>` | Mengubah direktori kerja sebelum menjalankan perintah. | `subprocess.run(["ls"], cwd="/tmp")` |

---

### 🔄 Metode pada objek Popen

| Metode | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `proc.communicate()` | Mengirim input ke proses dan membaca stdout/stderr. Mengembalikan tuple `(stdout, stderr)`. | `out, err = proc.communicate(input=b"data")` |
| `proc.wait()` | Menunggu proses selesai dan mengembalikan kode keluar. | `returncode = proc.wait()` |
| `proc.poll()` | Mengecek apakah proses masih berjalan (mengembalikan `None`) atau sudah selesai (mengembalikan return code). | `if proc.poll() is not None: print("Selesai")` |
| `proc.terminate()` | Mengirim sinyal SIGTERM untuk menghentikan proses secara halus. | `proc.terminate()` |
| `proc.kill()` | Mengirim sinyal SIGKILL untuk memaksa menghentikan proses. | `proc.kill()` |
| `proc.send_signal(signal)` | Mengirim sinyal tertentu ke proses (misal `signal.SIGINT`). | `proc.send_signal(signal.SIGINT)` |
| `proc.stdin.write()` | Menulis data ke stdin proses (jika dibuat dengan `stdin=PIPE`). | `proc.stdin.write(b"masukan\n")` |
| `proc.stdout.read()` | Membaca output dari stdout proses (jika dibuat dengan `stdout=PIPE`). | `output = proc.stdout.read()` |
| `proc.stderr.read()` | Membaca output error dari stderr proses (jika dibuat dengan `stderr=PIPE`). | `error = proc.stderr.read()` |

---

### ⚠️ Exception yang Sering Muncul

| Exception | Deskripsi | Contoh Kasus |
| :--- | :--- | :--- |
| `subprocess.CalledProcessError` | Muncul jika `check_call()` atau `check_output()` gagal (return code ≠ 0). | `subprocess.check_call(["false"])` |
| `subprocess.TimeoutExpired` | Muncul jika proses melebihi batas waktu yang ditentukan di parameter `timeout`. | `subprocess.run(["sleep", "10"], timeout=2)` |
| `FileNotFoundError` | Muncul jika perintah/executable yang diminta tidak ditemukan. | `subprocess.run(["perintah_tidak_ada"])` |

---

### 💡 Contoh Lengkap Penggunaan

```python
import subprocess

# Menjalankan perintah dan menangkap output sebagai teks
result = subprocess.run(
    ["ping", "-c", "2", "google.com"],
    capture_output=True,
    text=True
)

print("Return code:", result.returncode)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

# Menggunakan Popen untuk interaksi interaktif
proc = subprocess.Popen(
    ["grep", "error"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
out, err = proc.communicate(input="line1\nerror line\nline3")
print("Output grep:", out)
```

---

### 🧠 Tips Keamanan Penting
- **Hindari `shell=True`** jika memungkinkan untuk mencegah serangan **command injection**.
- Gunakan **list argumen** (misal `["ls", "-l"]`) daripada string tunggal.
- Jika menggunakan input dari pengguna, **sanitasi** terlebih dahulu.

Semoga tabel ini membantu! Kalau ada fungsi spesifik yang ingin diperjelas, beri tahu saya ya. 😊
