from PIL import Image
img = Image.open('small.png')
data = list(img.getdata())
WIDTH, HEIGHT = img.size
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))


