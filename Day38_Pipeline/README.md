# 🐺 Tactical Data Pipeline & Automated Reporting Engine

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange)
![Automation](https://img.shields.io/badge/Automation-SMTP_Bot-success)
![OPSEC](https://img.shields.io/badge/Security-Dotenv-red)

Bu proje, ham ve karmaşık veri setlerini otonom olarak alan, analiz eden, görselleştiren ve karar alıcılara e-posta yoluyla raporlayan **modüler bir veri boru hattıdır (Data Pipeline).** Spagetti kod mimarisi reddedilmiş, her bir işlem bağımsız motorlara (Engine) bölünerek %100 ölçeklenebilir ve kurumsal (Best Practice) bir yapı inşa edilmiştir.

## 🏗️ Mimari Tasarım (The Architecture)

Sistem 4 ana bileşenden (Modül) oluşur:

1. **`data_engine.py` (Veri Motoru):** Ham veriyi alır, Pandas ile saniyeler içinde filtreler, işler ve temizlenmiş bir Excel raporu (`.xlsx`) üretir.
2. **`visual_engine.py` (Görsel Motor):** İşlenmiş veri tablosunu alır, Matplotlib kullanarak yöneticiler için "Büyük Resmi" gösteren yüksek çözünürlüklü analiz grafiklerine (`.png`) dönüştürür.
3. **`mail_engine.py` (Haberci Motor):** Üretilen Excel ve PNG kanıtlarını alır, SMTP protokolü ile güvenli bir şekilde ilgili birimlere e-posta olarak fırlatır.
4. **`main_operator.py` (Ana Şalter):** Tüm orkestrayı tek tuşla yöneten komuta merkezidir.

## 🛡️ Operasyonel Güvenlik (OPSEC)
* Sistem, SMTP parolalarını ve kişisel API anahtarlarını `.env` dosyası üzerinden okuyarak kaynak koddan tamamen izole eder.
* `.gitignore` kalkanı sayesinde üretilen hassas veri raporları, grafikler ve şifreler versiyon kontrol sistemine (GitHub) sızmaz.

## 🚀 Sistemi Ateşleme

1. Ortamı kurun: `pip install pandas matplotlib python-dotenv openpyxl`
2. `.env` dosyanızı oluşturup `SENDER_EMAIL` ve `SENDER_PASSWORD` (Uygulama Şifresi) bilgilerinizi girin.
3. Operasyonu başlatın:
```bash
python main_operator.py

```

---

*Engineered for Tactical Automation & Maximum Efficiency.* 🐺

```

---