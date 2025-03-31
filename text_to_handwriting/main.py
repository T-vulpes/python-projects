from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, output_filename="handwriting.png"):
    try:
        font_path = "C:\\Windows\\Fonts\\segoesc.ttf" 
        font = ImageFont.truetype(font_path, 40)
    except:
        font = ImageFont.load_default()

    max_width = 800
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        text_bbox = font.getbbox(test_line) 
        text_width = text_bbox[2] - text_bbox[0]  

        if text_width <= max_width - 40:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1] + 10  
    img_height = (len(lines) + 1) * line_height + 40  

    img = Image.new("RGB", (max_width, img_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    y = 20
    for line in lines:
        draw.text((20, y), line, font=font, fill=(0, 0, 0))
        y += line_height

    img.save(output_filename)
    print(f"El yazısı görüntüsü oluşturuldu: {output_filename}")

text = input("Type your text: ")
text_to_image(text)
