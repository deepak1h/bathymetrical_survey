import data as project
from threading import *
import time


class Log(Thread):

    def __init__(self):

        Thread.__init__(self)
        self.__log_name = "/home/pi/Desktop/bathymetrical_survey/log/" + time.asctime().replace(":", "-") + ".txt"
        self.__old_time = 0.00
        self.__new_time = 0.00
        self.__log_file = open(self.__log_name, "w")
        self.__log_file.close()

    def run(self):

        while True:

            self.__new_time = project.time_update

            if self.__new_time > self.__old_time:

                self.__log_file = open(self.__log_name, "a")
                self.__old_time = self.__new_time
                print("log updated")
                self.__log_file.write(time.asctime().split()[3]+","+str(project.location)+"\n")
                self.__log_file.close()
                time.sleep(1)

            else:

                pass


log = Log()
