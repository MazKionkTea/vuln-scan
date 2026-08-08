Berikut arsitektur dan workflow untuk sistem *fingerprinting* dan *vulnerability scanning* ala Shodan/Nuclei:

## 🏗️ Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────────────┐
│                        TARGET MANAGER                           │
│  (IP Range, Domain List, Seed Targets, Rate Limiter)            │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SCANNER ENGINE                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Port Scanner │  │ Banner       │  │ HTTP Prober          │  │
│  │ (TCP/UDP)    │  │ Grabber      │  │ (Header, Body, TLS)  │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Protocol Handlers: HTTP, FTP, SSH, RTSP, SIP, SNMP, dll  │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Raw Response
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FINGERPRINT ENGINE                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Header       │  │ HTML/Body    │  │ Hash Calculator      │  │
│  │ Parser       │  │ Analyzer     │  │ (Favicon, TLS, JS)   │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Signature Matcher (Regex, Exact Match, Template YAML)    │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Structured Data
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DATA LAYER                                │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │ Raw Storage      │  │ Indexed DB       │                     │
│  │ (S3/MinIO/File)  │  │ (ES/PostgreSQL/  │                     │
│  │                  │  │  ClickHouse)     │                     │
│  └──────────────────┘  └──────────────────┘                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Signature Database (YAML/JSON Templates)                 │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    API & INTERFACE LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ REST API     │  │ Web UI /     │  │ Alert / Webhook      │  │
│  │ (Query)      │  │ Dashboard    │  │ Notification         │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## 🔄 Workflow

### Tahap 1: Persiapan Target
```
Input Target (IP/CIDR/Domain)
        │
        ▼
Validasi & Normalisasi
        │
        ▼
Masuk ke Job Queue
```

### Tahap 2: Discovery & Probing
```
Job Queue
    │
    ├──► Port Scan (TCP SYN/Connect) → Daftar port terbuka
    │
    ├──► Banner Grabbing → Baca respons awal tiap port
    │
    └──► HTTP Probing → Kirim GET/HEAD, ambil:
         • Status code
         • Header lengkap
         • Body HTML
         • Sertifikat TLS
         • Favicon
```

### Tahap 3: Penyimpanan Data Mentah
```
Raw Response
    │
    ▼
Simpan apa adanya ke Raw Storage
(tanpa filter, buat audit & re-analysis)
```

### Tahap 4: Ekstraksi Fingerprint
```
Raw Data
    │
    ├──► Parse Header → Server, X-Powered-By, Set-Cookie
    │
    ├──► Parse HTML → Meta generator, title, form field
    │
    ├──► Hash Favicon → Identifikasi aplikasi unik
    │
    ├──► TLS Fingerprint → JA3/JA4, issuer, CN
    │
    └──► JavaScript Variable → window.*, var config
```

### Tahap 5: Matching Signature
```
Extracted Features
    │
    ▼
Cocokkan dengan Signature DB
    │
    ├──► Exact Match → "Server: nginx/1.25.1" → Nginx 1.25.1
    │
    ├──► Regex Match → pola "RouterOS v[0-9.]+" → MikroTik
    │
    └──► Template Match → YAML/JSON condition → Aplikasi + Versi
```

### Tahap 6: Penyimpanan Terstruktur
```
Hasil Matching
    │
    ▼
Simpan ke Indexed DB
{
  "ip": "1.2.3.4",
  "port": 443,
  "service": "https",
  "product": "GitLab",
  "version": "16.10.17",
  "os": "Linux",
  "vulnerabilities": ["CVE-2023-XXXX"],
  "raw_data_ref": "s3://bucket/xxx",
  "timestamp": "2026-08-08T12:00:00Z"
}
```

### Tahap 7: Query & Pelaporan
```
User Query → API → Search Engine → Hasil
    │
    ├──► Filter by product, port, country, vuln
    ├──► Dashboard visualisasi
    └──► Alert jika ada target baru yang match signature
```

## ⚙️ Komponen Pendukung

| Komponen | Fungsi |
|----------|--------|
| **Rate Limiter** | Hindari flood, atur kecepatan scan |
| **Proxy Pool** | Rotasi IP agar tidak diblokir |
| **Scheduler** | Jalankan scan berkala (cron/interval) |
| **Deduplicator** | Hindari scan target yang sama berulang |
| **Health Checker** | Monitor status worker & storage |

## 📝 Catatan Penting

- **Raw data disimpan terpisah** dari hasil olahan biar bisa di-reprocess kalau ada signature baru.
- **Signature DB harus versioned** biar bisa track perubahan dan rollback.
- **Concurrency diatur** per worker, jangan langsung hammer semua IP sekaligus.
- **Legal scope wajib didefinisikan** di awal, biar scanner nggak jalan ke target yang nggak diizinkan.

Arsitektur ini bisa mulai dari versi sederhana (single worker + SQLite) lalu scale ke distributed system (Kubernetes + message queue) kalau target sudah jutaan.



# 🏗️ Arsitektur & Workflow Lengkap — Vulnerability Scanner & Fingerprinting Engine

---

## 📐 Arsitektur Sistem Full

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYER 1: TARGET MANAGEMENT                        │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐   │
│  │ IP/CIDR     │  │ Domain      │  │ ASN Range    │  │ Seed Target    │   │
│  │ Input       │  │ Input       │  │ Input        │  │ Import         │   │
│  └──────┬──────┘  └──────┬──────┘  └──────┬───────┘  └───────┬────────┘   │
│         └────────────────┴────────────────┴──────────────────┘            │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │    Target Normalizer       │                          │
│                    │  (CIDR expand, DNS resolve,│                          │
│                    │   dedup, validate)         │                          │
│                    └─────────────┬─────────────┘                          │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │    Rate Limiter &          │                          │
│                    │    Scope Validator         │                          │
│                    │  (whitelist/blacklist,     │                          │
│                    │   legal scope check)       │                          │
│                    └─────────────┬─────────────┘                          │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │    Job Queue              │                          │
│                    │  (Redis/RabbitMQ/Kafka)   │                          │
│                    └─────────────┬─────────────┘                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        LAYER 2: DISCOVERY ENGINE                            │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    PORT SCANNER                                        │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────────┐  │ │
│  │  │ TCP SYN Scan │  │ TCP Connect  │  │ UDP Scan                   │  │ │
│  │  │ (fast, raw)  │  │ (fallback)   │  │ (SNMP, RTSP, SIP, etc)    │  │ │
│  │  └──────────────┘  └──────────────┘  └────────────────────────────┘  │ │
│  │  Top ports: 21,22,23,25,53,80,110,135,139,143,443,445,993,995,      │ │
│  │  1433,1521,3306,3389,5432,554,8080,8443,8888,9090,27017,6379,etc   │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │  Open Port Result          │                          │
│                    │  {ip, port, protocol,      │                          │
│                    │   state, latency}          │                          │
│                    └─────────────┬─────────────┘                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       LAYER 3: SERVICE PROBING                              │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                 PROTOCOL HANDLERS                                      │ │
│  │                                                                       │ │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐   │ │
│  │  │ HTTP/   │ │ FTP     │ │ SSH     │ │ Telnet  │ │ RTSP        │   │ │
│  │  │ HTTPS   │ │         │ │         │ │         │ │ (CCTV)      │   │ │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────────┘   │ │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐   │ │
│  │  │ SMTP    │ │ SNMP    │ │ SIP     │ │ MySQL   │ │ Redis       │   │ │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────────┘   │ │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐   │ │
│  │  │ MongoDB │ │ AMQP    │ │ MQTT    │ │ UPnP    │ │ Modbus      │   │ │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────────┘   │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                 BANNER GRABBING                                        │ │
│  │                                                                       │ │
│  │  1. Connect ke port → tunggu respons awal (banner)                    │ │
│  │  2. Kalau tidak ada banner → kirim probe kosong / newline             │ │
│  │  3. Kalau HTTP → kirim GET / HTTP/1.0 + HEAD request                 │ │
│  │  4. Rekam semua byte yang masuk (raw)                                │ │
│  │  5. Timeout: 5-10 detik per koneksi                                  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              HTTP DEEP PROBING (khusus port 80/443/8080/8443)        │ │
│  │                                                                       │ │
│  │  Request yang dikirim:                                                │ │
│  │  • GET / → ambil status, header, body                                │ │
│  │  • GET /favicon.ico → hash untuk identifikasi                       │ │
│  │  • GET /robots.txt → cek path tersembunyi                           │ │
│  │  • GET /login, /admin, /wp-login.php → deteksi login page           │ │
│  │  • OPTIONS / → cek method yang didukung                             │ │
│  │  • TLS handshake → ambil sertifikat, JA3/JA4 fingerprint            │ │
│  │                                                                       │ │
│  │  Data yang diambil:                                                   │ │
│  │  • Status code (200, 301, 302, 401, 403, 404, 500)                  │ │
│  │  • Semua response headers                                            │ │
│  │  • Body HTML (limit 1MB)                                             │ │
│  │  • Set-Cookie names & values                                         │ │
│  │  • TLS certificate (CN, SAN, Issuer, fingerprint)                    │ │
│  │  • Redirect chain                                                    │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │   RAW RESPONSE STORAGE     │                          │
│                    │   (simpan mentah apa       │                          │
│                    │    adanya, tanpa filter)   │                          │
│                    └─────────────┬─────────────┘                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LAYER 4: FINGERPRINT ENGINE                            │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              FEATURE EXTRACTION PIPELINE                               │ │
│  │                                                                       │ │
│  │  Raw Response                                                         │ │
│  │      │                                                                │ │
│  │      ├──► Header Parser                                              │ │
│  │      │    • Server: nginx/1.25.1, Apache/2.4.57, Microsoft-IIS/10.0  │ │
│  │      │    • X-Powered-By: PHP/8.1, Express, ASP.NET                  │ │
│  │      │    • X-AspNet-Version, X-Generator                            │ │
│  │      │    • Set-Cookie: PHPSESSID, laravel_session, JSESSIONID       │ │
│  │      │    • WWW-Authenticate: Basic realm="...", Digest realm="..."   │ │
│  │      │    • Location (redirect)                                      │ │
│  │      │    • Content-Security-Policy                                  │ │
│  │      │                                                                │ │
│  │      ├──► HTML/Body Analyzer                                         │ │
│  │      │    • <title> tag                                              │ │
│  │      │    • <meta name="generator" content="...">                    │ │
│  │      │    • <meta name="author" content="...">                       │ │
│  │      │    • <meta name="keywords" content="...">                     │ │
│  │      │    • <meta name="csrf-token" content="...">                   │ │
│  │      │    • Form action URLs & hidden fields                         │ │
│  │      │    • JavaScript variables (var config = {...})                │ │
│  │      │    • Copyright text                                           │ │
│  │      │    • CSS/JS file paths                                        │ │
│  │      │                                                                │ │
│  │      ├──► Favicon Hasher                                             │ │
│  │      │    • Download /favicon.ico                                    │ │
│  │      │    • Base64 encode → MurmurHash3 / MD5                        │ │
│  │      │    • Bandingkan dengan database hash                          │ │
│  │      │                                                                │ │
│  │      ├──► TLS Fingerprinter                                          │ │
│  │      │    • JA3/JA4 hash dari ClientHello                            │ │
│  │      │    • Certificate CN, SAN, Issuer, Subject                     │ │
│  │      │    • Certificate fingerprint (SHA256)                         │ │
│  │      │                                                                │ │
│  │      ├──► JavaScript Variable Extractor                              │ │
│  │      │    • window.Laravel, window.__NUXT__, wpApiSettings           │ │
│  │      │    • var csrfMagicToken, var cactiVersion                     │ │
│  │      │    • Proxmox = {...}, PVE object                              │ │
│  │      │                                                                │ │
│  │      ├──► Error Page Analyzer                                        │ │
│  │      │    • 404 page structure hash                                  │ │
│  │      │    • 500 error stack trace                                    │ │
│  │      │    • Default error messages                                   │ │
│  │      │                                                                │ │
│  │      └──► Directory Listing Detector                                 │ │
│  │           • Index of / pattern                                       │ │
│  │           • Auto-index pages                                         │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │  Extracted Features        │                          │
│                    │  {headers, meta, cookies,  │                          │
│                    │   favicon_hash, tls_info,  │                          │
│                    │   js_vars, title, body}    │                          │
│                    └─────────────┬─────────────┘                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LAYER 5: SIGNATURE MATCHING                            │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              SIGNATURE DATABASE                                        │ │
│  │                                                                       │ │
│  │  Format: YAML / JSON                                                  │ │
│  │                                                                       │ │
│  │  Contoh signature:                                                    │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: gitlab-ce                                                   │  │ │
│  │  │ name: GitLab Community Edition                                  │  │ │
│  │  │ category: devops                                                │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: header                                                │  │ │
│  │  │     part: og_site_name                                          │  │ │
│  │  │     value: "GitLab"                                             │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     regex: "GitLab Community Edition"                           │  │ │
│  │  │   - type: header                                                │  │ │
│  │  │     part: csrf_param                                            │  │ │
│  │  │     value: "authenticity_token"                                 │  │ │
│  │  │ extractors:                                                     │  │ │
│  │  │   - name: version                                               │  │ │
│  │  │     regex: "footer-build-information\">([0-9.]+)"              │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: mikrotik-routeros                                           │  │ │
│  │  │ name: MikroTik RouterOS                                         │  │ │
│  │  │ category: network                                               │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     regex: "RouterOS v[0-9.]+"                                  │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "WebFig Login"                                       │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "mikrotik_logo.png"                                  │  │ │
│  │  │ extractors:                                                     │  │ │
│  │  │   - name: version                                               │  │ │
│  │  │     regex: "RouterOS v([0-9.]+)"                                │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: asus-router                                                 │  │ │
│  │  │ name: ASUS Router                                               │  │ │
│  │  │ category: network                                               │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     regex: "prod_madelName"                                     │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "Sign in with your ASUS router account"              │  │ │
│  │  │ extractors:                                                     │  │ │
│  │  │   - name: model                                                 │  │ │
│  │  │     regex: "prod_madelName\">([^<]+)"                          │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: cacti                                                       │  │ │
│  │  │ name: Cacti Monitoring                                          │  │ │
│  │  │ category: monitoring                                            │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "The Cacti Group"                                    │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     regex: "cactiVersion='[0-9.]+'"                            │  │ │
│  │  │ extractors:                                                     │  │ │
│  │  │   - name: version                                               │  │ │
│  │  │     regex: "cactiVersion='([0-9.]+)'"                          │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: proxmox                                                     │  │ │
│  │  │ name: Proxmox Virtual Environment                               │  │ │
│  │  │ category: virtualization                                        │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: header                                                │  │ │
│  │  │     part: set_cookie                                            │  │ │
│  │  │     value: "PVEAuthCookie"                                      │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "Proxmox Virtual Environment"                        │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     regex: "CSRFPreventionToken"                                │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: nuuo-nvr                                                    │  │ │
│  │  │ name: NUUO NVR                                                  │  │ │
│  │  │ category: cctv                                                  │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "VENDOR_NAME = \"NUUO\""                             │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "Network Video Recorder Login"                       │  │ │
│  │  │ extractors:                                                     │  │ │
│  │  │   - name: project                                               │  │ │
│  │  │     regex: "PROJECT_NAME = \"([^\"]+)\""                       │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: vos3000                                                     │  │ │
│  │  │ name: VOS3000 VoIP                                              │  │ │
│  │  │ category: voip                                                  │  │ │
│  │  │ matchers:                                                       │  │ │
│  │  │   - type: header                                                │  │ │
│  │  │     part: meta_keywords                                         │  │ │
│  │  │     value: "VOS3000"                                            │  │ │
│  │  │   - type: body                                                  │  │ │
│  │  │     value: "images/vos3000.ico"                                 │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ... (ribuan signature lainnya)                                      │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              MATCHING ENGINE                                           │ │
│  │                                                                       │ │
│  │  Strategi matching (prioritas):                                       │ │
│  │                                                                       │ │
│  │  1. EXACT MATCH → string persis sama                                  │ │
│  │     Contoh: "Server: nginx" di header                                │ │
│  │                                                                       │ │
│  │  2. REGEX MATCH → pola regex                                          │ │
│  │     Contoh: /RouterOS v[0-9.]+/ di body                              │ │
│  │                                                                       │ │
│  │  3. HASH MATCH → hash favicon / TLS cert                              │ │
│  │     Contoh: MD5(favicon) == "abc123..."                              │ │
│  │                                                                       │ │
│  │  4. COMBINATION MATCH → beberapa kondisi harus terpenuhi              │ │
│  │     Contoh: header contains "PVEAuthCookie" AND                      │ │
│  │             body contains "Proxmox"                                  │ │
│  │                                                                       │ │
│  │  5. CONDITIONAL MATCH → if-then logic                                 │ │
│  │     Contoh: IF status==401 AND header contains                       │ │
│  │             "WWW-Authenticate: Basic realm"                          │ │
│  │             THEN extract realm value                                  │ │
│  │                                                                       │ │
│  │  Confidence scoring:                                                  │ │
│  │  • 1 match → low confidence (mungkin false positive)                 │ │
│  │  • 2-3 match → medium confidence                                     │ │
│  │  • 4+ match → high confidence                                        │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │  Matched Result            │                          │
│                    │  {product, version,        │                          │
│                    │   category, confidence,    │                          │
│                    │   extracted_data}          │                          │
│                    └─────────────┬─────────────┘                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LAYER 6: VULNERABILITY CHECKING                        │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              VULNERABILITY TEMPLATES                                   │ │
│  │                                                                       │ │
│  │  Setelah fingerprint teridentifikasi, jalankan                        │ │
│  │  vulnerability check yang relevan:                                    │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: CVE-2022-1609                                               │  │ │
│  │  │ name: WordPress Subscribers Plugin RCE                          │  │ │
│  │  │ severity: critical                                              │  │ │
│  │  │ condition:                                                      │  │ │
│  │  │   product: wordpress                                            │  │ │
│  │  │   plugin: subscribers                                           │  │ │
│  │  │   version: "<1.5.4"                                             │  │ │
│  │  │ request:                                                        │  │ │
│  │  │   method: POST                                                  │  │ │
│  │  │   path: /wp-admin/admin-ajax.php                                │  │ │
│  │  │   body: "action=..."                                            │  │ │
│  │  │ match:                                                          │  │ │
│  │  │   status: 200                                                   │  │ │
│  │  │   body: "uid="                                                  │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: CVE-2017-9841                                               │  │ │
│  │  │ name: PHPUnit RCE                                               │  │ │
│  │  │ severity: critical                                              │  │ │
│  │  │ condition:                                                      │  │ │
│  │  │   product: phpunit                                              │  │ │
│  │  │ request:                                                        │  │ │
│  │  │   method: POST                                                  │  │ │
│  │  │   path: /vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php    │  │ │
│  │  │   body: "<?php echo md5('test'); ?>"                            │  │ │
│  │  │ match:                                                          │  │ │
│  │  │   status: 200                                                   │  │ │
│  │  │   body: "9f86d081884c7d65"                                     │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: default-credentials                                         │  │ │
│  │  │ name: Default Credential Check                                  │  │ │
│  │  │ severity: high                                                  │  │ │
│  │  │ condition:                                                      │  │ │
│  │  │   has_login_form: true                                          │  │ │
│  │  │ requests:                                                       │  │ │
│  │  │   - credentials: admin/admin                                    │  │ │
│  │  │   - credentials: admin/123456                                   │  │ │
│  │  │   - credentials: admin/password                                 │  │ │
│  │  │   - credentials: root/root                                      │  │ │
│  │  │ match:                                                          │  │ │
│  │  │   response_not_contains: "invalid"                              │  │ │
│  │  │   response_not_contains: "error"                                │  │ │
│  │  │   status: [200, 302]                                            │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: exposed-config                                              │  │ │
│  │  │ name: Exposed Configuration Files                               │  │ │
│  │  │ severity: medium                                                │  │ │
│  │  │ requests:                                                       │  │ │
│  │  │   - path: /.env                                                 │  │ │
│  │  │   - path: /.git/config                                          │  │ │
│  │  │   - path: /wp-config.php.bak                                    │  │ │
│  │  │   - path: /phpinfo.php                                          │  │ │
│  │  │   - path: /server-status                                        │  │ │
│  │  │   - path: /.htaccess                                            │  │ │
│  │  │   - path: /config.php                                           │  │ │
│  │  │ match:                                                          │  │ │
│  │  │   status: 200                                                   │  │ │
│  │  │   body_regex: "(DB_PASSWORD|APP_KEY|mysql://)"                  │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ id: directory-listing                                           │  │ │
│  │  │ name: Directory Listing Enabled                                 │  │ │
│  │  │ severity: low                                                   │  │ │
│  │  │ requests:                                                       │  │ │
│  │  │   - path: /                                                     │  │ │
│  │  │   - path: /uploads/                                             │  │ │
│  │  │   - path: /backup/                                              │  │ │
│  │  │ match:                                                          │  │ │
│  │  │   status: 200                                                   │  │ │
│  │  │   body: "Index of /"                                            │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                          │
│                    │  Vulnerability Result      │                          │
│                    │  {cve_id, severity,        │                          │
│                    │   evidence, affected_      │                          │
│                    │   product, version}        │                          │
│                    └─────────────┬─────────────┘                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LAYER 7: DATA STORAGE                               │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              RAW DATA STORAGE                                         │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ Object Storage (S3 / MinIO / Local Filesystem)                  │  │ │
│  │  │                                                                 │  │ │
│  │  │ Struktur:                                                       │  │ │
│  │  │ /raw/{year}/{month}/{day}/{ip}/{port}_{protocol}.raw           │  │ │
│  │  │                                                                 │  │ │
│  │  │ Isi: respons mentah lengkap (header + body + TLS cert)         │  │ │
│  │  │ Retensi: 90 hari - 1 tahun                                     │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              STRUCTURED DATA STORAGE                                  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ Search Engine (Elasticsearch / OpenSearch / ClickHouse)         │  │ │
│  │  │                                                                 │  │ │
│  │  │ Schema:                                                         │  │ │
│  │  │ {                                                               │  │ │
│  │  │   "ip": "192.168.1.1",                                         │  │ │
│  │  │   "port": 443,                                                  │  │ │
│  │  │   "protocol": "https",                                          │  │ │
│  │  │   "service": {                                                  │  │ │
│  │  │     "name": "http",                                             │  │ │
│  │  │     "product": "GitLab",                                        │  │ │
│  │  │     "version": "16.10.17",                                      │  │ │
│  │  │     "category": "devops",                                       │  │ │
│  │  │     "confidence": "high"                                        │  │ │
│  │  │   },                                                            │  │ │
│  │  │   "os": {                                                       │  │ │
│  │  │     "name": "Linux",                                            │  │ │
│  │  │     "family": "Debian"                                          │  │ │
│  │  │   },                                                            │  │ │
│  │  │   "tls": {                                                      │  │ │
│  │  │     "cn": "gitlab.example.com",                                 │  │ │
│  │  │     "issuer": "Let's Encrypt",                                  │  │ │
│  │  │     "ja3": "abc123...",                                         │  │ │
│  │  │     "expires": "2026-12-01"                                     │  │ │
│  │  │   },                                                            │  │ │
│  │  │   "vulnerabilities": [                                          │  │ │
│  │  │     {                                                           │  │ │
│  │  │       "id": "CVE-2024-XXXX",                                    │  │ │
│  │  │       "severity": "critical",                                   │  │ │
│  │  │       "cvss": 9.8                                               │  │ │
│  │  │     }                                                           │  │ │
│  │  │   ],                                                            │  │ │
│  │  │   "credentials_found": [                                        │  │ │
│  │  │     {                                                           │  │ │
│  │  │       "username": "admin",                                      │  │ │
│  │  │       "type": "default",                                        │  │ │
│  │  │       "service": "web"                                          │  │ │
│  │  │     }                                                           │  │ │
│  │  │   ],                                                            │  │ │
│  │  │   "tags": ["gitlab", "devops", "self-hosted"],                  │  │ │
│  │  │   "location": {                                                 │  │ │
│  │  │     "country": "ID",                                            │  │ │
│  │  │     "city": "Jakarta",                                          │  │ │
│  │  │     "asn": "AS12345",                                           │  │ │
│  │  │     "isp": "Example ISP"                                        │  │ │
│  │  │   },                                                            │  │ │
│  │  │   "first_seen": "2026-01-01T00:00:00Z",                        │  │ │
│  │  │   "last_seen": "2026-08-08T12:00:00Z",                         │  │ │
│  │  │   "raw_data_ref": "s3://bucket/raw/2026/08/08/192.168.1.1/"    │  │ │
│  │  │ }                                                               │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ Relational DB (PostgreSQL / MySQL)                              │  │ │
│  │  │                                                                 │  │ │
│  │  │ Untuk data transaksional:                                       │  │ │
│  │  │ • Scan jobs & status                                            │  │ │
│  │  │ • User accounts & API keys                                      │  │ │
│  │  │ • Scan schedules                                                │  │ │
│  │  │ • Alert configurations                                          │  │ │
│  │  │ • Audit logs                                                    │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │ │
│  │  │ Cache (Redis)                                                   │  │ │
│  │  │                                                                 │  │ │
│  │  │ Untuk:                                                          │  │ │
│  │  │ • Job queue                                                     │  │ │
│  │  │ • Rate limiting counters                                        │  │ │
│  │  │ • Session data                                                  │  │ │
│  │  │ • Hot query results                                             │  │ │
│  │  │ • Deduplication hashes                                          │  │ │
│  │  └─────────────────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LAYER 8: API & INTERFACE                               │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              REST API                                                 │ │
│  │                                                                       │ │
│  │  Endpoints:                                                           │ │
│  │                                                                       │ │
│  │  GET  /api/v1/search?q=product:"gitlab"&port=443&country=ID          │ │
│  │  GET  /api/v1/host/{ip}                                              │ │
│  │  GET  /api/v1/host/{ip}/ports                                        │ │
│  │  GET  /api/v1/host/{ip}/vulnerabilities                              │ │
│  │  POST /api/v1/scan            → trigger scan baru                    │ │
│  │  GET  /api/v1/scan/{id}       → cek status scan                      │ │
│  │  GET  /api/v1/scan/{id}/results                                      │ │
│  │  GET  /api/v1/signatures      → list semua signature                 │ │
│  │  POST /api/v1/signatures      → tambah signature baru                │ │
│  │  GET  /api/v1/stats           → statistik sistem                     │ │
│  │  GET  /api/v1/alerts          → list alerts                          │ │
│  │  POST /api/v1/webhooks        → register webhook                     │ │
│  │                                                                       │ │
│  │  Auth: API Key / JWT Token                                            │ │
│  │  Rate limit: 100 req/menit (free), 1000 req/menit (pro)             │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              WEB DASHBOARD                                            │ │
│  │                                                                       │ │
│  │  Fitur:                                                               │ │
│  │  • Search bar dengan syntax khusus                                    │ │
│  │    Contoh: product:"nginx" version:"1.25" country:"ID" port:443      │ │
│  │  • Peta geografis sebaran target                                     │ │
│  │  • Grafik tren (produk, versi, vuln)                                 │ │
│  │  • Detail host (semua port, service, vuln)                           │ │
│  │  • Manajemen signature                                               │ │
│  │  • Manajemen scan job                                                │ │
│  │  • Alert & notification center                                       │ │
│  │  • Export data (CSV, JSON, PDF)                                      │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              ALERTING & NOTIFICATION                                  │ │
│  │                                                                       │ │
│  │  Trigger:                                                             │ │
│  │  • Target baru muncul dengan produk tertentu                          │ │
│  │  • Vulnerability baru terdeteksi di target yang sudah ada             │ │
│  │  • Default credential masih aktif                                     │ │
│  │  • TLS certificate expired / akan expired                             │ │
│  │  • Perubahan konfigurasi terdeteksi                                  │ │
│  │                                                                       │ │
│  │  Channel:                                                             │ │
│  │  • Webhook (Slack, Discord, Telegram, custom)                        │ │
│  │  • Email                                                             │ │
│  │  • SMS (via gateway)                                                 │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Workflow Lengkap (Step by Step)

```
STEP 1: INPUT TARGET
═══════════════════════════════════════════════════════════════
User input → IP / CIDR / Domain / ASN
     │
     ▼
Validasi format
     │
     ├── IP valid? → lanjut
     ├── CIDR valid? → expand jadi daftar IP
     ├── Domain? → DNS resolve → dapat IP
     └── ASN? → lookup range IP
     │
     ▼
Cek scope (whitelist/blacklist)
     │
     ├── Di luar scope? → TOLAK, log attempt
     └── Di dalam scope? → lanjut
     │
     ▼
Deduplikasi (sudah pernah di-scan recently?)
     │
     ├── Sudah & masih fresh (<24h)? → skip atau refresh
     └── Belum / sudah lama? → masuk queue
     │
     ▼
Masuk Job Queue (Redis/Kafka)
     │
     ▼
Assign ke Worker yang available


STEP 2: PORT DISCOVERY
═══════════════════════════════════════════════════════════════
Worker ambil job dari queue
     │
     ▼
Port Scan (TCP SYN / Connect)
     │
     ├── Scan top 1000 ports (default)
     ├── Atau custom port list dari user
     ├── Timeout: 1-3 detik per port
     └── Retry: 1x kalau timeout
     │
     ▼
Hasil: daftar port terbuka
     │
     Contoh: [22, 80, 443, 3306, 8080]
     │
     ▼
Untuk setiap port terbuka → lanjut ke STEP 3


STEP 3: SERVICE PROBING & BANNER GRABBING
═══════════════════════════════════════════════════════════════
Untuk setiap port terbuka:
     │
     ▼
Identifikasi protokol berdasarkan port number
     │
     ├── Port 80/443/8080/8443 → HTTP/HTTPS probe
     ├── Port 21 → FTP probe
     ├── Port 22 → SSH probe
     ├── Port 23 → Telnet probe
     ├── Port 25 → SMTP probe
     ├── Port 161 → SNMP probe
     ├── Port 554 → RTSP probe
     ├── Port 3306 → MySQL probe
     ├── Port 6379 → Redis probe
     ├── Port 27017 → MongoDB probe
     └── Lainnya → generic TCP probe
     │
     ▼
Kirim probe sesuai protokol
     │
     ├── HTTP: GET / HTTP/1.0\r\nHost: {ip}\r\n\r\n
     ├── FTP: connect → tunggu banner
     ├── SSH: connect → tunggu banner
     ├── Generic: connect → kirim \r\n → tunggu
     └── TLS: handshake → ambil cert
     │
     ▼
Rekam RAW RESPONSE
     │
     ├── Semua byte yang masuk
     ├── Header lengkap
     ├── Body (limit 1MB)
     ├── TLS certificate (kalau HTTPS)
     └── Timestamp & latency
     │
     ▼
Simpan ke Raw Storage (tanpa filter)


STEP 4: HTTP DEEP PROBING (khusus HTTP/HTTPS)
═══════════════════════════════════════════════════════════════
Kalau port terdeteksi HTTP/HTTPS:
     │
     ▼
Request tambahan:
     │
     ├── GET /favicon.ico → download & hash
     ├── GET /robots.txt → parse paths
     ├── OPTIONS / → cek allowed methods
     ├── GET /login → deteksi login page
     ├── GET /admin → deteksi admin panel
     ├── GET /wp-login.php → cek WordPress
     ├── GET /phpmyadmin → cek phpMyAdmin
     └── HEAD / → quick check
     │
     ▼
Parse semua respons:
     │
     ├── Extract semua headers
     ├── Extract <title>, <meta> tags
     ├── Extract form fields & actions
     ├── Extract JavaScript variables
     ├── Extract comments HTML
     ├── Extract CSS/JS file paths
     ├── Extract copyright text
     └── Calculate favicon hash
     │
     ▼
Simpan extracted features


STEP 5: FINGERPRINT MATCHING
═══════════════════════════════════════════════════════════════
Ambil extracted features dari STEP 4
     │
     ▼
Load Signature Database
     │
     ▼
Untuk setiap signature di database:
     │
     ├── Cek matchers satu per satu
     │   ├── Header match? → cek
     │   ├── Body match? → cek
     │   ├── Regex match? → cek
     │   ├── Hash match? → cek
     │   └── Combination? → cek semua kondisi
     │
     ├── Hitung confidence score
     │   ├── 1 matcher hit → low (30%)
     │   ├── 2 matcher hit → medium (60%)
     │   ├── 3 matcher hit → high (85%)
     │   └── 4+ matcher hit → very high (95%+)
     │
     └── Kalau confidence > threshold (60%):
         ├── Catat sebagai matched product
         ├── Extract version kalau ada
         ├── Extract info tambahan (model, build, dll)
         └── Lanjut ke signature berikutnya
     │
     ▼
Hasil: list of matched products + versions
     │
     Contoh:
     ├── Product: GitLab CE, Version: 16.10.17, Confidence: 95%
     ├── Product: Nginx, Version: 1.25.1, Confidence: 90%
     └── Product: Ubuntu, Version: 22.04, Confidence: 80%


STEP 6: VULNERABILITY CHECKING
═══════════════════════════════════════════════════════════════
Berdasarkan product & version yang terdeteksi:
     │
     ▼
Filter vulnerability templates yang relevan
     │
     ├── GitLab 16.10.17 → cek CVE yang affect versi ini
     ├── Nginx 1.25.1 → cek known vulnerabilities
     ├── WordPress + plugin X → cek plugin vulns
     └── Default credentials → cek login form
     │
     ▼
Jalankan vulnerability checks
     │
     ├── SAFE checks dulu (tanpa exploit):
     │   ├── Cek version vs CVE database
     │   ├── Cek exposed files (.env, .git, phpinfo)
     │   ├── Cek directory listing
     │   ├── Cek missing security headers
     │   └── Cek TLS configuration (weak cipher, expired cert)
     │
     ├── ACTIVE checks (kalau diizinkan):
     │   ├── Default credential testing
     │   ├── SQL injection test (single quote)
     │   ├── XSS test (basic payload)
     │   ├── CORS misconfiguration test
     │   └── Open redirect test
     │
     └── EXPLOIT checks (HANYA kalau explicit permission):
         ├── RCE verification (echo/whoami)
         ├── File read test (/etc/passwd)
         └── SSRF test (callback to controlled server)
     │
     ▼
Catat hasil vulnerability check
     │
     ├── Vulnerable → {cve, severity, evidence, remediation}
     ├── Not vulnerable → log sebagai passed
     └── Inconclusive → flag untuk manual review


STEP 7: DATA ENRICHMENT
═══════════════════════════════════════════════════════════════
Tambahkan konteks ke hasil scan:
     │
     ├── GeoIP lookup → country, city, coordinates
     ├── ASN lookup → ISP, organization
     ├── Reverse DNS → PTR record
     ├── WHOIS → registrant info (kalau domain)
     ├── Historical data → pernah di-scan sebelumnya?
     ├── Threat intel → IP ada di blocklist?
     └── Technology stack → full stack mapping
     │
     ▼
Simpan enriched data ke Structured Storage


STEP 8: REPORTING & ALERTING
═══════════════════════════════════════════════════════════════
Generate report:
     │
     ├── Summary: total hosts, ports, services, vulns
     ├── Critical findings (sorted by severity)
     ├── Product distribution chart
     ├── Version distribution chart
     ├── Vulnerability breakdown by severity
     ├── Default credentials found
     ├── Exposed sensitive files
     └── Recommendations
     │
     ▼
Check alert rules:
     │
     ├── Ada critical vuln baru? → ALERT
     ├── Default credential aktif? → ALERT
     ├── Target baru muncul? → NOTIFY
     ├── Cert expired? → NOTIFY
     └── Konfigurasi berubah? → NOTIFY
     │
     ▼
Kirim alert via configured channels:
     ├── Webhook → Slack/Discord/Telegram
     ├── Email → security team
     └── Dashboard notification


STEP 9: SCHEDULING & RE-SCAN
═══════════════════════════════════════════════════════════════
Setup jadwal scan berkala:
     │
     ├── Full scan: setiap 7 hari
     ├── Critical ports only: setiap 24 jam
     ├── Specific targets: custom schedule
     └── On-demand: manual trigger
     │
     ▼
Bandingkan hasil scan baru vs sebelumnya:
     │
     ├── New host muncul → flag
     ├── Host hilang → flag
     ├── Port baru terbuka → flag
     ├── Version berubah → flag
     ├── Vuln baru terdeteksi → flag
     └── Vuln sudah di-patch → resolve
     │
     ▼
Update database & trigger alerts kalau ada perubahan
```

---

## ⚙️ Komponen Infrastruktur

| Komponen | Teknologi | Fungsi |
|----------|-----------|--------|
| **Job Queue** | Redis / RabbitMQ / Kafka | Distribusi tugas ke workers |
| **Worker Pool** | Go / Rust / Python asyncio | Eksekusi scan secara parallel |
| **Raw Storage** | MinIO / S3 / Local FS | Simpan respons mentah |
| **Search Engine** | Elasticsearch / ClickHouse | Index & query data terstruktur |
| **Relational DB** | PostgreSQL | Data transaksional (jobs, users, alerts) |
| **Cache** | Redis | Rate limiting, dedup, session |
| **API Server** | Go / Node.js / Python FastAPI | REST API untuk query & manajemen |
| **Web UI** | React / Vue / Next.js | Dashboard & visualisasi |
| **Scheduler** | Cron / Celery / Temporal | Jadwal scan berkala |
| **Monitoring** | Prometheus + Grafana | Monitor kesehatan sistem |
| **Logging** | ELK Stack / Loki | Audit trail & debugging |
| **Proxy Pool** | Rotating proxy service | Hindari IP blocking saat scan besar |

---

## 📊 Data Flow Diagram

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Target  │───►│  Port    │───►│  Banner  │───►│  Raw     │
│  Input   │    │  Scanner │    │  Grabber │    │  Storage │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
                                                      │
                                                      ▼
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Alert & │◄───│  Data    │◄───│  Vuln    │◄───│  Finger- │
│  Report  │    │  Storage │    │  Checker │    │  print   │
└──────────┘    └──────────┘    └──────────┘    │  Engine  │
                     │                           └──────────┘
                     ▼
              ┌──────────┐
              │  API &   │
              │  Web UI  │
              └──────────┘
```

---

## 🔒 Security & Compliance

| Aspek | Implementasi |
|-------|-------------|
| **Scope Validation** | Whitelist IP/domain yang boleh di-scan, tolak di luar scope |
| **Rate Limiting** | Batasi request per detik per target, hindari DoS |
| **Legal Check** | Verifikasi izin tertulis sebelum scan production |
| **Data Encryption** | Encrypt data at rest (AES-256) & in transit (TLS 1.3) |
| **Access Control** | RBAC untuk akses dashboard & API |
| **Audit Log** | Catat semua aksi scan, query, dan perubahan konfigurasi |
| **Data Retention** | Auto-delete raw data setelah periode tertentu |
| **Secret Management** | Vault untuk simpan API keys, credentials |

---

## 🚀 Skala & Performa

| Metrik | Target |
|--------|--------|
| Port scan speed | 10.000 port/detik per worker |
| HTTP probe throughput | 1.000 request/detik per worker |
| Concurrent workers | 10-100 (scalable) |
| Raw storage | ~500 MB per 1000 hosts (full probe) |
| Indexed data | ~50 KB per host (structured) |
| Query latency | <100ms untuk search sederhana |
| Scan full internet (top 100 ports) | ~6-12 jam dengan 50 workers |

---

## 📝 Catatan Implementasi

- **Mulai dari kecil**: bikin versi single-worker dulu, baru scale ke distributed
- **Signature DB harus versioned**: pakai git untuk track perubahan signature
- **Raw data jangan difilter**: simpan apa adanya, proses di layer fingerprint
- **Modular design**: tiap layer bisa di-replace tanpa ganggu layer lain
- **Plugin system**: biar komunitas bisa kontribusi signature & vuln templates
- **Graceful degradation**: kalau satu komponen down, yang lain tetap jalan
- **Idempotent operations**: scan yang sama dijalankan 2x hasilnya harus konsisten

---

Arsitektur ini bisa dimulai dari versi minimal (single machine, SQLite, 1 worker) dan dikembangkan bertahap ke distributed system (Kubernetes, message queue, cluster database) sesuai kebutuhan skala.
