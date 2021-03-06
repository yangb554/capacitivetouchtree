"""
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time


from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":

  client = udp_client.UDPClient("128.237.116.203", 12345)

  while True:

    msg = osc_message_builder.OscMessageBuilder(address = "/video")

    msg.add_arg(0)
    msg = msg.build()
    client.send(msg)
    time.sleep(1)
