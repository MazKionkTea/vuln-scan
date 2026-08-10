# gobuster

| command | deskripsi | contoh |
|---|---|---|
| `gobuster help` | Menampilkan bantuan umum Gobuster | `gobuster help` |
| `gobuster help <mode>` | Menampilkan bantuan untuk mode tertentu | `gobuster help dir` |
| `gobuster <mode> --help` | Alternatif untuk melihat bantuan suatu mode | `gobuster dir --help` |
| `gobuster version` | Menampilkan versi dan informasi build | `gobuster version` |
| `gobuster dir -u <URL> -w <WORDLIST>` | Enumerasi direktori dan file web | `gobuster dir -u https://example.com -w wordlist.txt` |
| `gobuster dir -u <URL> -w <WORDLIST> -x <EXT>` | Mencoba ekstensi file tertentu | `gobuster dir -u https://example.com -w wordlist.txt -x php,html,txt` |
| `gobuster dir -u <URL> -w <WORDLIST> -s <CODES>` | Hanya menampilkan HTTP status code tertentu | `gobuster dir -u https://example.com -w wordlist.txt -s 200,301,302` |
| `gobuster dir -u <URL> -w <WORDLIST> -b <CODES>` | Mengecualikan status code tertentu | `gobuster dir -u https://example.com -w wordlist.txt -b 404` |
| `gobuster dir -u <URL> -w <WORDLIST> -l` | Menampilkan panjang response | `gobuster dir -u https://example.com -w wordlist.txt -l` |
| `gobuster dir -u <URL> -w <WORDLIST> -H <HEADER>` | Menambahkan HTTP header | `gobuster dir -u https://example.com -w wordlist.txt -H "Authorization: Bearer TOKEN"` |
| `gobuster dir -u <URL> -w <WORDLIST> -c <COOKIE>` | Menambahkan cookie HTTP | `gobuster dir -u https://example.com -w wordlist.txt -c "session=value"` |
| `gobuster dir -u <URL> -w <WORDLIST> -o <FILE>` | Menyimpan hasil ke file | `gobuster dir -u https://example.com -w wordlist.txt -o hasil.txt` |
| `gobuster dir -u <URL> -w <WORDLIST> -q` | Mode quiet untuk output yang lebih bersih | `gobuster dir -u https://example.com -w wordlist.txt -q` |
| `gobuster dir -u <URL> -w <WORDLIST> -t <N>` | Mengatur jumlah thread | `gobuster dir -u https://example.com -w wordlist.txt -t 10` |
| `gobuster dir -u <URL> -w <WORDLIST> --delay <DURATION>` | Memberi jeda antar request | `gobuster dir -u https://example.com -w wordlist.txt --delay 500ms` |
| `gobuster dir -u <URL> -w <WORDLIST> --timeout <DURATION>` | Mengatur timeout request | `gobuster dir -u https://example.com -w wordlist.txt --timeout 10s` |
| `gobuster dir -u <URL> -w <WORDLIST> -r` | Mengikuti HTTP redirect | `gobuster dir -u https://example.com -w wordlist.txt -r` |
| `gobuster dir -u <URL> -w <WORDLIST> -k` | Tidak memvalidasi sertifikat TLS | `gobuster dir -u https://example.com -w wordlist.txt -k` |
| `gobuster dns -do <DOMAIN> -w <WORDLIST>` | Enumerasi subdomain melalui DNS | `gobuster dns -do example.com -w subdomains.txt` |
| `gobuster dns -do <DOMAIN> -w <WORDLIST> -t <N>` | Mengatur jumlah thread DNS | `gobuster dns -do example.com -w subdomains.txt -t 20` |
| `gobuster dns -do <DOMAIN> -w <WORDLIST> -r <DNS>` | Menggunakan DNS resolver tertentu | `gobuster dns -do example.com -w subdomains.txt -r 8.8.8.8:53` |
| `gobuster dns -do <DOMAIN> -w <WORDLIST> --check-cname` | Memeriksa CNAME pada hasil DNS | `gobuster dns -do example.com -w subdomains.txt --check-cname` |
| `gobuster dns -do <DOMAIN> -w <WORDLIST> --no-fqdn` | Menonaktifkan penggunaan search-domain sistem | `gobuster dns -do example.com -w subdomains.txt --no-fqdn` |
| `gobuster vhost -u <URL> -w <WORDLIST>` | Enumerasi virtual host | `gobuster vhost -u https://example.com -w vhosts.txt` |
| `gobuster vhost -u <URL> -w <WORDLIST> --append-domain` | Menambahkan domain target ke setiap kandidat | `gobuster vhost -u https://example.com -w vhosts.txt --append-domain` |
| `gobuster vhost -u <URL> -w <WORDLIST> -t <N>` | Mengatur jumlah thread vhost | `gobuster vhost -u https://example.com -w vhosts.txt -t 10` |
| `gobuster s3 -w <WORDLIST>` | Enumerasi nama bucket Amazon S3 | `gobuster s3 -w buckets.txt` |
| `gobuster s3 -w <WORDLIST> --debug` | Menampilkan informasi debug saat enumerasi S3 | `gobuster s3 -w buckets.txt --debug` |
| `gobuster gcs -w <WORDLIST>` | Enumerasi nama bucket Google Cloud Storage | `gobuster gcs -w buckets.txt` |
| `gobuster gcs -w <WORDLIST> --debug` | Menampilkan informasi debug GCS | `gobuster gcs -w buckets.txt --debug` |
| `gobuster tftp -s <SERVER> -w <WORDLIST>` | Mencari file pada server TFTP | `gobuster tftp -s 192.0.2.10 -w files.txt` |
| `gobuster fuzz -u <URL_WITH_FUZZ> -w <WORDLIST>` | Melakukan fuzzing menggunakan placeholder `FUZZ` | `gobuster fuzz -u https://example.com/?q=FUZZ -w words.txt` |
| `gobuster fuzz -u <URL> -w <WORDLIST> -H <HEADER>` | Fuzzing nilai HTTP header | `gobuster fuzz -u https://example.com -w words.txt -H "X-Test: FUZZ"` |
| `gobuster fuzz -u <URL> -w <WORDLIST> -d <DATA>` | Fuzzing data HTTP request | `gobuster fuzz -u https://example.com -w words.txt -d "value=FUZZ"` |
| `gobuster fuzz -u <URL> -w <WORDLIST> -m <METHOD>` | Menentukan HTTP method untuk fuzzing | `gobuster fuzz -u https://example.com -w words.txt -m POST` |
| `gobuster fuzz -u <URL> -w <WORDLIST> -o <FILE>` | Menyimpan hasil fuzzing | `gobuster fuzz -u https://example.com/?q=FUZZ -w words.txt -o hasil.txt` |
| `gobuster fuzz -u <URL> -w <WORDLIST> --exclude-length <N>` | Mengecualikan response berdasarkan panjang | `gobuster fuzz -u https://example.com/?q=FUZZ -w words.txt --exclude-length 1234` |
| `gobuster fuzz -u <URL> -w <WORDLIST> --exclude-status <CODES>` | Mengecualikan HTTP status tertentu | `gobuster fuzz -u https://example.com/?q=FUZZ -w words.txt --exclude-status 404` |
| `gobuster <mode> ... -a <USER_AGENT>` | Menentukan User-Agent HTTP | `gobuster dir -u https://example.com -w words.txt -a "Mozilla/5.0"` |
| `gobuster <mode> ... -p <PROXY>` | Menggunakan HTTP proxy | `gobuster dir -u https://example.com -w words.txt -p http://127.0.0.1:8080` |
| `gobuster <mode> ... --delay <DURATION>` | Memberikan jeda request untuk mengurangi beban target | `gobuster dir -u https://example.com -w words.txt --delay 1s` |
| `gobuster <mode> ... --debug` | Mengaktifkan output debugging | `gobuster dir -u https://example.com -w words.txt --debug` |
| `gobuster <mode> ... --no-progress` | Menonaktifkan progress indicator | `gobuster dir -u https://example.com -w words.txt --no-progress` |
| `gobuster <mode> ... --no-color` | Menonaktifkan warna output | `gobuster dir -u https://example.com -w words.txt --no-color` |
| `gobuster <mode> ... --no-error` | Menyembunyikan pesan error tertentu pada output | `gobuster dir -u https://example.com -w words.txt --no-error` |
| `gobuster <mode> ... -o <FILE>` | Menyimpan output hasil scanning | `gobuster dir -u https://example.com -w words.txt -o results.txt` |
