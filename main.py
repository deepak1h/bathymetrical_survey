from data import *
from csv import csv
from log import log
from upload import server
import time

project.start()
log.start()
csv.start()
server.start()
server.start_upload()

while True:
    time.sleep(1)
    collect_data()





