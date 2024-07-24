#!/bin/bash

# Nombre del archivo a comprobar
FILE="generar_imagenes.py"

# Comprobar si el archivo ya existe
if [ -f "$FILE" ]; then
    echo "$FILE ya existe. No se descargará de nuevo."
else
    echo "$FILE no encontrado. Descargando..."
    curl -o $FILE https://raw.githubusercontent.com/AlbertoEnsiklope/ToolsExperimentales/main/generar_imagenes.py
fi

# Comprobar si Pillow está instalado
if python3 -c "import PIL" &> /dev/null; then
    echo "Pillow ya está instalado."
else
    echo "Pillow no está instalado. Instalando..."
    pip3 install pillow
fi

# Vaciar Existentes
rm -rf aleatoriedad

# Ejecutar el script Python
python3 $FILE
