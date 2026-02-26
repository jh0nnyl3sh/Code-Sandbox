from port_scanner import hedef_tara
from web_recon import http_scanner

hedef = "scanme.nmap.org"
portlar = [80]

# 1. Ajanı gönder ve telsizden dönen cevabı (True/False) bir değişkene ata
port_acik_mi = hedef_tara(hedef, portlar)

# 2. Şefin Karar Mekanizması
if port_acik_mi == True:
    print("Port açık bulundu! Web ajanı gönderiliyor...")
    http_scanner(hedef)
else:
    print("Port kapalı. Operasyon iptal.")