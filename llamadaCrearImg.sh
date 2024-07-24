#!/bin/bash

# Instalar Pillow
pip3 install pillow

# Borrar imágenes previas
rm -rf aleatoriedad

# Ejecutar el script de Python
python3 generar_imagenes.py
