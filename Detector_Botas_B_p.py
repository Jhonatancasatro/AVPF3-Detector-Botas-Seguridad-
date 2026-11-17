import cv2
import numpy as np
import imutils
import os

Datos = "p"  # Carpeta donde se guardarán las fotos de las botas
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

# Conexión actualizada con tu DroidCam
cap = cv2.VideoCapture("http://192.168.158.74:4747/video")

x1, y1 = 120, 40
x2, y2 = 550, 450

count = 0
while True:
    ret, frame = cap.read()
    if not ret: 
        break
    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=38)

    k = cv2.waitKey(1)
    
    # Presiona 's' para guardar la foto de la bota dentro del recuadro
    if k == ord('s'):
        cv2.imwrite(Datos + '/bota_{}.jpg'.format(count), objeto)
        print('Imagen guardada: ' + Datos + '/bota_{}.jpg'.format(count))
        count = count + 1
        
    # Presiona 'ESC' (tecla 27) para salir de la cámara
    if k == 27:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

cap.release()
cv2.destroyAllWindows()