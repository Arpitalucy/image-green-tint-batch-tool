import os
from PIL import Image, ImageEnhance, ImageOps

input_folder = r"C:\Users\YourPath\Input"
output_folder = r"C:\Users\YourPath\Output"

os.makedirs(output_folder, exist_ok=True)

def apply_green_tint(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            grayscale = ImageOps.grayscale(img)

            green_tinted = Image.new("RGB", grayscale.size)
            for y in range(grayscale.size[1]):
                for x in range(grayscale.size[0]):
                    gray_value = grayscale.getpixel((x, y))
                    reduced_green = int(gray_value * 0.75)
                    green_tinted.putpixel((x, y), (gray_value // 2, reduced_green, gray_value // 2))

            contrast = ImageEnhance.Contrast(green_tinted)
            green_tinted = contrast.enhance(1.2)

            brightness = ImageEnhance.Brightness(green_tinted)
            green_tinted = brightness.enhance(1.1)

            green_tinted.save(output_path, "PNG")
            print(f"Processed: {output_path}")
    except Exception as e:
        print(f"Error: {image_path} -> {e}")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        apply_green_tint(input_path, output_path)

print("Done")
