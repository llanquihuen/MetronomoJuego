from PIL import Image
import os

image1=Image.open("c:/Users/Seth/Desktop/Introducción a la programación (+90 ejercicios propuestos)/Python/GamePython/Imagenes/designing-sea-and-stars-backdrop-sky-2000x4166.jpg")
image1.resize((400,600),Image.LANCZOS).save("c:/Users/Seth/Desktop/Introducción a la programación (+90 ejercicios propuestos)/Python/GamePython/Imagenes/fondo.jpg")