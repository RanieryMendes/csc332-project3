'''
    Raspberry Pi GPIO Status and Control
'''
from turtle import update
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

dataTime = [] 
dataDistance=[]
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define sensors GPIOs

senPIR = 16

#define actuators GPIOs

ledGrn = 26

#initialize GPIO status variables

senPIRSts = 0

ledGrnSts = 0

GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
# Define button and PIR sensor pins as an input
   
GPIO.setup(senPIR, GPIO.IN)

# Define led pins as output

GPIO.setup(ledGrn, GPIO.OUT) 

# turn leds OFF 

GPIO.output(ledGrn, GPIO.LOW)
    
# @app.route("/")
# def index():
#     # Read GPIO Status

#     senPIRSts = 0
    
#     ledGrnSts = GPIO.input(ledGrn)

#     # if(ledGrnSts==1):
#     #     ledGrnSts = "on"

     
#     templateData = {
#       'senPIR'  : senPIRSts,
#       'ledGrn'  : ledGrnSts,
#       'reading' : 0,
#       }
#     return render_template('index.html', **templateData)
    
# # The function below is executed when someone requests a URL with the actuator name and action in it:
# @app.route("/<deviceName>/<action>")
# def action(deviceName, action):
    
#     if deviceName == 'ledGrn':
#         actuator = ledGrn
    
#     if deviceName == 'sensor':
#         actuator = 'sensor'
    
#     if action == "on":
#         GPIO.output(actuator, GPIO.HIGH)
#     #  status = "on"

#     if action == "off":
#         GPIO.output(actuator, GPIO.LOW)
#     #    status = "off"

#     if action == 'update':
#         senPIRSts = distance()


#     senPIRSts = distance() 

#     lastReading = dataDistance[-1]

#     ledGrnSts = GPIO.input(ledGrn)

#     templateData = {

#       'senPIR'  : senPIRSts,
  
#       'ledGrn'  : ledGrnSts,

#       'reading' : lastReading,}
#     return render_template('index.html', **templateData)


def distance():
    # set Trigger to HIGH
    DATA = open("data.txt", "a")
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
   # print("In distance function")
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    dataTime.append(TimeElapsed)
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    dataDistance.append(distance)
    print(str(distance) + ", " + str(time.time()) + "\n")
    output = str(distance) + ", " + str(StartTime) + "\n" 
    DATA.write(output)

 
    return distance
    
if __name__ == "__main__":
  

   while(True):
       a = distance()
       time.sleep(5)


       
   #app.run(host='0.0.0.0', port=80, debug=True)

#    for i in len(dataTime):
#        print(str(dataTime[i]) + ", " + str(dataDistance[i]))
#   # print(str(distance()) + ", in function " + str(time.time()) + "\n")
       
    
    

