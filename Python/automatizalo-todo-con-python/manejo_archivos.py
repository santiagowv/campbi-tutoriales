""" OS module
    Provee funciones para interactuar con el sistema operativo
    Tareas comunes como listar el contenido de un directorio o carpeta, ver las propiedades de un archivo
"""
import os

# Listar todos los archivos en un directorio
files = os.listdir("directorio_pruebas")
for file in files:
    print(" -", file)

# Construir una ruta de archivo utilizando os.path.join
file_path = os.path.join("directorio_pruebas", "sample_file_1.csv")
print(file_path)



""" OS.path module
    Es un módulo que hace parte de OS e incluye funcionalidades para manipulación de rutas como unir y dividir
    rutas de archivos. 
"""

# Chequear si un archivo existe y obtener su tamaño
if os.path.exists(file_path):
    stats = os.stat(file_path)
    print(f"El archivo {file_path} existe y su tamaño es {stats.st_size} bytes.")
else:
    print(f"El archivo {file_path} no existe.")

# Agregar y obtener variables de entorno
os.environ["MY_VARIABLE"] = "12345"
print(f"MY_VARIABLE:", os.environ.get("MY_VARIABLE"))



""" pathlib module
    Más moderna y es una forma orientadaba objetos para manejar rutas de archivos. Hace el código más entendible
    y conciso. En general, es una mejor opción que OS.path.
"""

from pathlib import Path

# Crear objeto para el directorio actual
current_dir = Path(".")

# Construir una ruta de archivo usando el operador /
file_path = current_dir / "directorio_pruebas" / "sample_file_1.csv"

# Chequear si un archivo existe y leer o crear el archivo
if file_path.exists():
    content = file_path.read_text()
    print(f"Contenido de {file_path}:{content}")
else:
    file_path.write_text("Hola, pathlib")
    print(f"El archivo {file_path} fue creado con un texto de muestra")



""" shutil module
    Ofrece funciones para copiar, mover y eliminar archivos y carpetas.
"""
import shutil
from pathlib import Path
current_dir = Path(".")
source_file = current_dir / "directorio_pruebas" / "sample_file_1.csv"
backup_file = current_dir / "directorio_backup" / "backup_sample_file_1.csv"

# Copiar el archivo de origen y hacer backup
if source_file.exists():
    shutil.copy2(source_file, backup_file)
    print(f"Archivo copiado {source_file} a {backup_file}")
else:
    print(f"Archivo de origen {source_file} no existe")

# crear directorio temporal
temp_dir = Path("temp_dir")
temp_dir.mkdir(exist_ok = True)
print(f"Directorio temporal creado {temp_dir}")

# Eliminar directorio temporal y todo su contenido
shutil.rmtree(temp_dir)
print(f"Directorio temporal eliminado: {temp_dir}")



""" glob module
    Permite buscar rutas de archivos que coinciden con un patron especifico.
"""
import glob

csv_files = glob.glob("*.py")
print("Archivos .py en el directorio actual:")
for csv_file in csv_files:
    print(" -", csv_file)