import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import numpy as np


def leer_codigo_qr():
    # Capturar video desde la cámara
    captura = cv2.VideoCapture(0)

    while True:
        # Leer el fotograma actual
        _, fotograma = captura.read()

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)

        # Buscar y decodificar los códigos QR
        codigos = decode(gray)

        # Iterar sobre los códigos QR encontrados
        for codigo in codigos:
            # Extraer la información del código QR
            datos = codigo.data.decode("utf-8")

            # Mostrar la información en la consola
            print("Información del código QR:", datos)

            # Almacenar el nombre en un archivo de texto junto a la fecha y hora actual
            guardar_nombre(datos)

            # Esperar un segundo para evitar la lectura repetida del mismo código
            cv2.waitKey(2000)

            # Dibujar un contorno alrededor del código QR
            puntos = codigo.polygon
            if puntos:
                # Convertir los puntos a un arreglo numpy
                puntos = np.array(puntos, dtype=np.int32)
                # Dibujar el contorno
                cv2.polylines(fotograma, [puntos], True, (0, 255, 0), 2)

            # Mostrar un texto indicando que se ha leído correctamente el código QR
            cv2.putText(fotograma, "Código QR leído", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Mostrar el fotograma actual en una ventana
        cv2.imshow("Lector de códigos QR", fotograma)

        # Romper el bucle si se presiona la tecla 'q'
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            break

    # Liberar los recursos
    captura.release()
    cv2.destroyAllWindows()

def guardar_nombre(nombre):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Abrir el archivo en modo de escritura y agregar el nombre y la fecha
    with open("nombres.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}, Fecha y hora: {fecha_actual}\n")

# Llamar a la función para leer los códigos QR
leer_codigo_qr()