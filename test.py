import main as project
import time

while True:
    project.collect_data()
    print(project.data, project.time_update_log, project.location)
    time.sleep(1)

