from picamera import PiCamera
from time import sleep
import os
import  shutil


#from flask import Flask, send_file,request
#app = Flask(__name__)

camera = PiCamera()
#camera.resolution = (2592 ,1944 )
camera.resolution = (3280,2464 )
#print("Starting preview.... wait 1 sec...")
#camera.start_preview()
#time.sleep(2)
camera.rotation =  180

camera.start_preview()
sleep(100)
camera.stop_preview()
    
