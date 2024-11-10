import cv2

cap = cv2.VideoCapture("road.mp4")

# Background subtractor for vehicle detection
object_detector = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=40)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame for display
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # Adjust fx and fy to change the scale
    
    height, width, _ = frame.shape    

    # Adjust ROI based on the vehicle positions in the uploaded image (with new frame size)
    roi = frame[100:350, 150:500]  # Adjust coordinates as per the new resized frame

    # Apply object detector on ROI
    mask = object_detector.apply(roi)
    
    # Remove shadows for clearer detection
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    
    # Find contours for detected objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        # Calculate area and filter out small elements
        area = cv2.contourArea(cnt)
        if area > 800:  # Adjust this threshold to filter out small contours that are not vehicles
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(roi, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display resized frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:  # 'ESC' key to break
        break

cap.release()
cv2.destroyAllWindows()
