import main as project
from threading import *
import time
import re
import urllib3
import json



class Csv(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.__csv_name = "/home/pi/Desktop/bathymetry_project/csv/" + time.asctime() + ".csv"
        self.__old_data = "00,00,00,00"
        self.__new_data = "00,00,00,00"

    def put(self):
        http = urllib3.PoolManager()

        r = http.request('GET',
                         "https://deepakhome.000webhostapp.com/updateacp.php?lat={}&lon={}&ele={}&dep={}".format(lat,long,ele,)                                                                                                      dep))
        data = r.data.decode('utf-8')

    def run(self):
        while True:
            self.__new_data = project.data
            if self.__new_data == self.__old_data:
                self.__csv_file = open(self.__csv_name,"a+")
                self.__old_data = self.__new_data
                self.__csv_file.write(self.__new_data)
                self.__csv_file.close()
            else:
                pass
