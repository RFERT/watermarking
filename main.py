import cv2
print(cv2.__version__)

img = cv2.imread("ravus.jpg")

# # cv2.imshow("Vusra", img)
# # Redimensionner
# resized = cv2.resize(img, (300, 300))

# # Convertir en niveaux de gris
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Détection de contours
# edges = cv2.Canny(img, 100, 200)

# # Afficher le résultat
# cv2.imshow("Contours", edges)
# cv2.imshow("Gris", gray)
# cv2.imshow("resized", resized)
cap = cv2.VideoCapture(0)  # 0 = webcam par défaut

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam", frame)

    # Quitter si on appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()