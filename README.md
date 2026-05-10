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
```python
#Project 13 - Burglar Detector With Photo Capture
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(2)
pir = MotionSensor(4)
camera = PiCamera()

#start the camera
camera.rotation = 180
camera.start_preview()

#image image names
i = 0

#stop the camera when the pushbutton is pressed
def stop_camera():
    camera.stop_preview()
    #exit the program
    exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    sleep(10)

#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

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
