import socket

def hedef_tara(hedef_ip, port_listesi):
    print(f"\n[🚀] Entegre Recon Botu Başlatılıyor... Hedef : {hedef_ip}")
    print("-" * 50)
    
    # Döngü kuralım
    for port in port_listesi:
        # 1. Soketi Yarat : İnternet (Ipv4) üzerinden TCP protokolü ile git
        ajan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Timeout Kalkanı: Kapı açılmazsa sonsuza kadar beklememeli
        ajan.settimeout(1) # 1 saniye beklesin yeterli
        
        # 3. Kapıyı Çal (connet_ex başarılıys 0 döndürür, kapalıysa hata döndürür)
        sonuc = ajan.connect_ex((hedef_ip, port))
        
        # 4. İstihbarayı Raporla
        if sonuc == 0:
            ajan.close()
            return True
        else:
            ajan.close()
            return False


        # 5. İzi kaybettir (Ajanı imha et)
        ajan.close()
        
if __name__ == "__main__":
    # Nmap projesinin yasal test sunucunucu hedef alalım
    # Etik Hacking Kuralı 1 : İzinsiz tarama yapma!
    hedef = "htts://scanme.nmap.org"
    
    #bazı_portlar = [21, 22, 80, 443, 3306, 3389, 23, 25, 110, 445, 139]
    hedef_port = [80]
        
        
    hedef_tara(hedef, hedef_port)
    

