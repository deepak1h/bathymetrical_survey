import bathymetry.bathymetry_data as bathymetry
from threading import *
import time


data = "00.00.00,00.0000,00.0000,00,00,00"
location = [00.0000, 00.0000]
collect = False
time_update = ""


def collect_data():
    global collect
    collect = True


class Project(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__project = bathymetry.BathymetryData()


    def run(self):
        
        global data
        global location
        global collect
        global time_update
        self.__project.start()

        while True:

            if collect:

                data = self.__project.data()
                collect = False

            location = self.__project.lat_long()
            time_update = time.time()


project = Project()