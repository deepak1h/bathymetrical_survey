import data as project
from threading import *
import time

file_name = ""


class Csv(Thread):

    def __init__(self):

        Thread.__init__(self)
        global file_name
        self.__csv_name = "/home/pi/Desktop/bathymetrical_survey/csv/" + time.asctime().replace(":", "-") + ".csv"
        self.__old_data = "00.00.00,00.0000,00.0000,00,00,00"
        self.__new_data = "00.00.00,00.0000,00.0000,00,00,00"
        self.__csv_file = open(self.__csv_name, "w")
        file_name = self.__csv_name
        self.__csv_file.close()

    def run(self):

        while True:
            
            self.__new_data = project.data
            # print(project.collect, self.__new_data)

            if not self.__new_data == self.__old_data:
                
                self.__old_data = self.__new_data
                data = self.__new_data.split(",")
                print(data)
                
                if data[0] != "GPSLCKERR":
                    
                    print("CSV UPDATED.")
                    data = ",".join([data[0], data[1], data[2], data[-1]])
                    self.__csv_file = open(self.__csv_name, "a")
                    self.__csv_file.write(data+"\n")
                    self.__csv_file.close()
                    
                else:
                    
                    print("GPSLCKERR")
                    
                time.sleep(0.2)
            
            else:

                pass
            
            time.sleep(0.2)


csv = Csv()
