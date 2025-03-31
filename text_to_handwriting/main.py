from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, output_filename="handwriting.png"):
    try:
        font_path = "C:\\Windows\\Fonts\\segoesc.ttf" 
        font = ImageFont.truetype(font_path, 40)
    except:
        font = ImageFont.load_default()

    # Maksimum genişlik belirle
    max_width = 800
    words = text.split()
    
    lines = []
    current_line = ""

    # Metni satır satır böl
    for word in words:
        test_line = current_line + " " + word if current_line else word
        text_bbox = font.getbbox(test_line)  # Yeni yöntem (getsize yerine getbbox)
        text_width = text_bbox[2] - text_bbox[0]  # Genişliği hesapla

        if text_width <= max_width - 40:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    # Satır yüksekliği hesapla
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1] + 10  
    img_height = (len(lines) + 1) * line_height + 40  

    # Görüntü oluştur
    img = Image.new("RGB", (max_width, img_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Metni resme yaz
    y = 20
    for line in lines:
        draw.text((20, y), line, font=font, fill=(0, 0, 0))
        y += line_height

    # Görüntüyü kaydet
    img.save(output_filename)
    print(f"El yazısı görüntüsü oluşturuldu: {output_filename}")

text = input("Type your text: ")
text_to_image(text)
