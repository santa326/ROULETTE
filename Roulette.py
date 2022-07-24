# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:09:23 2022

@author: santa
"""

import random
import numpy as np
from matplotlib import pyplot as plt 
import time


# Bet size to start with 1
start_time = time.time()


Initial_Bet = 2
Bet = Initial_Bet
#Money in Poket 99 times Bet A total of 100 Bets
Pocket = 199*Bet
#Set Number of hands to simulate
Total_Hands = 500000


lstreak = 0 
wstreak = 0

#WIN/LOSS/HAND COUNTERS
win_c = 0
loss_c = 0
Hand = 0



#CREATE NUMPY ARRAY TO RECORD DATA TO HAVE HAND/BET/RESULT/POCKET

results = np.empty((Total_Hands,5),int)
results.fill(0)

#We will always pick the same color 0 for RED 1 For BLACK
Color_Pick = 1




# For loop to run the sim for Number of hands
for i in range(0,Total_Hands,1):
    # Increment Hand
    Hand = Hand + 1
    #print("Hand # :",Hand)
    #print("BET/POCKET",Bet,Pocket)
    results[Hand-1,0] = Hand
    results[Hand-1,1] = Bet

    
    # Assigning a Randon Outcome for the Colour
    RoB = random.randint(0,1)
    

    
    # Assigning a Number between 0 and 37 , 0 is 0 and 37 is 00
    Number = random.randint(0,37)
    
    # print(Number)
    
    # We lose always when number is 0 OR the number is 00 OR Colour is not what we picked , Losing is RESULT = 0   
    if Number==0 or Number==37 or RoB != Color_Pick:     
        RESULT = 0
        #When lost , Incremnt the LOSS counter
        loss_c = loss_c + 1
        #print("RESULT : LOSS")
        results[Hand-1,2] = RESULT
    # Only other case is when we WIN
    else:
        RESULT = 1
        #When WIN increment the WIN counter
        win_c = win_c + 1
        #print("RESULT : WIN")
        results[Hand-1,2] = RESULT
        
    # Descision Making based on Hand outcome
    if RESULT ==1:
        #If we win , we take the profit add to pocket and reset the Bet size to 1
        # That means if our last bet was 5 , we win 5 out of which we take 9 and add to pocket
        Pocket = Pocket + (Bet*2)-Initial_Bet
        results[Hand-1,3] = Pocket
        Bet = Initial_Bet
        #if Pocket < Bet:
            #print("Bro ????",Hand)
        
    else:
        #If we loose we play the next had with double the size of bet , this new bet is taken from pocket
        Bet = Bet*2
        results[Hand-1,3] = Pocket
        Pocket = Pocket - Bet
        #if Pocket < Bet:
            #print("Bro ????",Hand)
        

   # print("-------------------------------")
        
print("WINS :",win_c)
print("LOSS :",loss_c)
print("TOTAL PROFIT : ", Pocket-(100*Initial_Bet))
print("TOTAL TIME PLAYED (Hrs) :" ,Hand/55)
print("Biggest Bet :",np.max(results[:,1]))


#print(results)

plt.plot(results[:,0],results[:,3])
plt.plot(results[:,0],results[:,1])
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))