import os
import subprocess
import mysql.connector

tsharkCall = ['C:\\Program Files\\WireShark\\tshark.exe', '-a', 'duration:600']
tsharkOut = open('tshark.txt', 'wb')

tsharkProc = subprocess.call(tsharkCall, stdout = tsharkOut)

#Things to add to the program.
# 1: Inserting into database (in progress, still debugging)
# 2: Picking a good run time for our tshark data collection. Will need advice on that
# 3: Utilizing data to model network behavior. Probably R or some matlab sollution.
# 4: Use mathematical approach to handle blocking of ports. Probably block port 23 (telnet)