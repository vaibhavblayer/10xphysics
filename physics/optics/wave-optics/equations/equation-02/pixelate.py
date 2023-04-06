from PIL import Image

image = Image.open('new.png')
p_image = image.resize((400, 400), resample=Image.Resampling.BILINEAR)

p_image.resize(image.size, Image.Resampling.NEAREST).save('t.png', 'PNG')
