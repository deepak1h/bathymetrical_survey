import sonic
import gps
import time
from threading import *


class bathymetry_data(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__gps = gps.gps();
        self.__sonic = sonic.sonic(18,23);
        self.__gps.start()
        self.__sonic.start()

    def reset(self):
        self.__depth = "00"
        self.__location = "00.0000,00.0000";
        self.__time = "00.00.00";
        self.__data = []
        self.__lat_long = []

    def depth(self):
        self.__depth = self.__sonic.depth()

    def location(self):
        if self.__gps.is_working():
            self.__location = self.__gps.location()
        else:
            self.__location == "GPSERR"

    def data(self):
        self.reset()
        self.depth()
        self.location()
        self.__location.append(self.__depth)
        return ",".join(self.__location)

    def run(self):
        while True:
            self.__lat_long = self.__gps.lat_long()

    def lat_long(self):
        return self.__lat_long