import smbus
import time
bus = smbus.SMBus(1)
address = 0x04

while True:
    i2cread = bus.read_byte(address)
    print i2cread
    time.sleep(0.1)
