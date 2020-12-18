import urllib3
from threading import *
import csv
import time


class Server(Thread):

    def __init__(self):

        Thread.__init__(self)
        self.__file_name = 1
        self.__latitude = "0.0000"
        self.__longitude = "0.0000"
        self.__depth = "0.00"
        self.__time = "00,00,00"
        self.__uploading = False

    def start_upload(self):
        self.__uploading = True

    def pause_upload(self):
        self.__uploading = False

    def run(self):

        while True:

            if self.__uploading:

                try:

                    self.__file_name = "/home/pi/Desktop/bathymetrical_survey/csv/Fri Dec 18 16-20-16 2020.csv"
                    

                    with open(self.__file_name, 'r') as file:
                        
                        while True:

                            line = file.readline()
                            if line != "":

                                self.update(line)
                                self.put_data()
                                print("data")

                            else:

                                time.sleep(1)

                except IOError:
                    time.sleep(5)

    def update(self, line):

        line = line.split(",")
        self.__time, self.__latitude, self.__longitude, = line[:-1]
        self.__depth= line[-1].replace("\n","")

    def put_data(self):

        http = urllib3.PoolManager()
        
        r = http.request('GET', "https://deepakhome.000webhostapp.com/updateacp.php?Time={}&lat={}&lon={}&dep={}".format(self.__time, self.__latitude, self.__longitude, self.__depth))
        data = r.data.decode('utf-8')
        r.close()

        if data=="\nsuccess":
            print("true")
            return True

        else:
            time.sleep(1)
            print("Retrying_upload")
            self.put_data()
            
    
s = Server()