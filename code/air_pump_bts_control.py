import RPi.GPIO as GPIO
import time

# Pin configuration
PWM_PIN = 18
DIR_PIN = 23

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set direction
GPIO.output(DIR_PIN, GPIO.HIGH)

# Start PWM
pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)

try:
    while True:

        print("Air Pump LOW Speed")
        pwm.ChangeDutyCycle(30)   # Low speed
        time.sleep(5)

        print("Air Pump HIGH Speed")
        pwm.ChangeDutyCycle(80)   # High speed
        time.sleep(5)

except KeyboardInterrupt:
    print("Stopping pump")

finally:
    pwm.stop()
    GPIO.cleanup()
