import main as project
from threading import *
import time


class log(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.__log_name = "/home/pi/Desktop/bathymetry_project/log/" + time.asctime() + ".txt"
        self.__old_time = []
        self.__new_time = []


    def run(self):
        while True:
            self.__new_time = project.time_update_log
            if self.__new_time > self.__old_time:
                self.__log_file = open(self.__log_name, "a+")
                self.__old_time = self.__new_time
                self.__log_file.write(time.asctime().split()[3]+","+str(project.location))
                self.__log_file.close()
            else:
                pass
