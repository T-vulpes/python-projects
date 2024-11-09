#Please wait a moment for the video to open.
#Press 't' to reset the calculator.
#press esc to exit calculator

import cv2
from cvzone.HandTrackingModule import HandDetector

# Button class for displaying and detecting button clicks
class Button:
    def __init__(self, position, width, height, value):
        self.position = position
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        # Draw button rectangle
        cv2.rectangle(img, self.position, 
                      (self.position[0] + self.width, self.position[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.position, 
                      (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        
        # Draw button text
        cv2.putText(img, self.value, (self.position[0] + 40, self.position[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def check_click(self, x, y):
        # Check if the coordinates are within the button boundaries
        if self.position[0] < x < self.position[0] + self.width and \
           self.position[1] < y < self.position[1] + self.height:
            return True
        return False

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Button layout and creation
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

# Variables for calculations and click delay
equation = ''
click_delay_counter = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip for a mirrored view

    # Detect hand and landmarks
    hands, img = detector.findHands(img, flipType=False)

    # Draw display area for the equation
    cv2.rectangle(img, (700, 50), (1100, 150), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (700, 50), (1100, 150), (50, 50, 50), 3)

    # Draw buttons
    for button in buttons:
        button.draw(img)

    # Hand presence check and button click handling
    if hands:
        lmList = hands[0]['lmList']  # Landmark list for the first detected hand
        x, y = lmList[8][:2]  # Get only x and y coordinates for index finger tip
        length, _, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)

        # Check if the index finger and middle finger are close to each other (click gesture)
        if length < 50 and click_delay_counter == 0:
            for i, button in enumerate(buttons):
                if button.check_click(x, y):
                    button_value = button_values[i % 4][i // 4]
                    if button_value == '=':
                        try:
                            equation = str(eval(equation))  # Evaluate the equation
                        except:
                            equation = "Error"  # Show error on invalid input
                    else:
                        equation += button_value
                    click_delay_counter = 1  # Start click delay counter

    # Reset click delay counter to prevent repeated clicks
    if click_delay_counter > 0:
        click_delay_counter += 1
        if click_delay_counter > 10:
            click_delay_counter = 0

    # Display the current equation
    cv2.putText(img, equation, (710, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    # Show the image
    cv2.imshow('Calculator', img)

    # Keyboard controls
    key = cv2.waitKey(1)
    if key == ord('c'):  # Clear the equation on 'c' press
        equation = ''
    elif key == ord('t'):  # Clear the equation on 't' press (like a reset button)
        equation = ''
    elif key == 27:  # Exit on 'Esc' press
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
