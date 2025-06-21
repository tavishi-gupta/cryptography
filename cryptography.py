def caesar_cipher_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(cipher_text, shift):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted

def main():
    while True:
        print("\nCaesar Cipher Tool")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '2':
            cipher_text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(cipher_text, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()