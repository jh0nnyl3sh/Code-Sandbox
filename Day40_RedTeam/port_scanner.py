import socket

def hedef_tara(hedef_ip, port_listesi):
    print(f"\n[🚀] Taktiksel Tarama Başlatılıyor: {hedef_ip}")
    print("-" * 45)
    
    # Basit bir döngü kullanalım
    for port in port_listesi:
        # 1. Ajanı (Soketi) Yarat : İnternet (Ipv4) üzerinden TCP protokolü ile git
        ajan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Timeout Kalkanı : Kapı açılmazsa sonsuza kadar beklememesi için
        ajan.settimeout(1) # 1 saniye bekle
        
        # 3. Kapıyı Çal (connect_ex: Başarılıysa 0 döndürür, kapalıysa hata döndürür)
        sonuc = ajan.connect_ex((hedef_ip, port))
        
        # 4 İstihbaratı Raporla
        if sonuc == 0:
            print(f"[+] Port {port:<4} : AÇIK (Sızma için potansiyel kapı!)")
        else:
            print(f"[-] Port {port:<4} : KAPALI")


        # 5. İzi kaybettir (Ajanı imha et)
        ajan.close()
        
if __name__ == "__main__":
    # Nmap projesinin yasal test sucunusunu hedef alıyoruz 
    # Etik Hacking Kuralı 1 : İzinsiz tarama yapma!
    hedef = "scanme.nmap.org"
    
    # En kritik kapılar: 21 (FTP), 22 (SSH),
    # 80 (HTTP), 443 (HTTPS) 3306 (MySQL), 3389 (RDP)
    kritik_portlar = [21, 22, 80, 443, 3306, 3389]
    
    hedef_tara(hedef, kritik_portlar)
        
        