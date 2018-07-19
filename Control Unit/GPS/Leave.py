#!/usr/bin/env python
# Leave.py tracks when a person has
# left the designated area. This
# system is designed for two people.
# The ensures the alarm is not played
# when no one is in the room.
#When a person leaves, it checks
# dataBase2.txt. If it reads that
# both people were there ("present"),
# it modifies dataBase2.txt to "absent1"
# If it reads  that one person were there
# "absent1", then it modifies
# dataBase2.txt to "absent2" and
# dataBase.txt (in the Alarm folder) to
# "flag", turning off the alarm.

#Path
path1 = '/home/pi/GPS/dataBase2.txt'
path2 = '/home/pi/Alarm/dataBase.txt'

#Set Up
new_flag = open(path1, 'r')
check = new_flag.read().replace('\n','')
#print(check)

#If both members were present
if (check == "present"):
	#Edit the GPS database
	fix = open(path1, 'w')
	fix.write('absent1')
	#print("absent")
	fix.close()
else:
#If only one member were present
        #Edit the GPS database
	fix2 = open(path1, 'w')
        fix2.write('absent2')
        #print("absent2")
        fix2.close()
	#Edit the Alarm database
	edit = open(path2, 'w')
	edit.write('flag')
	print("flag")
	edit.close()

new_flag.close()
