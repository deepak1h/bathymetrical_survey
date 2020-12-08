import bathymetry.bathymetry_data as bathymetry
from threading import *
import time


data = ""
location = []
collect = False
time_update_log = ""


def collect_data():
    global collect
    collect = True


class Project(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__project = bathymetry.bathymetry_data()
        self.__project.start()

    def run(self):
        global data
        global location
        global collect
        global time_update_log
        while True:
            if collect:
                data = self.__project.data()
                collect = False

            time.sleep(0.2)
            location = self.__project.lat_long()
            time_update_log = time.time()


project = Project()
project.start()
