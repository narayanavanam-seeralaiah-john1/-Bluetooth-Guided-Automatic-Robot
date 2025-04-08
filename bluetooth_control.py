import bluetooth

# Replace with your HC-05 Bluetooth module's MAC address
ROBOT_BT_ADDRESS = "00:11:22:33:44:55"  # Change this

def connect_bluetooth():
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((ROBOT_BT_ADDRESS, 1))
    return sock

def send_command(sock, command):
    try:
        sock.send(command + "\n")
    except Exception as e:
        print("Bluetooth Error:", e)

if __name__ == "__main__":
    sock = connect_bluetooth()
    while True:
        cmd = input("Enter command: ")
        send_command(sock, cmd)
