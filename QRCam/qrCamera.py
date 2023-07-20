import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import numpy as np
import mysql.connector



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
            #guardar_nombre(datos)
            enviar_nombre(datos)

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
            cv2.putText(fotograma, "CODIGO QR LEIDO", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Mostrar el fotograma actual en una ventana
        cv2.imshow("Lector de codigos QR", fotograma)

        # Romper el bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
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

    try:
        # Establecer la conexión con la base de datos
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='asistencia'
        )

        # Crear un cursor para ejecutar las consultas SQL
        cursor = cnx.cursor()

        # Definir la consulta SQL para insertar los datos
        query = "INSERT INTO data (Nombre, FechaHora) VALUES (%s, %s)"
        record = (nombre, fecha_actual)

        # Ejecutar la consulta SQL
        cursor.execute(query, record)

        # Confirmar los cambios en la base de datos
        cnx.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        cnx.close()

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)

import requests

def enviar_nombre(nombre):
    # Construir la URL del endpoint con el parámetro de código
    url = f"http://localhost:8080/endpoint?code={nombre}"

    try:
        # Realizar la solicitud HTTP GET al endpoint
        response = requests.get(url)

        # Verificar el código de respuesta
        if response.status_code == 200:
            print("Nombre enviado correctamente al endpoint.")
        else:
            print(f"Error al enviar el nombre al endpoint. Código de respuesta: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error de conexión:", str(e))


# Llamar a la función para leer los códigos QR
leer_codigo_qr()