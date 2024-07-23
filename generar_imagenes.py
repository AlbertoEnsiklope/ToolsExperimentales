import random
import struct
import os
import zlib

# Función para calcular el CRC (Cyclic Redundancy Check)
def crc32(data):
    return zlib.crc32(data) & 0xffffffff

# Cabecera PNG estándar
png_header = bytearray([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG signature
])

# IHDR chunk
width = 800
height = 800
bit_depth = 8
color_type = 2  # Truecolor
compression_method = 0
filter_method = 0
interlace_method = 0

ihdr_data = struct.pack(">IIBBBBB", width, height, bit_depth, color_type, compression_method, filter_method, interlace_method)
ihdr_length = struct.pack(">I", len(ihdr_data))
ihdr_type = b'IHDR'
ihdr_crc = struct.pack(">I", crc32(ihdr_type + ihdr_data))

ihdr_chunk = ihdr_length + ihdr_type + ihdr_data + ihdr_crc

# IEND chunk
iend_chunk = b'\x00\x00\x00\x00IEND\xAE\x42\x60\x82'

# Crear carpeta para guardar las imágenes
output_folder = 'imagenes'
os.makedirs(output_folder, exist_ok=True)

# Generar y guardar 20 imágenes
for i in range(1, 21):
    # Generar contenido aleatorio
    random_content = bytearray(random.getrandbits(8) for _ in range(width * height * 3))  # 3 bytes por píxel (RGB)

    # Comprimir el contenido aleatorio
    compressed_content = zlib.compress(random_content)

    # IDAT chunk
    idat_length = struct.pack(">I", len(compressed_content))
    idat_type = b'IDAT'
    idat_crc = struct.pack(">I", crc32(idat_type + compressed_content))

    idat_chunk = idat_length + idat_type + compressed_content + idat_crc

    # Combinar todos los chunks
    png_data = png_header + ihdr_chunk + idat_chunk + iend_chunk

    # Nombre del archivo
    file_name = f'imagen{i}.png'
    file_path = os.path.join(output_folder, file_name)

    # Escribir los datos en un archivo
    with open(file_path, 'wb') as f:
        f.write(png_data)

print("Imágenes generadas y guardadas en la carpeta 'imagenes'.")
