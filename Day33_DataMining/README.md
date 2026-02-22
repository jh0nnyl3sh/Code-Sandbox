# 📰 Hacker News Scraper & Reporter

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Active-green)

**Hacker News** (ycombinator) üzerindeki en güncel teknoloji başlıklarını ve linklerini otomatik olarak çeken, veriyi işleyen ve analiz edilebilir bir **CSV formatına** dönüştüren Python otomasyon aracıdır.

## 🚀 Özellikler

* **Akıllı İstek Yönetimi:** `requests` kütüphanesi ile hedef siteye bağlanır.
* **Anti-Bot Koruması:** `time` modülü ile insan taklidi yaparak IP engellemelerini önler.
* **Veri Madenciliği:** `BeautifulSoup` kullanarak HTML yapısını ayrıştırır (`span`, `a`, `href` analizi).
* **Raporlama:** Çekilen verileri Excel uyumlu `.csv` formatında, Türkçe karakter desteğiyle (`utf-8`) kaydeder.

## 🛠️ Kullanılan Teknolojiler

* **Python 3**
* **Requests** (HTTP Bağlantıları için)
* **BeautifulSoup4** (HTML Parsing için)
* **CSV** (Veri Depolama için)

## 📦 Kurulum

Gerekli kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:

```bash
pip install requests beautifulsoup4

⚙️ Nasıl Çalışır?
Script çalıştırıldığında news.ycombinator.com adresine istek atar.

Gelen HTML verisini parçalar ve başlık/link ikililerini ayıklar.

Bulunduğu dizinde hacker_news_raporu.csv adında bir dosya oluşturur.

Eğer dosya varsa üzerine yazar (Güncel Rapor Modu).


📄 Örnek Çıktı (CSV)
Sıra,Haber Başlığı,Link
1,Show HN: I built a scraping bot,[https://github.com/project](https://github.com/project)...
2,Python 3.14 Release Notes,[https://python.org/](https://python.org/)...
3,New AI Model developed by Google,https://googleblog...

Developed by Jhonny Lesh
