from PIL import Image

image = Image.open('image.png')
image = image.convert('RGB')
image.save('NEW.jpg', quality=30)