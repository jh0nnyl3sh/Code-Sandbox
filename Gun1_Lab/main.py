import datetime

CURRENT_DATE = datetime.date.today().year
TARGET_YEAR = 2030
name = input("Enter your name : ").strip().capitalize()

while True:  # Sonsuz döngü başlat. doğru girene kadar çıkamaz.
    try:
        age_input = input("Enter your age : ")
        age = int((age_input)) # int e çevirmeyi dene
        if age < 0 or age > 120 : # Mantıksal kontrol
            print("Error! Please enter your real age ")
        else:
            break # Hata yoksa döngüden çık
    
    except ValueError:
        print("Error! Please enter just number.")


        
future_age = age + (TARGET_YEAR - CURRENT_DATE)

print(f"Merhaba {name}, demek {age} yaşındasın! Tanıştığımıza memnun oldum")
print(f"{TARGET_YEAR} yılında {future_age} yaşında olacaksın.")

