import serial
from pythonosc import osc_message_builder
from pythonosc import udp_client
import argparse
import time

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)

while True:
    #port.write("\r\nSay something:")
    rcv = port.readline(10)
    print(rcv)
    
    #port.write("\r\nYou sent:" + repr(rcv))
