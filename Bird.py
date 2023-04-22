
from grovepi import *
import time
from grove_rgb_lcd import *
grovepi.set_bus("RPI_1") # set I2C to use the hardware bus

ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4
range = 150 #mid point of range
birdpos = (posx, posy)
rand1 = [0,1]
rand2 = [0,1]

time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5
# Vcc of the grove interface is normally 5v
grove_vcc = 5
while cnt = 1:
    #pipe 
     pipeonepos = (rand1, 2)
     pipeonepos = (rand2, 6)
     posx = 10 #last pixel of lcd
     cnt = 0 

 
while cnt = 0:
 
 try:  
  dist= grovepi.ultrasonicRead(ultrasonic_ranger) # Read distance value from Ultrasonic

  time.sleep(0.1) # don't overload the i2c bus 
  sensor_value = range

  if(dist >= sensor_value): #if distance is higher or equal than the threshhold flappy moves up
   posx = 1
  
  elif(dist < sensor_value):  #if distance is lower than the threshhold flappy moves down 
   posx = 0    
  
  posy = count +1

  if(posy == rand1 or rand2)
    if(posx == 2 or 6):
        #Red light 
        #Reset score
        #Send score 
        #go to lose page 
  elif(posx =0)
    #Pause
    #Score update (pop up screen) check if last point win or loss 
    #Green light 
    #next player

    
 
 except IOError:
  
  print ("Error angle")
