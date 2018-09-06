from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
app.debug = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(2.5)

@app.route("/fire")
def fire():
    p.ChangeDutyCycle(6.5)
    time.sleep(2)
    p.ChangeDutyCycle(2.5)
    return "Firing", 200

app.run(host='0.0.0.0')