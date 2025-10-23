from PIL import Image, ImageDraw, ImageFont
import random
import os

TEMPLATES = ["templates/drake.jpg", "templates/wojak.jpg"]
TOPICS_PATH = "data/topics.json"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def generate_meme_pair():
    with open(TOPICS_PATH, "r", encoding="utf-8") as f:
        topics = f.read().splitlines()

    topic1 = random.choice(topics)
    topic2 = random.choice(topics)

    meme1 = create_meme(random.choice(TEMPLATES), topic1)
    meme2 = create_meme(random.choice(TEMPLATES), topic2)

    return meme1, meme2

def create_meme(template_path, text):
    img = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, size=36)

    w, h = img.size
    text_w, text_h = draw.textsize(text, font=font)
    x = (w - text_w) // 2
    y = h - text_h - 20

    draw.text((x, y), text, font=font, fill="white")
    return img
