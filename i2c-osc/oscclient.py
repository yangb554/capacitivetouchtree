"""
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import smbus
import time


from pythonosc import osc_message_builder
from pythonosc import udp_client

bus = smbus.SMBus(1)
address = 0x04

if __name__ == "__main__":

  client = udp_client.UDPClient("128.237.116.203", 12345)

  while True:

    msg = osc_message_builder.OscMessageBuilder(address = "/video")

    i2cread = bus.read_byte(address)
    #print i2cread
    
    sendvalue = 0
    if i2cread > 70
      sendvalue = 1

    msg.add_arg(sendvalue)
    msg = msg.build()
    client.send(msg)
    time.sleep(0.1) 




while True:

