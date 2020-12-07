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
        self.__trigger = Trigger
        self.__echo = Echo
        GPIO.setup(self.__trigger, GPIO.OUT)
        GPIO.setup(self.__echo, GPIO.IN)
        self.__status = 0
        self.reset()
        self.__timeout = 0.5


    def reset(self):
        self.__dist = 0
        self.__TimeElapsed = 0
        self.__updatedtime = 0
        self.__curr_time = ""

    def on(self):
        self.__status = True;
    def off(self):
        self.__status = False

    def depth(self):
        if self.status = True
        if self.__dist > 0 and self.is_working():
            return str(self.__depth)
        else:
            print("Not working")
            return "SONICERR"
        self.__status = False


    def run(self):
        while True:
            try:
                if self.status==1:
                    self.distance()
                else:
                    print("Sonic Status OFF.")

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
        while GPIO.input(self.echo) == 0 and time.time()-StartTime<self.__timeout:
            StartTime = time.time()
                                                                # save time of arrival
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
                                                                # time difference between start and arrival
        self.TimeElapsed = StopTime - StartTime
        
        if self.__TimeElapsed < self.__timeout:                                            # multiply with the sonic speed (34300 cm/s)                                                            # and divide by 2, because there and back
            self.dist = round((self.TimeElapsed * 34300) / 2,2)
            self.updatedtime = time.time()
            self.curr_time = time.asctime().split()[3]
        
    def is_working(self):
        self.distance()
        tim = self.updatedtime
        currtime = time.time()
        if currtime-tim<0.5:
            return True
        else:
            return False