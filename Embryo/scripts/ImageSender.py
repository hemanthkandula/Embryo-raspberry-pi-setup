from picamera import PiCamera
from time import sleep

camera = PiCamera()

from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.start_preview()
#sleep(10)
#camera.stop_preview()




#camera = PiCamera()
#camera.sharpness = 100
#camera.contrast = 100
#camera.brightness = 50
#camera.saturation = 0
#camera.ISO = 0
#camera.video_stabilization = True
#camera.exposure_compensation = 8
#camera.exposure_mode = 'auto'
#camera.meter_mode = 'average'
#camera.awb_mode = 'auto'
#camera.image_effect = 'none'
#camera.color_effects = None
#camera.rotation = 0
#camera.hflip = False
#camera.vflip = False
#camera.crop = (0.0, 0.0, 1.0, 1.0)
#camera.framerate = 
camera.resolution = (2592 ,1944 )
#camera.resolution = (3280,2464 )

print("Starting preview.... wait 1 sec...")
camera.start_preview()

#sleep(1)






camera.capture('image.jpeg')
camera.stop_preview()
