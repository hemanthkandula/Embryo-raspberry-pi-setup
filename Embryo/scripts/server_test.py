from picamera import PiCamera
from time import sleep
import os
import  shutil
import threading
from queue import Queue



from flask import Flask, send_file,request

import RPi.GPIO as GPIO
#from mfrc522 import SimpleMFRC522
from uidtag import RC522Reader


app = Flask(__name__)
camera = PiCamera()
#camera.resolution = (2592 ,1944 )
camera.resolution = (3280,2464 )
#print("Starting preview.... wait 1 sec...")
#camera.start_preview()
#time.sleep(2)
#camera.rotation =  180

@app.route("/")
def hello():
    return "Shafiee Lab Embryo Imaging"

@app.route("/server")
def server():
    return "server running v1.0"

@app.route("/check_slide")
def slide():
    slide  = request.args.get('slide', default = 'noname', type = str)
    try: 
        reader = RC522Reader()
        text = reader.force_read_id()
        #print(id)
        #print(text)
    finally:
        GPIO.cleanup()
    slide = slide.strip()
    text = text.strip()
    del reader

    #return slide+text
    #return text
    if(text==slide):
        return "Embryo dish ID matched"

    elif (text!= slide):
        return "Embryo dish ID is: "+text



@app.route("/get_image")
def get_image():
    slide  = request.args.get('slide', default = 'noname', type = str)
    directory = '/home/pi/Embryo/data/'+slide +'/'
    if not os.path.exists(directory):
       os.makedirs(directory)

    id = len(os.listdir(directory))
    filePath = '/home/pi/Embryo/scripts/image.jpg'

    if os.path.exists(filePath):
        os.remove(filePath)

    camera.capture(filePath)

    shutil.copy2(filePath, directory+slide+'_'+str(id)+'.jpg')
    return send_file(filePath, mimetype='image/jpg')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print("server started")

