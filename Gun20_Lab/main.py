# Başkasının yazdığı kütüphaneyi çağırıyoruz
from termcolor import colored
import sys

# Standart print (Sıkıcı)
print("Bu normal bir yazıdır.")

# İndirdiğimiz kütüphanenin gücü (Havalı)
print(colored("MERHABA DÜNYA! Ben Kırmızı Yazıyorum!", "red"))
print(colored("Siber Güvenlik Uyarısı!", "yellow", attrs=["bold", "blink"]))
print(colored("Onaylandı ✅", "green", attrs=["bold"]))

# Python'un nerede çalıştığını görelim (Sanal ortam kanıtı)
print("\nBu kod şu Python exe'sini kullanıyor:")
print(sys.executable)