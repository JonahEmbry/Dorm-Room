#!/usr/bin/env python

# Come.py tracks when a person has
# come into the designated area. This
# system is designed for two people.
# The ensures the alarm is re-armed
# when a person is in the room.
# When a person comes, it checks
# dataBase2.txt. If it reads that
# no one was there ("absent2"),
# it modifies dataBase2.txt to "absent1"
# If it reads  that one person was there
# ("absent1"), then it modifies
# dataBase2.txt to "present". In both
# cases, it re-arms the alarm

#Path
path1 = '/home/pi/GPS/dataBase2.txt'
path2 = '/home/pi/Alarm/dataBase.txt'

#Arms Alarm system
fix = open(path2, 'w')
fix.write('no')
fix.close()

#Resets  GPS database if both members are present (file has been run twice)
check = open(path1, 'r')
val = check.read().replace('\n','')

#If no one was present
if (val == "absent1"):
	#Edit GPS database 
	new_flag = open(path1, 'w')
	new_flag.write('present')
	new_flag.close()
#If one person were present
else:
	#Edit GPS database
	new = open(path1, 'w')
	new.write('absent1')
	new.close()

check.close()
