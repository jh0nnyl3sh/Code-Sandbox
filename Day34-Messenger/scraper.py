import requests
from bs4 import BeautifulSoup
import csv
import time

# Fonksiyonumuzu tanımlıyoruz
def get_adalet_news():
    url = "https://www.adalet.gov.tr/arsiv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"📡 [SCRAPER] '{url}' adresine sızılıyor...")
    time.sleep(1)
    
    response = requests.get(url, headers=headers)
    file_name = "adalet_duyurular.csv"
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        announcements = soup.find_all("a", class_="ab-announcement")
        
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Sıra", "Duyuru Başlığı", "Link"])
            
            count = 0
            for index, item in enumerate(announcements, 1):
                try:
                    href = item.get("href")
                    full_link = "https://www.adalet.gov.tr" + href if href and not href.startswith("http") else href
                    title_tag = item.find("h5")
                    title_text = title_tag.text.strip() if title_tag else item.text.strip()

                    if title_text:
                        writer.writerow([index, title_text, full_link])
                        count += 1
                except Exception:
                    continue
        
        print(f"✅ [SCRAPER] {count} duyuru çekildi. Dosya hazır: {file_name}")
        # İŞTE KRİTİK NOKTA: Dosyanın adını geri döndürüyoruz (return)
        return file_name 
    else:
        print(f"❌ [SCRAPER] Bağlantı hatası: {response.status_code}")
        return None # Hata varsa None döndür