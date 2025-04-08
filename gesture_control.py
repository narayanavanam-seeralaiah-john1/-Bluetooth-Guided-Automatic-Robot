import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

def get_gesture():
    ret, frame = cap.read()
    if not ret:
        return None
    
    hands, img = detector.findHands(frame)
    
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        
        if fingers == [0, 1, 0, 0, 0]:
            return "FORWARD"
        elif fingers == [0, 1, 1, 0, 0]:
            return "BACKWARD"
        elif fingers == [0, 0, 1, 1, 0]:
            return "LEFT"
        elif fingers == [0, 0, 0, 1, 1]:
            return "RIGHT"
        elif fingers == [0, 0, 0, 0, 0]:
            return "STOP"
    
    return None

if __name__ == "__main__":
    while True:
        gesture = get_gesture()
        if gesture:
            print(f"Detected Gesture: {gesture}")
        
        cv2.waitKey(1)
