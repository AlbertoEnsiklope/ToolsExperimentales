#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip
pip3 install selenium requests
sudo apt-get install firefox-geckodriver

# Nombre del archivo de Python
PYTHON_FILE="automatizacion.py"

# Contenido del archivo de Python
cat <<EOL > $PYTHON_FILE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el navegador Firefox
options = webdriver.FirefoxOptions()
# options.add_argument('--headless')  # Ejecuta el navegador en modo headless (sin interfaz gráfica)
driver = webdriver.Firefox(options=options)

# Abre la URL especificada
driver.get("https://codeshare.io/EEEEEqQqw1232")

# Espera a que el textarea esté presente y sea interactivo
try:
    text_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#editor textarea"))
    )
except:
    print("El área de texto no se encontró.")
    driver.quit()
    exit()

# Escribe los números del 1 al 600, esperando 3 segundos entre cada uno
for i in range(1, 601):
    text_area.send_keys(str(i) + ",")
    time.sleep(3)

# Cierra el navegador
driver.quit()
EOL

echo "El archivo de Python '$PYTHON_FILE' ha sido creado."
