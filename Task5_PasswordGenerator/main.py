# 🔐 Password Generator – Created by Malini M

import random
import string

def generate_password(length):
    if length < 4:
        return "⚠️ Password length should be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Python Password Generator!")
    
    try:
        length = int(input("🧮 Enter desired password length: "))
        password = generate_password(length)
        print(f"\n🧾 Your Secure Password is: {password}")
    except ValueError:
        print("🚫 Please enter a valid number.")

    print("✅ Stay secure, stay smart!")

main()
