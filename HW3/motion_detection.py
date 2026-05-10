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