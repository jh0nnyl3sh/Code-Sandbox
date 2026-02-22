import requests # -> internete çıkacağız
from bs4 import BeautifulSoup # -> anlamsız html kodlarını anlamlı hale getirecek
import csv # -> Verileri kaydetmek için
import time # -> işlem sırasında bekler, böylece ip ban yemeyiz, insan taklidi yapar.

url = "https://news.ycombinator.com"
print(f"📡 '{url}' taranıyor...")
time.sleep(1) # -> 1 saniye beklesin.

response = requests.get(url) # istek atıyoruz. GET (getir) POST (Gönder)


if response.status_code == 200:
    print("✅ Bağlantı Başarılı! Veri Alındı.\n")
    
    # çorbayı hazırla (html'i parçala)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # hackernews başlıklarını al
    headlines = soup.find_all("span", class_="titleline")
    
    print("-" * 40)
    print("📰 GÜNCEL HACKER HABERLERİ")
    print("-" * 40)
    
    
    # ----  CSV İŞLEMLERİ BAŞLIYOR ----
    # 1. Dosyayı 'w' (write) modunda açıyoruz.
    # newsline='' -> Satır aralarında boiluk olmaması için Windowsta şart.
    # encoding='utf-8' -> Türkçe karakter sorunu yaşamamak için.
    file_name = "hacker_news_raporu.csv"
    
    
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    #with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        # 2. Yazıcıyı (Writer) oluştur.
        writer = csv.writer(file)
        
        # 3. Başlık (Header) Satırını Yaz
        writer.writerow(["Sıra", "Haber Başlığı", "Link"])
        
        print(f"💾 '{file_name}' dosyası oluşturuldu, veri yazılıyor...\n")
        
        # 4. Döngü ile verileri satır satır yaz
        for index, headline in enumerate(headlines[:10], 1):
            # Başlığın içindeki metni al
            title_text = headline.find("a").text
            # linki al
            link = headline.find("a")["href"]
            
            print(f"{index}. {title_text}")
            print(f".   🔗 {link}\n")
            
            # Veriyi CSV dosyasına yaz
            writer.writerow([index, title_text, link])

            
    print(f"✅ İŞLEM TAMAM! toplam {index} haber kaydedildi.")
    print(f"📁 Dosyayı şuradan kontrol et : {file_name}")
    

else:
    print("❌ Siteye erişilemedi.")
        
        
        
        
        
        
        
        
        
        
        
        