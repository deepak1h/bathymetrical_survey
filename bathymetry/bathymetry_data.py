import bathymetry.sonic as sonic
import bathymetry.gps as gps
from threading import *


class BathymetryData(Thread):

    def __init__(self):

        Thread.__init__(self)
        self.__gps = gps.Gps()
        self.__sonic = sonic.Sonic(18, 23)
        self.__gps.start()
        self.__sonic.start()
        self.__depth = "00"
        self.__location = ["00.00.00", "0.0000,0.0000"]
        self.__time = "00.00.00"
        self.__data = ["00.00.00", "0.0000", "0.0000", "00", "00", "00"]
        self.__lat_long = []

    def reset(self):

        self.__depth = "00"
        self.__location = ["00.00.00", "0.0000", "0.0000"]
        self.__time = "00.00.00"
        self.__data = ["00.00.00", "0.0000", "0.0000", "00", "00", "00"]
        self.__lat_long = ["0.0000", "0.0000", "00","00"]

    def depth(self):
        
        self.__sonic.on()
        self.__depth = self.__sonic.depth()
        self.__sonic.off()
        return self.__depth

    def location(self):

        if not self.__gps.locked():
            
            # print(self.__gps.locked())
            self.__location = ["GPSLCKERR"]
            

        else:
            self.__location = self.__gps.location()
            

    def data(self):

        self.reset()
        self.depth()
        self.location()
        self.__location.append(self.__depth)
        return ",".join(self.__location)

    def run(self):

        while True:
            
            if self.__gps.locked():

                self.__lat_long = self.__gps.lat_long()

    def lat_long(self):

        return self.__lat_long
