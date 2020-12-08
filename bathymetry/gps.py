import serial
import time
from threading import *

class gps(Thread):

    def __init__(self):

        Thread.__init__(self)
        self.reset()
        self.__ser = serial.Serial("/dev/ttyS0", 38400, timeout=0.5)               # Open port with baud rate
        self.__NMEA_buff = []
        self.__received_data = "SERIALERR"
        self.__info = "$GNGGA,"
        self.__buffer = 0
        self.__nmea_lat = 0
        self.__nmea_long = 0
        self.__lat_in_degree = 0
        self.__long_in_degree = 0
        self.__locked = 0
        self.__location = []
        self.__status = False
        self.__nmea_time = []
        self.__satellite = "0"
        self.__curr_time = "00.00.00"

    def reset(self):

        self.__received_data = "SERIALERR"
        self.__info = "$GNGGA,"
        self.__buffer = 0
        self.__nmea_lat = 0
        self.__nmea_long = 0
        self.__lat_in_degree = 0
        self.__long_in_degree = 0
        self.__locked = 0
        self.__location = []
        self.__status = False
        self.__nmea_time = []
        self.__satellite = "0"
        self.__curr_time = "00.00.00"

    def status(self):

        return str(self.__status)

    def satellite(self):

        return self.__satellite

    def locked(self):

        if self.__locked > 0:

            return True

        else:

            return False

    def get_data(self):
        while True:

            try:
                self.__received_data = str(self.__ser.readline())
                data_available = self.__received_data.find(self.__info)
                
                if data_available > 0:
                    self.__buffer = self.__received_data.split("$GNGGA,", 1)[1]
                    # print(self.__buffer)
                    if len(self.__buffer) < 50:
                        print("booting")
                        self.reset()
                        self.get_data()
                    else:
                        self.__NMEA_buff = (self.__buffer.split(','))
                        break
            finally:
                pass

    def lock(self):

        print("GPS locking....")
        while True:
            try:
                self.get_data()
                # print(self.__NMEA_buff)
                self.__locked = int(self.__NMEA_buff[5])
                if self.locked():
                    break
            except IndexError:
                print("INDEXERR")
            except ValueError:
                print("VALUEERR")
        print("locked")

    def __update_data(self):

        self.__nmea_time = self.__NMEA_buff[0]
        self.__nmea_lat = float(self.__NMEA_buff[1])
        self.__nmea_long = float(self.__NMEA_buff[3])
        self.__locked = int(self.__NMEA_buff[5])
        self.__satellite = int(self.__NMEA_buff[6])
        self.__NMEA_buff = []
        self.__curr_time = time.asctime().split()[3]

    def run(self):

        self.lock()
        while True:
            self.reset()
            self.get_data()
            self.__update_data()
            self.__GPS_Info()

    def __GPS_Info(self):

        if self.locked():           
            self.__lat_in_degrees = self.__convert_to_degrees(self.__nmea_lat)
            self.__long_in_degree = self.__convert_to_degrees(self.__nmea_long)
        else:
            self.__lat_in_degree = "NODATA"
            self.__long_in_degree = "NODATA"
            
    def __convert_to_degrees(self, raw_value):

        decimal_value = raw_value/100.00
        degrees = int(decimal_value)
        mm_mmmm = (decimal_value - int(decimal_value))/0.6
        position = degrees + mm_mmmm
        position = "%.6f" % position
        return str(position)

    def is_working(self):
        
        tim = self.__nmea_time
        time.sleep(0.2)
        tim2 = self.__nmea_time
        if tim2 > tim:
            return True
        else:
            return False

    def location(self):
        self.__location = [self.__curr_time,
                           self.__long_in_degree,
                           self.__long_in_degree,
                           self.__locked,
                           self.__satellite]
        return self.__location

    def lat_long(self):
        return [self.__lat_in_degree, self.__long_in_degree]
