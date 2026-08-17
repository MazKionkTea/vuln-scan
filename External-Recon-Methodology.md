Baik, saya sudah membaca dan mengekstrak seluruh isi halaman **External Recon Methodology** beserta link-link dan tools yang disebutkan di dalamnya. Berikut saya sajikan dalam bentuk **katalog referensi terstruktur** yang siap kita gunakan sebagai bahan acuan untuk membangun sistem testing penetrasi.

---

## 📚 KATALOG REFERENSI & TOOLS – EXTERNAL RECON METHODOLOGY

---

### 🔹 FASE 1: ASSET DISCOVERY (Menemukan Seluruh Aset Perusahaan)

#### A. Mencari Akuisisi & Perusahaan Anak

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| Crunchbase | https://www.crunchbase.com/ | Mencari perusahaan yang diakuisisi oleh target |
| Wikipedia | https://www.wikipedia.org | Mencari daftar akuisisi perusahaan |
| SEC/EDGAR | https://www.sec.gov/edgar | Filing perusahaan publik AS |
| OpenCorporates | https://opencorporates.com/ | Database global struktur perusahaan & anak perusahaan |
| GLEIF LEI Database | https://www.gleif.org/ | Database legal entity identifier global |

#### B. Mencari ASN (Autonomous System Number) & IP Range

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| BGP.he.net | https://bgp.he.net/ | Mencari ASN berdasarkan nama perusahaan, IP, atau domain |
| BGPView.io | https://bgpview.io/ | Alternatif pencarian ASN |
| IPInfo.io | https://ipinfo.io/ | Informasi IP dan ASN |
| ASNLookup.com | http://asnlookup.com/ | Mencari IP range organisasi (dengan free API) |
| IPv4Info.com | http://ipv4info.com/ | Mencari IP dan ASN dari sebuah domain |
| **BBOT** | https://github.com/blacklanternsecurity/bbot | Otomatisasi agregasi ASN di akhir scan |
| **Amass** | https://github.com/OWASP/Amass | `amass intel -org <nama>` atau `-asn <ASN>` |
| AFRINIC | https://www.afrinic.net | Regional registry untuk Afrika |
| ARIN | https://www.arin.net | Regional registry untuk Amerika Utara |
| APNIC | https://www.apnic.net | Regional registry untuk Asia |
| LACNIC | https://www.lacnic.net | Regional registry untuk Amerika Latin |
| RIPE NCC | https://www.ripe.net | Regional registry untuk Eropa |

---

### 🔹 FASE 2: DOMAIN DISCOVERY (Menemukan Domain & Subdomain)

#### A. Reverse DNS

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| PTRArchive.com | http://ptrarchive.com/ | Online tool untuk reverse DNS lookup |
| **dnsrecon** | (tool CLI) | `dnsrecon -r <IP/range> -n <DNS>` |
| **massdns** | https://github.com/blechschmidt/massdns | Reverse lookup skala besar |
| **dnsx** | https://github.com/projectdiscovery/dnsx | Reverse lookup dan enrichment |

#### B. Reverse Whois (Loop)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| ViewDNS.info | https://viewdns.info/reversewhois/ | Reverse whois gratis |
| DomainEye | https://domaineye.com/reverse-whois | Reverse whois |
| Whoxy.com | https://www.whoxy.com/ | API reverse whois (berbayar) |
| **DomLink** | https://github.com/vysecurity/DomLink | Otomatisasi reverse whois (butuh Whoxy API key) |
| **Amass** | https://github.com/OWASP/Amass | `amass intel -d <domain> -whois` |

#### C. Tracker (Google Analytics, Adsense, dll)

| **Tool / Sumber** | **Fungsi** |
|-------------------|------------|
| Mencari Google Analytics ID yang sama di beberapa domain | Menemukan domain yang dikelola tim yang sama |
| Mencari Adsense ID yang sama | Sama seperti di atas |

#### D. Favicon Hash

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **favihash.py** | https://github.com/m4ll0k/Bug-Bounty-Toolz/blob/master/favihash.py | Mencari domain dengan hash favicon yang sama |
| **httpx** | https://github.com/projectdiscovery/httpx | `httpx -l targets.txt -favicon` |
| **Shodan** | https://www.shodan.io | `http.favicon.hash:<hash>` |
| **FOFA** | https://fofa.info | `icon_hash="<hash>"` |

#### E. Copyright / Unique String

| **Tool / Sumber** | **Fungsi** |
|-------------------|------------|
| **Shodan** | `http.html:"Copyright string"` |
| Google / Browser search | Mencari string unik yang muncul di beberapa web target |

#### F. Certificate Transparency (CRT)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| crt.sh | https://crt.sh/ | Mencari domain dari certificate transparency logs |
| **sublert** | https://github.com/yassineaboukir/sublert | Monitoring subdomain baru dari Certificate Transparency Logs |

#### G. Mail DMARC

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| DMARC.live | https://dmarc.live/info/<domain> | Mencari domain dengan DMARC yang sama |
| **dmarc-subdomains** | https://github.com/Tedixx/dmarc-subdomains | Menemukan subdomain dari DMARC |
| **spoofcheck** | https://github.com/BishopFox/spoofcheck | Pengecekan spoofing email |
| dmarcian.com | https://dmarcian.com/ | Analisis DMARC |

#### H. Passive DNS / Historical DNS

| **Tool / Sumber** | **Fungsi** |
|-------------------|------------|
| SecurityTrails | https://securitytrails.com/ | Riwayat IP dan subdomain |
| Censys | https://censys.io/ | Data sertifikat dan IP historis |
| VirusTotal | https://www.virustotal.com | Data DNS historis |

#### I. Lainnya (Shodan, SSL, dll)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **Shodan** | https://www.shodan.io | `org:"Tesla, Inc."` atau `ssl:"Tesla Motors"` |
| **sslsearch** | https://github.com/HarshVaragiya/sslsearch | Mencari organisasi di TLS certificate |
| **Assetfinder** | https://github.com/tomnomnom/assetfinder | Mencari domain terkait dengan domain utama |

---

### 🔹 FASE 3: SUBDOMAIN ENUMERATION (Metode & Tools Lengkap)

#### A. OSINT / Passive Subdomain Enumeration

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **BBOT** | https://github.com/blacklanternsecurity/bbot | `bbot -t <domain> -f subdomain-enum` |
| **Amass** | https://github.com/OWASP/Amass | `amass enum [-active] [-ip] -d <domain>` |
| **Subfinder** | https://github.com/projectdiscovery/subfinder | `subfinder -d <domain> [-silent]` |
| **Findomain** | https://github.com/Findomain/Findomain | `findomain -t <domain> [--quiet]` |
| **OneForAll** | https://github.com/shmilylty/OneForAll | `python3 oneforall.py --target <domain> run` |
| **Assetfinder** | https://github.com/tomnomnom/assetfinder | `assetfinder --subs-only <domain>` |
| **Sudomy** | https://github.com/screetsec/Sudomy | `sudomy -d <domain>` |
| **Vita** | (tool) | `vita -d <domain>` |
| **theHarvester** | https://github.com/laramies/theHarvester | `theHarvester -d <domain> -b <sources>` |
| **Crobat** | https://github.com/cgboal/sonarsearch | Menggunakan API sonar.omnisint.io |
| **chaospy** | https://github.com/dr-0x0x/chaospy | Mengakses data Chaos Project Discovery |

#### B. DNS Brute Force (Active)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **massdns** | https://github.com/blechschmidt/massdns | DNS brute force cepat, rentan false positive |
| **gobuster** | https://github.com/OJ/gobuster | `gobuster dns -d <domain> -w <wordlist>` |
| **shuffledns** | https://github.com/projectdiscovery/shuffledns | Wrapper massdns dengan wildcard handling |
| **puredns** | https://github.com/d3mondev/puredns | Menggunakan massdns |
| **aiodnsbrute** | https://github.com/blark/aiodnsbrute | Brute force asinkron |
| **dnsrecon** | (tool CLI) | `dnsrecon -a -d <domain>` untuk zone transfer |
| **dnsenum** | (tool CLI) | DNS enumeration |
| **dnscan** | https://github.com/rbsec/dnscan | Brute force subdomain rekursif |

**Wordlist & Resolver:**
- Subdomain wordlists: SecLists (https://github.com/danielmiessler/SecLists)
- DNS resolvers: https://www.wirewiki.com/dns-servers/all.txt
- Trusted resolvers: https://raw.githubusercontent.com/trickest/resolvers/main/resolvers-trusted.txt
- **dnsvalidator** – filter resolver yang valid: https://github.com/vortexau/dnsvalidator

#### C. Second Round / Permutation Generation

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **dnsgen** | https://github.com/ProjectAnte/dnsgen | Generate permutasi dari subdomain yang ditemukan |
| **goaltdns** | https://github.com/subfinder/goaltdns | Generate permutasi subdomain |
| **gotator** | https://github.com/Josue87/gotator | Generate permutasi subdomain |
| **altdns** | https://github.com/infosec-au/altdns | Generate permutasi dan resolusi |
| **dmut** | https://github.com/bp0lr/dmut | Mutasi dan alterasi subdomain |
| **alterx** | https://github.com/projectdiscovery/alterx | Generate subdomain berdasarkan pattern |

#### D. Smart Permutations (Machine Learning / Regex)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **regulator** | https://github.com/cramppet/regulator | Belajar pattern regex dari subdomain dan generate candidate |
| **subzuf** | https://github.com/elceef/subzuf | DNS brute-force fuzzer dengan algoritma guided response |

---

### 🔹 FASE 4: VHOST / VIRTUAL HOST DISCOVERY

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **HostHunter** | https://github.com/SpiderLabs/HostHunter | Mencari VHost di IP |
| **ffuf** | https://github.com/ffuf/ffuf | Fuzzing Host header dengan auto-calibration |
| **gobuster** | https://github.com/OJ/gobuster | `gobuster vhost -u <url> -w <wordlist>` |
| **wfuzz** | https://github.com/xmendez/wfuzz | Fuzzing Host header |
| **vhostbrute** | https://github.com/allyshka/vhostbrute | Brute force VHost |
| **VHostScan** | https://github.com/codingo/VHostScan | VHost scanner |

---

### 🔹 FASE 5: WEB SERVER DISCOVERY & SCREENSHOT

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **masscan** | https://github.com/robertdavidgraham/masscan | Port scanning cepat untuk web server |
| **httprobe** | https://github.com/tomnomnom/httprobe | Mendeteksi web server di port 80/443 |
| **fprobe** | https://github.com/theblackturtle/fprobe | Alternatif httprobe |
| **httpx** | https://github.com/projectdiscovery/httpx | HTTP probing dengan banyak fitur |
| **gowitness** | https://github.com/sensepost/gowitness | Screenshot web server |
| **EyeWitness** | https://github.com/FortyNorthSecurity/EyeWitness | Screenshot dan reporting |
| **Aquatone** | https://github.com/michenriksen/aquatone | Screenshot web server |
| **eyeballer** | https://github.com/BishopFox/eyeballer | Analisis screenshot untuk menemukan yang rentan |

---

### 🔹 FASE 6: PUBLIC CLOUD ASSETS

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **cloud_enum** | https://github.com/initstring/cloud_enum | Enumerasi resource cloud publik |
| **CloudScraper** | https://github.com/jordanpotti/CloudScraper | Scrape web untuk link ke cloud resources |
| **S3Scanner** | https://github.com/sa7mon/S3Scanner | Scan S3 bucket terbuka |

---

### 🔹 FASE 7: VULNERABILITY SCANNING (Otomatis)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **Nessus** | (Tenable) | Vulnerability scanner komersial |
| **OpenVAS** | https://www.openvas.org/ | Vulnerability scanner open-source |
| **Nuclei** | https://github.com/projectdiscovery/nuclei | Template-based vulnerability scanner |
| **brutespray** | https://github.com/x90skysn3k/brutespray | Brute force service dengan default credentials |

---

### 🔹 TOOLS UNTUK IP & HISTORICAL DATA

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **hakip2host** | https://github.com/hakluke/hakip2host | Mencari domain yang pointing ke IP tertentu |
| **gau** | https://github.com/lc/gau | Mengambil URL dari AlienVault OTX, Wayback Machine, Common Crawl |
| **SubDomainizer** | https://github.com/nsonaniya2010/SubDomainizer | Scrape JS untuk subdomain |
| **subscraper** | https://github.com/Cillian-Collins/subscraper | Scrape web untuk subdomain dari JS |

---

### 🔹 PLATFORM & API PENDATA

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **Shodan** | https://www.shodan.io | Search engine untuk perangkat terhubung internet |
| **Censys** | https://censys.io/ | Search engine untuk sertifikat dan host |
| **ZoomEye** | https://www.zoomeye.org/ | Search engine cybersecurity China |
| **SecurityTrails** | https://securitytrails.com/ | Data DNS historis dan subdomain |
| **VirusTotal** | https://www.virustotal.com | Intelligence threat |
| **URLScan** | https://urlscan.io/ | Analisis website |
| **RapidDNS** | https://rapiddns.io | Free API DNS |
| **IP.THC.ORG** | https://ip.thc.org | Free API |
| **Chaos Project Discovery** | https://chaos.projectdiscovery.io/ | Data subdomain bug bounty |
| **Censys Subdomain Finder** | https://github.com/christophetd/censys-subdomain-finder | Mencari subdomain via Censys |

---

### 🔹 MONITORING (Subdomain Baru)

| **Tool / Sumber** | **Link** | **Fungsi** |
|-------------------|----------|------------|
| **sublert** | https://github.com/yassineaboukir/sublert | Monitor subdomain baru dari Certificate Transparency Logs |

---

## 🗺️ PEMETAAN KE ROADMAP SISTEM TESTING PENETRASI

| **Fase Roadmap** | **Modul Sistem** | **Tools Referensi** |
|------------------|------------------|---------------------|
| **1. Discovery / Recon** | Asset Discovery | Crunchbase, OpenCorporates, BGP.he.net, BBOT, Amass, ASNLookup |
| | Domain Discovery | Assetfinder, Shodan, Censys, SecurityTrails, crt.sh, DMARC tools |
| **2. Subdomain Enumeration** | Subdomain Finder | Subfinder, Amass, BBOT, theHarvester, massdns, shuffledns, puredns |
| | Permutation Generator | dnsgen, goaltdns, gotator, altdns, dmut, alterx, regulator, subzuf |
| **3. Port Scanning** | Port Scanner | masscan, nmap (dari halaman sebelumnya) |
| **4. Service Discovery** | Web Server Discovery | httpx, httprobe, fprobe |
| **5. Vulnerability Scanning** | Vuln Scanner | Nuclei, Nessus, OpenVAS |
| **6. Brute-Force** | Auth Tester | brutespray |
| **7. Cloud Asset Discovery** | Cloud Enumeration | cloud_enum, CloudScraper, S3Scanner |

---

## ✅ STATUS SAAT INI

- **Roadmap utama** sudah ditetapkan (dari halaman pertama).
- **Fuzzing methodology** sudah dipetakan (dari halaman kedua).
- **External Recon methodology + seluruh tools** sudah dikatalogkan secara lengkap (dari halaman ketiga).
- **Belum ada kode** yang saya tulis (sesuai instruksi Anda).

Silakan berikan **referensi/link tambahan** berikutnya, atau jika sudah cukup, berikan instruksi untuk mulai membuat kode sesuai modul-modul yang Anda prioritaskan.

---

# Database Leaks

Baik, saya sudah membaca dan memahami halaman **Database Leaks** ini. Halaman ini merupakan **sub-modul dari External Recon Methodology** yang fokus pada pemanfaatan data dari kebocoran database (data breach) untuk menemukan kredensial atau informasi sensitif dari target.

Berikut saya sajikan katalog lengkap dari halaman ini, yang akan saya integrasikan ke dalam roadmap sistem testing penetrasi yang sudah kita bangun sebelumnya.

---

## 📚 KATALOG REFERENSI & TOOLS – DATABASE LEAKS (Sub-modul External Recon)

---

### 🔹 DATA BREACH SEARCH ENGINES (Mesin Pencari Kebocoran Data)

Halaman ini mendaftarkan berbagai layanan/platform yang dapat digunakan untuk mencari data yang bocor dari sebuah perusahaan atau individu, berdasarkan berbagai parameter seperti email, domain, username, IP, dll.

| **Tool / Platform** | **Link** | **Fungsi / Selector yang Didukung** |
|---------------------|----------|--------------------------------------|
| **GreyNoise Visualizer** | https://viz.greynoise.io/ | Mencari IP dan CIDR, serta query aktivitas scanner berdasarkan tag, CVE, dan metadata |
| **DeHashed** | https://www.dehashed.com/ | Mencari data terekspos berdasarkan username, email, IP, dan selector lainnya. Menyediakan monitoring dan API |
| **Have I Been Pwned? (HIBP)** | https://haveibeenpwned.com/ | Mengecek apakah sebuah email muncul dalam kebocoran data atau paste records yang diketahui. Menyediakan notifikasi dan API |
| **ScamSearch** | https://scamsearch.io/ | Mencari rekaman scammers berdasarkan foto profil, email, username, nomor telepon, alamat crypto, atau website |
| **Intelligence X** | https://intelx.io/ | Mencari selector seperti email, domain, URL, IP, dan CIDR di berbagai sumber yang terindeks |
| **SpyCloud** | https://spycloud.com/check-your-exposure/ | Mengecek email bisnis atau domain untuk kredensial terekspos, identitas yang terinfeksi infostealer, dan session cookie yang dicuri |
| **WeLeakInfo** | https://weleakinfo.io/ | Mencari database bocor menggunakan domain, nama, email, ID, telepon, IP, URL, atau hash |
| **BreachDirectory** | https://breachdirectory.org/ | Mengecek apakah email atau username telah dikompromikan |
| **LeakCheck** | https://leakcheck.io/ | Mencari email, username, telepon, hash, atau domain yang terekspos dan memonitor entri baru |
| **Findemail.io** | https://findemail.io/ | Menemukan alamat email untuk sebuah perusahaan tertentu |
| **Library of Leaks** | https://search.libraryofleaks.org/ | Mencari dokumen publik, perusahaan, dan orang, termasuk dataset kebocoran |
| **LeakRadar** | https://leakradar.io/ | Mencari kredensial bocor berdasarkan email, domain, atau string mentah, serta memonitor eksposur baru |
| **InfoStealers** | https://infostealers.info/en/info | Mencari log infostealer dari perangkat yang terinfeksi dan memonitor data baru |
| **Leak-Lookup** | https://leak-lookup.com/ | Mencari di berbagai kebocoran data dan memonitor eksposur kredensial |
| **Scylla.so** | https://scylla.so/ | Mesin pencari kebocoran database berbasis komunitas |
| **Leaked.domains** | https://leaked.domains/ | Mencari kredensial bocor dan rekaman terkait berdasarkan domain, email, username, password, IP, dan selector lainnya |
| **WhiteIntel** | https://whiteintel.io/ | Memonitor aktivitas dark-web, kebocoran kredensial, data infostealer, dan mention brand |
| **PSBDMP** | https://psbdmp.ws/ | Platform pencarian dan monitoring dump Pastebin |

---

### 🔹 TOOLS UNTUK ENUMERASI DATA LEAKS (Command Line)

| **Tool** | **Link** | **Fungsi** |
|----------|----------|------------|
| **Leaker** | https://github.com/vflame6/leaker | CLI untuk penemuan leak secara pasif yang mencari di berbagai sumber online berdasarkan email, username, domain, keyword, atau telepon |

---

## 🗺️ PEMETAAN KE ROADMAP SISTEM TESTING PENETRASI

Modul **Database Leaks** ini akan masuk ke dalam fase:

| **Fase Roadmap** | **Sub-Modul Sistem** | **Kontribusi dari Halaman Ini** |
|------------------|----------------------|--------------------------------|
| **1. Discovery / Recon** | **Credential Discovery** | Menemukan kredensial karyawan/ admin yang bocor dari database breach, yang bisa digunakan untuk fase **Brute-Force** atau **Phishing** |
| **7. Brute-Force** | **Password List Generator** | Kredensial yang ditemukan dari leak bisa digunakan sebagai wordlist untuk brute-force ke service-service target |
| **8. Phishing** | **Target Profiling** | Email dan informasi karyawan yang ditemukan bisa digunakan untuk spear-phishing |
| **11. Post-Exploit (Looting)** | **Credential Enrichment** | Setelah mendapatkan email/user dari sistem target, bisa dicocokkan dengan database leak untuk mencari password yang mungkin digunakan ulang |

---

## ✅ STATUS TERBARU

- **Roadmap utama** sudah ditetapkan (dari halaman pertama).
- **Fuzzing methodology** sudah dipetakan (dari halaman kedua).
- **External Recon methodology + seluruh tools** sudah dikatalogkan (dari halaman ketiga).
- **Database Leaks** sebagai sub-modul External Recon sudah ditambahkan ke katalog.

**Total tools & platform yang tercatat hingga saat ini: 50+**

---

Silakan berikan **referensi/link tambahan** berikutnya, atau jika sudah cukup, berikan instruksi untuk mulai membuat kode sesuai modul-modul yang Anda prioritaskan.

---

# Wide Source Code Search

Baik, saya sudah membaca dan memahami halaman **Wide Source Code Search** ini. Halaman ini merupakan **sub-modul dari External Recon Methodology** yang berfokus pada pencarian kode sumber secara luas di berbagai platform untuk menemukan informasi yang bocor, pola rentan, maupun infrastruktur internal.

Berikut saya sajikan katalog lengkap dari halaman ini, yang akan saya integrasikan ke dalam roadmap sistem testing penetrasi yang sudah kita bangun sebelumnya.

---

## 📚 KATALOG REFERENSI & TOOLS – WIDE SOURCE CODE SEARCH (Sub-modul External Recon)

---

### 🔹 PLATFORM CODE SEARCH (Pencarian Kode Sumber)

Halaman ini mendaftarkan berbagai platform yang memungkinkan pencarian kode secara literal, regex, symbol-aware, atau path-scoped di ribuan/jutaan repositori.

| **Tool / Platform** | **Link** | **Fungsi / Fitur Utama** |
|---------------------|----------|---------------------------|
| **Sourcebot** | https://www.sourcebot.dev/ | Open-source / self-hosted code search dengan regex, symbol, dan filtered search. Dapat dikonfigurasi untuk mengindeks branch/tag tambahan dan dicari dengan filter `rev:` |
| **Sourcegraph** | https://sourcegraph.com/search | Code search dengan regex, boolean, symbol, repository/file/language, branch/commit, diff, dan commit-message queries. Structural search tersedia opsional (dinonaktifkan secara default karena keterbatasan performa) |
| **GitHub Code Search** | https://github.com/search | Mendukung regex, boolean logic, dan qualifiers seperti `repo:`, `org:`, `user:`, `path:`, `language:`, `symbol:`, `content:`, dan `is:` |
| **GitLab Exact Code Search** | https://docs.gitlab.com/user/search/exact_code_search/ | Code search berbasis Zoekt dengan mode exact dan regex, serta filter `file:`, `lang:`, `repo:`, dan `sym:` |
| **GitLab Advanced Search** | https://docs.gitlab.com/user/search/advanced_search/ | Pencarian yang lebih luas karena dapat mencari code, comments, commits, merge requests, dan wikis |
| **SearchCode** | https://searchcode.com/ | Code-intelligence service dengan boolean/regex/structural code search serta file dan symbol retrieval |
| **Grep** | https://grep.app/ | Pencarian kode publik di lebih dari satu juta repositori GitHub, dengan content, file, dan path search |

---

### 🔹 KEMAMPUAN PENCARIAN YANG BERGUNA (Useful Search Capabilities)

Dalam konteks bug bounty / red team, kemampuan yang paling berguna adalah:

| **Kemampuan** | **Deskripsi** |
|---------------|---------------|
| **Regex support** | Mencari format token, skema URL, nama fungsi berbahaya, atau fragmen multiline |
| **Path filters** | Melompat langsung ke file bernilai tinggi seperti `.github/workflows/`, `terraform/`, `helm/`, `.env`, `values.yaml`, `secrets.*`, `credentials.*`, `Dockerfile`, `Jenkinsfile`, `nginx.conf` |
| **Language filters** | Memisahkan kode aplikasi dari IaC dan pipeline |
| **Symbol-aware search** | Menemukan handlers, auth middleware, webhook consumers, fungsi helper berbahaya, atau class/method spesifik |
| **Boolean operators** | Mengurangi noise: `NOT path:test`, `NOT is:generated`, `NOT is:vendored`, `foo OR bar` |
| **Revision/diff search** | Memulihkan string yang dihapus, mengikuti perubahan keamanan, atau memeriksa branch/tag non-default tanpa cloning |

---

### 🔹 HIGH-SIGNAL QUERY IDEAS (Ide Query Bernilai Tinggi)

Halaman ini memberikan contoh query yang dapat diadaptasi ke GitHub, GitLab, Sourcegraph, atau Sourcebot:

| **Target Area** | **Contoh Query** |
|-----------------|------------------|
| **CI/CD Workflows** | `org:target path:.github/workflows ("pull_request_target" OR "workflow_run" OR "ACTIONS_STEP_DEBUG")` |
| **Infrastructure as Code** | `org:target (path:terraform OR path:helm OR language:HCL OR language:YAML) ("role_arn" OR "assume_role" OR "client_secret" OR "access_key")` |
| **Secrets & Keys** | `org:target ("BEGIN PRIVATE KEY" OR "ghp_" OR "github_pat_" OR "AIza" OR "xoxb-")` |
| **Environment Files** | `org:target (path:.env OR path:values.yaml OR path:application-prod OR path:credentials)` |
| **Privileged Workflows** | `org:target path:.github/workflows ("pull_request_target" OR "workflow_run" OR "workflow_call" OR "secrets: inherit" OR "id-token: write" OR "self-hosted")` |
| **Unpinned Third-Party Actions** | `org:target path:.github/workflows ("uses:" AND NOT /@[0-9a-f]{40}/)` |
| **Dev Containers** | `org:target (path:.devcontainer OR path:devcontainer.json) ("remoteEnv" OR "containerEnv" OR "initializeCommand" OR "postCreateCommand" OR "mounts")` |
| **Dev Container Features** | `org:target ("devcontainer-feature.json" OR "install.sh") ("curl " OR "wget " OR "docker.sock" OR "sudo ")` |
| **Internal/Staging Hosts** | `org:target ("internal" OR "corp" OR "staging") ("https://" OR "ssh://") NOT path:test` |

---

### 🔹 FILE-FILE BERNILAI TINGGI YANG PERLU DIPRIORITASKAN

| **File / Path** | **Apa yang Dicari** |
|-----------------|---------------------|
| `.github/workflows/*.yml` | Trigger `pull_request_target` dan `workflow_run` yang berisiko, third-party actions yang hanya di-pin ke tag/branch (bukan full commit SHA) |
| `.devcontainer/devcontainer.json` | `remoteEnv`, `containerEnv`, `initializeCommand`, `postCreateCommand`, `mounts`, dan Dockerfile/script yang direferensikan |
| `devcontainer-feature.json` & `install.sh` | Metadata dan entrypoint script dari Dev Container Features |
| `.gitlab-ci.yml`, `azure-pipelines.yml`, `cloudbuild.yaml`, `Jenkinsfile`, `buildkite*`, `atlantis.yaml`, `terragrunt.hcl`, `helmfile.yaml`, `skaffold.yaml`, `argocd*` | File CI / control-plane lainnya |

---

### 🔹 MASS LOCAL SEARCH (Ketika Pencarian Terindeks Tidak Cukup)

Jika pencarian terindeks tidak cukup, lakukan cloning massal dan pencarian lokal:

```bash
# Clone semua repo dari organisasi target
gh repo list TARGET_ORG --limit 1000 --json nameWithOwner,sshUrl \
  | jq -r '.[].sshUrl' \
  | while read -r repo; do
      dst="repos/$(basename "$repo" .git)"
      git clone --depth 1 "$repo" "$dst" 2>/dev/null || true
    done

# Cari secrets dengan ripgrep
rg -n --pcre2 \
  -g '!{.git,node_modules,vendor,dist,build,coverage}' \
  '(AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9_]{20,255}|github_pat_[A-Za-z0-9_]{20,255}|AIza[0-9A-Za-z\-_]{35}|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)' \
  repos/
```

Gunakan local searching ketika perlu:
- Mencari branch atau tag non-default
- Mencari history git
- Menjalankan query PCRE2/multiline secara lebih agresif
- Batch triage banyak repositori tanpa batasan UI

---

### 🔹 SEARCH HISTORY, BRANCHES, AND DIFFS

Untuk mencari di seluruh branch, tag, dan history:

```bash
REPO_DIR=repos/some-repo
git -C "$REPO_DIR" fetch --all --tags --prune
git -C "$REPO_DIR" for-each-ref --format='%(refname:short)' refs/remotes/origin refs/tags \
  | while read -r ref; do
      git -C "$REPO_DIR" grep -nI -E 'pull_request_target|workflow_call|id-token: write|secrets: inherit|remoteEnv|containerEnv' "$ref" || true
    done
git -C "$REPO_DIR" log --all -p -G 'gh[pousr]_|github_pat_|BEGIN [A-Z ]+PRIVATE KEY|internal.*https?://' -- .
```

Ini sangat berguna ketika string yang menarik hanya ada di branch release, tag, atau commit yang sudah dihapus.

---

### 🔹 BLIND SPOTS & PLATFORM-SPECIFIC GOTCHAS

| **Blind Spot / Gotcha** | **Penjelasan** |
|--------------------------|----------------|
| **Default-branch-only indexing** | Banyak platform hanya mengindeks branch default. Jangan berasumsi code search mencakup semua branch/tag/history |
| **Large files, vendored code, generated code** | Mungkin dilewati atau menjadi noise |
| **Comments, issues, PRs, gists, wikis** | Sering di luar cakupan generic code search dan memerlukan tooling platform-specific |
| **Codespaces / devcontainer configs** | Dapat bersifat branch-specific. Branch default yang bersih tidak berarti environment dev bersih di semua tempat |
| **Reusable workflows/actions** | Mungkin berada di luar file workflow utama. Cari `.github/actions/`, `action.yml`, `action.yaml`, `devcontainer-feature.json`, `install.sh` |
| **GitHub Code Search** | Hanya mencari di default branch. Untuk feature branches, deleted secrets, atau historical code, clone repo dan cari secara lokal |
| **GitLab Exact Code Search** | Hanya mengindeks file lebih kecil dari 1 MB dengan kurang dari 20.000 trigrams |
| **Sourcebot** | Default branch by default, tapi dapat dikonfigurasi untuk branch/tag tambahan dan dicari dengan filter `rev:` |
| **Sourcegraph** | Structural search hanya jika di-enable dan perhatikan batasan performa |

---

### 🔹 TOOLS TERKAIT (Disebutkan dalam Referensi)

| **Tool** | **Fungsi** |
|----------|------------|
| **TruffleHog** | Dedicated secret hunting di repositori |
| **Gitleaks** | Dedicated secret hunting di repositori |

---

## 🗺️ PEMETAAN KE ROADMAP SISTEM TESTING PENETRASI

Modul **Wide Source Code Search** ini akan masuk ke dalam fase:

| **Fase Roadmap** | **Sub-Modul Sistem** | **Kontribusi dari Halaman Ini** |
|------------------|----------------------|--------------------------------|
| **1. Discovery / Recon** | **Source Code Reconnaissance** | Mencari kode sumber publik milik target untuk menemukan: credentials/rahasia yang bocor, pola kerentanan, teknologi yang digunakan, host internal, staging/admin panel, CI/CD pipeline, dan infrastruktur-as-code |
| **5. Exploit Matching** | **Vulnerable Pattern Discovery** | Menemukan pola kode berbahaya (exec, template rendering, SSRF fetchers, deserializers, dll) yang bisa dieksploitasi |
| **9. Getting Shell** | **CI/CD Exploitation** | Menemukan workflow CI/CD yang bisa disalahgunakan untuk eksekusi kode |
| **11. Post-Exploit (Looting)** | **Credential Harvesting** | Mencari secrets yang tersembunyi di history git, branch non-default, atau commit yang sudah dihapus |

---

## ✅ STATUS TERBARU

- **Roadmap utama** sudah ditetapkan (dari halaman pertama).
- **Fuzzing methodology** sudah dipetakan (dari halaman kedua).
- **External Recon methodology + seluruh tools** sudah dikatalogkan (dari halaman ketiga).
- **Database Leaks** sebagai sub-modul External Recon sudah ditambahkan.
- **Wide Source Code Search** sebagai sub-modul External Recon sudah ditambahkan.

**Total tools & platform yang tercatat hingga saat ini: 60+**

---

Silakan berikan **referensi/link tambahan** berikutnya, atau jika sudah cukup, berikan instruksi untuk mulai membuat kode sesuai modul-modul yang Anda prioritaskan.

---

# Github Dorks & Leaks

Baik, saya sudah membaca dan memahami halaman **GitHub Dorks & Leaks** ini. Halaman ini merupakan **sub-modul dari External Recon Methodology** yang berfokus secara spesifik pada pencarian dan pemanfaatan rahasia (secrets) yang bocor di platform GitHub.

Berikut saya sajikan katalog lengkap dari halaman ini, yang akan saya integrasikan ke dalam roadmap sistem testing penetrasi.

---

## 📚 KATALOG REFERENSI & TOOLS – GITHUB LEAKED SECRETS (Sub-modul External Recon)

---

### 🔹 TOOLS PENCARI SECRETS (Tools to find secrets in git repos and file system)

| **Tool** | **Link / Repo** | **Fungsi / Fitur Utama** |
|----------|-----------------|---------------------------|
| **TruffleHog v3** | https://github.com/trufflesecurity/trufflehog | Mampu memverifikasi banyak kredensial secara *live*; dapat memindai GitHub org, issues/PRs, gists, dan wikis. |
| **Gitleaks** | https://github.com/gitleaks/gitleaks | Memindai repositori Git, direktori, dan arsip. Mendukung `--log-opts="--all"` untuk history penuh, `--max-archive-depth 1` untuk inspeksi arsip. |
| **Nosey Parker / Titus** | https://github.com/praetorian-inc/noseyparker (diarsipkan, digantikan oleh Titus) | Untuk instalasi yang masih ada: `noseyparker scan --datastore np.db` dilanjutkan `noseyparker report --datastore np.db` |
| **ggshield (GitGuardian CLI)** | https://github.com/GitGuardian/ggshield | Memindai file, repositori, dan image Docker; terintegrasi dengan workflow lokal atau CI: `ggshield secret scan repo .` |

---

### 🔹 DI MANA SECRETS UMUMNYA BOCOR DI GITHUB (Where secrets commonly leak)

| **Lokasi** | **Penjelasan** | **Cara Mengakses** |
|------------|----------------|---------------------|
| **Default branch (code search)** | GitHub Code Search hanya mengindeks branch default | Gunakan UI GitHub atau API (tanpa regex) |
| **Non-default branches & tags** | Tidak terindeks oleh search default | Clone repositori dan scan secara lokal |
| **Full git history** | Commit yang sudah dihapus tetap menyimpan secrets | Clone dan scan dengan `gitleaks` / `trufflehog` |
| **Issues, PRs, comments, descriptions** | Sering mengandung secrets yang terpapar | TruffleHog dengan flag `--issue-comments` dan `--pr-comments` |
| **Actions workflow logs & artifacts** | Redaksi secret tidak dijamin; logs dapat di-download | Akses read ke repositori cukup untuk melihat/mendownload |
| **Wikis** | Sering luput dari perhatian | TruffleHog dengan flag `--include-wikis` |
| **Release assets** | File yang diunggah sebagai release | Download manual atau via API |
| **Gists** | Sering mengandung secrets yang tidak disadari | Cari dengan tooling atau UI; beberapa tools bisa menyertakan gists |

---

### 🔹 GOTCHAS / PERANGKAP YANG PERLU DIWASPADAI

| **Masalah** | **Penjelasan** |
|-------------|----------------|
| **Regex di UI vs API** | UI GitHub Code Search mendukung regex, sedangkan REST/API path (termasuk `gh search code`) menggunakan legacy engine dan **tidak** mendukung regex. |
| **Batas ukuran file** | GitHub search mengecualikan file di atas batas ukuran yang didokumentasikan dan **tidak exhaustive** |
| **Hanya default branch** | Untuk pencarian menyeluruh, clone dan scan secara lokal dengan secrets scanner |

---

### 🔹 PROGRAMMATIC ORG-WIDE SCANNING (Scan Seluruh Organisasi Secara Terprogram)

#### Menggunakan TruffleHog

```bash
export GITHUB_TOKEN=<token>
trufflehog github --org Target \
  --results=verified \
  --include-wikis \
  --issue-comments \
  --pr-comments \
  --gist-comments
```


#### Menggunakan Gitleaks (clone shallow dan scan)

```bash
gh repo list Target --limit 1000 --json nameWithOwner,url \
  | jq -r '.[].url' | while read -r r; do
      tmp=$(mktemp -d)
      git clone --depth 1 "$r" "$tmp" && \
        gitleaks dir -v "$tmp" || true
      rm -rf "$tmp"
    done
```


#### Menggunakan Nosey Parker (mono checkout)

```bash
# setelah cloning banyak repositori di ./org
noseyparker scan --datastore np.db org/ && \
noseyparker report --datastore np.db
```


#### Menggunakan ggshield

```bash
# current working tree
ggshield secret scan path -r .
# full git history of a repo
ggshield secret scan repo <repo>
```


> **Tips untuk git history:** Preferensikan scanner yang mem-parsing `git log -p --all` untuk menangkap secrets yang sudah dihapus.

---

### 🔹 UPDATED DORKS UNTUK MODERN TOKENS (Dork untuk Token Modern)

| **Jenis Token** | **Pattern / Contoh** |
|-----------------|----------------------|
| **GitHub Tokens** | `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`, `github_pat_` |
| **Slack Tokens** | `xoxb-`, `xoxp-`, `xoxa-`, `xoxs-`, `xoxc-`, `xoxe-` |
| **AWS** | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `aws_session_token` |
| **Google / Azure** | `GOOGLE_API_KEY`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET` |
| **AI API Keys** | `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` |

---

### 🔹 DORKS (Kumpulan Query Pencarian GitHub)

#### Keyword-based Dorks (Parsial)

| **Keyword** |
|-------------|
| `".mlab.com password"` | `"access_key"` | `"access_token"` | `"amazonaws"` |
| `"api.googlemaps AIza"` | `"api_key"` | `"api_secret"` | `"apidocs"` |
| `"apikey"` | `"apiSecret"` | `"app_key"` | `"app_secret"` |
| `"appkey"` | `"appkeysecret"` | `"application_key"` | `"appsecret"` |
| `"appspot"` | `"auth"` | `"auth_token"` | `"authorizationToken"` |
| `"aws_access"` | `"aws_access_key_id"` | `"aws_key"` | `"aws_secret"` |
| `"aws_token"` | `"AWSSecretKey"` | `"bashrc password"` | `"bucket_password"` |
| `"client_secret"` | `"cloudfront"` | `"codecov_token"` | `"config"` |
| `"conn.login"` | `"connectionstring"` | `"consumer_key"` | `"credentials"` |
| `"database_password"` | `"db_password"` | `"db_username"` | `"dbpasswd"` |
| `"dbpassword"` | `"dbuser"` | `"dot-files"` | `"dotfiles"` |
| `"encryption_key"` | `"fabricApiSecret"` | `"fb_secret"` | `"firebase"` |
| `"ftp"` | `"gh_token"` | `"github_key"` | `"github_token"` |
| `"gitlab"` | `"gmail_password"` | `"gmail_username"` | `"herokuapp"` |
| `"internal"` | `"irc_pass"` | `"JEKYLL_GITHUB_TOKEN"` | `"key"` |
| `"keyPassword"` | `"ldap_password"` | `"ldap_username"` | `"login"` |
| `"mailchimp"` | `"mailgun"` | `"master_key"` | `"mydotfiles"` |
| `"mysql"` | `"node_env"` | `"npmrc _auth"` | `"oauth_token"` |
| `"pass"` | `"passwd"` | `"password"` | `"passwords"` |
| `"pem private"` | `"preprod"` | `"private_key"` | `"prod"` |
| `"pwd"` | `"pwds"` | `"rds.amazonaws.com password"` | `"redis_password"` |
| `"root_password"` | `"secret"` | `"secret.password"` | `"secret_access_key"` |
| `"secret_key"` | `"secret_token"` | `"secrets"` | `"secure"` |
| `"security_credentials"` | `"send.keys"` | `"send_keys"` | `"sendkeys"` |
| `"SF_USERNAME salesforce"` | `"sf_username"` | `"site.com" FIREBASE_API_JSON=` | `"site.com" vim_settings.xml` |
| `"slack_api"` | `"slack_token"` | `"sql_password"` | `"ssh"` |
| `"ssh2_auth_password"` | `"sshpass"` | `"staging"` | `"stg"` |
| `"storePassword"` | `"stripe"` | `"swagger"` | `"testuser"` |
| `"token"` | `"x-api-key"` | `"xoxb "` | `"xoxp"` |



#### File Extension-based Dorks

| **Extension** |
|---------------|
| `extension:ica` | `extension:avastlic` | `"support.avast.com"` | `extension:bat` |
| `extension:cfg` | `extension:env` | `extension:exs` | `extension:ini` |
| `extension:json api.forecast.io` | `extension:json googleusercontent client_secret` | `extension:json mongolab.com` | `extension:pem` |
| `extension:pem private` | `extension:ppk` | `extension:ppk private` | `extension:properties` |
| `extension:sh` | `extension:sls` | `extension:sql` | `extension:sql mysql dump` |
| `extension:sql mysql dump password` | `extension:yaml mongolab.com` | `extension:zsh` |



#### Filename-based Dorks

| **Filename Pattern** |
|----------------------|
| `filename:.bash_history` | `filename:.bash_history DOMAIN-NAME` | `filename:.bash_profile aws` |
| `filename:.bashrc mailchimp` | `filename:.bashrc password` | `filename:.cshrc` |
| `filename:.dockercfg auth` | `filename:.env DB_USERNAME NOT homestead` | `filename:.env MAIL_HOST=smtp.gmail.com` |
| `filename:.esmtprc password` | `filename:.ftpconfig` | `filename:.git-credentials` |
| `filename:.history` | `filename:.htpasswd` | `filename:.netrc password` |
| `filename:.npmrc _auth` | `filename:.pgpass` | `filename:.remote-sync.json` |
| `filename:.s3cfg` | `filename:.sh_history` | `filename:.tugboat NOT _tugboat` |
| `filename:_netrc password` | `filename:apikey` | `filename:bash` |
| `filename:bash_history` | `filename:bash_profile` | `filename:bashrc` |
| `filename:beanstalkd.yml` | `filename:CCCam.cfg` | `filename:composer.json` |
| `filename:config` | `filename:config irc_pass` | `filename:config.json auths` |
| `filename:config.php dbpasswd` | `filename:configuration.php JConfig password` | `filename:connections` |
| `filename:connections.xml` | `filename:constants` | `filename:credentials` |
| `filename:credentials aws_access_key_id` | `filename:cshrc` | `filename:database` |
| `filename:dbeaver-data-sources.xml` | `filename:deployment-config.json` | `filename:dhcpd.conf` |
| `filename:dockercfg` | `filename:environment` | `filename:express.conf` |
| `filename:express.conf path:.openshift` | `filename:filezilla.xml` | `filename:filezilla.xml Pass` |
| `filename:git-credentials` | `filename:gitconfig` | `filename:global` |
| `filename:history` | `filename:htpasswd` | `filename:hub oauth_token` |
| `filename:id_dsa` | `filename:id_rsa` | `filename:id_rsa or filename:id_dsa` |
| `filename:idea14.key` | `filename:known_hosts` | `filename:logins.json` |
| `filename:makefile` | `filename:master.key path:config` | `filename:netrc` |
| `filename:npmrc` | `filename:pass` | `filename:passwd path:etc` |
| `filename:pgpass` | `filename:prod.exs` | `filename:prod.exs NOT prod.secret.exs` |
| `filename:prod.secret.exs` | `filename:proftpdpasswd` | `filename:recentservers.xml` |
| `filename:recentservers.xml Pass` | `filename:robomongo.json` | `filename:s3cfg` |
| `filename:secrets.yml password` | `filename:server.cfg` | `filename:server.cfg rcon password` |
| `filename:settings` | `filename:settings.py SECRET_KEY` | `filename:sftp-config.json` |
| `filename:sftp-config.json password` | `filename:sftp.json path:.vscode` | `filename:shadow` |
| `filename:shadow path:etc` | `filename:spec` | `filename:sshd_config` |
| `filename:token` | `filename:tugboat` | `filename:ventrilo_srv.ini` |
| `filename:WebServers.xml` | `filename:wp-config` | `filename:wp-config.php` |
| `filename:zhrc HEROKU_API_KEY` | `language:json HEROKU_API_KEY` | `language:shell HOMEBREW_GITHUB_API_TOKEN` |
| `language:shell jsforce extension:js conn.login` | `language:yaml -filename:travis` | `msg nickserv identify filename:config` |



#### Organization-specific Dorks

| **Dork** |
|----------|
| `org:Target "AWS_ACCESS_KEY_ID"` |
| `org:Target "list_aws_accounts"` |
| `org:Target "aws_access_key"` |
| `org:Target "aws_secret_key"` |
| `org:Target "bucket_name"` |
| `org:Target "S3_ACCESS_KEY_ID"` |
| `org:Target "S3_BUCKET"` |
| `org:Target "S3_ENDPOINT"` |
| `org:Target "S3_SECRET_ACCESS_KEY"` |
| `path:sites databases password private -language:java` |
| `PT_TOKEN language:bash` |
| `SECRET_KEY_BASE= language:bash` |
| `shodan_api_key language:python` |
| `WORDPRESS_DB_PASSWORD= language:python` |
| `xoxp OR xoxb OR xoxa` |
| `s3.yml` | `.exs` | `beanstalkd.yml` | `deploy.rake` | `.sls` |



#### Miscellaneous Dorks

| **Dork** |
|----------|
| `AWS_SECRET_ACCESS_KEY` |
| `API KEY` | `API SECRET` | `API TOKEN` |
| `ROOT PASSWORD` | `ADMIN PASSWORD` |
| `GCP SECRET` | `AWS SECRET` |
| `"private" extension:pgp` |



---

### 🔹 REFERENSI TAMBAHAN

| **Referensi** | **Link** |
|---------------|----------|
| Wide Source Code Search | https://hacktricks.wiki/wide-source-code-search.html |

---

## 🗺️ PEMETAAN KE ROADMAP SISTEM TESTING PENETRASI

Modul **GitHub Leaked Secrets** ini akan masuk ke dalam fase:

| **Fase Roadmap** | **Sub-Modul Sistem** | **Kontribusi dari Halaman Ini** |
|------------------|----------------------|--------------------------------|
| **1. Discovery / Recon** | **GitHub Reconnaissance** | Mencari secrets yang bocor di repositori publik milik target (organisasi, user, atau repositori terkait) |
| **1. Discovery / Recon** | **Credential Discovery** | Menemukan kredensial AWS, GCP, Azure, Slack, GitHub, API keys, database credentials, dll |
| **7. Brute-Force** | **Password List Generator** | Kredensial yang ditemukan bisa digunakan sebagai wordlist atau langsung untuk login ke service target |
| **8. Phishing** | **Target Profiling** | Informasi internal yang bocor (hostnames, staging URLs, dll) bisa digunakan untuk spear-phishing |
| **11. Post-Exploit (Looting)** | **Credential Enrichment** | Mencocokkan kredensial yang ditemukan dengan sistem target |
| **5. Exploit Matching** | **Vulnerable Pattern Discovery** | Menemukan pola kode yang rentan atau konfigurasi yang salah |

---

## ✅ STATUS TERBARU

- **Roadmap utama** sudah ditetapkan (dari halaman pertama).
- **Fuzzing methodology** sudah dipetakan (dari halaman kedua).
- **External Recon methodology + seluruh tools** sudah dikatalogkan (dari halaman ketiga).
- **Database Leaks** sebagai sub-modul External Recon sudah ditambahkan.
- **Wide Source Code Search** sebagai sub-modul External Recon sudah ditambahkan.
- **GitHub Leaked Secrets** sebagai sub-modul External Recon sudah ditambahkan.

**Total tools & platform yang tercatat hingga saat ini: 65+**

---

Silakan berikan **referensi/link tambahan** berikutnya, atau jika sudah cukup, berikan instruksi untuk mulai membuat kode sesuai modul-modul yang Anda prioritaskan.
