import cv2

# Carga tu archivo xml recién entrenado
botas_cascade = cv2.CascadeClassifier('classifier/cascade.xml')

# Conexión a la cámara de tu celular con DroidCam
cap = cv2.VideoCapture("http://192.168.158.74:4747/video")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar las botas con mayor sensibilidad ajustada
    botas = botas_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.2, 
        minNeighbors=2, 
        minSize=(50, 50)
    )
    
    # Dibujar un rectángulo azul alrededor de cada bota detectada
    for (x, y, w, h) in botas:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Bota V2 (Estable)', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow('Detector de Botas - V2', frame)
    
    # Presiona la tecla ESC (27) para salir
    if cv2.waitKey(1) == 27:  
        break

cap.release()
cv2.destroyAllWindows()