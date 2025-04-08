# Bluetooth-Guided Automatic Robot Controlled by Hand Gestures with Webcam Integration

## 📌 Project Overview
This project enables a **Bluetooth-controlled robot** that moves based on **hand gestures**, using:
- **OpenCV & CVZone** for real-time gesture detection.
- **PyBluez** for Bluetooth communication with the robot.
- **Arduino (or any microcontroller with Bluetooth)** to receive commands and move accordingly.

## 🚀 Features
✅ Detects hand gestures using a webcam
✅ Translates gestures into movement commands
✅ Sends commands via Bluetooth
✅ Controls the robot wirelessly

---

## 🛠️ Hardware Requirements
- **Bluetooth-enabled robot** (e.g., Arduino + HC-05 module)
- **Computer with a webcam**
- **Bluetooth adapter (if not built-in)**

## 🖥️ Software & Dependencies
Ensure Python is installed, then install dependencies using:
```sh
pip install opencv-python mediapipe cvzone pybluez
```

---

## 📂 Project Structure
```
/gesture_robot
   ├── gesture_control.py   # Hand gesture recognition
   ├── bluetooth_control.py # Bluetooth communication
   ├── main.py              # Integration & execution
```

---

## 📜 How It Works
1️⃣ **Hand gestures are detected using OpenCV & CVZone**  
2️⃣ **Gestures are translated into movement commands** (`FORWARD`, `BACKWARD`, etc.)  
3️⃣ **Commands are sent via Bluetooth to the robot**  
4️⃣ **Robot executes movements based on received commands**  

---

## 🏗️ Setup & Usage
### 1️⃣ Run the Gesture Recognition Script
```sh
python gesture_control.py
```
This will detect your hand gestures and display the recognized commands.

### 2️⃣ Connect to the Robot via Bluetooth
```sh
python bluetooth_control.py
```
Manually send movement commands to test Bluetooth communication.

### 3️⃣ Run the Complete System
```sh
python main.py
```
This will integrate **gesture detection** and **Bluetooth control** to operate the robot.

---

## 🎯 Future Enhancements
🔹 Add **voice control** for hands-free operation  
🔹 Use **AI models** for more complex gesture detection  
🔹 Implement **Wi-Fi communication** for long-range control  

---

## 🤝 Contributing
Feel free to **modify, improve, and share**! If you encounter issues, report them or submit a pull request. 🚀

---

## 🏆 Credits
Developed using **Python, OpenCV, CVZone, and PyBluez**. Inspired by the need for **intuitive and wireless robot control**. 🤖✨
