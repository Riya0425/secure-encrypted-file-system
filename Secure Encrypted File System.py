import os

ENCRYPTION_KEY = 4   # Fixed encryption number


def encrypt(text):
    """Encrypt text using Caesar cipher + reverse"""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + ENCRYPTION_KEY) % 26 + start)
        else:
            result += char
    return result[::-1]


def decrypt(text):
    """Decrypt text using Caesar cipher + reverse"""
    text = text[::-1]
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - ENCRYPTION_KEY) % 26 + start)
        else:
            result += char
    return result


def create_secure_file():
    filename = input("Enter filename (with .txt): ").strip()
    normal_password = input("Set password: ").strip()
    secret_password = input("Set SECRET password: ").strip()

    print("\nEnter content for the file (type 'END' in a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    content = "\n".join(lines)
    encrypted_content = encrypt(content)

    with open(filename, "w") as f:
        f.write(normal_password + "\n")
        f.write(secret_password + "\n")
        f.write(encrypted_content)

    print(f"\nFile '{filename}' created and encrypted successfully!")


def open_secure_file():
    filename = input("Enter filename (with .txt): ").strip()

    if not os.path.exists(filename):
        print("File does not exist!")
        return

    with open(filename, "r") as f:
        normal_password = f.readline().strip()
        secret_password = f.readline().strip()
        encrypted_content = f.read()

    password = input("Enter password: ").strip()

    if password == normal_password:
        print("\nAccess granted (NORMAL MODE)")
        print("\n----- Encrypted Content -----")
        print(encrypted_content)
        print("-----------------------------")

    elif password == secret_password:
        print("\nAccess granted (SECRET MODE)")
        print("\n----- Decrypted Content -----")
        print(decrypt(encrypted_content))
        print("-----------------------------")

    else:
        print("Incorrect password! Access denied.")


def main():
    while True:
        print("\n===== Secure Editable Encrypted File =====")
        print("1. Create New Secure File")
        print("2. Open Existing Secure File")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_secure_file()
        elif choice == '2':
            open_secure_file()
        elif choice == '3':
            print("Exiting application...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
