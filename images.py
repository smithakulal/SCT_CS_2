import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

def load_image(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    image = Image.open(image_path).convert("L")  
    return np.array(image, dtype=np.uint8)

def save_image(image_array, output_path):
    image = Image.fromarray(image_array)
    image.save(output_path)

def pixel_swap_encrypt(image_data, key):
    encrypted = image_data.copy()
    np.random.seed(key)
    indices = np.arange(encrypted.size)
    np.random.shuffle(indices)  
    encrypted = encrypted.flatten()[indices].reshape(image_data.shape)
    return encrypted, indices

def pixel_swap_decrypt(encrypted_data, indices):
    decrypted = np.zeros_like(encrypted_data.flatten())
    decrypted[indices] = encrypted_data.flatten()
    return decrypted.reshape(encrypted_data.shape)

def math_operation_encrypt(image_data, key):
    return (image_data + key) % 256

def math_operation_decrypt(encrypted_data, key):
    return (encrypted_data - key) % 256

if __name__ == "__main__":
    print("Image Encryption Tool")
    image_path = input("Enter the path to the image (e.g., 'image.png'): ")
    
    try:
        image_data = load_image(image_path)
        print("Original Image Loaded.")
        
        plt.imshow(image_data, cmap='gray')
        plt.title("Original Image")
        plt.axis('off')
        plt.show()
        
        key = int(input("Enter a numeric key for encryption: "))
        encrypted_data, swap_indices = pixel_swap_encrypt(image_data, key)
        encrypted_data = math_operation_encrypt(encrypted_data, key)
        
        encrypted_path = "encrypted_image.png"
        save_image(encrypted_data, encrypted_path)
        print(f"Encrypted image saved to {encrypted_path}")
        
        plt.imshow(encrypted_data, cmap='gray')
        plt.title("Encrypted Image")
        plt.axis('off')
        plt.show()
        
        decrypted_data = math_operation_decrypt(encrypted_data, key)
        decrypted_data = pixel_swap_decrypt(decrypted_data, swap_indices)
        
        decrypted_path = "decrypted_image.png"
        save_image(decrypted_data, decrypted_path)
        print(f"Decrypted image saved to {decrypted_path}")
        
        plt.imshow(decrypted_data, cmap='gray')
        plt.title("Decrypted Image")
        plt.axis('off')
        plt.show()
        
        if np.array_equal(image_data, decrypted_data):
            print("Decryption successful! The original image was restored.")
        else:
            print("Decryption failed! The original image was not restored.")
    
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
if np.array_equal(image_data, decrypted_data):
    print("Decryption successful! The original image was restored.")
else:
    print("Decryption failed! The original image was not restored.")
