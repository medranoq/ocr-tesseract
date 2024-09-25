# ocr-tesseract

## Descripción

Este es un proyecto de OCR simple que utiliza **Tesseract** y **OpenCV**. El proyecto puede extraer texto de imágenes y archivos
PDF.

## Estrucutra del proyecto

**.gitignore**

Indica los archivos que no se deben subir al repositorio.

**README.md**

Archivo de descripción del proyecto.

**requirements.txt**

Archivo que contiene las dependencias del proyecto.

**Dockerfile**

Archivo que contiene las instrucciones para crear una imagen de Docker.

* Utiliza una imagen de **Python 3.12** en su version slim.
* Instala el engine de **OCR Tesseract** y la libreria nativa de **OpenCV**.
* Crea un directorio de trabajo en el contenedor llamado app, mismo en el que agrega el archivo `requirements.txt`.
* Instala los requerimientos del proyecto utilizando el comando `pip3 install`.

**docker-compose.yml**

Archivo que contiene las instrucciones para crear un contenedor de Docker.

* Se define un servicio llamado `ocr-tesseract` y mediante la instruccion `build` se le indica que debe construir la
  imagen a partir del archivo `Dockerfile` ubicado en la raiz del proyecto.
* La instruccion `volumes` se utiliza para montar el directorio actual en el contenedor en el directorio `/app`.
* Por ultimo, se indica que el contenedor debe ejecutar el comando `python3 app.py`.

**app.py**

Archivo que contiene el código fuente del proyecto.


## Instrucciones de uso

Ejecutar el siguiente comando para construir la imagen de Docker y crear el contenedor.

```bash 
docker-compose up