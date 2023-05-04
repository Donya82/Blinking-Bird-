
from grovepi import *
import time
import random
from grove_rgb_lcd import *

set_bus("RPI_1") # set I2C to use the hardware bus

#ultrasonic_ranger = 4 # Connect the Grove Ultrasonic Ranger to digital port D4
#range = 150 #mid point of range

potentiometer = 0 # Connect the Grove Rotary Angle Sensor to analog port A0
pinMode(potentiometer,"INPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5
# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300
# Vcc of the grove interface is normally 5v
grove_vcc = 5
cnt = 1
oldpos = 0
posx = 0
disp= "                                "
player =1 
score1=0
score2=0

while True:
  if cnt == 3:
    score1=0
    score2=0
    player=1
    cnt=1
   
  while cnt == 1: #when cnt=1 game is in the begining set up phase 
    setRGB(100,0,255)
    posx = 0
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
    pipepos1 = (rand1*16) + random.randint(2,5)
    pipepos2 = (rand2*16) + random.randint(6,10)
    
    if pipepos1 <= pipepos2:
      disp = "@" + disp[1:pipepos1] + "!" + disp[pipepos1+1:pipepos2] + "!" + disp[pipepos2:]
    else:
      disp = "@" + disp[1:pipepos2] + "!" + disp[pipepos2+1:pipepos1] + "!" + disp[pipepos1:]
  
    setText(disp) 
    time.sleep(0.1)
    #set the initial conditions of bird 
    posx = 0 #last pixel of lcd
    cnt = 0 #start the game 
    
  
  while cnt == 0:#start the game
     #setText("DEBUG")
     #time.sleep(0.1)
     # moves flappy up and down
     setRGB(100,0,255)
    # dist= ultrasonicRead(ultrasonic_ranger) # Read distance value from Ultrasonic
     sensor_value = (analogRead(potentiometer)/2)
      
     time.sleep(0.25) # don't overload the i2c bus 
    
     if(sensor_value >= 150): #if distance is higher or equal than the threshhold flappy moves up
      posy = 1
      setText("low")
     elif(sensor_value < 150):  #if distance is lower than the threshhold flappy moves down 
      posy = 0  
      setText("high")
     
     
     #posy = random.randint(0,1)
     
     # moves flappy forward
     posx += 1 
      
     birdpos = (posy*16)+posx
     if oldpos <= birdpos:
      disp = disp[:oldpos] + " " + disp[oldpos+1:birdpos] + "@" + disp[birdpos+1:]
     else:
      disp = disp[:birdpos] + "@" + disp[birdpos+1:oldpos] + " " + disp[oldpos+1:]
     
     oldpos = birdpos
     setText(disp)
     time.sleep(0.25)
     

     #print bird
    
     #grovepi.setCursor(posx, posy) 
     #setText( "    @")
     #time.sleep(0.5)

    #check if bird hit pipe or won
     if(birdpos == pipepos1 or birdpos == pipepos2):
      #flash red
      setRGB(255,0,0)
      #change player 
      if player==1:
          player = 2
          cnt=1
      elif player==2:
          if score1 > score2:
            setText("Player 1 Wins") 
          elif score1< score2:
            setText("Player 2 Wins")          
          elif score1 == score2:
            setText("Tie")   
          cnt=3
       
        
       
       #Send score 

     elif(birdpos == 15 or birdpos == 31):
      #Score update (pop up screen) check if last point win or loss 
      if player ==1:
        score1 += 1
      elif player ==2:
        score2 += 1
      #Green light 
      setRGB(0,255,0)
      time.sleep(0.50)
      #continue game
      cnt =1
     else:
      cnt =0



