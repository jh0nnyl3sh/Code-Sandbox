"""
Requests -> İnternetteki bir sayfaya bana
verini ver diye kuryemiz.


BeautifulSoup -> Gelen karmaşık HTML kodunu, bizim
anlayacağımız temiz metne çeviren tercümanımız.

Borsa : Dolar kurunu saniye saniye takip et.
Hacking : Sitenin HTML kodlarını tara ve gizli yorum satırlarını bul.

"""


import requests
from bs4 import BeautifulSoup

# 1. HEDEF URL (Nereye Bağlanacağız.)
url = "https://news.ycombinator.com/"

print(f"📡 '{url}' adresine bağlanılıyor.")

# 2. İSTEK GÖNDER (Kuryeyi Yolla)
# Burada get kullanmamızın sebebi, get, post tur.
response = requests.get(url) 

# Durum Kodunu Kontrol Et (200 = Başarılı, 404 = Bulunamadı)
if response.status_code == 200:
    print("✅ Bağlantı Başarılı! Veri alındı.\n")
    
    # 3. ÇORBAYI HAZIRLA (HTML'i Parçala, anlayabileceğimiz hale getir)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 4. VERİYİ ÇEK (HTML Madenciliği)
    # Hacker News'te başlıklar 'span' etiketi içinde ve class'ı 'titleline'
    headlines = soup.find_all("span", class_="titleline")
    
    print("-" * 40)
    print("📰 GÜNCEL HACKER HABERLERİ")
    print("-" * 40)

    """Burada başlıkları çekmek istediğimiz için önceden
    başıkların hangi HTML etikei ile yazıldığını, classına bakıp
    ona göre kodu yazmamız gerekiyor"""
    
    # İlk 10 haberi yazdır.
    for index, headline in enumerate(headlines[:10], 1):
        # Başlığın içindeki metni (text) al
        title_text = headline.find("a").text
        """Burada başlıklar html de <a> tagi içine yazıldığı 
        için .find("a") dedik."""
        
        
        # Linki al
        link = headline.find("a")["href"]
        """aynı şekilde burda da <a> tagine adresi belirtmek için
        href kullanılır, linki almak için a tagi içindeki 
        href e bak dedik"""
        
        
        
        print(f"{index}. {title_text}")
        print(f"  🔗 {link}\n")
        
else:
    print(f"❌ Hata oluştu! Durum Kodu : {response.status_code}")
    
print("🏁 Tarama Tamamlandı.")