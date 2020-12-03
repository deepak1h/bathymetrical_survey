#Libraries
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from threading import *

depth = ""

class sonic(Thread):
    
    def __init__(self,Trigger,Echo):
        Thread.__init__(self)
        self.trigger = Trigger
        self.echo = Echo
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        self.dist = 0
        self.status = 0
        self.TimeElapsed = 0
        self.updatedtime = 0
        self.curr_time=""
        
        
    def run(self):
        try:
            print("Thread Started")
            while True:
                if self.status==1:
                    self.distance()
                    #print(self.dist)
                else:
                    continue
                
                
        except KeyboardInterrupt:
            print("Thread Ended.")
            
        

    def distance(self):
        GPIO.output(self.trigger,False)
        time.sleep(0.1)
        # set Trigger to HIGH
        GPIO.output(self.trigger, True)
                                                         # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)


        StartTime = time.time()
        StopTime = time.time()


                                                                # save StartTime
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
                                                                # save time of arrival
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
                                                                # time difference between start and arrival
        self.TimeElapsed = StopTime - StartTime
        
                                                    # multiply with the sonic speed (34300 cm/s)                                                            # and divide by 2, because there and back
        self.dist = round((self.TimeElapsed * 34300) / 2,2)
        global depth
        depth = ",".join([str(self.dist),self.curr_time])
        self.updatedtime = time.time()
        self.curr_time = time.asctime().split()[3]
        
    def is_working(self):
        tim = self.updatedtime
        currtime = time.time()
        if currtime-tim<1:
            return True
        else:
            return False