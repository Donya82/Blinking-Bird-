
from grovepi import *
import time
from grove_rgb_lcd import *
grovepi.set_bus("RPI_1") # set I2C to use the hardware bus

ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4
range = 150

grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5
# Vcc of the grove interface is normally 5v
grove_vcc = 5

while True:
 try:  
  dist= grovepi.ultrasonicRead(ultrasonic_ranger) # Read distance value from Ultrasonic
  time.sleep(0.1) # don't overload the i2c bus 
  sensor_value = range

  if(dist >= sensor_value): #if distance is higher or equal than the threshhold flappy moves up
   birdposx = 1
  
  elif(dist < sensor_value):  #if distance is lower than the threshhold flappy moves down 
   birdposx = 0    
  
 except IOError:
  print ("Error angle")
