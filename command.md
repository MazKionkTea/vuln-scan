#  tmux

<details>

| Perintah | Deskripsi | Contoh |
|---|---|---|
| `tmux` | Membuka sesi tmux baru | `tmux` |
| `tmux new -s nama` | Membuat sesi baru dengan nama tertentu | `tmux new -s kerja` |
| `tmux new-session -s nama` | Membuat sesi baru | `tmux new-session -s dev` |
| `tmux ls` | Melihat daftar sesi tmux | `tmux ls` |
| `tmux list-sessions` | Melihat semua sesi | `tmux list-sessions` |
| `tmux attach -t nama` | Masuk kembali ke sesi tertentu | `tmux attach -t kerja` |
| `tmux attach` | Masuk ke sesi terakhir | `tmux attach` |
| `tmux switch-client -t nama` | Berpindah sesi dari dalam tmux | `tmux switch-client -t dev` |
| `tmux has-session -t nama` | Mengecek apakah sesi tersedia | `tmux has-session -t dev` |
| `tmux kill-session -t nama` | Menghapus sesi tertentu | `tmux kill-session -t kerja` |
| `tmux kill-server` | Menghapus semua sesi tmux | `tmux kill-server` |
| `tmux rename-session -t lama baru` | Mengganti nama sesi | `tmux rename-session -t kerja proyek` |
| `tmux detach-client` | Melepaskan client dari sesi | `tmux detach-client -s dev` |

### Shortcut Dasar tmux
| Shortcut | Deskripsi | Contoh |
|---|---|---|
| `Ctrl+b d` | Keluar dari sesi tanpa menghentikan proses (detach) | `Ctrl+b` lalu `d` |
| `Ctrl+b c` | Membuat window baru | `Ctrl+b` lalu `c` |
| `Ctrl+b n` | Pindah ke window berikutnya | `Ctrl+b` lalu `n` |
| `Ctrl+b p` | Pindah ke window sebelumnya | `Ctrl+b` lalu `p` |
| `Ctrl+b 0-9` | Pindah ke window berdasarkan nomor | `Ctrl+b` lalu `1` |
| `Ctrl+b ,` | Mengganti nama window aktif | `Ctrl+b` lalu `,` |
| `Ctrl+b w` | Melihat daftar window | `Ctrl+b` lalu `w` |
| `Ctrl+b &` | Menutup window aktif | `Ctrl+b` lalu `&` |
| `Ctrl+b s` | Melihat dan memilih sesi | `Ctrl+b` lalu `s` |
| `Ctrl+b l` | Kembali ke sesi terakhir | `Ctrl+b` lalu `l` |
| `Ctrl+b $` | Mengganti nama sesi | `Ctrl+b` lalu `$` |

### Window tmux
| Perintah | Deskripsi | Contoh |
|---|---|---|
| `tmux new-window` | Membuat window baru | `tmux new-window` |
| `tmux new-window -n nama` | Membuat window dengan nama | `tmux new-window -n editor` |
| `tmux list-windows` | Melihat daftar window | `tmux list-windows` |
| `tmux rename-window nama` | Mengganti nama window | `tmux rename-window server` |
| `tmux select-window -t nomor` | Memilih window tertentu | `tmux select-window -t 2` |
| `tmux kill-window` | Menghapus window aktif | `tmux kill-window` |
| `Ctrl+b f` | Mencari window berdasarkan nama | `Ctrl+b` lalu `f` |
| `Ctrl+b .` | Memindahkan window ke nomor lain | `Ctrl+b` lalu `.` |

### Panel (Pane) tmux
| Perintah | Deskripsi | Contoh |
|---|---|---|
| `Ctrl+b %` | Membagi panel vertikal | `Ctrl+b` lalu `%` |
| `Ctrl+b "` | Membagi panel horizontal | `Ctrl+b` lalu `"` |
| `tmux split-window -h` | Membagi panel kiri-kanan | `tmux split-window -h` |
| `tmux split-window -v` | Membagi panel atas-bawah | `tmux split-window -v` |
| `Ctrl+b arah` | Berpindah antar panel | `Ctrl+b` lalu `←` |
| `tmux select-pane -L/R/U/D` | Memilih panel berdasarkan arah | `tmux select-pane -L` |
| `tmux list-panes` | Melihat daftar panel | `tmux list-panes` |
| `Ctrl+b x` | Menutup panel aktif | `Ctrl+b` lalu `x` |
| `Ctrl+b z` | Membesarkan panel aktif | `Ctrl+b` lalu `z` |
| `tmux kill-pane` | Menghapus panel aktif | `tmux kill-pane` |
| `tmux resize-pane -L angka` | Memperbesar panel ke kiri | `tmux resize-pane -L 10` |
| `tmux resize-pane -R angka` | Memperbesar panel ke kanan | `tmux resize-pane -R 10` |
| `tmux resize-pane -U angka` | Memperbesar panel ke atas | `tmux resize-pane -U 5` |
| `tmux resize-pane -D angka` | Memperbesar panel ke bawah | `tmux resize-pane -D 5` |
| `tmux swap-pane -D` | Menukar panel ke bawah | `tmux swap-pane -D` |
| `tmux swap-pane -U` | Menukar panel ke atas | `tmux swap-pane -U` |
| `Ctrl+b Space` | Mengganti layout panel | `Ctrl+b` lalu `Space` |
| `Ctrl+b !` | Mengubah panel menjadi window baru | `Ctrl+b` lalu `!` |
| `Ctrl+b {` | Memindahkan panel ke kiri | `Ctrl+b` lalu `{` |
| `Ctrl+b }` | Memindahkan panel ke kanan | `Ctrl+b` lalu `}` |

### Copy Mode dan Buffer
| Perintah | Deskripsi | Contoh |
|---|---|---|
| `Ctrl+b [` | Masuk mode scroll/copy | `Ctrl+b` lalu `[` |
| `Ctrl+b ]` | Paste teks buffer | `Ctrl+b` lalu `]` |
| `tmux capture-pane -p` | Mengambil isi terminal | `tmux capture-pane -p` |
| `tmux save-buffer file.txt` | Menyimpan buffer ke file | `tmux save-buffer output.txt` |
| `tmux load-buffer file.txt` | Memuat buffer dari file | `tmux load-buffer output.txt` |
| `tmux paste-buffer` | Menempelkan buffer | `tmux paste-buffer` |

### Command Mode
| Shortcut | Deskripsi | Contoh |
|---|---|---|
| `Ctrl+b :` | Membuka command mode | `Ctrl+b` lalu `:` |
| `Ctrl+b q` | Menampilkan nomor panel | `Ctrl+b` lalu `q` |
| `Ctrl+b t` | Menampilkan jam | `Ctrl+b` lalu `t` |

### Konfigurasi ~/.tmux.conf
| Konfigurasi | Deskripsi | Contoh |
|---|---|---|
| `set -g mouse on` | Mengaktifkan mouse | `set -g mouse on` |
| `set -g history-limit angka` | Mengatur jumlah history | `set -g history-limit 10000` |
| `set -g base-index 1` | Nomor window mulai dari 1 | `set -g base-index 1` |
| `set -g pane-base-index 1` | Nomor panel mulai dari 1 | `set -g pane-base-index 1` |
| `setw -g mode-keys vi` | Menggunakan mode Vim | `setw -g mode-keys vi` |
| `set -g status off` | Menyembunyikan status bar | `set -g status off` |
| `tmux source-file ~/.tmux.conf` | Memuat ulang konfigurasi | `tmux source-file ~/.tmux.conf` |

### Perintah Keluar
| Perintah | Deskripsi | Contoh |
|---|---|---|
| `exit` | Keluar dari shell/panel aktif | `exit` |
| `Ctrl+d` | Keluar dari shell aktif | `Ctrl+d` |

</details>

---

# nmap

<details>

| Command | Deskripsi | Contoh |
|---|---|---|
| `nmap TARGET` | Scan dasar terhadap target | `nmap 192.168.1.1` |
| `nmap HOSTNAME` | Scan berdasarkan hostname | `nmap scanme.nmap.org` |
| `nmap IP1 IP2` | Scan beberapa target sekaligus | `nmap 192.168.1.1 192.168.1.2` |
| `nmap 192.168.1.0/24` | Scan seluruh subnet | `nmap 192.168.1.0/24` |
| `nmap 192.168.1.1-254` | Scan rentang alamat IP | `nmap 192.168.1.1-254` |
| `nmap -iL FILE` | Membaca daftar target dari file | `nmap -iL targets.txt` |
| `nmap -iR N` | Memilih target secara acak | `nmap -iR 10` |
| `nmap --exclude HOST` | Mengecualikan host tertentu | `nmap 192.168.1.0/24 --exclude 192.168.1.10` |
| `nmap --excludefile FILE` | Mengecualikan target berdasarkan file | `nmap 192.168.1.0/24 --excludefile exclude.txt` |
| `nmap -sL TARGET` | List Scan tanpa melakukan port scan | `nmap -sL 192.168.1.0/24` |
| `nmap -sn TARGET` | Host discovery tanpa port scan | `nmap -sn 192.168.1.0/24` |
| `nmap -Pn TARGET` | Menganggap semua host aktif dan melewati host discovery | `nmap -Pn 192.168.1.10` |
| `nmap -PS PORT TARGET` | TCP SYN ping ke port tertentu | `nmap -PS80,443 192.168.1.0/24` |
| `nmap -PA PORT TARGET` | TCP ACK ping ke port tertentu | `nmap -PA80,443 192.168.1.0/24` |
| `nmap -PU PORT TARGET` | UDP ping ke port tertentu | `nmap -PU53,161 192.168.1.0/24` |
| `nmap -PE TARGET` | ICMP Echo discovery | `nmap -PE 192.168.1.0/24` |
| `nmap -PP TARGET` | ICMP Timestamp discovery | `nmap -PP 192.168.1.0/24` |
| `nmap -PM TARGET` | ICMP Address Mask discovery | `nmap -PM 192.168.1.0/24` |
| `nmap -PR TARGET` | ARP discovery pada jaringan Ethernet lokal | `nmap -PR 192.168.1.0/24` |
| `nmap -PY PORT TARGET` | SCTP INIT discovery | `nmap -PY5000 192.168.1.0/24` |
| `nmap -PO PROTOCOL TARGET` | IP Protocol Ping | `nmap -PO1,2,6 192.168.1.10` |
| `nmap -n TARGET` | Menonaktifkan reverse DNS resolution | `nmap -n 192.168.1.0/24` |
| `nmap -R TARGET` | Selalu melakukan reverse DNS resolution | `nmap -R 192.168.1.10` |
| `nmap --dns-servers SERVER TARGET` | Menggunakan DNS server tertentu | `nmap --dns-servers 8.8.8.8 example.com` |
| `nmap -sS TARGET` | TCP SYN scan | `nmap -sS 192.168.1.10` |
| `nmap -sT TARGET` | TCP Connect scan | `nmap -sT 192.168.1.10` |
| `nmap -sU TARGET` | UDP scan | `nmap -sU 192.168.1.10` |
| `nmap -sF TARGET` | TCP FIN scan | `nmap -sF 192.168.1.10` |
| `nmap -sN TARGET` | TCP NULL scan | `nmap -sN 192.168.1.10` |
| `nmap -sX TARGET` | TCP Xmas scan | `nmap -sX 192.168.1.10` |
| `nmap -sA TARGET` | TCP ACK scan | `nmap -sA 192.168.1.10` |
| `nmap -sW TARGET` | TCP Window scan | `nmap -sW 192.168.1.10` |
| `nmap -sM TARGET` | TCP Maimon scan | `nmap -sM 192.168.1.10` |
| `nmap -sI ZOMBIE TARGET` | TCP Idle scan menggunakan zombie host | `nmap -sI 192.168.1.20 192.168.1.10` |
| `nmap -sO TARGET` | IP Protocol scan | `nmap -sO 192.168.1.10` |
| `nmap -sY TARGET` | SCTP INIT scan | `nmap -sY 192.168.1.10` |
| `nmap -sZ TARGET` | SCTP COOKIE-ECHO scan | `nmap -sZ 192.168.1.10` |
| `nmap -b FTP_RELAY TARGET` | FTP bounce scan | `nmap -b ftp.example.com 192.168.1.10` |
| `nmap --scanflags FLAGS TARGET` | Menentukan flag TCP secara manual | `nmap --scanflags SYNFIN 192.168.1.10` |
| `nmap -p PORT TARGET` | Scan port tertentu | `nmap -p 80 192.168.1.10` |
| `nmap -p PORT1,PORT2 TARGET` | Scan beberapa port tertentu | `nmap -p 22,80,443 192.168.1.10` |
| `nmap -p 1-1000 TARGET` | Scan rentang port | `nmap -p 1-1000 192.168.1.10` |
| `nmap -p- TARGET` | Scan semua port TCP 1-65535 | `nmap -p- 192.168.1.10` |
| `nmap -p U:PORT TARGET` | Menentukan port UDP | `nmap -p U:53,161 192.168.1.10` |
| `nmap -p T:PORT TARGET` | Menentukan port TCP | `nmap -p T:22,80,443 192.168.1.10` |
| `nmap -p S:PORT TARGET` | Menentukan port SCTP | `nmap -p S:2905 192.168.1.10` |
| `nmap -p T:80,U:53 TARGET` | Scan port TCP dan UDP tertentu | `nmap -p T:80,U:53 192.168.1.10` |
| `nmap --exclude-ports PORTS TARGET` | Mengecualikan port tertentu dari scan | `nmap --exclude-ports 25,110 192.168.1.10` |
| `nmap -F TARGET` | Fast scan terhadap port umum | `nmap -F 192.168.1.10` |
| `nmap --top-ports N TARGET` | Scan N port paling umum | `nmap --top-ports 100 192.168.1.10` |
| `nmap -r TARGET` | Scan port secara berurutan | `nmap -r 192.168.1.10` |
| `nmap --port-ratio RATIO TARGET` | Scan port dengan rasio frekuensi tertentu atau lebih tinggi | `nmap --port-ratio 0.1 192.168.1.10` |
| `nmap -sV TARGET` | Mendeteksi service dan versi | `nmap -sV 192.168.1.10` |
| `nmap --version-intensity LEVEL TARGET` | Mengatur intensitas version detection | `nmap -sV --version-intensity 5 192.168.1.10` |
| `nmap --version-light TARGET` | Menggunakan version detection dengan probe lebih sedikit | `nmap -sV --version-light 192.168.1.10` |
| `nmap --version-all TARGET` | Mencoba seluruh probe version detection | `nmap -sV --version-all 192.168.1.10` |
| `nmap --version-trace TARGET` | Menampilkan detail proses version detection | `nmap -sV --version-trace 192.168.1.10` |
| `nmap -sC TARGET` | Menjalankan default NSE scripts | `nmap -sC 192.168.1.10` |
| `nmap --script SCRIPT TARGET` | Menjalankan NSE script tertentu | `nmap --script http-title 192.168.1.10` |
| `nmap --script SCRIPT1,SCRIPT2 TARGET` | Menjalankan beberapa NSE script | `nmap --script http-title,http-headers 192.168.1.10` |
| `nmap --script CATEGORY TARGET` | Menjalankan kategori NSE tertentu | `nmap --script safe 192.168.1.10` |
| `nmap --script "PATTERN" TARGET` | Menjalankan script berdasarkan pola | `nmap --script "http-*" 192.168.1.10` |
| `nmap --script-args ARG=VALUE TARGET` | Memberikan argumen kepada NSE script | `nmap --script http-title --script-args http.useragent="Mozilla/5.0" 192.168.1.10` |
| `nmap --script-args-file FILE TARGET` | Membaca argumen NSE dari file | `nmap --script http-title --script-args-file args.txt 192.168.1.10` |
| `nmap --script-help SCRIPT` | Menampilkan bantuan NSE script | `nmap --script-help http-title` |
| `nmap --script-trace TARGET` | Menampilkan seluruh komunikasi NSE | `nmap --script http-title --script-trace 192.168.1.10` |
| `nmap --script-updatedb` | Memperbarui database indeks NSE script | `nmap --script-updatedb` |
| `nmap -O TARGET` | Mendeteksi sistem operasi | `nmap -O 192.168.1.10` |
| `nmap --osscan-limit TARGET` | Membatasi OS detection hanya pada target yang cocok | `nmap -O --osscan-limit 192.168.1.0/24` |
| `nmap --osscan-guess TARGET` | Mencoba menebak OS secara lebih agresif | `nmap -O --osscan-guess 192.168.1.10` |
| `nmap --fuzzy TARGET` | Alias untuk OS detection guessing | `nmap -O --fuzzy 192.168.1.10` |
| `nmap --max-os-tries N TARGET` | Mengatur jumlah percobaan OS detection | `nmap -O --max-os-tries 2 192.168.1.10` |
| `nmap -A TARGET` | Mengaktifkan OS detection, version detection, default scripts, dan traceroute | `nmap -A 192.168.1.10` |
| `nmap --traceroute TARGET` | Melakukan traceroute menuju target | `nmap --traceroute 192.168.1.10` |
| `nmap -T0 TARGET` | Timing paranoid, sangat lambat | `nmap -T0 192.168.1.10` |
| `nmap -T1 TARGET` | Timing sneaky, lambat | `nmap -T1 192.168.1.10` |
| `nmap -T2 TARGET` | Timing polite | `nmap -T2 192.168.1.10` |
| `nmap -T3 TARGET` | Timing normal | `nmap -T3 192.168.1.10` |
| `nmap -T4 TARGET` | Timing aggressive | `nmap -T4 192.168.1.10` |
| `nmap -T5 TARGET` | Timing insane, sangat cepat | `nmap -T5 192.168.1.10` |
| `nmap --min-hostgroup SIZE TARGET` | Menentukan ukuran minimum host group | `nmap --min-hostgroup 32 192.168.1.0/24` |
| `nmap --max-hostgroup SIZE TARGET` | Menentukan ukuran maksimum host group | `nmap --max-hostgroup 64 192.168.1.0/24` |
| `nmap --min-parallelism NUM TARGET` | Menentukan minimum probe paralel | `nmap --min-parallelism 10 192.168.1.10` |
| `nmap --max-parallelism NUM TARGET` | Membatasi probe paralel | `nmap --max-parallelism 20 192.168.1.10` |
| `nmap --min-rtt-timeout TIME TARGET` | Menentukan minimum RTT timeout | `nmap --min-rtt-timeout 100ms 192.168.1.10` |
| `nmap --max-rtt-timeout TIME TARGET` | Menentukan maksimum RTT timeout | `nmap --max-rtt-timeout 1s 192.168.1.10` |
| `nmap --initial-rtt-timeout TIME TARGET` | Menentukan initial RTT timeout | `nmap --initial-rtt-timeout 500ms 192.168.1.10` |
| `nmap --max-retries N TARGET` | Membatasi jumlah retransmission probe | `nmap --max-retries 2 192.168.1.10` |
| `nmap --host-timeout TIME TARGET` | Membatasi waktu maksimum per host | `nmap --host-timeout 30s 192.168.1.10` |
| `nmap --scan-delay TIME TARGET` | Memberikan jeda antar probe | `nmap --scan-delay 1s 192.168.1.10` |
| `nmap --max-scan-delay TIME TARGET` | Membatasi maksimum jeda antar probe | `nmap --max-scan-delay 5s 192.168.1.10` |
| `nmap --defeat-rst-ratelimit TARGET` | Mengabaikan pembatasan RST pada kondisi tertentu untuk mempercepat scan | `nmap --defeat-rst-ratelimit 192.168.1.10` |
| `nmap --defeat-icmp-ratelimit TARGET` | Mengurangi dampak ICMP rate limiting pada scan UDP | `nmap -sU --defeat-icmp-ratelimit 192.168.1.10` |
| `nmap -f TARGET` | Memecah paket IP menjadi fragment | `nmap -f 192.168.1.10` |
| `nmap -ff TARGET` | Menggunakan fragmentasi IP yang lebih kecil | `nmap -ff 192.168.1.10` |
| `nmap --mtu SIZE TARGET` | Menentukan ukuran MTU fragmentasi | `nmap --mtu 24 192.168.1.10` |
| `nmap -D DECOY1,DECOY2,ME TARGET` | Menggunakan decoy addresses pada scan | `nmap -D 192.168.1.20,192.168.1.30,ME 192.168.1.10` |
| `nmap -S IP TARGET` | Memalsukan source IP address | `nmap -S 192.168.1.20 192.168.1.10` |
| `nmap -e INTERFACE TARGET` | Menggunakan network interface tertentu | `nmap -e eth0 192.168.1.10` |
| `nmap -g PORT TARGET` | Menggunakan source port tertentu | `nmap -g 53 192.168.1.10` |
| `nmap --source-port PORT TARGET` | Menentukan source port | `nmap --source-port 53 192.168.1.10` |
| `nmap --proxies URL TARGET` | Menggunakan proxy untuk koneksi tertentu | `nmap --proxies http://127.0.0.1:8080 192.168.1.10` |
| `nmap --data-length LENGTH TARGET` | Menambahkan data acak dengan panjang tertentu ke paket | `nmap --data-length 20 192.168.1.10` |
| `nmap --ip-options OPTIONS TARGET` | Menentukan opsi IP header | `nmap --ip-options R 192.168.1.10` |
| `nmap --ttl VALUE TARGET` | Menentukan IP TTL | `nmap --ttl 64 192.168.1.10` |
| `nmap --spoof-mac MAC TARGET` | Menggunakan MAC address tertentu atau vendor tertentu | `nmap --spoof-mac 00:11:22:33:44:55 192.168.1.10` |
| `nmap --badsum TARGET` | Menggunakan checksum IP/TCP/UDP yang salah untuk probe | `nmap --badsum 192.168.1.10` |
| `nmap --send-eth TARGET` | Mengirim paket melalui raw Ethernet | `nmap --send-eth 192.168.1.10` |
| `nmap --send-ip TARGET` | Mengirim paket melalui raw IP | `nmap --send-ip 192.168.1.10` |
| `nmap -6 TARGET` | Mengaktifkan scanning IPv6 | `nmap -6 2001:db8::1` |
| `nmap -4 TARGET` | Memaksa penggunaan IPv4 | `nmap -4 example.com` |
| `nmap --reason TARGET` | Menampilkan alasan port/host mendapatkan status tertentu | `nmap --reason 192.168.1.10` |
| `nmap --open TARGET` | Hanya menampilkan port yang open atau mungkin open | `nmap --open 192.168.1.10` |
| `nmap -v TARGET` | Meningkatkan verbosity output | `nmap -v 192.168.1.10` |
| `nmap -vv TARGET` | Verbosity lebih tinggi | `nmap -vv 192.168.1.10` |
| `nmap -d TARGET` | Mengaktifkan debugging | `nmap -d 192.168.1.10` |
| `nmap -dd TARGET` | Debugging dengan tingkat lebih tinggi | `nmap -dd 192.168.1.10` |
| `nmap --packet-trace TARGET` | Menampilkan paket yang dikirim dan diterima | `nmap --packet-trace 192.168.1.10` |
| `nmap --iflist` | Menampilkan interface dan route jaringan | `nmap --iflist` |
| `nmap -oN FILE TARGET` | Menyimpan output dalam format normal | `nmap -oN scan.txt 192.168.1.10` |
| `nmap -oX FILE TARGET` | Menyimpan output dalam format XML | `nmap -oX scan.xml 192.168.1.10` |
| `nmap -oS FILE TARGET` | Menyimpan output dalam format s|<r>I|p|t | `nmap -oS scan.txt 192.168.1.10` |
| `nmap -oG FILE TARGET` | Menyimpan output dalam format grepable | `nmap -oG scan.gnmap 192.168.1.10` |
| `nmap -oA BASENAME TARGET` | Menyimpan output dalam format normal, XML, dan grepable | `nmap -oA scan 192.168.1.10` |
| `nmap --append-output TARGET` | Menambahkan hasil ke file output yang sudah ada | `nmap -oN scan.txt --append-output 192.168.1.10` |
| `nmap --resume FILE` | Melanjutkan scan dari file output normal | `nmap --resume scan.txt` |
| `nmap --stylesheet PATH FILE.xml` | Menggunakan stylesheet XSL untuk output XML | `nmap -oX scan.xml --stylesheet style.xsl 192.168.1.10` |
| `nmap --webxml TARGET` | Menghasilkan XML yang cocok untuk stylesheet web resmi Nmap | `nmap -oX scan.xml --webxml 192.168.1.10` |
| `nmap --no-stylesheet TARGET` | Menghilangkan referensi stylesheet dari output XML | `nmap -oX scan.xml --no-stylesheet 192.168.1.10` |
| `nmap -oN - TARGET` | Mengirim normal output ke stdout | `nmap -oN - 192.168.1.10` |
| `nmap -oX - TARGET` | Mengirim XML output ke stdout | `nmap -oX - 192.168.1.10` |
| `nmap -oG - TARGET` | Mengirim grepable output ke stdout | `nmap -oG - 192.168.1.10` |
| `nmap --stats-every TIME TARGET` | Menampilkan statistik progres secara berkala | `nmap --stats-every 10s 192.168.1.0/24` |
| `nmap --noninteractive TARGET` | Menonaktifkan interaksi runtime tertentu | `nmap --noninteractive 192.168.1.10` |
| `nmap -d9 TARGET` | Mengaktifkan debugging level tinggi | `nmap -d9 192.168.1.10` |
| `nmap --log-errors TARGET` | Mencatat error ke output | `nmap --log-errors 192.168.1.10` |
| `nmap --append-output TARGET` | Menambahkan hasil ke file output, bukan menimpanya | `nmap -oN scan.txt --append-output 192.168.1.10` |
| `nmap --resume FILENAME` | Melanjutkan scan yang terhenti dari file output | `nmap --resume scan.txt` |
| `nmap -6 -sV TARGET` | Version detection pada IPv6 | `nmap -6 -sV 2001:db8::1` |
| `nmap -sV -p PORT TARGET` | Mendeteksi service/version pada port tertentu | `nmap -sV -p 80,443 192.168.1.10` |
| `nmap -sC -sV TARGET` | Menjalankan default scripts dan version detection | `nmap -sC -sV 192.168.1.10` |
| `nmap -A -T4 TARGET` | Scan agresif dengan timing T4 | `nmap -A -T4 192.168.1.10` |
| `nmap -Pn -p- TARGET` | Scan semua port tanpa host discovery | `nmap -Pn -p- 192.168.1.10` |
| `nmap -sn -PE TARGET` | Host discovery menggunakan ICMP Echo | `nmap -sn -PE 192.168.1.0/24` |
| `nmap -sn -PS80,443 TARGET` | Host discovery menggunakan TCP SYN | `nmap -sn -PS80,443 192.168.1.0/24` |
| `nmap -sn -PR TARGET` | Host discovery menggunakan ARP pada LAN | `nmap -sn -PR 192.168.1.0/24` |
| `nmap -p 22,80,443 --open TARGET` | Hanya menampilkan port tertentu yang terbuka | `nmap -p 22,80,443 --open 192.168.1.10` |
| `nmap -sU -p 53,161 TARGET` | Scan UDP pada port tertentu | `nmap -sU -p 53,161 192.168.1.10` |
| `nmap -sS -sV -O TARGET` | SYN scan dengan service/version dan OS detection | `nmap -sS -sV -O 192.168.1.10` |
| `nmap -A -p- TARGET` | Scan agresif seluruh port TCP | `nmap -A -p- 192.168.1.10` |
| `nmap --top-ports 100 -sV TARGET` | Scan 100 port umum sekaligus version detection | `nmap --top-ports 100 -sV 192.168.1.10` |
| `nmap -iL targets.txt -oA results` | Scan target dari file dan menyimpan tiga format output | `nmap -iL targets.txt -oA results` |
| `nmap -sV --version-light TARGET` | Version detection ringan | `nmap -sV --version-light 192.168.1.10` |
| `nmap -sC TARGET` | Menjalankan kumpulan default NSE scripts | `nmap -sC 192.168.1.10` |
| `nmap --script vuln TARGET` | Menjalankan kategori NSE terkait pemeriksaan vulnerability | `nmap --script vuln 192.168.1.10` |
| `nmap --script safe TARGET` | Menjalankan kategori NSE yang diklasifikasikan safe | `nmap --script safe 192.168.1.10` |
| `nmap --script discovery TARGET` | Menjalankan kategori discovery NSE | `nmap --script discovery 192.168.1.10` |
| `nmap --script version TARGET` | Menjalankan script NSE kategori version | `nmap --script version 192.168.1.10` |
| `nmap --script-help '*'` | Menampilkan bantuan script NSE | `nmap --script-help '*'` |
| `nmap --version` | Menampilkan versi Nmap | `nmap --version` |
| `nmap -V` | Alias untuk menampilkan versi Nmap | `nmap -V` |
| `nmap -h` | Menampilkan bantuan singkat | `nmap -h` |
| `nmap --help` | Menampilkan bantuan penggunaan | `nmap --help` |
| `nmap -h --help` | Menampilkan ringkasan opsi bantuan | `nmap -h` |
| `nmap --iflist` | Menampilkan daftar interface dan route | `nmap --iflist` |
| `nmap --privileged TARGET` | Menganggap user memiliki hak istimewa untuk raw packet operations | `nmap --privileged 192.168.1.10` |
| `nmap --unprivileged TARGET` | Menganggap user tidak memiliki hak raw packet | `nmap --unprivileged 192.168.1.10` |
| `nmap --release-memory TARGET` | Melepaskan memori sebelum keluar | `nmap --release-memory 192.168.1.10` |
| `nmap --datadir DIRECTORY TARGET` | Menentukan direktori data Nmap | `nmap --datadir /usr/share/nmap 192.168.1.10` |
| `nmap --servicedb FILE TARGET` | Menggunakan service database tertentu | `nmap --servicedb services.txt 192.168.1.10` |
| `nmap --versiondb FILE TARGET` | Menggunakan version detection database tertentu | `nmap --versiondb nmap-service-probes 192.168.1.10` |
| `nmap --system-dns TARGET` | Menggunakan DNS resolver sistem | `nmap --system-dns example.com` |
| `nmap --resolve-all TARGET` | Memindai seluruh alamat hasil resolusi hostname | `nmap --resolve-all example.com` |
| `nmap --unique TARGET` | Memindai setiap IP hanya sekali setelah resolusi | `nmap --unique example.com` |
| `nmap --privileged -sS TARGET` | Menjalankan SYN scan dengan asumsi hak istimewa | `nmap --privileged -sS 192.168.1.10` |
| `nmap --unprivileged -sT TARGET` | Memaksa perilaku scan tanpa raw packet privilege | `nmap --unprivileged -sT 192.168.1.10` |
| `nmap --resume FILE` | Melanjutkan scan dari file output sebelumnya | `nmap --resume scan.nmap` |

</details>

---

# curl

<details>

| Command | Deskripsi | Contoh |
|---|---|---|
| `curl URL` | Mengambil resource dari URL menggunakan HTTP/HTTPS | `curl https://example.com` |
| `curl -o FILE URL` | Menyimpan output ke file dengan nama tertentu | `curl -o page.html https://example.com` |
| `curl -O URL` | Mengunduh file menggunakan nama file dari URL | `curl -O https://example.com/file.zip` |
| `curl -L URL` | Mengikuti redirect HTTP | `curl -L https://example.com` |
| `curl -I URL` | Mengambil HTTP header saja | `curl -I https://example.com` |
| `curl -i URL` | Menampilkan HTTP header dan response body | `curl -i https://example.com` |
| `curl -v URL` | Menampilkan detail proses koneksi dan request | `curl -v https://example.com` |
| `curl -s URL` | Menjalankan curl tanpa progress meter | `curl -s https://example.com` |
| `curl -S URL` | Menampilkan error meskipun menggunakan silent mode | `curl -sS https://example.com` |
| `curl -f URL` | Menganggap HTTP 4xx/5xx sebagai error | `curl -f https://example.com` |
| `curl -w FORMAT URL` | Menampilkan informasi tambahan setelah request | `curl -w "%{http_code}\n" https://example.com` |
| `curl -X METHOD URL` | Menentukan HTTP method secara manual | `curl -X DELETE https://example.com/users/1` |
| `curl -G URL` | Mengirim data sebagai query parameter GET | `curl -G -d "q=curl" https://example.com/search` |
| `curl -d DATA URL` | Mengirim data menggunakan POST | `curl -d "name=John" https://example.com/users` |
| `curl --data-raw DATA URL` | Mengirim data POST tanpa interpretasi khusus | `curl --data-raw '{"name":"John"}' https://example.com` |
| `curl --data-binary DATA URL` | Mengirim data secara binary/raw | `curl --data-binary @data.json https://example.com` |
| `curl -d @FILE URL` | Mengirim isi file sebagai data POST | `curl -d @data.json https://example.com` |
| `curl --json DATA URL` | Mengirim data JSON dengan header JSON yang sesuai | `curl --json '{"name":"John"}' https://api.example.com/users` |
| `curl -H "Header: Value" URL` | Menambahkan HTTP header | `curl -H "Accept: application/json" https://api.example.com` |
| `curl -A "User-Agent" URL` | Mengubah User-Agent | `curl -A "Mozilla/5.0" https://example.com` |
| `curl -e URL URL` | Menentukan HTTP Referer | `curl -e "https://google.com" https://example.com` |
| `curl -b "name=value" URL` | Mengirim cookie | `curl -b "session=abc123" https://example.com` |
| `curl -c FILE URL` | Menyimpan cookie ke file | `curl -c cookies.txt https://example.com` |
| `curl -b FILE URL` | Membaca cookie dari file | `curl -b cookies.txt https://example.com` |
| `curl -u USER:PASS URL` | Menggunakan HTTP Basic Authentication | `curl -u admin:secret https://example.com` |
| `curl --digest -u USER:PASS URL` | Menggunakan HTTP Digest Authentication | `curl --digest -u admin:secret https://example.com` |
| `curl -F "field=value" URL` | Mengirim form multipart | `curl -F "name=John" https://example.com/upload` |
| `curl -F "file=@FILE" URL` | Mengunggah file melalui multipart form | `curl -F "file=@photo.jpg" https://example.com/upload` |
| `curl -T FILE URL` | Mengunggah file ke URL | `curl -T file.txt https://example.com/file.txt` |
| `curl -X POST URL` | Mengirim HTTP POST | `curl -X POST https://api.example.com/users` |
| `curl -X PUT URL` | Mengirim HTTP PUT | `curl -X PUT https://api.example.com/users/1` |
| `curl -X PATCH URL` | Mengirim HTTP PATCH | `curl -X PATCH https://api.example.com/users/1` |
| `curl -X DELETE URL` | Mengirim HTTP DELETE | `curl -X DELETE https://api.example.com/users/1` |
| `curl -X OPTIONS URL` | Mengirim HTTP OPTIONS | `curl -X OPTIONS https://example.com` |
| `curl -X HEAD URL` | Mengirim HTTP HEAD | `curl -X HEAD https://example.com` |
| `curl -x PROXY URL` | Menggunakan proxy | `curl -x http://proxy:8080 https://example.com` |
| `curl --proxy-user USER:PASS URL` | Autentikasi ke proxy | `curl -x http://proxy:8080 --proxy-user user:pass https://example.com` |
| `curl --noproxy HOST URL` | Melewati proxy untuk host tertentu | `curl --noproxy localhost http://localhost:8080` |
| `curl -k URL` | Melewati verifikasi sertifikat TLS | `curl -k https://internal.example.com` |
| `curl --cacert FILE URL` | Menggunakan CA certificate tertentu | `curl --cacert ca.pem https://example.com` |
| `curl --cert FILE URL` | Menggunakan client certificate | `curl --cert client.pem https://example.com` |
| `curl --key FILE URL` | Menentukan private key client certificate | `curl --cert client.pem --key client.key https://example.com` |
| `curl --tlsv1.2 URL` | Menggunakan TLS 1.2 atau lebih baru | `curl --tlsv1.2 https://example.com` |
| `curl --tls-max VERSION URL` | Membatasi versi TLS maksimum | `curl --tls-max 1.2 https://example.com` |
| `curl --http1.1 URL` | Memaksa penggunaan HTTP/1.1 | `curl --http1.1 https://example.com` |
| `curl --http2 URL` | Menggunakan HTTP/2 | `curl --http2 https://example.com` |
| `curl --http3 URL` | Menggunakan HTTP/3 jika tersedia | `curl --http3 https://example.com` |
| `curl --compressed URL` | Meminta dan menangani response terkompresi | `curl --compressed https://example.com` |
| `curl --limit-rate RATE URL` | Membatasi kecepatan transfer | `curl --limit-rate 1M https://example.com/file.zip` |
| `curl --max-time SECONDS URL` | Membatasi total waktu request | `curl --max-time 10 https://example.com` |
| `curl --connect-timeout SECONDS URL` | Membatasi waktu koneksi | `curl --connect-timeout 5 https://example.com` |
| `curl --retry N URL` | Mengulangi request ketika terjadi kegagalan tertentu | `curl --retry 3 https://example.com` |
| `curl --retry-delay SECONDS URL` | Memberikan jeda antar retry | `curl --retry 3 --retry-delay 2 https://example.com` |
| `curl --retry-all-errors URL` | Mengizinkan retry untuk berbagai error | `curl --retry 3 --retry-all-errors https://example.com` |
| `curl -C - -O URL` | Melanjutkan download yang terputus | `curl -C - -O https://example.com/file.zip` |
| `curl -r RANGE URL` | Mengunduh bagian byte tertentu dari file | `curl -r 0-999 https://example.com/file` |
| `curl --remote-name-all URL` | Mengunduh beberapa URL menggunakan nama file remote | `curl --remote-name-all https://example.com/a.txt https://example.com/b.txt` |
| `curl --parallel URL...` | Menjalankan beberapa transfer secara paralel | `curl --parallel -O https://example.com/a https://example.com/b` |
| `curl --interface IFACE URL` | Menggunakan network interface tertentu | `curl --interface eth0 https://example.com` |
| `curl --ipv4 URL` | Memaksa penggunaan IPv4 | `curl --ipv4 https://example.com` |
| `curl --ipv6 URL` | Memaksa penggunaan IPv6 | `curl --ipv6 https://example.com` |
| `curl --resolve HOST:PORT:IP URL` | Memetakan hostname ke IP tertentu | `curl --resolve example.com:443:192.0.2.10 https://example.com` |
| `curl --connect-to HOST:PORT:HOST:PORT URL` | Mengubah tujuan koneksi tanpa mengubah URL | `curl --connect-to example.com:443:test.example.com:443 https://example.com` |
| `curl --unix-socket SOCKET URL` | Mengakses service melalui Unix socket | `curl --unix-socket /var/run/docker.sock http://localhost/info` |
| `curl --path-as-is URL` | Mempertahankan path URL tanpa normalisasi | `curl --path-as-is https://example.com/a/../b` |
| `curl --get -d PARAM URL` | Menambahkan parameter ke query string | `curl --get -d "page=2" https://example.com/api` |
| `curl --url URL` | Menentukan URL secara eksplisit | `curl --url https://example.com` |
| `curl --proto PROTOCOL URL` | Membatasi protokol yang boleh digunakan | `curl --proto https https://example.com` |
| `curl --proto-redir PROTOCOL URL` | Membatasi protokol ketika redirect | `curl --proto-redir =https -L https://example.com` |
| `curl --max-redirs N URL` | Membatasi jumlah redirect | `curl -L --max-redirs 5 https://example.com` |
| `curl --fail-with-body URL` | Gagal pada HTTP error tetapi tetap mempertahankan response body | `curl --fail-with-body https://example.com/api` |
| `curl --stderr FILE URL` | Mengarahkan pesan error ke file | `curl --stderr error.log https://example.com` |
| `curl --trace FILE URL` | Menyimpan trace komunikasi ke file | `curl --trace trace.log https://example.com` |
| `curl --trace-ascii FILE URL` | Menyimpan trace dalam format ASCII | `curl --trace-ascii trace.log https://example.com` |
| `curl --trace-time URL` | Menambahkan timestamp pada trace | `curl --trace-time --trace-ascii trace.log https://example.com` |
| `curl -D FILE URL` | Menyimpan response header ke file | `curl -D headers.txt https://example.com` |
| `curl -D - URL` | Menampilkan response header di terminal | `curl -D - https://example.com` |
| `curl -o /dev/null URL` | Membuang response body | `curl -o /dev/null https://example.com` |
| `curl --globoff URL` | Menonaktifkan URL globbing | `curl --globoff 'https://example.com/[1-3]'` |
| `curl --config FILE` | Membaca konfigurasi curl dari file | `curl --config curl.conf` |
| `curl -K FILE` | Alias pendek untuk --config | `curl -K curl.conf` |
| `curl --create-dirs -o FILE URL` | Membuat direktori output jika belum ada | `curl --create-dirs -o out/file.txt https://example.com/file.txt` |
| `curl -J -O URL` | Menggunakan nama file dari Content-Disposition | `curl -JO https://example.com/download` |
| `curl -sS -f URL` | Silent, tetapi tetap menampilkan error dan gagal pada HTTP error | `curl -sSf https://example.com` |
| `curl -H "Content-Type: application/json" -d JSON URL` | Mengirim JSON melalui POST | `curl -H "Content-Type: application/json" -d '{"id":1}' https://api.example.com` |
| `curl -H "Accept: application/json" URL` | Meminta response dalam format JSON | `curl -H "Accept: application/json" https://api.example.com/users` |
| `curl -H "Authorization: Bearer TOKEN" URL` | Mengirim Bearer token | `curl -H "Authorization: Bearer TOKEN" https://api.example.com/me` |
| `curl -H "X-API-Key: KEY" URL` | Mengirim API key melalui header | `curl -H "X-API-Key: KEY" https://api.example.com/data` |
| `curl -w "%{http_code}" -o /dev/null URL` | Menampilkan HTTP status code saja | `curl -s -o /dev/null -w "%{http_code}\n" https://example.com` |
| `curl -w "%{time_total}" -o /dev/null URL` | Menampilkan total waktu request | `curl -s -o /dev/null -w "%{time_total}\n" https://example.com` |
| `curl -w "%{url_effective}" URL` | Menampilkan URL akhir setelah redirect | `curl -Ls -o /dev/null -w "%{url_effective}\n" https://example.com` |
| `curl -w "%{size_download}" URL` | Menampilkan jumlah byte yang diunduh | `curl -s -o /dev/null -w "%{size_download}\n" https://example.com` |
| `curl -w "%{content_type}" URL` | Menampilkan Content-Type response | `curl -s -o /dev/null -w "%{content_type}\n" https://example.com` |
| `curl --help` | Menampilkan bantuan penggunaan curl | `curl --help` |
| `curl --help all` | Menampilkan daftar opsi curl yang lebih lengkap | `curl --help all` |
| `curl --version` | Menampilkan versi, protokol, dan fitur curl | `curl --version` |

### API
| Command | Deskripsi | Contoh |
|---|---|---|
| `curl URL` | GET sederhana | `curl https://api.example.com/users` |
| `curl -G -d "q=value" URL` | GET dengan query parameter | `curl -G -d "q=john" https://api.example.com/users` |
| `curl -H "Accept: application/json" URL` | GET dengan header | `curl -H "Accept: application/json" https://api.example.com/users` |
| `curl --json '{}' URL` | POST JSON | `curl --json '{"name":"John"}' https://api.example.com/users` |
| `curl -X PUT --json '{}' URL` | PUT JSON | `curl -X PUT --json '{"name":"Jane"}' https://api.example.com/users/1` |
| `curl -X PATCH --json '{}' URL` | PATCH JSON | `curl -X PATCH --json '{"name":"Jane"}' https://api.example.com/users/1` |
| `curl -X DELETE URL` | DELETE resource | `curl -X DELETE https://api.example.com/users/1` |
| `curl -H "Authorization: Bearer TOKEN" URL` | API dengan Bearer token | `curl -H "Authorization: Bearer eyJ..." https://api.example.com/me` |
| `curl -u USER:PASS URL` | API dengan Basic Auth | `curl -u admin:password https://api.example.com/me` |
| `curl -F "file=@FILE" URL` | Upload file | `curl -F "file=@report.pdf" https://api.example.com/upload` |
| `curl -o FILE URL` | Download response ke file | `curl -o response.json https://api.example.com/data` |

</details>

---

# telnet

<details>

| Command | Deskripsi | Contoh |
|---|---|---|
| `telnet` | Memulai koneksi Telnet ke host | `telnet 192.168.1.1` |
| `open` | Membuka koneksi ke host dan port tertentu | `open example.com 23` |
| `close` | Menutup koneksi aktif | `close` |
| `quit` | Keluar dari program Telnet | `quit` |
| `exit` | Keluar dari program Telnet | `exit` |
| `status` | Menampilkan status koneksi saat ini | `status` |
| `display` | Menampilkan konfigurasi Telnet saat ini | `display` |
| `mode` | Mengubah mode transfer (line/character) | `mode character` |
| `send` | Mengirim karakter atau sinyal kontrol | `send ao` |
| `set` | Mengubah parameter atau opsi Telnet | `set localecho` |
| `unset` | Menonaktifkan parameter atau opsi | `unset localecho` |
| `toggle` | Mengaktifkan/menonaktifkan opsi tertentu | `toggle crlf` |
| `slc` | Mengatur Special Line Characters | `slc export` |
| `auth` | Mengatur atau melihat autentikasi | `auth status` |
| `encrypt` | Mengatur enkripsi sesi Telnet (jika didukung) | `encrypt enable` |
| `environ` | Mengelola variabel lingkungan | `environ list` |
| `z` | Menangguhkan (suspend) sesi Telnet (Unix) | `z` |
| `?` | Menampilkan bantuan singkat | `?` |
| `help` | Menampilkan daftar bantuan | `help` |
| `help send` | Bantuan untuk subperintah send | `help send` |
| `help set` | Bantuan untuk subperintah set | `help set` |
| `help toggle` | Bantuan untuk subperintah toggle | `help toggle` |
| `send ao` | Mengirim Abort Output | `send ao` |
| `send ayt` | Mengirim Are You There | `send ayt` |
| `send brk` | Mengirim Break | `send brk` |
| `send ec` | Mengirim Erase Character | `send ec` |
| `send el` | Mengirim Erase Line | `send el` |
| `send eof` | Mengirim End of File | `send eof` |
| `send eor` | Mengirim End of Record | `send eor` |
| `send escape` | Mengirim karakter escape | `send escape` |
| `send ga` | Mengirim Go Ahead | `send ga` |
| `send ip` | Mengirim Interrupt Process | `send ip` |
| `send nop` | Mengirim No Operation | `send nop` |
| `send synch` | Mengirim Synch | `send synch` |
| `send susp` | Mengirim Suspend Process | `send susp` |
| `send abort` | Mengirim Abort Process | `send abort` |
| `send do` | Negosiasi opsi (DO) | `send do echo` |
| `send dont` | Negosiasi opsi (DONT) | `send dont echo` |
| `send will` | Negosiasi opsi (WILL) | `send will suppress-go-ahead` |
| `send wont` | Negosiasi opsi (WONT) | `send wont echo` |
| `set escape` | Mengatur karakter escape | `set escape ^]` |
| `set localecho` | Mengaktifkan echo lokal | `set localecho` |
| `unset localecho` | Menonaktifkan echo lokal | `unset localecho` |
| `set crlf` | Mengaktifkan translasi CR/LF | `set crlf` |
| `unset crlf` | Menonaktifkan translasi CR/LF | `unset crlf` |
| `set binary` | Mengaktifkan mode biner | `set binary` |
| `unset binary` | Menonaktifkan mode biner | `unset binary` |
| `toggle autoflush` | Toggle autoflush | `toggle autoflush` |
| `toggle autosynch` | Toggle autosynch | `toggle autosynch` |
| `toggle autologin` | Toggle autologin | `toggle autologin` |
| `toggle skiprc` | Toggle pembacaan file .telnetrc | `toggle skiprc` |
| `toggle localchars` | Toggle pemrosesan karakter lokal | `toggle localchars` |
| `toggle netdata` | Toggle tampilan data jaringan | `toggle netdata` |
| `toggle prettydump` | Toggle format dump data | `toggle prettydump` |
| `toggle options` | Toggle tampilan negosiasi opsi | `toggle options` |
| `toggle debug` | Toggle mode debug | `toggle debug` |
| `toggle termdata` | Toggle tampilan data terminal | `toggle termdata` |
| `toggle inbinary` | Toggle mode input biner | `toggle inbinary` |
| `toggle outbinary` | Toggle mode output biner | `toggle outbinary` |
| `toggle binary` | Toggle mode biner dua arah | `toggle binary` |
| `toggle crmod` | Toggle mode carriage return | `toggle crmod` |
| `toggle echo` | Toggle echo lokal | `toggle echo` |
| `toggle verbose_encrypt` | Toggle informasi enkripsi | `toggle verbose_encrypt` |
| `toggle verbose` | Toggle output verbose | `toggle verbose` |
| `toggle rlogin` | Toggle mode kompatibilitas rlogin | `toggle rlogin` |
| `toggle flowcontrol` | Toggle flow control | `toggle flowcontrol` |

</details>

---

# metasploit 

<details>

| Fitur Metasploit | Deskripsi |
|---|---|
| `Exploits` | Modul untuk memanfaatkan kerentanan (vulnerability) pada target agar memperoleh akses atau mengeksekusi kode. Biasanya dipasangkan dengan payload. |
| `Auxiliary` | Modul yang tidak melakukan eksploitasi. Digunakan untuk tugas seperti scanning, fingerprinting, enumerasi, fuzzing, atau pengecekan layanan. |
| `Payloads` | Kode yang dijalankan pada target setelah exploit berhasil. Contohnya membuka shell, menjalankan perintah, atau membuat koneksi balik (reverse connection). |
| `Post` | Modul yang dijalankan setelah akses ke target diperoleh. Digunakan untuk pengumpulan informasi, pemeriksaan konfigurasi, atau tugas pasca-eksploitasi lainnya. |
| `Encoders` | Modul yang mengubah representasi payload agar sesuai dengan batasan tertentu (misalnya menghindari karakter yang dilarang atau bad characters). Bukan jaminan untuk menghindari deteksi keamanan. |
| `NOPs` | Modul yang menghasilkan rangkaian instruksi No Operation (NOP) untuk membantu penyelarasan eksekusi payload pada beberapa jenis exploit. |
| `Evasion` | Modul yang digunakan untuk menghasilkan atau memodifikasi payload agar lebih sulit dianalisis atau terdeteksi oleh mekanisme keamanan tertentu. Penggunaannya umumnya dibatasi pada lingkungan pengujian yang sah dan berizin. |

| Fitur Metasploit | Deskripsi |
|---|---|
| `Exploits` | Modul untuk memanfaatkan kerentanan (vulnerability) pada target agar memperoleh akses atau mengeksekusi kode. Biasanya dipasangkan dengan payload. |
| `Auxiliary` | Modul yang tidak melakukan eksploitasi. Digunakan untuk tugas seperti scanning, fingerprinting, enumerasi, fuzzing, atau pengecekan layanan. |
| `Payloads` | Kode yang dijalankan pada target setelah exploit berhasil. Contohnya membuka shell, menjalankan perintah, atau membuat koneksi balik (reverse connection). |
| `Post` | Modul yang dijalankan setelah akses ke target diperoleh. Digunakan untuk pengumpulan informasi, pemeriksaan konfigurasi, atau tugas pasca-eksploitasi lainnya. |
| `Encoders` | Modul yang mengubah representasi payload agar sesuai dengan batasan tertentu (misalnya menghindari karakter yang dilarang atau bad characters). Bukan jaminan untuk menghindari deteksi keamanan. |
| `NOPs` | Modul yang menghasilkan rangkaian instruksi No Operation (NOP) untuk membantu penyelarasan eksekusi payload pada beberapa jenis exploit. |
| `Evasion` | Modul yang digunakan untuk menghasilkan atau memodifikasi payload agar lebih sulit dianalisis atau terdeteksi oleh mekanisme keamanan tertentu. Penggunaannya umumnya dibatasi pada lingkungan pengujian yang sah dan berizin. |

| Command | Deskripsi | Contoh |
|---|---|---|
| `msfconsole` | Membuka Metasploit Framework console | `msfconsole` |
| `msfdb init` | Menginisialisasi database Metasploit | `msfdb init` |
| `msfdb start` | Menjalankan database Metasploit | `msfdb start` |
| `msfdb stop` | Menghentikan database Metasploit | `msfdb stop` |
| `msfdb restart` | Me-restart database Metasploit | `msfdb restart` |
| `msfdb status` | Melihat status database | `msfdb status` |
| `help` | Menampilkan daftar bantuan perintah | `help` |
| `help <command>` | Menampilkan bantuan perintah tertentu | `help search` |
| `?` | Alias untuk bantuan | `?` |
| `version` | Melihat versi Metasploit | `version` |
| `banner` | Menampilkan banner Metasploit | `banner` |
| `exit` | Keluar dari Metasploit console | `exit` |
| `quit` | Keluar dari Metasploit console | `quit` |
| `clear` | Membersihkan tampilan terminal | `clear` |
| `history` | Melihat riwayat perintah | `history` |
| `save` | Menyimpan konfigurasi sesi | `save` |
| `route` | Mengatur routing melalui sesi aktif | `route add 10.0.0.0/24 1` |
| `connect` | Membuat koneksi TCP sederhana | `connect 192.168.1.10 80` |
| `irb` | Membuka Ruby interpreter internal | `irb` |
| `jobs` | Melihat daftar job yang berjalan | `jobs` |
| `jobs -l` | Melihat detail job | `jobs -l` |
| `jobs -k <id>` | Menghentikan job tertentu | `jobs -k 1` |
| `jobs -K` | Menghentikan semua job | `jobs -K` |
| `sessions` | Melihat sesi aktif | `sessions` |
| `sessions -l` | Menampilkan daftar sesi | `sessions -l` |
| `sessions -i <id>` | Masuk ke sesi tertentu | `sessions -i 1` |
| `sessions -k <id>` | Menutup sesi tertentu | `sessions -k 1` |
| `sessions -K` | Menutup semua sesi | `sessions -K` |
| `background` | Memindahkan sesi aktif ke background | `background` |
| `search` | Mencari modul Metasploit | `search type:exploit windows` |
| `use` | Memilih modul | `use exploit/windows/smb/ms17_010_eternalblue` |
| `show` | Menampilkan informasi modul | `show options` |
| `show exploits` | Menampilkan daftar exploit | `show exploits` |
| `show payloads` | Menampilkan daftar payload | `show payloads` |
| `show auxiliary` | Menampilkan modul auxiliary | `show auxiliary` |
| `show encoders` | Menampilkan encoder | `show encoders` |
| `show nops` | Menampilkan generator NOP | `show nops` |
| `show evasion` | Menampilkan modul evasion | `show evasion` |
| `info` | Menampilkan informasi modul | `info exploit/windows/smb/ms17_010_eternalblue` |
| `options` | Melihat opsi modul aktif | `show options` |
| `set` | Mengatur nilai opsi modul | `set RHOSTS 192.168.1.10` |
| `setg` | Mengatur variabel global | `setg RHOSTS 192.168.1.10` |
| `unset` | Menghapus nilai opsi | `unset RHOSTS` |
| `unsetg` | Menghapus variabel global | `unsetg RHOSTS` |
| `get` | Melihat nilai opsi | `get RHOSTS` |
| `getg` | Melihat nilai global | `getg RHOSTS` |
| `check` | Mengecek target tanpa menjalankan modul | `check` |
| `run` | Menjalankan modul aktif | `run` |
| `exploit` | Menjalankan exploit aktif | `exploit` |
| `reload` | Memuat ulang modul | `reload` |
| `reload_all` | Memuat ulang semua modul | `reload_all` |
| `back` | Kembali ke menu utama | `back` |
| `previous` | Kembali ke modul sebelumnya | `previous` |
| `edit` | Membuka modul di editor | `edit` |
| `makerc` | Membuat file resource dari perintah | `makerc commands.rc` |
| `resource` | Menjalankan file resource | `resource script.rc` |
| `spool` | Menyimpan output console ke file | `spool output.txt` |
| `db_status` | Melihat status koneksi database | `db_status` |
| `db_connect` | Menghubungkan database | `db_connect user:pass@localhost/msf` |
| `db_disconnect` | Memutus koneksi database | `db_disconnect` |
| `db_rebuild_cache` | Membuat ulang cache database | `db_rebuild_cache` |
| `hosts` | Melihat daftar host database | `hosts` |
| `services` | Melihat layanan host | `services` |
| `vulns` | Melihat kerentanan yang tersimpan | `vulns` |
| `creds` | Melihat kredensial tersimpan | `creds` |
| `loot` | Melihat data loot | `loot` |
| `notes` | Melihat catatan database | `notes` |
| `workspace` | Mengelola workspace | `workspace` |
| `workspace -a` | Membuat workspace baru | `workspace -a lab` |
| `workspace -d` | Menghapus workspace | `workspace -d lab` |
| `workspace -r` | Mengganti nama workspace | `workspace -r old new` |
| `db_nmap` | Menjalankan Nmap melalui database Metasploit | `db_nmap -sV 192.168.1.10` |
| `db_import` | Mengimpor hasil scan | `db_import scan.xml` |
| `db_export` | Mengekspor database | `db_export -f xml export.xml` |
| `db_autopwn` | Menjalankan autopwn (versi lama) | `db_autopwn` |
| `resource` | Menjalankan script otomatisasi | `resource auto.rc` |
| `load` | Memuat plugin | `load db_tracker` |
| `unload` | Menghapus plugin | `unload db_tracker` |
| `loadpath` | Menambah path modul | `loadpath /opt/modules` |
| `unloadpath` | Menghapus path modul | `unloadpath /opt/modules` |
| `plugins` | Melihat plugin aktif | `plugins` |
| `sessions -u` | Upgrade shell menjadi Meterpreter | `sessions -u 1` |
| `sysinfo` | Melihat informasi sistem Meterpreter | `sysinfo` |
| `getuid` | Melihat user aktif Meterpreter | `getuid` |
| `pwd` | Melihat direktori aktif | `pwd` |
| `ls` | Melihat isi direktori | `ls` |
| `cd` | Berpindah direktori | `cd /tmp` |
| `cat` | Membaca file | `cat file.txt` |
| `download` | Mengambil file dari host | `download file.txt` |
| `upload` | Mengirim file ke host | `upload file.txt` |
| `shell` | Membuka shell sistem | `shell` |
| `execute` | Menjalankan program | `execute -f cmd.exe` |
| `ps` | Melihat proses berjalan | `ps` |
| `kill` | Menghentikan proses | `kill 1234` |
| `getpid` | Melihat PID Meterpreter | `getpid` |
| `migrate` | Memindahkan proses Meterpreter | `migrate 1234` |
| `background` | Menaruh Meterpreter di background | `background` |
| `run` | Menjalankan script Meterpreter | `run post/windows/gather/hashdump` |
| `resource` | Menjalankan script Meterpreter | `resource script.rc` |
| `help` | Bantuan Meterpreter | `help` |
| `hashdump` | Mengambil hash password (modul tertentu) | `hashdump` |
| `getsystem` | Mencoba eskalasi hak akses | `getsystem` |
| `keyscan_start` | Memulai keylogger | `keyscan_start` |
| `keyscan_stop` | Menghentikan keylogger | `keyscan_stop` |
| `keyscan_dump` | Menampilkan hasil keylogger | `keyscan_dump` |
| `screenshot` | Mengambil screenshot layar | `screenshot` |
| `webcam_list` | Melihat perangkat webcam | `webcam_list` |
| `webcam_snap` | Mengambil gambar webcam | `webcam_snap` |
| `record_mic` | Merekam mikrofon | `record_mic -d 10` |
| `enumdesktops` | Melihat desktop aktif | `enumdesktops` |
| `getsystem` | Mendapatkan hak sistem jika memungkinkan | `getsystem` |
| `run post` | Menjalankan modul post exploitation | `run post/windows/gather/enum_logged_on_users` |
| `search <file>` | Mencari file pada sistem target | `search -f password.txt` |
| `clearev` | Membersihkan event log (jika memiliki izin) | `clearev` |
| `reboot` | Restart sistem target | `reboot` |
| `shutdown` | Mematikan sistem target | `shutdown` |

(Daftar mencakup perintah inti Metasploit Console, modul, database, job/session, dan Meterpreter. Perintah modul sangat banyak dan terus berubah sesuai versi Metasploit.)

</details>

---

# scp

<details>

| Command | Deskripsi | Contoh |
|---|---|---|
| `scp SOURCE USER@HOST:DEST` | Menyalin file dari komputer lokal ke server remote. | `scp file.txt root@192.168.1.10:/root/` |
| `scp USER@HOST:SOURCE DEST` | Mengunduh file dari server remote ke komputer lokal. | `scp root@192.168.1.10:/root/file.txt ./` |
| `scp USER1@HOST1:SOURCE USER2@HOST2:DEST` | Menyalin file langsung dari satu server remote ke server remote lain. | `scp root@server1:/root/a.txt root@server2:/root/` |
| `scp file1 file2 USER@HOST:DEST` | Mengirim beberapa file sekaligus ke server. | `scp a.txt b.txt root@192.168.1.10:/root/` |
| `scp USER@HOST:/path/* DEST` | Mengunduh beberapa file menggunakan wildcard. | `scp root@192.168.1.10:/root/*.txt ./` |
| `scp -r DIRECTORY USER@HOST:DEST` | Menyalin direktori beserta seluruh isinya secara rekursif. | `scp -r website/ root@192.168.1.10:/var/www/` |
| `scp -r USER@HOST:DIRECTORY DEST` | Mengunduh direktori dari server remote. | `scp -r root@192.168.1.10:/var/www/site ./` |
| `scp -p SOURCE USER@HOST:DEST` | Mempertahankan permission dan timestamp file. | `scp -p file.txt root@192.168.1.10:/root/` |
| `scp -P PORT SOURCE USER@HOST:DEST` | Menggunakan port SSH tertentu. | `scp -P 2222 file.txt root@192.168.1.10:/root/` |
| `scp -i KEY SOURCE USER@HOST:DEST` | Menggunakan private key SSH tertentu. | `scp -i ~/.ssh/id_ed25519 file.txt root@192.168.1.10:/root/` |
| `scp -C SOURCE USER@HOST:DEST` | Mengaktifkan kompresi selama transfer. | `scp -C backup.tar.gz root@192.168.1.10:/backup/` |
| `scp -v SOURCE USER@HOST:DEST` | Menampilkan informasi detail proses koneksi dan transfer untuk debugging. | `scp -v file.txt root@192.168.1.10:/root/` |
| `scp -q SOURCE USER@HOST:DEST` | Mengurangi output/status yang ditampilkan selama transfer. | `scp -q file.txt root@192.168.1.10:/root/` |
| `scp -4 SOURCE USER@HOST:DEST` | Memaksa penggunaan IPv4. | `scp -4 file.txt root@server.example.com:/root/` |
| `scp -6 SOURCE USER@HOST:DEST` | Memaksa penggunaan IPv6. | `scp -6 file.txt root@[2001:db8::10]:/root/` |
| `scp -B SOURCE USER@HOST:DEST` | Menggunakan batch mode dan tidak meminta input interaktif. | `scp -B file.txt root@192.168.1.10:/root/` |
| `scp -l LIMIT SOURCE USER@HOST:DEST` | Membatasi bandwidth transfer dalam Kbit/s. | `scp -l 8000 backup.tar.gz root@192.168.1.10:/backup/` |
| `scp -S PROGRAM SOURCE USER@HOST:DEST` | Menentukan program SSH yang digunakan oleh `scp`. | `scp -S /usr/bin/ssh file.txt root@192.168.1.10:/root/` |
| `scp -F CONFIG SOURCE USER@HOST:DEST` | Menggunakan file konfigurasi SSH tertentu. | `scp -F ~/.ssh/config-prod file.txt root@server:/root/` |
| `scp -o OPTION SOURCE USER@HOST:DEST` | Memberikan opsi konfigurasi SSH secara langsung. | `scp -o ConnectTimeout=10 file.txt root@192.168.1.10:/root/` |
| `scp -O SOURCE USER@HOST:DEST` | Memaksa penggunaan protokol SCP lama. | `scp -O file.txt root@192.168.1.10:/root/` |
| `scp -T SOURCE USER@HOST:DEST` | Menonaktifkan pemeriksaan nama file/target pada sisi remote. | `scp -T file.txt root@192.168.1.10:/root/` |
| `scp -3 USER1@HOST1:SOURCE USER2@HOST2:DEST` | Merutekan transfer antara dua host remote melalui komputer lokal. | `scp -3 root@server1:/a.txt root@server2:/backup/` |
| `scp -c CIPHER SOURCE USER@HOST:DEST` | Memilih cipher SSH yang digunakan untuk enkripsi transfer. | `scp -c aes256-gcm@openssh.com file.txt root@192.168.1.10:/root/` |
| `scp -E LOGFILE SOURCE USER@HOST:DEST` | Menulis pesan diagnostik ke file log pada versi OpenSSH yang mendukung opsi ini. | `scp -E scp.log file.txt root@192.168.1.10:/root/` |
| `scp -o Compression=yes SOURCE USER@HOST:DEST` | Mengaktifkan kompresi melalui konfigurasi SSH. | `scp -o Compression=yes backup.sql root@192.168.1.10:/backup/` |
| `scp -o ConnectTimeout=10 SOURCE USER@HOST:DEST` | Membatasi waktu tunggu koneksi menjadi 10 detik. | `scp -o ConnectTimeout=10 file.txt root@192.168.1.10:/root/` |
| `scp -J USER@JUMP_HOST SOURCE USER@HOST:DEST` | Mengakses server tujuan melalui jump/bastion host. | `scp -J root@10.0.0.5 file.txt root@10.0.0.10:/root/` |
| `scp 'USER@HOST:/path/file name.txt' ./` | Mengunduh file remote yang memiliki spasi pada nama file/path. | `scp 'root@192.168.1.10:/root/my file.txt' ./` |
| `scp ./file.txt USER@HOST:'/path/my file.txt'` | Mengirim file dengan path tujuan yang memiliki spasi. | `scp ./file.txt root@192.168.1.10:'/root/my file.txt'` |
| `scp USER@HOST:/path/file.txt ./newname.txt` | Mengunduh file sekaligus mengganti namanya di lokal. | `scp root@192.168.1.10:/root/file.txt ./backup.txt` |
| `scp ./file.txt USER@HOST:/path/newname.txt` | Mengirim file sekaligus mengganti namanya di server. | `scp ./file.txt root@192.168.1.10:/root/backup.txt` |
| `scp -r -C DIRECTORY USER@HOST:DEST` | Mengirim direktori secara rekursif dengan kompresi. | `scp -r -C website/ root@192.168.1.10:/var/www/` |
| `scp -r -p DIRECTORY USER@HOST:DEST` | Mengirim direktori secara rekursif dan mempertahankan timestamp serta permission. | `scp -r -p website/ root@192.168.1.10:/var/www/` |
| `scp -r -P PORT -i KEY DIRECTORY USER@HOST:DEST` | Mengirim direktori menggunakan port dan private key tertentu. | `scp -r -P 2222 -i ~/.ssh/id_ed25519 website/ root@192.168.1.10:/var/www/` |
| `scp -4 -P PORT -i KEY SOURCE USER@HOST:DEST` | Transfer menggunakan IPv4, port SSH tertentu, dan private key. | `scp -4 -P 2222 -i ~/.ssh/id_ed25519 file.txt root@192.168.1.10:/root/` |
| `scp --help` | Menampilkan bantuan dan opsi `scp` yang tersedia. | `scp --help` |
| `man scp` | Membuka dokumentasi/manual `scp` pada sistem. | `man scp` |

</details>

---

```text
sekarang buatkan semua daftar perintah scp beserta dekripsinya dalam format tabel markdown mentah dengan format:
| Command | Deskripsi | Contoh |
|---|---|---|```


