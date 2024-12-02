from captcha.image import ImageCaptcha
from random import choice
from string import ascii_letters, digits


def generate_captcha():
    image_object = ImageCaptcha()
    random_text = ''.join(choice(ascii_letters + digits) for _ in range(4))
    random_text = random_text.upper()
    captcha_bytes = image_object.generate(random_text)
    return captcha_bytes, random_text