#!/usr/bin/env python

# Written by Jonah Embry
# backup.py checks the file dataBase.txt.
# If dataBase.txt matches check variable, 
# then the alarm plays. The variable
# beak is a flag that tracks the number
# of times the alarm has rung. The
# length variable controls the maximum
# number of rings. The program checks
# dataBase.txt after every ring.

import os

#Path to database
path = '/home/pi/Security/SDB.txt'

#Variables
beak = 0;
check = "no"
#print(check)


while(check  == "no"):
        #Plays sound (wave) file
	os.system('aplay /home/pi/Security/SA1.wav')
        #Flag count
	beak = beak + 1
	#Check database
        new_flag = open(path, 'r')
        check = new_flag.read().replace('\n','')
	new_flag.close()


