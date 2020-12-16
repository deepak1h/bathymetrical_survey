import data as project
import time


while True:
    
    project.collect_data()
    print(project.data, project.time_update, project.location)
    time.sleep(1)

