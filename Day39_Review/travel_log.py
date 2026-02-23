import datetime

def sistem_logu_olustur(km, saat, konum, durum):
    # Anlık zamanı alıyoruz
    su_an = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # rapor metni hazırlıyoruz.
    rapor = f"""
[{su_an}] OPERATÖR SEYAHAT LOGU
-------------------------------
Hedef Konum : {konum}
Katedilen Yol : {km} km
Geçen Süre : {saat} Saat
Anlık Durum : {durum}
-------------------------------\n
"""
    
    # Dosyaya yazma işlemi 
    with open("operator_gunlugu.txt", "a", encoding="utf-8") as dosya:
        dosya.write(rapor)
    
    print(f"✅ {km} km'lik operasyon başarıyla txt dosyasına gönderildi.")
    
    
    
    
# Ana Yönetim
if __name__ == "__main__":
    sistem_logu_olustur(
        km= 800,
        saat= 11,
        konum = "Memleket (Ana Karargah)",
        durum = "Fiziksel olarak bitkin ama GitHub yeşillerini koruyacak kadar disiplinli"
    )    