import random # -> 1. rastgele sayı alacağız.

HIDDEN_NUMBER = random.randint(1, 100)
print(f"(Debug modu : Sayı {HIDDEN_NUMBER})") # Test ederken sayıyı görmek için


while True: # 2. oyun bitene kadar döngü
    try:
        guess_input = input("1-100 Arasında bir sayı girin (Çıkış 'q'): ").strip().lower()

        if guess_input == "q":
            print("Pes ettin! Oyun bitti.")
            break
        
        guess_number = int(guess_input)
        
        # 3. üç ihtimalli mantık (logic flow)
        if guess_number < HIDDEN_NUMBER:
            print("⬆️ Daha BÜYÜK bir sayı gir.")
        elif guess_number > HIDDEN_NUMBER:
            print("⬇️ Daha KÜÇÜK bir sayı gir.")
        else:
            # Eşitlik durumu 
            print("🔥 Tebrikler sayıyı buldun.")
            break
        
    except ValueError:
        print("Hata: Lütfen sayı girin.")