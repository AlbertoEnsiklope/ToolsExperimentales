# Requiere instalar Pillow: pip3 install pillow

import random
import os
from PIL import Image

def generar_imagen_aleatoria(ancho, alto, nombre_archivo):
    imagen = Image.new('RGB', (ancho, alto))
    pixeles = imagen.load()

    for x in range(ancho):
        for y in range(alto):
            pixeles[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    imagen.save(nombre_archivo)

if __name__ == '__main__':
    directorio = 'aleatoriedad'
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    for i in range(60):
        nombre_archivo = os.path.join(directorio, f'imagen_aleatoria_{i+1}.png')
        generar_imagen_aleatoria(1920, 1080, nombre_archivo)
