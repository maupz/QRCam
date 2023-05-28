# Lector de Códigos QR en Tiempo Real

Este proyecto es un lector de códigos QR en tiempo real utilizando la cámara de un dispositivo. Detecta y decodifica los códigos QR presentes en el campo de visión de la cámara, guarda el nombre extraído en un archivo de texto junto con la fecha y hora actuales, y proporciona una interfaz visual para mostrar el fotograma actual con indicadores visuales de los códigos QR detectados.

## Requisitos

- Python 3.x
- OpenCV (`pip install opencv-python`)
- PyZBar (`pip install pyzbar`)

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Instala las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso
1. Ejecuta el script qrCamera.py para iniciar el lector de códigos QR:

```bash
python ./QRCamera/qrCamera.py
```
2. Asegúrate de que tu cámara esté funcionando y bien enfocada.
3. Apunta la cámara hacia un código QR y espera a que se detecte y decodifique. La información del código QR se mostrará en la consola y se guardará en el archivo nombres.txt junto con la fecha y hora actuales.
4. En la ventana de visualización de la cámara, se dibujará un contorno alrededor del código QR detectado y se mostrará un texto indicando que se ha leído correctamente.
5. Presiona la tecla 'q' para salir del programa.