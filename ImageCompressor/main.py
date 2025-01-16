import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image

def compress_image():
    try:
        file_path = askopenfilename(
            title="Select an image to compress",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        
        if not file_path:
            print("No file selected. Exiting.")
            return
        
        # Resmi aç
        img = Image.open(file_path)
        original_size = os.path.getsize(file_path) / 1024  # KB cinsinden boyut
        print(f"Original image size: {original_size:.2f} KB")
        
        # Yeniden boyutlandırma ve sıkıştırma
        img = img.resize(img.size, Image.LANCZOS)
        
        # Kullanıcıdan kaydetme konumu isteyin
        save_path = asksaveasfilename(
            title="Save compressed image",
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg")]
        )
        
        if not save_path:
            print("No save location selected. Exiting.")
            return
        
        # Sıkıştırılmış resmi kaydet
        img.save(save_path, "JPEG", quality=85)  # Quality ayarı sıkıştırma oranını kontrol eder
        compressed_size = os.path.getsize(save_path) / 1024  # KB cinsinden boyut
        print(f"Compressed image size: {compressed_size:.2f} KB")
        
        print("Image successfully compressed and saved!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    compress_image()
