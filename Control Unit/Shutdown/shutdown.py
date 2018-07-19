#!/usr/bin/env python
#Shuts down the RPi
from subprocess import call
call("sudo nohup shutdown -h now", shell=True)
