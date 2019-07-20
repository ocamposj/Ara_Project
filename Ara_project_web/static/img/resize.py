
import unicodedata 

from PIL import Image
from resizeimage import resizeimage 

lista = ["education.jpg", "kidswithcomputer.jpg", "negri.jpg"]

for titulo in lista:
    with open(titulo, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [600, 600])
            cover.save(titulo, image.format)