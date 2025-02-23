import random
import string
import json

# File to store passwords
PASSWORD_FILE = "passwords.json"

# Function to generate a strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to save password
def save_password(account, password):
    try:
        with open(PASSWORD_FILE, "r") as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}

    passwords[account] = password

    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)
    
    print(f"✅ Password saved for {account}")

# Function to retrieve password
def get_password(account):
    try:
        with open(PASSWORD_FILE, "r") as file:
            passwords = json.load(file)
            return passwords.get(account, "⚠️ No password found for this account!")
    except (FileNotFoundError, json.JSONDecodeError):
        return "⚠️ No passwords stored yet!"

# Main Menu
while True:
    print("\n🔐 Password Manager")
    print("1️⃣ Save a new password")
    print("2️⃣ Retrieve a password")
    print("3️⃣ Exit")
    
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        account = input("Enter the account name (e.g., Gmail, Facebook): ")
        password = generate_password()
        save_password(account, password)
        print(f"🔑 Generated Password: {password}")

    elif choice == "2":
        account = input("Enter the account name to retrieve the password: ")
        print(f"🔓 Password for {account}: {get_password(account)}")

    elif choice == "3":
        print("👋 Exiting Password Manager. Stay Secure!")
        break

    else:
        print("❌ Invalid choice! Please select 1, 2, or 3.")
