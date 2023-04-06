from PIL import Image

image = Image.open("new.png").convert("RGBA")
data = image.getdata()
new_data = []

for n, i in enumerate(data):
    if (n%5) in [0, 1]:
        new_data.append((255, 255, 255, 255))
    else:
        new_data.append(i)

image.putdata(new_data)
image.save('t.png', 'PNG')
