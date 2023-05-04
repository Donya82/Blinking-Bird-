
from grovepi import *
import time
import random
from grove_rgb_lcd import *

set_bus("RPI_1") # set I2C to use the hardware bus

ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4
#range = 150 #mid point of range



time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5
# Vcc of the grove interface is normally 5v
grove_vcc = 5
cnt = 1
oldpos = 0
posx = 0
disp= "                                "
while True:
  while cnt == 1: #when cnt=1 game is in the begining set up phase 
    oldpos = 0
    rand1 = random.randint(0,1) #setting random ints for the position of the pipes
    rand2 = random.randint(0,1)
    disp= "                                "
    #set player (1 or 2)
    setText(disp)
    #position and print the pipes
    """
    grovepi.setCursor (4, rand1)
    setText( "!")
    grovepi.setCursor(6, rand2)
    setText( "!")
    """
    pipepos1 = (rand1*16) + random.randint(2,8)
    pipepos2 = (rand2*16) + random.randint(2,8)
    if pipepos1 <= pipepos2:
      disp = "@" + disp[1:pipepos1] + "!" + disp[pipepos1+1:pipepos2] + "!" + disp[pipepos2:]
    else:
      disp = "@" + disp[1:pipepos2] + "!" + disp[pipepos2+1:pipepos1] + "!" + disp[pipepos1:]
  
    setText(disp)  
    #set the initial conditions of bird 
    posx = 0 #last pixel of lcd
    cnt = 0 #start the game 
    
  
  while cnt == 0:#start the game
     setText("DEBUG")
     # moves flappy up and down
     dist= ultrasonicRead(ultrasonic_ranger) # Read distance value from Ultrasonic
     time.sleep(0.1) # don't overload the i2c bus 
     sensor_value = 150 #set midway sensor value
     if(dist >= sensor_value): #if distance is higher or equal than the threshhold flappy moves up
      posy = 1
     elif(dist < sensor_value):  #if distance is lower than the threshhold flappy moves down 
      posy = 0    

     # moves flappy forward
     posx += 1 
      
     birdpos = (posy*16)+1
     if oldpos <= birdpos:
      disp = disp[:oldpos] + " " + disp[oldpos+1:birdpos] + "@" + disp[birdpos:]
     else:
      disp = disp[:birdpos] + "@" + disp[birdpos+1:oldpos] + " " + disp[oldpos:]
     
     oldpos = birdpos
     setText(disp)
     

     #print bird
    
     #grovepi.setCursor(posx, posy) 
     #setText( "    @")
     #time.sleep(0.5)

    #check if bird hit pipe or won
     if(birdpos == pipepos1 or birdpos == pipepos2):
       #Red light 
       #Reset score
       #Send score 
       #go to lose page 
       cnt=1
     elif(birdpos == 15 or birdpos == 31):
      #Pause
      #Score update (pop up screen) check if last point win or loss 
      #Green light 
      #next player
      cnt =1
     else:
      cnt =0



