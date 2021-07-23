# first install RPi.GPIO module on your system by (pip install RPi.GPIO)
import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rlight = 13
Ylight = 19
ledGreen = 26

rsts = 0
YSts = 0
GSts = 0

GPIO.setup(rlight, GPIO.OUT)
GPIO.setup(Ylight, GPIO.OUT)
GPIO.setup(Glight, GPIO.OUT)

GPIO.output(Rlight, GPIO.LOW)
GPIO.output(ylight, GPIO.LOW)
GPIO.output(Glight, GPIO.LOW)


@app.route('/')
def index():
    RSts = GPIO.input(Rligth)
    YSts = GPIO.input(Ylight)
    GSts = GPIO.input(Glight)

    templateData = {'Rligth': RSts,
                    'Yligth': YSts,
                    'Gligth': GSts}

    return render_template('index.html', **templateData)


@app.route('/<deviceName>/<action>')
def do(deviceName, action):
    if deviceName == "Rlight":
        actuator = ledRed
    if deviceName == "Ylight":
        actuator = ledYellow
    if deviceName == "Glight":
        actuator = ledGreen

    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)

    RSts = GPIO.input(ledRed)
    YSts = GPIO.input(ledYellow)
    GSts = GPIO.input(ledGreen)

    templateData = {'ledRed': RSts,
                    'ledYellow': YSts,
                    'ledGreen': GSts}

    return render_template('index.html', **templateData)

app.run(debug=True)
