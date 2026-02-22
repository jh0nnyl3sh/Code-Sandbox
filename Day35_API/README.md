# 🐺 The Keymaster (API Operations)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Data](https://img.shields.io/badge/Data-JSON-orange)
![Status](https://img.shields.io/badge/Status-Active-green)

**Faz 1 (Veri Toplama ve API Entegrasyonu)**

Bu modül, "Web Scraping" (HTML kazıma) hantallığını geride bırakıp, hedef sistemlerin resmi arka kapılarından (API) sızarak **JSON** formatında, milisaniyeler içinde saf veri çekmek için tasarlanmıştır.

## 📡 Operasyon Detayı: Finansal İstihbarat

Bu script, küresel kripto para piyasalarını (Bitcoin, Ethereum, Solana) takip etmek için **CoinGecko API** altyapısını kullanır. Karmaşık web sitelerini kazımak yerine, doğrudan veritabanı "Veznesine" yasal bir HTTP GET isteği atarak anlık fiyatları çeker ve operatörün anlayacağı formata çevirir.

### 🛠️ Teknik Nitelikler (Architecture)
* **REST API & JSON:** Sistemlerin evrensel dili olan JSON verilerini Python Sözlük (Dictionary) yapılarına dönüştürerek işleme.
* **Rate Limit (HTTP 429) Farkındalığı:** Hedef sunucuların hız sınırlarına (DDoS korumalarına) saygı duyan, optimize edilmiş istek yapısı.
* **String Manipülasyonu:** Gelen Amerikan standartlarındaki (virgüllü) finansal verileri, bölgesel (lokal) okunabilirliği artırmak adına nokta (1.500.000) formatına çeviren çevik (agile) dönüşüm algoritmaları.

## 📦 Kurulum ve Çalıştırma

**1. Gereksinimleri Yükleyin:**
```bash
pip install requests

```

**2. Operasyonu Başlatın:**

```bash
python crypto_bot.py

```

## 🧠 Taktiksel Felsefe (The Keymaster)

> *"Kapısı açık bir vezneden (API) net bilgi almak varken, pencereden gizlice girip HTML dosyalarını karıştırmak (Scraping) ameleliktir. Verinin saf haline ulaş."*

---

*Engineered by **Jhonny Lesh** 🤠

```

***
