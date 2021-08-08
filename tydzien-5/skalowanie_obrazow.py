from PIL import Image

# przykład na przeskalowanie pliku a.jpg
im = Image.open('a.jpg')
thumbnail = im.resize((300,300))
thumbnail.save('resizeg.jpg')

