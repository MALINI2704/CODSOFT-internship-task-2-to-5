# 📒 Simple Contact Book Application
# 🔧 Developed by Malini M

contacts = {}

def show_menu():
    print("\n📘 CONTACT BOOK MENU")
    print("1️⃣ Add Contact")
    print("2️⃣ View All Contacts")
    print("3️⃣ Search Contact by Name")
    print("4️⃣ Delete Contact")
    print("5️⃣ Exit")

def add_contact():
    name = input("👤 Enter Name: ").strip()
    phone = input("📞 Enter Phone Number: ").strip()
    email = input("✉️ Enter Email: ").strip()
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n📋 All Contacts:")
        for name, details in contacts.items():
            print(f"\n🔹 Name: {name}")
            print(f"   📞 Phone: {details['Phone']}")
            print(f"   ✉️ Email: {details['Email']}")

def search_contact():
    name = input("🔍 Enter Name to Search: ").strip()
    if name in contacts:
        print(f"\n👁 Found Contact:\n📞 {contacts[name]['Phone']}\n✉️ {contacts[name]['Email']}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("🗑 Enter Name to Delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"🧹 Contact '{name}' deleted successfully!")
    else:
        print("⚠️ Contact not found.")

# 🔄 Main Loop
while True:
    show_menu()
    choice = input("\n🔢 Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("👋 Exiting Contact Book. Stay connected!")
        break
    else:
        print("🚫 Invalid choice. Please enter a number from 1 to 5.")
# CODSOFT-internship-task-2-to-5
