import requests
import time

def osint_tarama(hedef_kullanici_adi):
    print(f"\n[👁️] OSINT Gözlemcisi Uyandı. Hedef : {hedef_kullanici_adi}")
    print("-" * 50)
    
    # Hedef sitelerin URL şablonları ({} olan yere username gelecek)
    siteler = {
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Medium": "https://medium.com/@{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Vimeo": "https://vimeo.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        
        # benim eklediklerim (Bunlar için her siteye girip username
        # linklerinin nasıl olduklarına tek tek baktım)
        "Linkedin" : "https://www.linkedin.com/in/{}",
        "Facebook" : "https://www.facebook.com/public/{}",
        "Instagram" : "https://www.instagram.com/{}",
        "X" : "https://x.com/{}",
        "Tiktok": "https://www.tiktok.com/@{}",
        "Telegram" : "https://t.me/s/{}"
        # şimdilik bunlar yeterli denemeye geçelim
    }
    
    
    # Tarayıcı kimliğine bürünmek için User-Agent
    # Eğer bunu yapmazsak, siteler bizim python botu olduğumuz anlar
    
    kimlik = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        
    }
    
    bulunan_hesaplar = 0
    
    for site_adi, url_sablonu in siteler.items():
        # URL hedef isimle birleştiriyoruz
        hedef_url = url_sablonu.format(hedef_kullanici_adi)
        
        
        try:
            # Ajanımız siteye GET isteği atıyor
            cevap = requests.get(hedef_url, headers=kimlik, timeout=5)
            
            # Eğer sunucu 200 önderse 
            if cevap.status_code == 200:
                print(f"[+] BULUNDU! {site_adi} -> {hedef_url}")
                bulunan_hesaplar += 1
                
            else:
                print(f"[-] Yok   [{site_adi}]")
                
        except requests.exceptions.RequestException:
            print(f"[!] HATA [{site_adi}] (Bağlantı Kurulamadı)")
            
        # Sitelerin güvenlik duvarlarına yakalanmamak için araya 1 saniye bekleme koyalım
        time.sleep(1)
        
    print("=" * 50)
    print(f"[🎯] Operasyon Tamamlandı. Toplam {bulunan_hesaplar} platformda iz bulundu.")
        
        
if __name__ == "__main__":
    hedef = input("Hedef Kullanıcı Adını (Username) Girin : ")
    osint_tarama(hedef)