#!/usr/bin/env python

# flag.py turns the alarm off. It
# does this by editing the database
# file, pausing, then editing it back 

import time

# Path to database
path = '/home/pi/Alarm/dataBase.txt'

# Edits database to turn off alarm
new_flag = open(path, 'a')
new_flag.write('flag')
#print('flag')
new_flag.close()

# Pause ******Must be long enough to interrupt the loop in backup.py
time.sleep(6)

# Edits database back, re-arming system
fix = open(path, 'w')
fix.write('no')
fix.close()


