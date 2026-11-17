import cv2
import numpy as np
import os

Datos = "n"  # Carpeta donde se guardarán los fondos sin botas
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

# Conexión actualizada con tu DroidCam
cap = cv2.VideoCapture("http://192.168.158.74:4747/video")

count = 0
while True:
    ret, frame = cap.read()
    if not ret: 
        break

    k = cv2.waitKey(1)
    
    # Presiona 's' para capturar y guardar el fondo completo
    if k == ord('s'):
        cv2.imwrite(Datos + '/neg_{}.jpg'.format(count), frame)
        print('Imagen guardada: ' + Datos + '/neg_{}.jpg'.format(count))
        count = count + 1
        
    # Presiona 'ESC' (tecla 27) para salir
    if k == 27:
        break

    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()