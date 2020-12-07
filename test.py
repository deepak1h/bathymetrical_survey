import bethymetry.sonic as sonic
import bethymetry.gps as gps
import time
from threading import *

while True:
    time.sleep(0.5)
    data = ",".join([gps.data, sonic.depth])
    print(data)