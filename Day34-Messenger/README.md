# 🐺 Project Cerberus: Tactical Intelligence Messenger

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Architecture](https://img.shields.io/badge/Architecture-Modular-success)
![Status](https://img.shields.io/badge/Status-Active-green)

**Project Cerberus**, hedef sistemlerden (kamu açık verileri) otomatik istihbarat toplayan, veriyi anlamlı raporlara (CSV) dönüştüren ve güvenli bir şekilde operatöre e-posta ile ileten otonom bir Python botudur. 

Bu modül, "Separation of Concerns" (Sorumlulukların Ayrılığı) prensibiyle tasarlanmış temiz bir mimariye sahiptir.

## 🏗️ Sistem Mimarisi (Modüler Yapı)

Proje, Spagetti koddan kaçınmak için iki ana motor üzerinde çalışır:

1. **`scraper.py` (The Analyst):** Hedef siteye (Adalet Bakanlığı) insan taklidi yaparak (`User-Agent`) sızar, HTML hiyerarşisini `BeautifulSoup` ile çözer ve veriyi `.csv` formatında paketler.
2. **`cerberus.py` (The Architect):** Ana kontrolcüdür. Analistten gelen veriyi alır, `smtplib` ve modern `EmailMessage` sınıflarını kullanarak güvenli SSL portları üzerinden operatöre e-postalar.

## 🛡️ Operasyonel Güvenlik (OPSEC)

* **Credential Management:** E-posta şifreleri ve hassas veriler asla kodun içine yazılmaz (Hardcoded değildir). `python-dotenv` kullanılarak `.env` dosyasında izole edilmiştir.
* **Data Leak Prevention:** `.gitignore` dosyası ile yerel verilerin (`*.csv`), sistem dosyalarının ve `.env` şifrelerinin GitHub'a sızması engellenmiştir.

## 📦 Kurulum ve Çalıştırma

**1. Gerekli Kütüphaneleri Yükleyin:**
```bash
pip install requests beautifulsoup4 python-dotenv

2. Çevresel Değişkenleri Ayarlayın:
Proje dizininde bir .env dosyası oluşturun ve Google Uygulama Şifrenizi ekleyin:

Kod snippet'i
EMAIL_USER=sizin_mailiniz@gmail.com
EMAIL_PASS=16_haneli_uygulama_sifreniz

3. Operasyonu Başlatın:
Bash
python cerberus.py
⚖️ Yasal ve Etik Bilgilendirme
Bu araç tamamen eğitim ve kişisel otomasyon amacıyla geliştirilmiştir. Hedef sunucuları yormamak adına time.sleep() ile hız sınırlandırması (Rate Limiting) uygulanmış olup, sadece kamuya açık (Public) veriler işlenmektedir.

Developed by Jhonny Lesh 🤠
