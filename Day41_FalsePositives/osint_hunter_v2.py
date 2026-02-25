import requests
import time

def osint_tarama_v2(hedef_kullanici_adi):
    print(f"\n[👁️] OSINT Gözlemcisi V2 Uyandı. Hedef : {hedef_kullanici_adi}")
    print("-" * 50)
    
    # MİMARİ DEĞİŞİKLİK: Sadece URL değil, artık her sitenin "Hata İmzasını" da tutuyoruz.
    # Bu kelimeleri o sitelere sahte bir isimle girip ekrandaki yazılara bakarak bulduk.
    siteler = {
        "GitHub": {
            "url": "https://github.com/{}",
            "hata_imzasi": "not found"
        },
        "Reddit": {
            "url": "https://www.reddit.com/user/{}",
            "hata_imzasi": "nobody on reddit goes by that name"
        },
        "Instagram": {
            "url": "https://www.instagram.com/{}",
            "hata_imzasi": "üzgünüz, bu sayfaya ulaşılamadı" 
        },
        "X (Twitter)": {
            "url": "https://x.com/{}",
            "hata_imzasi": "bu hesap mevcut değil"
        }
    }
    
    # Taktik 2: Sitelere "Bana Türkçe hata ver" demek için 'Accept-Language' ekledik.
    kimlik = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    bulunan_hesaplar = 0
    
    for site_adi, veri in siteler.items():
        hedef_url = veri["url"].format(hedef_kullanici_adi)
        # Hata kelimesini küçük harfe çeviriyoruz (Büyük/küçük harf duyarlılığından kaçmak için)
        hata_kelimesi = veri["hata_imzasi"].lower() 
        
        try:
            cevap = requests.get(hedef_url, headers=kimlik, timeout=5)
            
            # 1. KALKAN: Site dürüst davranıp direkt 404 döndüyse
            if cevap.status_code == 404:
                print(f"[-] Yok      [{site_adi}] (Gerçek 404)")
                continue # Bu siteyi bitir, sonrakine geç
                
            # 2. KALKAN: Site 200 OK döndü. Yalan söylüyor olabilir mi? İçeriye bakıyoruz!
            if cevap.status_code == 200:
                # Sayfanın tüm HTML kaynak kodunu al ve küçük harfe çevir
                sayfa_icerigi = cevap.text.lower()
                
                # Eğer bizim tespit ettiğimiz hata kelimesi bu sayfanın içindeyse:
                if hata_kelimesi in sayfa_icerigi:
                    print(f"[!] KANMADI! [{site_adi}] (200 döndü ama içerik sahte/boş)")
                else:
                    print(f"[+] BULUNDU! [{site_adi}] -> {hedef_url}")
                    bulunan_hesaplar += 1
            else:
                print(f"[-] Yok      [{site_adi}] (Kod: {cevap.status_code})")
                
        except requests.exceptions.RequestException:
            print(f"[x] HATA     [{site_adi}] (Bağlantı Kurulamadı)")
            
        time.sleep(1)
        
    print("=" * 50)
    print(f"[🎯] Operasyon Tamamlandı. Gerçekten var olan platform sayısı: {bulunan_hesaplar}")

if __name__ == "__main__":
    hedef = input("Hedef Kullanıcı Adını (Username) Girin : ")
    osint_tarama_v2(hedef)