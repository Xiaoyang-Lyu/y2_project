# ELEC273 Y2 Group Project - Raspberry Pi Car-Parking System

This project is part of the ELEC273 course at the University of Liverpool and is referred to as the Y2 Group Project.

## Project Overview

The project involves the implementation of an Intelligent Parking Management System using OpenCV and PyTesseract. This system is designed to facilitate efficient parking space management. Please refer our [blog][1] for more details

## How to Use

### Running Environment

- Python Version: 3.11
- Required Packages:
  - cv2
  - pytesseract
  - re
  - RPi.GPIO
  - time
  - smbus
  - abc
  - os
  - signal
  - sqlite3

### Hardware Requirements

- Servo Motor: 
    - Micro Servo Motor SG90
    - Please makesure the Motor is connect to the pin 17 on the Pi
- LCD
    - LCD Display 16x2 I2C
- Raspberry Pi: 
    - Raspberry Pi 4b

### Instructions

1. Ensure you have Python 3.11 installed.
2. Install the required packages using the following command:

    ```bash
    pip install cv2 pytesseract re RPi.GPIO time smbus abc os signal sqlite3
    ```

3. Connect the required hardware components (Servo Motor, LCD, Raspberry Pi).
4. Clone the project repository using the following command:

    ```bash
    git clone https://github.com/Xiaoyang-Lyu/y2_project.git
    ```

5. Navigate to the project folder and switch to the appropriate software environment.
6. Run the following command to start the program:

    ```bash
    python main.py
    ```

7. To manage database data, run the following command:

    ```bash
    python ./imdb/ui_app.py
    ```

## Project Description

This project utilizes computer vision for license plate recognition on vehicles. It then compares the obtained data with the database, controlling the behavior of the motor and LCD based on authentication results. For project structure details, refer to the `software_structure.md` file.


[1]: https://raspberrypi-car-parking-system.blogspot.com/?m=1