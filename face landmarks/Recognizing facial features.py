import cv2
import mediapipe as mp

# Mediapipe yüz tanıyıcıları
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Video kaynağını aç
cap = cv2.VideoCapture(0)

# Mediapipe FaceMesh Modeli
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

    while True:
        _, frame = cap.read()
        # BGR'den RGB'ye dönüştür
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Yüzün noktalarını tespit et
        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Yüzün 468 noktasına çizim yap
                for landmark in face_landmarks.landmark:
                    # Yüz noktalarının konumlarını al
                    h, w, _ = frame.shape
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    # Noktalara daire çiz
                    cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
        
        # Sonuçları göster
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC tuşuna basınca çık
            break

cap.release()
cv2.destroyAllWindows()
