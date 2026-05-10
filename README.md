# IoT26-HW03
Gachon Univ. IoT Team F HW03

## Project Overview
This project demonstrates a Raspberry Pi motion detector system with photo capture.  
When motion is detected by the sensor, the Raspberry Pi captures a photo automatically.

---

## Objective
- Detect motion using Raspberry Pi
- Capture photos when motion is detected
- Practice GPIO control and camera-based IoT interaction

---

## Hardware Setup
- Raspberry Pi
- Breadboard
- Motion sensor
- Camera module
- Jumper wires

---

## Circuit
- Motion sensor connected to Raspberry Pi GPIO input pin
- Camera module connected to Raspberry Pi camera interface
- Raspberry Pi processes motion detection and triggers photo capture

# IoT26-HW03

## 📖 Project Overview
This project demonstrates a Raspberry Pi motion detector system with photo capture.  
When motion is detected by the sensor, the Raspberry Pi captures a photo automatically.

---

## 🎯 Objective
- Detect motion using Raspberry Pi
- Capture photos when motion is detected
- Practice GPIO control and camera-based IoT interaction

---

## 🛠️ Hardware Setup
- Raspberry Pi
- Breadboard
- Motion sensor
- Camera module
- Jumper wires

---

## ⚙️ Circuit
- Motion sensor connected to Raspberry Pi GPIO input pin
- Camera module connected to Raspberry Pi camera interface
- Raspberry Pi processes motion detection and triggers photo capture

<img src="https://github.com/user-attachments/assets/9e7d42e7-b53a-4199-b1c6-fbd3f716d0f3" width="400"/>

## IDE / Terminal
<img src="https://github.com/user-attachments/assets/0defceaa-064f-4aca-8b4e-83ab119bde2f" width="400" />

---
## 🎥 Video
[https://youtube.com/shorts/VEWtVfIeT-U?feature=share](https://www.youtube.com/shorts/7F73OUBFvlA)


---

## 💻 Code   
Changing code for raspberrypie 5 OS (picamera -> picamera2)
```python
import os
import sys
from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
from time import sleep
from signal import pause

# 1. Hardware Object Creation
# Button: GPIO 2, Motion Sensor: GPIO 4
button = Button(2)
pir = MotionSensor(4)

# 2. Camera Initialization
camera = Picamera2()

# Configure for Raspberry Pi 5 + v1.3 (ov5647)
# Using a standard preview configuration to ensure it shows on screen
config = camera.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
camera.configure(config)

# Start preview window
camera.start()

i = 0

# 3. Shutdown Function
def stop_camera():
    print("\nShutting down the program...")
    camera.stop()
    os._exit(0)

# 4. Photo Capture Function
def take_photo():
    global i
    i = i + 1
    file_path = f'/home/pi/Desktop/motion_capture{i}.jpg'
   
    try:
        camera.capture_file(file_path)
        print(f'Success: Saved to {file_path}')
        # Delay to prevent multiple captures for a single movement
        sleep(2)
    except Exception as e:
        print(f'Capture Failed: {e}')

# 5. Event Binding
button.when_pressed = stop_camera
pir.when_motion = take_photo

# Keep the program running
pause()
```

---
## Team Roles
- **Raspberry Pi Setup**: 김채윤, 김현보  
  (Raspberry Pi connection and development environment setup)

- **Development**: 김건
  (Code execution and refactoring, version synchronization)

- **Documentation**: 김현보
  (Video recording and GitHub repository organization)
