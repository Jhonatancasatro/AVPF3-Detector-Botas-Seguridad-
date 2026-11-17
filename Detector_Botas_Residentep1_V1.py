import cv2

# Carga tu archivo xml de clasificación entrenado
botas_cascade = cv2.CascadeClassifier('classifier/cascade.xml')

# Conexión a la cámara de tu celular con DroidCam
cap = cv2.VideoCapture("http://192.168.158.74:4747/video")

if not cap.isOpened():
    print("Error: No se pudo conectar a la cámara de DroidCam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Se perdió la señal de video.")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detección con máxima sensibilidad para forzar el reconocimiento
    botas = botas_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.05, 
        minNeighbors=1, 
        minSize=(20, 20)
    )
    
    # Dibujar un rectángulo verde alrededor de cada bota detectada
    for (x, y, w, h) in botas:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Bota de Seguridad', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('Detector de Botas - V1', frame)
    
    # Presiona la tecla ESC (27) para salir
    if cv2.waitKey(1) == 27:  
        break

cap.release()
cv2.destroyAllWindows()