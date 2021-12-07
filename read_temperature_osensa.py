from osensapy import osensapy
import time
from datetime import datetime
import numpy as np

print("ports: ", osensapy.serial_get_portlist())

transmitter = osensapy.Transmitter("/dev/ttyUSB0", 247)
print("serial no: ", transmitter.read_serial_number())
print("device id: ",transmitter.read_device_id())

start_time = time.time()
elapsed_time = 0
while elapsed_time <= 200:
    temp = transmitter.fast_single("A")[1]
    elapsed_time = time.time() - start_time
    print([temp, elapsed_time])
    time.sleep(0.01)

transmitter.close()