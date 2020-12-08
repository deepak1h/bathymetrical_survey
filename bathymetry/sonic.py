# Libraries
import RPi.GPIO as GPIO
import time
from threading import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
depth = ""


class sonic(Thread):
    
    def __init__(self, trigger, echo):

        Thread.__init__(self)
        self.__trigger = trigger
        self.__echo = echo
        GPIO.setup(self.__trigger, GPIO.OUT)
        GPIO.setup(self.__echo, GPIO.IN)
        self.__status = 0
        self.reset()
        self.__timeout = 0.5
        self.__dist = 0
        self.__time_elapsed = 0
        self.__updated_time = 0
        self.__curr_time = ""

    def reset(self):

        self.__dist = 0
        self.__time_elapsed = 0
        self.__updated_time = 0
        self.__curr_time = ""

    def on(self):

        self.__status = True

    def off(self):

        self.__status = False

    def depth(self):

        if self.__status:

            if self.__dist > 0 and self.is_working():

                return str(self.__dist)

        else:

            print("Not working")
            return "SONICERR"

        self.__status = False

    def run(self):

        while True:

            try:

                if self.__status:

                    self.distance()

                else:

                    print("Sonic Status OFF.")

            except KeyboardInterrupt:

                print("Thread Ended.")

    def distance(self):

        GPIO.output(self.__trigger, False)
        time.sleep(0.1)
        # set Trigger to HIGH
        GPIO.output(self.__trigger, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.__trigger, False)

        start_time = time.time()
        stop_time = time.time()
        # save StartTime

        while GPIO.input(self.__echo) == 0 and time.time()-start_time < self.__timeout:

            start_time = time.time()
        # save time of arrival

        while GPIO.input(self.__echo) == 1:

            stop_time = time.time()
        # time difference between start and arrival

        self.__time_elapsed = stop_time - start_time
        
        if self.__time_elapsed < self.__timeout:

            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back

            self.__dist = round((self.__time_elapsed * 34300) / 2, 2)
            self.__updated_time = time.time()
            self.__curr_time = time.asctime().split()[3]
        
    def is_working(self):

        self.distance()
        tim = self.__updated_time
        curr_time = time.time()

        if curr_time-tim < 0.5:

            return True

        else:

            return False
