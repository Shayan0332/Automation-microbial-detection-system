import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import messagebox

# ---------------- GPIO SETUP ----------------
STEP_PIN = 18
DIR_PIN = 23
EN_PIN = 24

LEFT_LIMIT = 17     # Suction
RIGHT_LIMIT = 27    # Filtration

GPIO.setmode(GPIO.BCM)

GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(EN_PIN, GPIO.OUT)

GPIO.setup(LEFT_LIMIT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_LIMIT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(EN_PIN, GPIO.LOW)   # Enable motor

STEP_DELAY = 0.001
running = False

# ---------------- MOTOR FUNCTIONS ----------------
def move_left():
    global running
    running = True
    GPIO.output(DIR_PIN, GPIO.HIGH)  # LEFT direction
    while GPIO.input(LEFT_LIMIT) == GPIO.HIGH and running:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(STEP_DELAY)
    running = False
    print("LEFT limit reached")

def move_right():
    global running
    running = True
    GPIO.output(DIR_PIN, GPIO.LOW)   # RIGHT direction
    while GPIO.input(RIGHT_LIMIT) == GPIO.HIGH and running:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(STEP_DELAY)
    running = False
    print("RIGHT limit reached")

def stop_motor():
    global running
    running = False
    print("Motor stopped")

def exit_app():
    stop_motor()
    GPIO.output(EN_PIN, GPIO.HIGH)
    GPIO.cleanup()
    root.destroy()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Automation Microbial Detection System")
root.geometry("400x300")

tk.Label(root, text="Motor Control Panel", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Suction (LEFT)", width=25, height=2,
          command=move_left, bg="lightgreen").pack(pady=5)

tk.Button(root, text="Filtration (RIGHT)", width=25, height=2,
          command=move_right, bg="lightblue").pack(pady=5)

tk.Button(root, text="STOP", width=25, height=2,
          command=stop_motor, bg="orange").pack(pady=5)

tk.Button(root, text="EXIT", width=25, height=2,
          command=exit_app, bg="red").pack(pady=5)

root.mainloop()
