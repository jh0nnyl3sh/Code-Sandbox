# Önce diğer dosyalardaki ustaları (fonksiyonlar) buraya çağırıyoruz
from data_engine import process_data
from visual_engine import create_chart
from mail_engine import send_report

print("🚀 [CERBERUS PIPELINE] Otomasyon Başlatılıyor...")

# 1. PAS: Veri motorunu çalıştır, bize 'df' (tablo) ve 'excel_dosyasi' adını ver
df, excel_dosyasi = process_data()

# Eğer tablo boş değilse yola devam et
if df is not None and not df.empty:
    # 2. PAS: O 'df' tablosunu Görsel Motora ver, o da bize çizdiği 'resim_dosyasi'nın adını versin
    resim_dosyasi = create_chart(df)
    
    # 3. PAS: Excel ve Resim dosyalarını al, Haberci Motora verip fırlat!
    hedef_mail = "basdasugur@gmail.com" # -> Test için kendi mailim
    send_report(excel_dosyasi, resim_dosyasi, hedef_mail)
    
    print("\n🏁 [GÖREV BAŞARILI] Orkestra susar, işlem tamam!")
    
else:
    print("⚠️ İşlenecek açık dosya bulunamadığı için sistem durduruldu.")
