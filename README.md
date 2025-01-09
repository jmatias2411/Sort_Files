# Sort_Files
# Organizador de Archivos en Python

Este proyecto es un script en Python que organiza los archivos de una carpeta en subcarpetas según su tipo y la fecha de creación, con opciones adicionales como filtrado por palabras clave y respaldo de archivos. 

## Características

- **Clasificación por tipo de archivo**: Ordena los archivos en categorías como Documentos, Imágenes, Vídeos, Audios, Archivos Comprimidos, entre otros.
- **Orden por mes**: Opción para agrupar los archivos por mes de creación.
- **Filtrado por palabras clave**: Permite organizar solo los archivos que contengan palabras específicas en su nombre.
- **Copia de seguridad**: Posibilidad de crear una copia de respaldo de los archivos antes de moverlos.
- **Configuración personalizada**: Define las carpetas de destino para cada categoría.

## Requisitos

- Python 3.7 o superior.
- Librerías estándar de Python: `os`, `shutil`, y `datetime`.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/organizador-archivos.git

	2.	Navega al directorio del proyecto:

cd organizador-archivos



Uso
	1.	Ejecuta el script desde la terminal:

python organizador_archivos.py


	2.	Sigue las instrucciones en pantalla:
	•	Ruta de la carpeta: Ingresa la ubicación de la carpeta que deseas organizar.
	•	Categorías: Selecciona las categorías de archivos que deseas organizar.
	•	Opciones adicionales: Elige si deseas ordenar por meses, usar palabras clave o crear un respaldo.
	•	Carpetas de destino: Define los nombres de las carpetas para cada categoría.
	3.	El script organizará los archivos según la configuración seleccionada.

Estructura de carpetas por defecto

Por defecto, los archivos se clasifican en las siguientes categorías:
	•	Documentos: .pdf, .docx, .txt, .xlsx
	•	Imágenes: .jpg, .jpeg, .png, .gif
	•	Vídeos: .mp4, .avi, .mov, .mkv
	•	Audios: .mp3, .wav, .aac
	•	Archivos comprimidos: .zip, .rar, .7z, .tar.gz
	•	Otros: Cualquier otro archivo no incluido en las categorías anteriores.

Personalización

Puedes personalizar las extensiones de archivo asociadas a cada categoría editando el diccionario FOLDERS_BY_TYPE en el código.

Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto, abre un issue o envía un pull request.

Licencia

Este proyecto está bajo la Licencia MIT.

Puedes actualizar los enlaces, como el del repositorio o el de la licencia, según sea necesario. Si necesitas algo más, ¡házmelo saber!