import serial
import time
from threading import *


class Gps(Thread):

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
        self.__nmea_time = []
        self.__satellite = "0"
        self.__curr_time = "00.00.00"

    def reset(self):

        self.__received_data = "SERIALERR"
        self.__info = "$GNGGA,"
        self.__buffer = 0
        self.__nmea_lat = 0
        self.__nmea_long = 0
        self.__locked = 0
        self.__lat_in_degree = 0
        self.__long_in_degree = 0
        self.__location = []
        self.__nmea_time = []
        self.__satellite = "0"
        self.__curr_time = "00.00.00"

    def satellite(self):
        
        return self.__satellite

    def locked(self):

        if self.__locked:

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
                        # print(self.__NMEA_buff)
                        return True

            finally:

                pass

    def lock(self):

        print("GPS locking...")

        while True:

            try:

                self.get_data()
                # print(self.__NMEA_buff)
                self.__locked = int(self.__NMEA_buff[5])
                # print(type(self.__locked),self.__locked)

                if self.locked():

                    print("locked")
                    break

            except IndexError:

                print("INDEXERR")

            except ValueError:

                print("VALUEERR")

    def __update_data(self):

        # print(self.__NMEA_buff)
        self.reset()
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

            self.get_data()
            self.__update_data()
            self.__gps_info()

    def __gps_info(self):

        if self.locked():

            self.__lat_in_degree = self.__convert_to_degrees(self.__nmea_lat)
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
        time.sleep(0.5)
        tim2 = self.__nmea_time
        # print(tim,tim2)

        if tim2 > tim:

            return True

        else:

            return False

    def location(self):

        if self.locked():

            self.__location = [str(self.__curr_time),
                               str(self.__lat_in_degree),
                               str(self.__long_in_degree),
                               str(self.__locked),
                               str(self.__satellite)]
            return self.__location

        else:

            return["00.00.00", "0.0000", "0.0000", "0", "00"]

    def lat_long(self):

        return [self.__lat_in_degree, self.__long_in_degree]
