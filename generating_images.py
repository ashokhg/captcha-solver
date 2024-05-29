from PIL import Image, ImageDraw, ImageFont
import random

def generate_captcha():
    digits = [random.randint(2, 9) for _ in range(6)]
    # Ensure no adjacent digits are the same
    for i in range(5):
        if digits[i] == digits[i + 1]:
            digits[i + 1] = random.choice([d for d in range(2, 10) if d != digits[i]])

    return ''.join(map(str, digits))

def create_image(text, filename):
    width, height = 190, 80
    image = Image.new('RGB', (width, height), color = (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('serif.ttf', 40)
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)
    image.save(filename)

# Generate 6000 images
for i in range(6000):
    captcha_text = generate_captcha()
    filename = f'{captcha_text}.png'
    create_image(captcha_text, filename)
    print(f"Generated: {filename}")