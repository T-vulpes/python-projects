#Please wait a moment for the video to open.
#Press 'c' or 't' to reset the calculator.
#press esc to exit calculator

import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, position, width, height, value):
        self.position = position
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.position, 
                      (self.position[0] + self.width, self.position[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.position, 
                      (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.position[0] + 40, self.position[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def check_click(self, x, y):
        if self.position[0] < x < self.position[0] + self.width and \
           self.position[1] < y < self.position[1] + self.height:
            return True
        return False

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=1)

button_values = [['7', '8', '9', '*'],
                 ['4', '5', '6', '='],
                 ['1', '2', '3', '+'],
                 ['0', '/', '.', '-']]
buttons = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 700
        ypos = y * 100 + 150
        buttons.append(Button((xpos, ypos), 100, 100, button_values[y][x]))

equation = ''
click_delay_counter = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  
    hands, img = detector.findHands(img, flipType=False)

    cv2.rectangle(img, (700, 50), (1100, 150), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (700, 50), (1100, 150), (50, 50, 50), 3)

    for button in buttons:
        button.draw(img)
    if hands:
        lmList = hands[0]['lmList']  # Landmark list for the first detected hand
        x, y = lmList[8][:2]  # Get only x and y coordinates for index finger tip
        length, _, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)

        if length < 50 and click_delay_counter == 0:
            for i, button in enumerate(buttons):
                if button.check_click(x, y):
                    button_value = button_values[i % 4][i // 4]
                    if button_value == '=':
                        try:
                            equation = str(eval(equation))  
                        except:
                            equation = "Error"  
                    else:
                        equation += button_value
                    click_delay_counter = 1  

    if click_delay_counter > 0:
        click_delay_counter += 1
        if click_delay_counter > 10:
            click_delay_counter = 0

    cv2.putText(img, equation, (710, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)
    cv2.imshow('Calculator', img)

    key = cv2.waitKey(1)
    if key == ord('c'):  
        equation = ''
    elif key == ord('t'): 
        equation = ''
    elif key == 27: 
        break

cap.release()
cv2.destroyAllWindows()
