from data import *
from csv import csv
from log import log
from upload import server
import time
from tkinter import *

project.start()
log.start()
csv.start()
server.start()
server.start_upload()

window = Tk()

b1 = Button(window,text = "Take Data", command = collect_data)

b1.pack

window.mainloop()






