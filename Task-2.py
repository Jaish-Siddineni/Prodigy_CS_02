from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """Encrypts an image by modifying pixel values with a key."""
    img = Image.open(image_path)
    img_array = np.array(img)  # Convert image to NumPy array

    encrypted_array = img_array ^ key  # Apply XOR operation with key
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))

    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    """Decrypts an image using the same XOR operation."""
    encrypt_image(image_path, key, output_path)  # XOR is reversible

if __name__ == "__main__":
    while True:
        mode = input("Choose mode: (1) Encrypt Image (2) Decrypt Image (3) Exit: ").strip()

        if mode == "1":
            img_path = input("Enter image path: ").strip()
            key = int(input("Enter encryption key (integer 1-255): "))
            output_path = input("Enter output file name (with .png or .jpg extension): ").strip()
            encrypt_image(img_path, key, output_path)

        elif mode == "2":
            img_path = input("Enter encrypted image path: ").strip()
            key = int(input("Enter decryption key (same as encryption key): "))
            output_path = input("Enter output file name (with .png or .jpg extension): ").strip()
            decrypt_image(img_path, key, output_path)

        elif mode == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
