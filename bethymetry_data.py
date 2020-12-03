import bethymetry.sonic as sonicc
import bethymetry.gps as gpss
import time
from threading import *


class bethymetry_data(Thread):

    
    def __init__(self):
        Thread.__init__(self)
        self.gps = self.gpss.gps()
        sonic = self.sonicc.sonic(18,23)
        depth = 0
        location = ""
        curr_time = "00.00.00"
        bethy_data = []
        gps_running = False
        sonic_running = False
        satellite = 0
    
    def run(self):
        
        file = open("/home/pi/Desktop/bethymetry_project/csv/"+time.asctime()+".csv","w")
        try:
            while True:
                self.start_bethymetry()
                location = gpss.get_position()
                depth = self.sonicc.distance()
                
                string = curr_time + "," + location + "," + str(depth) + "\n"
                file.write(string)
                bethy_data.append([self.curr_time,self.location,self.depth])
                
        
        except KeyboardInterrupt:
            file.close()
            
            sys.exit(0)
    
    def start_bethymetry(self):
        self.sonic.start()
        gpss.start()
        sonic.status = 1

        gps_running = gpss.is_running()
        sonic_running = sonicc.is_running()
        if gpss.locked == 1:
            if gps_running == True:
                if sonic_running == True:
                    satellite = self.gpss.satellite
                    location = self.gpss.location
                    curr_time = self.gpss.curr_time
                    depth = self.sonicc.dist
                else:
                    print("Print SONIC Error.")
            else:
                print("GPS not Running")
        else:
            print("Gps not locked.")
                    
                        
                        
                        
                        
        
        

        
        
    
        
    