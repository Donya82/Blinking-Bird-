
from grovepi import * 
import random
import flask
from grove_rgb_lcd import *
import numpy as np
import requests
import json
from typing import Dict, List, Optional

IP = "172.20.10.7"
#melissa: 172.20.10.7
#donya: 10.26.254.4

def postScore(hostname: str, score: Dict[str, str]) -> List[Dict[str, str]]:
    """Post the winning score on leaderboard
    
    Args:
        hostname: 
        score: 
        
    Returns:
        NA
    """
                     
    post_score = requests.post(f"http://{hostname}:5000/leaderboard/sendscore", data=score)
    #request_leaderboard = requests.get(f"http://{hostname}:5000/leaderboard/makeboard")
    myboard = post_score.json()
    sorted_list = sorted(myboard, key=lambda x: list(x.values())[0], reverse=True)
    for item in sorted_list:
        print(item)
    

def main():
  set_bus("RPI_1") # set I2C to use the hardware bus
  potentiometer = 0 # Connect the Grove Rotary Angle Sensor to analog port A0
  button = 4
  pinMode(potentiometer,"INPUT")
  pinMode(button,"INPUT")
  time.sleep(1)
  # Reference voltage of ADC is 5v
  adc_ref = 5
  # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
  full_angle = 300
  grove_vcc = 5 # Set Vcc of the grove interface is to 5v

  #setting all initial conditions of variables 
  cnt = 1 
  oldpos = 0
  posx = 0
  disp = "                                "
  player = 1 
  score1 = 0
  score2 = 0

  while True: #reset (after both players have played)
    if cnt == 3:
      #set all variables back to start
      score1 = 0 
      score2 = 0
      player = 1
      setRGB(110,0,255)
      setText("Player 1 now playing") 
      time.sleep(0.75)
      #start set up of game
      cnt = 1 

    while cnt == 1: #set up phase of game
      
      setRGB(110,0,255)
      posx = 0
      oldpos = 0
      rand1 = random.randint(0,1) #setting random ints for the position of the pipes
      rand2 = random.randint(0,1)
      disp= "                                "

      #position the pipes on random
      setText(disp)
      pipepos1 = (rand1*16) + random.randint(2,5) 
      pipepos2 = (rand2*16) + random.randint(6,10)

      #print the pipes on the screen 
      if pipepos1 <= pipepos2:
        disp = "@" + disp[1:pipepos1] + "!" + disp[pipepos1+1:pipepos2] + "!" + disp[pipepos2:]
      else:
        disp = "@" + disp[1:pipepos2] + "!" + disp[pipepos2+1:pipepos1] + "!" + disp[pipepos1:]
      setText(disp) 
      time.sleep(0.1)

      #set the initial conditions of bird 
      posx = 0 #last pixel of lcd
      cnt = 0 #start the game for player

    while cnt == 0:#start the game
       setRGB(110,0,255)
       sensor_value = (analogRead(potentiometer)/2) #get info from potentiometer  
       time.sleep(0.25) # don't overload the i2c bus 

       #get row (y-axis) position of the bird
       if(sensor_value >= 150): #if distance is higher or equal than the threshhold flappy moves up
        posy = 1
        setText("low")
       elif(sensor_value < 150):  #if distance is lower than the threshhold flappy moves down 
        posy = 0  
        setText("high")

       #moves flappy forward
       posx += 1 

       #get xolumn postion of bird and prints
       birdpos = (posy*16)+posx
       if oldpos <= birdpos:
        disp = disp[:oldpos] + " " + disp[oldpos+1:birdpos] + "@" + disp[birdpos+1:]
       else:
        disp = disp[:birdpos] + "@" + disp[birdpos+1:oldpos] + " " + disp[oldpos+1:]
       oldpos = birdpos
       setText(disp)
       time.sleep(0.25)

      #check if bird hit pipe or won
       if(birdpos == pipepos1 or birdpos == pipepos2): #did bird hit pipe?
        #flash red
        setRGB(255,0,0)
        #change player 
        if player==1:
            player = 2
            setText("Player 2 now playing") 
            time.sleep(0.75)
            setRGB(110,0,255)
            cnt=1
        elif player==2:#if round oevr check who won
            if score1 > score2:
              setText("Player 1 Wins") 
              name1 = input("Enter Winner's name: ")
              scoreDict = {name1:score1}
              ldrbrd = postScore(IP, str(scoreDict))
              print(ldrbrd)
            elif score1< score2:
              setText("Player 2 Wins")
              name1 = input("Enter Winner's name: ")
              scoreDict = {name1:score2}
              ldrbrd = postScore(IP, str(scoreDict))
              print(ldrbrd)
            elif score1 == score2:
              setText("Tie")   
            cnt=3 #reset game
           
        #sending scores to leaderboard API: 
          
            
            #if we have enough time: use the rotary encoder for this?
            '''
            rotaryAlph = "abcdefghijklmnopqrstuvwxyz0"
            sensor_value = (analogRead(potentiometer)/2) #get info from potentiometer
            exit_status = False
            name1 = "@"
            disp = "Enter Name:     " + name1
            namelen = 0
            while exit_status is False:
                if sensor_value <= 25:
                  letterChoice = rotaryAlph[sensor_value]
                else:
                  letterChoice = "0"
                setText(disp + letterChoice)
                button_status = digitalRead(button)
                if button_status:
                  if letterChoice == "0" or namelen == 16:
                   exit_status = True
                  else:
                   name1 = name1 + letterChoice
                   disp = "Enter Name:     " + name1
                   namelen += 1
            '''
            #send score

            time.sleep(1)
            

       elif(birdpos == 15 or birdpos == 31):#did player score?
        #update scores 
        if player ==1:
          score1 += 1
        elif player ==2:
          score2 += 1
        #Green light 
        setRGB(0,255,0)
        time.sleep(0.50)
        #continue game
        cnt =1
            
       else:#keep game going
        cnt =0

if __name__ == '__main__':
    main()
'''
FOR API:
import mail  API
send score via email
receive to VM
graph using pyplot

'''
