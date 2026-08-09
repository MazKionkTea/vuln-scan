##  CURL

| curl option | deskripsi | contoh |
|---|---|---|
| `--abstract-unix-socket <path>` | Koneksi melalui abstract Unix domain socket. | `curl --abstract-unix-socket /socket https://example.com` |
| `--alt-svc <file>` | Menggunakan cache Alt-Svc untuk HTTP. | `curl --alt-svc alt-svc.txt https://example.com` |
| `--anyauth` | Memilih metode autentikasi HTTP secara otomatis. | `curl --anyauth -u user:pass https://example.com` |
| `-a, --append` | Menambahkan data ke file remote saat upload FTP/SFTP. | `curl -a -T file ftp://example.com/` |
| `--aws-sigv4 <provider>` | Menggunakan autentikasi AWS Signature V4. | `curl --aws-sigv4 aws:amz:us-east-1:s3 -u key:secret https://example.com` |
| `--basic` | Menggunakan HTTP Basic Authentication. | `curl --basic -u user:pass https://example.com` |
| `--ca-native` | Menggunakan certificate store native OS. | `curl --ca-native https://example.com` |
| `--cacert <file>` | Menentukan file CA certificate. | `curl --cacert ca.pem https://example.com` |
| `--capath <dir>` | Menentukan direktori CA certificate. | `curl --capath /etc/ssl/certs https://example.com` |
| `--cert-status` | Memeriksa status OCSP stapling certificate. | `curl --cert-status https://example.com` |
| `--cert-type <type>` | Menentukan format certificate client. | `curl --cert-type PEM --cert client.pem https://example.com` |
| `-E, --cert <certificate[:password]>` | Menggunakan client certificate. | `curl --cert client.pem https://example.com` |
| `--ciphers <list>` | Menentukan cipher TLS yang boleh digunakan. | `curl --ciphers ECDHE-RSA-AES256-GCM-SHA384 https://example.com` |
| `--compressed` | Meminta response HTTP terkompresi dan mendekompresinya. | `curl --compressed https://example.com` |
| `--compressed-ssh` | Mengaktifkan compression untuk SSH. | `curl --compressed-ssh sftp://example.com/file` |
| `-K, --config <file>` | Membaca opsi curl dari file konfigurasi. | `curl --config curl.conf` |
| `--connect-timeout <seconds>` | Batas waktu untuk proses koneksi. | `curl --connect-timeout 10 https://example.com` |
| `--connect-to <HOST1:PORT1:HOST2:PORT2>` | Mengarahkan koneksi host/port tertentu ke host/port lain. | `curl --connect-to example.com:443:127.0.0.1:8443 https://example.com` |
| `-C, --continue-at <offset>` | Melanjutkan transfer dari posisi tertentu. | `curl -C - -O https://example.com/file.zip` |
| `-c, --cookie-jar <file>` | Menyimpan cookie ke file. | `curl -c cookies.txt https://example.com` |
| `-b, --cookie <data>` | Mengirim cookie. | `curl -b "session=abc123" https://example.com` |
| `--create-dirs` | Membuat direktori lokal yang diperlukan. | `curl --create-dirs -o out/file.txt https://example.com/file.txt` |
| `--create-file-mode <mode>` | Menentukan permission file baru. | `curl --create-file-mode 0644 -O https://example.com/file.txt` |
| `--crlf` | Mengubah LF menjadi CRLF pada upload. | `curl --crlf -T file ftp://example.com/` |
| `--crlfile <file>` | Menggunakan Certificate Revocation List. | `curl --crlfile revoked.pem https://example.com` |
| `--curves <list>` | Menentukan elliptic curves TLS. | `curl --curves X25519:P-256 https://example.com` |
| `--data-ascii <data>` | Mengirim data HTTP POST sebagai ASCII; alias `--data`. | `curl --data-ascii "name=John" https://example.com` |
| `--data-binary <data>` | Mengirim data POST tanpa transformasi. | `curl --data-binary @data.json https://example.com` |
| `--data-raw <data>` | POST data tanpa memperlakukan `@` secara khusus. | `curl --data-raw '@test' https://example.com` |
| `--data-urlencode <data>` | URL-encode data POST. | `curl --data-urlencode "name=John Doe" https://example.com` |
| `-d, --data <data>` | Mengirim data HTTP POST. | `curl -d "name=John" https://example.com` |
| `--delegation <level>` | Mengatur delegation GSS-API. | `curl --delegation always https://example.com` |
| `--digest` | Menggunakan HTTP Digest Authentication. | `curl --digest -u user:pass https://example.com` |
| `--disable-eprt` | Menonaktifkan EPRT FTP. | `curl --disable-eprt ftp://example.com` |
| `--disable-epsv` | Menonaktifkan EPSV FTP. | `curl --disable-epsv ftp://example.com` |
| `-q, --disable` | Mengabaikan konfigurasi `.curlrc` default. | `curl -q https://example.com` |
| `--disallow-username-in-url` | Menolak URL yang mengandung username. | `curl --disallow-username-in-url https://user@example.com` |
| `--dns-interface <interface>` | Memakai interface tertentu untuk DNS. | `curl --dns-interface eth0 https://example.com` |
| `--dns-ipv4-addr <address>` | Menentukan alamat IPv4 lokal untuk DNS. | `curl --dns-ipv4-addr 192.168.1.10 https://example.com` |
| `--dns-ipv6-addr <address>` | Menentukan alamat IPv6 lokal untuk DNS. | `curl --dns-ipv6-addr ::1 https://example.com` |
| `--dns-servers <addresses>` | Menentukan DNS server yang digunakan. | `curl --dns-servers 1.1.1.1 https://example.com` |
| `--doh-cert-status` | Memeriksa OCSP status certificate server DoH. | `curl --doh-cert-status --doh-url https://dns.example/dns-query https://example.com` |
| `--doh-insecure` | Tidak memverifikasi TLS server DoH. | `curl --doh-insecure --doh-url https://dns.example/dns-query https://example.com` |
| `--doh-url <url>` | Menggunakan DNS-over-HTTPS. | `curl --doh-url https://dns.example/dns-query https://example.com` |
| `--dump-ca-embed` | Menampilkan CA bundle yang tertanam pada curl. | `curl --dump-ca-embed` |
| `-D, --dump-header <file>` | Menyimpan response headers ke file. | `curl -D headers.txt https://example.com` |
| `--ech <config>` | Mengaktifkan Encrypted Client Hello. | `curl --ech true https://example.com` |
| `--egd-file <file>` | Menentukan EGD socket/file untuk entropy. | `curl --egd-file /var/run/egd-pool https://example.com` |
| `--engine <name>` | Memilih OpenSSL crypto engine. | `curl --engine pkcs11 https://example.com` |
| `--etag-compare <file>` | Membandingkan response dengan ETag tersimpan. | `curl --etag-compare etag.txt https://example.com` |
| `--etag-save <file>` | Menyimpan ETag response. | `curl --etag-save etag.txt https://example.com` |
| `--expect100-timeout <seconds>` | Timeout menunggu HTTP 100-continue. | `curl --expect100-timeout 2 -d @file https://example.com` |
| `--fail-early` | Berhenti ketika salah satu transfer gagal. | `curl --fail-early https://a.example https://b.example` |
| `--fail-with-body` | Gagal untuk HTTP 4xx/5xx tetapi tetap menampilkan body. | `curl --fail-with-body https://example.com/error` |
| `-f, --fail` | Tidak menampilkan body untuk HTTP error 400+. | `curl -f https://example.com/error` |
| `--false-start` | Mengaktifkan TLS False Start jika didukung backend. | `curl --false-start https://example.com` |
| `--form-escape` | Menggunakan escaping untuk data multipart form. | `curl --form-escape -F "name=value" https://example.com` |
| `--form-string <name=data>` | Mengirim multipart form tanpa special interpretation. | `curl --form-string "name=@file" https://example.com` |
| `-F, --form <name=content>` | Mengirim multipart/form-data. | `curl -F "file=@photo.jpg" https://example.com/upload` |
| `--ftp-account <data>` | Mengirim account FTP tambahan. | `curl --ftp-account account ftp://example.com/` |
| `--ftp-alternative-to-user <command>` | Perintah alternatif jika login FTP gagal. | `curl --ftp-alternative-to-user "anonymous" ftp://example.com/` |
| `--ftp-create-dirs` | Membuat direktori FTP yang diperlukan. | `curl --ftp-create-dirs -T file ftp://example.com/a/b/` |
| `--ftp-method <method>` | Memilih metode akses direktori FTP. | `curl --ftp-method nocwd ftp://example.com/file` |
| `--ftp-pasv` | Menggunakan passive mode FTP. | `curl --ftp-pasv ftp://example.com/` |
| `-P, --ftp-port <address>` | Menggunakan active mode FTP. | `curl --ftp-port 192.168.1.10 ftp://example.com/` |
| `--ftp-pret` | Mengirim PRET sebelum PASV/transfer FTP. | `curl --ftp-pret ftp://example.com/` |
| `--ftp-skip-pasv-ip` | Mengabaikan alamat IP dari response PASV. | `curl --ftp-skip-pasv-ip ftp://example.com/` |
| `--ftp-ssl-ccc-mode <active/passive>` | Menentukan mode clear-command-channel FTP. | `curl --ftp-ssl-ccc --ftp-ssl-ccc-mode active ftp://example.com/` |
| `--ftp-ssl-ccc` | Mengakhiri TLS pada FTP command channel. | `curl --ftp-ssl-ccc ftps://example.com/` |
| `--ftp-ssl-control` | Meminta TLS pada FTP control connection. | `curl --ftp-ssl-control ftp://example.com/` |
| `-G, --get` | Mengubah data POST menjadi query string GET. | `curl -G -d "q=curl" https://example.com/search` |
| `-g, --globoff` | Menonaktifkan URL globbing. | `curl -g "https://example.com/a[1-10].txt"` |
| `--happy-eyeballs-timeout-ms <ms>` | Mengatur timeout Happy Eyeballs IPv4/IPv6. | `curl --happy-eyeballs-timeout-ms 200 https://example.com` |
| `--haproxy-clientip <ip>` | Mengirim alamat client melalui HAProxy PROXY protocol. | `curl --haproxy-clientip 192.0.2.10 https://example.com` |
| `--haproxy-protocol` | Menggunakan HAProxy PROXY protocol. | `curl --haproxy-protocol https://example.com` |
| `-I, --head` | Mengambil HTTP headers saja. | `curl -I https://example.com` |
| `-H, --header <header>` | Menambahkan HTTP header. | `curl -H "Authorization: Bearer TOKEN" https://example.com` |
| `-h, --help [subject]` | Menampilkan bantuan curl. | `curl --help all` |
| `--hostpubmd5 <md5>` | Memverifikasi MD5 host public key SSH. | `curl --hostpubmd5 HASH sftp://example.com/` |
| `--hostpubsha256 <sha256>` | Memverifikasi SHA-256 host public key SSH. | `curl --hostpubsha256 HASH sftp://example.com/` |
| `--hsts <file>` | Mengaktifkan HSTS cache. | `curl --hsts hsts.txt https://example.com` |
| `--http0.9` | Mengizinkan HTTP/0.9. | `curl --http0.9 http://example.com` |
| `-0, --http1.0` | Memaksa HTTP/1.0. | `curl --http1.0 https://example.com` |
| `--http1.1` | Memaksa HTTP/1.1. | `curl --http1.1 https://example.com` |
| `--http2-prior-knowledge` | Menggunakan HTTP/2 tanpa HTTP/1.1 negotiation. | `curl --http2-prior-knowledge https://example.com` |
| `--http2` | Meminta HTTP/2 melalui ALPN. | `curl --http2 https://example.com` |
| `--http3-only` | Memaksa penggunaan HTTP/3. | `curl --http3-only https://example.com` |
| `--http3` | Mencoba menggunakan HTTP/3. | `curl --http3 https://example.com` |
| `--ignore-content-length` | Mengabaikan Content-Length. | `curl --ignore-content-length ftp://example.com/file` |
| `-k, --insecure` | Menonaktifkan verifikasi TLS certificate. | `curl -k https://example.com` |
| `--interface <name>` | Memilih network interface/address lokal. | `curl --interface eth0 https://example.com` |
| `--ip-tos <value>` | Mengatur IP Type of Service. | `curl --ip-tos lowdelay https://example.com` |
| `--ipfs-gateway <url>` | Menentukan IPFS gateway. | `curl --ipfs-gateway https://ipfs.io https://ipfs.example/hash` |
| `-4, --ipv4` | Memaksa IPv4. | `curl -4 https://example.com` |
| `-6, --ipv6` | Memaksa IPv6. | `curl -6 https://example.com` |
| `--json <data>` | Mengirim JSON dengan header JSON yang sesuai. | `curl --json '{"name":"John"}' https://example.com/api` |
| `-j, --junk-session-cookies` | Mengabaikan session cookies saat membaca cookie file. | `curl -j -b cookies.txt https://example.com` |
| `--keepalive-cnt <count>` | Menentukan jumlah keepalive probe TCP. | `curl --keepalive-cnt 5 https://example.com` |
| `--keepalive-time <seconds>` | Menentukan interval TCP keepalive. | `curl --keepalive-time 60 https://example.com` |
| `--key-type <type>` | Menentukan tipe private key client. | `curl --key-type PEM --key client.key https://example.com` |
| `--key <file>` | Menentukan private key client. | `curl --key client.key https://example.com` |
| `--krb <level>` | Mengaktifkan autentikasi Kerberos. | `curl --krb clear https://example.com` |
| `--libcurl <file>` | Menghasilkan source code libcurl dari perintah. | `curl --libcurl example.c https://example.com` |
| `--limit-rate <speed>` | Membatasi kecepatan transfer. | `curl --limit-rate 1M https://example.com/file` |
| `-l, --list-only` | Menampilkan daftar file saja pada FTP. | `curl -l ftp://example.com/` |
| `--local-port <range>` | Menentukan port lokal yang digunakan. | `curl --local-port 5000-5100 https://example.com` |
| `--location-trusted` | Mengikuti redirect sambil meneruskan credential ke host lain. | `curl --location-trusted -u user:pass https://example.com` |
| `-L, --location` | Mengikuti HTTP redirect. | `curl -L https://example.com` |
| `--login-options <options>` | Menentukan login options untuk protokol tertentu. | `curl --login-options AUTH=PLAIN imap://example.com/` |
| `--mail-auth <address>` | Menentukan SMTP authentication address. | `curl --mail-auth sender@example.com smtp://example.com` |
| `--mail-from <address>` | Menentukan SMTP MAIL FROM. | `curl --mail-from sender@example.com smtp://example.com` |
| `--mail-rcpt-allowfails` | Tetap melanjutkan SMTP jika sebagian recipient gagal. | `curl --mail-rcpt-allowfails --mail-rcpt a@example.com smtp://example.com` |
| `--mail-rcpt <address>` | Menentukan SMTP recipient. | `curl --mail-rcpt user@example.com smtp://example.com` |
| `-M, --manual` | Menampilkan manual curl. | `curl --manual` |
| `--max-filesize <bytes>` | Membatasi ukuran file maksimum. | `curl --max-filesize 10M -O https://example.com/file` |
| `--max-redirs <num>` | Membatasi jumlah redirect. | `curl --max-redirs 5 -L https://example.com` |
| `-m, --max-time <seconds>` | Batas waktu total transfer. | `curl --max-time 30 https://example.com` |
| `--metalink` | Menggunakan Metalink untuk transfer. | `curl --metalink file.meta4` |
| `--mptcp` | Mengaktifkan Multipath TCP jika tersedia. | `curl --mptcp https://example.com` |
| `--negotiate` | Menggunakan HTTP Negotiate/GSS-API. | `curl --negotiate -u : https://example.com` |
| `--netrc-file <file>` | Menggunakan file netrc tertentu. | `curl --netrc-file ~/.netrc https://example.com` |
| `--netrc-optional` | Menggunakan `.netrc` jika tersedia. | `curl --netrc-optional https://example.com` |
| `-n, --netrc` | Membaca credential dari `.netrc`. | `curl -n https://example.com` |
| `-:, --next` | Memulai transfer berikutnya dengan option state baru. | `curl URL1 --next URL2` |
| `--no-alpn` | Menonaktifkan ALPN. | `curl --no-alpn https://example.com` |
| `-N, --no-buffer` | Menonaktifkan buffering output. | `curl -N https://example.com/stream` |
| `--no-clobber` | Tidak menimpa file lokal yang sudah ada. | `curl --no-clobber -O https://example.com/file` |
| `--no-keepalive` | Menonaktifkan TCP keepalive. | `curl --no-keepalive https://example.com` |
| `--no-npn` | Menonaktifkan NPN. | `curl --no-npn https://example.com` |
| `--no-progress-meter` | Menonaktifkan progress meter. | `curl --no-progress-meter https://example.com` |
| `--no-sessionid` | Tidak menggunakan SSL session ID cache. | `curl --no-sessionid https://example.com` |
| `--noproxy <list>` | Menentukan host yang tidak menggunakan proxy. | `curl --noproxy localhost https://localhost` |
| `--ntlm-wb` | NTLM dengan winbind helper lama. | `curl --ntlm-wb -u user:pass https://example.com` |
| `--ntlm` | Menggunakan NTLM authentication. | `curl --ntlm -u user:pass https://example.com` |
| `--oauth2-bearer <token>` | Mengirim OAuth 2 Bearer token. | `curl --oauth2-bearer TOKEN https://example.com` |
| `--output-dir <dir>` | Menentukan direktori output. | `curl --output-dir downloads -O https://example.com/file` |
| `-o, --output <file>` | Menyimpan response ke file. | `curl -o page.html https://example.com` |
| `--parallel-immediate` | Segera menjalankan transfer paralel. | `curl --parallel --parallel-immediate URL1 URL2` |
| `--parallel-max <num>` | Membatasi jumlah transfer paralel. | `curl --parallel --parallel-max 5 URL1 URL2` |
| `-Z, --parallel` | Menjalankan beberapa transfer secara paralel. | `curl -Z URL1 URL2 URL3` |
| `--pass <phrase>` | Menentukan password untuk private key/certificate. | `curl --pass secret --key client.key https://example.com` |
| `--path-as-is` | Tidak menormalisasi path URL. | `curl --path-as-is https://example.com/a/../b` |
| `--pinnedpubkey <file/hash>` | Memvalidasi public key certificate tertentu. | `curl --pinnedpubkey sha256//HASH https://example.com` |
| `--post301` | Mempertahankan POST setelah redirect 301. | `curl --post301 -L -d data https://example.com` |
| `--post302` | Mempertahankan POST setelah redirect 302. | `curl --post302 -L -d data https://example.com` |
| `--post303` | Mempertahankan POST setelah redirect 303. | `curl --post303 -L -d data https://example.com` |
| `--preproxy <proxy>` | Menggunakan SOCKS proxy sebelum proxy utama. | `curl --preproxy socks5://localhost:1080 -x http://proxy:8080 https://example.com` |
| `-#, --progress-bar` | Menggunakan progress bar. | `curl -# -O https://example.com/file` |
| `--proto-default <protocol>` | Menentukan protocol default jika URL tidak punya scheme. | `curl --proto-default https https://example.com` |
| `--proto-redir <protocols>` | Membatasi protocol yang boleh digunakan saat redirect. | `curl --proto-redir =https -L http://example.com` |
| `--proto <protocols>` | Membatasi protocol yang boleh digunakan. | `curl --proto =https https://example.com` |
| `--proxy-anyauth` | Memilih autentikasi proxy secara otomatis. | `curl --proxy-anyauth -U user:pass -x proxy:8080 https://example.com` |
| `--proxy-basic` | Menggunakan Basic authentication untuk proxy. | `curl --proxy-basic -U user:pass -x proxy:8080 https://example.com` |
| `--proxy-ca-native` | Menggunakan CA store native untuk proxy TLS. | `curl --proxy-ca-native -x https://proxy:443 https://example.com` |
| `--proxy-cacert <file>` | CA certificate untuk proxy. | `curl --proxy-cacert proxy-ca.pem -x https://proxy:443 https://example.com` |
| `--proxy-capath <dir>` | Direktori CA certificate proxy. | `curl --proxy-capath /etc/ssl/certs -x https://proxy:443 https://example.com` |
| `--proxy-cert-type <type>` | Tipe client certificate proxy. | `curl --proxy-cert-type PEM --proxy-cert client.pem -x https://proxy:443 https://example.com` |
| `--proxy-cert <file>` | Client certificate untuk proxy TLS. | `curl --proxy-cert client.pem -x https://proxy:443 https://example.com` |
| `--proxy-ciphers <list>` | Cipher TLS untuk koneksi proxy. | `curl --proxy-ciphers AES256-SHA -x https://proxy:443 https://example.com` |
| `--proxy-crlfile <file>` | CRL untuk koneksi TLS proxy. | `curl --proxy-crlfile proxy-crl.pem -x https://proxy:443 https://example.com` |
| `--proxy-digest` | Digest authentication untuk proxy. | `curl --proxy-digest -U user:pass -x proxy:8080 https://example.com` |
| `--proxy-header <header>` | Menambahkan header ke proxy request. | `curl --proxy-header "X-Test: 1" -x proxy:8080 https://example.com` |
| `--proxy-http2` | Menggunakan HTTP/2 ke proxy HTTPS. | `curl --proxy-http2 -x https://proxy:443 https://example.com` |
| `--proxy-insecure` | Tidak memverifikasi certificate proxy TLS. | `curl --proxy-insecure -x https://proxy:443 https://example.com` |
| `--proxy-key-type <type>` | Tipe private key proxy client. | `curl --proxy-key-type PEM --proxy-key key.pem -x https://proxy:443 https://example.com` |
| `--proxy-key <file>` | Private key client untuk proxy TLS. | `curl --proxy-key key.pem -x https://proxy:443 https://example.com` |
| `--proxy-negotiate` | Negotiate authentication untuk proxy. | `curl --proxy-negotiate -U : -x proxy:8080 https://example.com` |
| `--proxy-ntlm` | NTLM authentication untuk proxy. | `curl --proxy-ntlm -U user:pass -x proxy:8080 https://example.com` |
| `--proxy-pass <phrase>` | Password private key proxy. | `curl --proxy-pass secret --proxy-key key.pem -x https://proxy:443 https://example.com` |
| `--proxy-pinnedpubkey <file/hash>` | Pin public key certificate proxy. | `curl --proxy-pinnedpubkey sha256//HASH -x https://proxy:443 https://example.com` |
| `--proxy-service-name <name>` | Service name untuk proxy authentication. | `curl --proxy-service-name HTTP -x proxy:8080 https://example.com` |
| `--proxy-ssl-allow-beast` | Mengizinkan TLS BEAST workaround lama pada proxy. | `curl --proxy-ssl-allow-beast -x https://proxy:443 https://example.com` |
| `--proxy-ssl-auto-client-cert` | Otomatis mencari client certificate untuk proxy TLS. | `curl --proxy-ssl-auto-client-cert -x https://proxy:443 https://example.com` |
| `--proxy-tls13-ciphers <list>` | Cipher TLS 1.3 untuk proxy. | `curl --proxy-tls13-ciphers TLS_AES_256_GCM_SHA384 -x https://proxy:443 https://example.com` |
| `--proxy-tlsauthtype <type>` | Tipe TLS authentication proxy. | `curl --proxy-tlsauthtype SRP -x https://proxy:443 https://example.com` |
| `--proxy-tlspassword <password>` | Password TLS authentication proxy. | `curl --proxy-tlspassword secret -x https://proxy:443 https://example.com` |
| `--proxy-tlsuser <user>` | Username TLS authentication proxy. | `curl --proxy-tlsuser user -x https://proxy:443 https://example.com` |
| `--proxy-tlsv1` | Meminta TLS 1.x untuk koneksi proxy. | `curl --proxy-tlsv1 -x https://proxy:443 https://example.com` |
| `-U, --proxy-user <user:password>` | Credential untuk proxy. | `curl -U user:pass -x proxy:8080 https://example.com` |
| `-x, --proxy <proxy>` | Menggunakan proxy. | `curl -x http://proxy:8080 https://example.com` |
| `--proxy1.0 <proxy>` | Menggunakan HTTP proxy versi 1.0. | `curl --proxy1.0 proxy:8080 https://example.com` |
| `-p, --proxytunnel` | Membuat HTTP CONNECT tunnel melalui proxy. | `curl -p -x proxy:8080 https://example.com` |
| `--pubkey <file>` | Public key untuk SCP/SFTP authentication. | `curl --pubkey id_rsa.pub sftp://user@example.com/file` |
| `-Q, --quote <command>` | Mengirim command FTP/IMAP/POP3 sebelum/sesudah transfer. | `curl -Q "PWD" ftp://example.com/` |
| `--random-file <file>` | File sumber entropy SSL lama. | `curl --random-file random.dat https://example.com` |
| `-r, --range <range>` | Mengunduh byte range tertentu. | `curl -r 0-999 https://example.com/file` |
| `--rate <requests>` | Membatasi rate transfer/request. | `curl --rate 10/s URL1 URL2` |
| `--raw` | Menonaktifkan decoding HTTP content encoding. | `curl --raw https://example.com` |
| `-e, --referer <url>` | Menentukan HTTP Referer. | `curl -e https://google.com https://example.com` |
| `-J, --remote-header-name` | Menggunakan filename dari Content-Disposition. | `curl -J -O https://example.com/download` |
| `--remote-name-all` | Menggunakan nama remote untuk semua URL. | `curl --remote-name-all URL1 URL2` |
| `-O, --remote-name` | Menyimpan dengan nama file dari URL. | `curl -O https://example.com/file.zip` |
| `-R, --remote-time` | Menyetel timestamp lokal berdasarkan remote file. | `curl -R -O ftp://example.com/file` |
| `--remove-on-error` | Menghapus file output jika transfer gagal. | `curl --remove-on-error -o file https://example.com/file` |
| `--request-target <target>` | Menentukan HTTP request-target secara manual. | `curl --request-target /custom -X GET https://example.com` |
| `-X, --request <method>` | Menentukan HTTP request method. | `curl -X DELETE https://example.com/item/1` |
| `--resolve <host:port:address>` | Memetakan hostname ke IP tertentu. | `curl --resolve example.com:443:127.0.0.1 https://example.com` |
| `--retry-all-errors` | Retry hampir semua error transfer. | `curl --retry-all-errors --retry 5 https://example.com` |
| `--retry-connrefused` | Retry jika koneksi ditolak. | `curl --retry-connrefused --retry 5 https://example.com` |
| `--retry-delay <seconds>` | Jeda antar retry. | `curl --retry 5 --retry-delay 2 https://example.com` |
| `--retry-max-time <seconds>` | Batas total waktu retry. | `curl --retry 10 --retry-max-time 60 https://example.com` |
| `--retry <num>` | Jumlah retry ketika transfer gagal. | `curl --retry 5 https://example.com` |
| `--sasl-authzid <id>` | Menentukan SASL authorization identity. | `curl --sasl-authzid admin -u user:pass imap://example.com/` |
| `--sasl-ir` | Mengaktifkan SASL initial response. | `curl --sasl-ir -u user:pass imap://example.com/` |
| `--service-name <name>` | Service name untuk GSS authentication. | `curl --service-name HTTP https://example.com` |
| `-S, --show-error` | Menampilkan error meskipun silent mode aktif. | `curl -sS https://example.com` |
| `-i, --show-headers` | Menampilkan response headers bersama body. | `curl -i https://example.com` |
| `-s, --silent` | Menyembunyikan progress dan error output. | `curl -s https://example.com` |
| `--skip-existing` | Melewati download jika file sudah ada. | `curl --skip-existing -O https://example.com/file` |
| `--socks4 <host:port>` | Menggunakan SOCKS4 proxy. | `curl --socks4 localhost:1080 https://example.com` |
| `--socks4a <host:port>` | Menggunakan SOCKS4a proxy dengan DNS remote. | `curl --socks4a localhost:1080 https://example.com` |
| `--socks5-basic` | Menggunakan username/password SOCKS5. | `curl --socks5-basic --socks5 localhost:1080 https://example.com` |
| `--socks5-gssapi-nec` | Menggunakan NEC compatibility mode untuk SOCKS5 GSS-API. | `curl --socks5-gssapi-nec --socks5 localhost:1080 https://example.com` |
| `--socks5-gssapi-service <name>` | Menentukan service name SOCKS5 GSS-API. | `curl --socks5-gssapi-service rcmd --socks5 localhost:1080 https://example.com` |
| `--socks5-gssapi` | Menggunakan GSS-API pada SOCKS5. | `curl --socks5-gssapi --socks5 localhost:1080 https://example.com` |
| `--socks5-hostname <host:port>` | SOCKS5 dengan DNS dilakukan proxy. | `curl --socks5-hostname localhost:1080 https://example.com` |
| `--socks5 <host:port>` | SOCKS5 proxy dengan DNS lokal. | `curl --socks5 localhost:1080 https://example.com` |
| `-Y, --speed-limit <speed>` | Batas minimum transfer speed. | `curl --speed-limit 1000 https://example.com/file` |
| `-y, --speed-time <seconds>` | Durasi minimum speed sebelum dianggap terlalu lambat. | `curl --speed-limit 1000 --speed-time 30 URL` |
| `--ssl-allow-beast` | Mengizinkan TLS BEAST workaround lama. | `curl --ssl-allow-beast https://example.com` |
| `--ssl-auto-client-cert` | Otomatis mencari client certificate TLS. | `curl --ssl-auto-client-cert https://example.com` |
| `--ssl-no-revoke` | Menonaktifkan pemeriksaan certificate revocation tertentu. | `curl --ssl-no-revoke https://example.com` |
| `--ssl-reqd` | Memerlukan TLS pada protokol yang mendukung STARTTLS. | `curl --ssl-reqd smtp://example.com` |
| `--ssl-revoke-best-effort` | Menganggap kegagalan revocation check tertentu sebagai non-fatal. | `curl --ssl-revoke-best-effort https://example.com` |
| `--ssl-sessions <file>` | Menyimpan/menggunakan TLS session cache. | `curl --ssl-sessions sessions.txt https://example.com` |
| `--ssl` | Mencoba menggunakan SSL/TLS untuk protokol yang mendukungnya. | `curl --ssl ftp://example.com/` |
| `-2, --sslv2` | Memaksa SSLv2 jika didukung. | `curl --sslv2 https://example.com` |
| `-3, --sslv3` | Memaksa SSLv3 jika didukung. | `curl --sslv3 https://example.com` |
| `--stderr <file>` | Mengarahkan error/progress ke file. | `curl --stderr errors.log https://example.com` |
| `--styled-output` | Mengaktifkan output terminal bergaya/warna bila tersedia. | `curl --styled-output -v https://example.com` |
| `--suppress-connect-headers` | Menyembunyikan headers CONNECT proxy dari output. | `curl -i --suppress-connect-headers -x proxy:8080 https://example.com` |
| `--tcp-fastopen` | Mengaktifkan TCP Fast Open. | `curl --tcp-fastopen https://example.com` |
| `--tcp-nodelay` | Mengaktifkan TCP_NODELAY. | `curl --tcp-nodelay https://example.com` |
| `-t, --telnet-option <opt=value>` | Mengatur opsi TELNET. | `curl --telnet-option TTYPE=xterm telnet://example.com` |
| `--tftp-blksize <value>` | Menentukan ukuran block TFTP. | `curl --tftp-blksize 1024 tftp://example.com/file` |
| `--tftp-no-options` | Tidak mengirim TFTP option request. | `curl --tftp-no-options tftp://example.com/file` |
| `-z, --time-cond <date/file>` | Transfer berdasarkan kondisi waktu. | `curl -z file.txt https://example.com/file` |
| `--tls-earlydata` | Mengaktifkan TLS 1.3 early data. | `curl --tls-earlydata https://example.com` |
| `--tls-max <version>` | Menentukan maksimum versi TLS. | `curl --tls-max 1.2 https://example.com` |
| `--tls13-ciphers <list>` | Menentukan cipher TLS 1.3. | `curl --tls13-ciphers TLS_AES_256_GCM_SHA384 https://example.com` |
| `--tlsauthtype <type>` | Menentukan tipe TLS authentication. | `curl --tlsauthtype SRP https://example.com` |
| `--tlspassword <password>` | Password TLS authentication. | `curl --tlspassword secret https://example.com` |
| `--tlsuser <user>` | Username TLS authentication. | `curl --tlsuser user https://example.com` |
| `--tlsv1.0` | Memaksa TLS 1.0 sebagai minimum. | `curl --tlsv1.0 https://example.com` |
| `--tlsv1.1` | Memaksa TLS 1.1 sebagai minimum. | `curl --tlsv1.1 https://example.com` |
| `--tlsv1.2` | Memaksa TLS 1.2 sebagai minimum. | `curl --tlsv1.2 https://example.com` |
| `--tlsv1.3` | Memaksa TLS 1.3 sebagai minimum. | `curl --tlsv1.3 https://example.com` |
| `-1, --tlsv1` | Memaksa TLS 1.x sebagai minimum. | `curl --tlsv1 https://example.com` |
| `--tr-encoding` | Meminta HTTP Transfer-Encoding compression. | `curl --tr-encoding https://example.com` |
| `--trace-ascii <file>` | Menyimpan trace transfer dalam format ASCII. | `curl --trace-ascii trace.txt https://example.com` |
| `--trace-config <file>` | Menampilkan konfigurasi trace. | `curl --trace-config trace.txt https://example.com` |
| `--trace-ids` | Menambahkan connection/transfer IDs pada trace. | `curl --trace-ids --trace trace.txt https://example.com` |
| `--trace-time` | Menambahkan timestamp pada trace. | `curl --trace-time --trace trace.txt https://example.com` |
| `--trace <file>` | Menyimpan trace lengkap transfer. | `curl --trace trace.txt https://example.com` |
| `--unix-socket <path>` | Menghubungkan ke Unix domain socket. | `curl --unix-socket /var/run/app.sock http://localhost/` |
| `-T, --upload-file <file>` | Meng-upload file. | `curl -T file.txt https://example.com/upload` |
| `--upload-flags <flags>` | Mengatur flag khusus upload. | `curl --upload-flags append -T file ftp://example.com/` |
| `--url-query <data>` | Menambahkan parameter query ke URL. | `curl --url-query "q=curl" https://example.com/search` |
| `--url <url>` | Menentukan URL secara eksplisit. | `curl --url https://example.com` |
| `-B, --use-ascii` | Mengaktifkan ASCII transfer untuk FTP. | `curl -B ftp://example.com/file.txt` |
| `-A, --user-agent <string>` | Menentukan HTTP User-Agent. | `curl -A "MyApp/1.0" https://example.com` |
| `-u, --user <user:password>` | Menentukan username dan password. | `curl -u user:pass https://example.com` |
| `--variable <name=content>` | Membuat command-line variable. | `curl --variable name=John --expand-url "https://example.com/{{name}}"` |
| `-v, --verbose` | Menampilkan detail proses request/response. | `curl -v https://example.com` |
| `-V, --version` | Menampilkan versi curl dan fitur build. | `curl --version` |
| `--vlan-priority <priority>` | Mengatur VLAN priority pada jaringan tertentu. | `curl --vlan-priority 5 https://example.com` |
| `-w, --write-out <format>` | Menampilkan informasi transfer dengan format tertentu. | `curl -w "%{http_code}\n" https://example.com` |
| `--xattr` | Menyimpan metadata URL/response sebagai extended attributes. | `curl --xattr -O https://example.com/file` |
