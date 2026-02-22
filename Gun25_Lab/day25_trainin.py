
# Adım 1
# İstihbarat Toplama
user_name = input("Enter Your Name : ").strip().capitalize()
user_lastname = input("Enter Your Lastname : ").strip().upper()

birth_year = input("Enter Your Birth Year (Örn: 1990) : ").strip()


# Adım 2
# Agent Name
agent_name = user_name[:2].upper() + user_lastname[-2:].upper()
print(f"Agent Name : {agent_name}")


# Password
#reverse name
reverse_name = user_name[::-1].lower()
print(f"Reverse Name : {reverse_name}")

# change a to @
new_reverse_name = reverse_name.replace("a", "@")
print(f"Chane a to @ : {new_reverse_name}")

# add birth year
new_reverse_name = new_reverse_name + birth_year
print(f"Add birth year : {new_reverse_name}")


# 3 security level
len_name = len(user_name)
security_level = len_name * int(birth_year)
print(f"Securiyt Level : {security_level}")


# Adım 3 
print(" --- TARGET ANALYZED ---")
print(f"Codename : {agent_name}")
print(f"Generated Password : {new_reverse_name}")
print(f"Entropy Score : {security_level}")