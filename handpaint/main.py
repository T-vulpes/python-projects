import cv2
import numpy as np
import mediapipe as mp
import os

brush_thickness = 25
eraser_thickness = 100
draw_color = (255, 0, 255)
dark_blue = (255, 0, 0)  
dark_green = (0, 150, 0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

folder_path = "menu"
overlay_list = [cv2.imread(f'{folder_path}/{imPath}') for imPath in os.listdir(folder_path)]
header = overlay_list[0] if overlay_list else None

img_canvas = np.zeros((720, 1280, 3), np.uint8)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def fingers_up(lm_list, tip_ids):
    fingers = []
    if lm_list[tip_ids[0]][1] < lm_list[tip_ids[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    for id in range(1, 5):
        if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7) as hands:
    xp, yp = 0, 0  

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)  # Aynalama
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        lm_list = []
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_lms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
                
                if lm_list:
                    x1, y1 = lm_list[8][1:]  # İşaret parmağı
                    x2, y2 = lm_list[12][1:]  # Orta parmak

                    tip_ids = [4, 8, 12, 16, 20]
                    fingers = fingers_up(lm_list, tip_ids)
                    if fingers[1] and fingers[2]:
                        if y1 < 125:
                            if 250 < x1 < 450:
                                header = overlay_list[0]
                                draw_color = (255, 0, 255)
                            elif 550 < x1 < 750:
                                header = overlay_list[1]
                                draw_color = dark_blue
                            elif 800 < x1 < 950:
                                header = overlay_list[2]
                                draw_color = dark_green
                            elif 1050 < x1 < 1250:
                                header = overlay_list[3]
                                draw_color = (0, 0, 0)
                        cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), draw_color, cv2.FILLED)
                    elif fingers[1] and not fingers[2]:
                        cv2.circle(img, (x1, y1), 15, draw_color, cv2.FILLED)
                        if xp == 0 and yp == 0:
                            xp, yp = x1, y1
                        if draw_color == (0, 0, 0):
                            cv2.line(img, (xp, yp), (x1, y1), draw_color, eraser_thickness)
                            cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, eraser_thickness)
                        else:
                            cv2.line(img, (xp, yp), (x1, y1), draw_color, brush_thickness)
                            cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, brush_thickness)
                        xp, yp = x1, y1
                mp_drawing.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
        
        if header is not None:
            img[0:125, 0:1280] = header
        
        img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
        _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
        img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, img_inv)
        img = cv2.bitwise_or(img, img_canvas)

        cv2.imshow("Image", img)
        #cv2.imshow("Canvas", img_canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
