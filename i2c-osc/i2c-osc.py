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

sendvalue = 0
oldsendvalue = sendvalue
if __name__ == "__main__":

  client1 = udp_client.UDPClient("128.237.116.203", 12345)
  client2 = udp_client.UDPClient("KOOTEK1.WV.CC.CMU.EDU", 12345)

  while True:

    msg1 = osc_message_builder.OscMessageBuilder(address = "/video")
    msg2 = osc_message_builder.OscMessageBuilder(address = "/hello")

    i2cread = bus.read_byte(address)
    print(i2cread)
    
    oldsendvalue = sendvalue
    sendvalue = 0
    if i2cread > 70:
      sendvalue = 1

    if oldsendvalue != sendvalue:

      msg1.add_arg(sendvalue)
      msg2.add_arg(sendvalue)
      msg1 = msg1.build()
      msg2 = msg2.build()
      print('sending to video')
      client1.send(msg1)
      print('done sending to video, sending to audio')
      client2.send(msg2)
      print('done sending to audio')
      print(sendvalue)
    time.sleep(0.1) 

