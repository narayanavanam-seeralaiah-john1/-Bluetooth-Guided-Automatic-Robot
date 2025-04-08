from gesture_control import get_gesture
from bluetooth_control import connect_bluetooth, send_command
import time

# Connect to Bluetooth
sock = connect_bluetooth()
print("Connected to Robot via Bluetooth.")

while True:
    gesture = get_gesture()
    if gesture:
        print(f"Sending Command: {gesture}")
        send_command(sock, gesture)
    time.sleep(0.5)
