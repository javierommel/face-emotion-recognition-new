import cv2

# Abre la webcam. Cambia el índice si tienes más de una cámara.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

while True:
    # Captura frame por frame
    ret, frame = cap.read()

    # Si el frame fue leído correctamente, ret es True
    if not ret:
        print("Error: No se puede recibir el frame.")
        break

    # Muestra el frame en una ventana
    cv2.imshow('Webcam', frame)

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()
