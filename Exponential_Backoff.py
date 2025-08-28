# this scenerio come when you clicked on button but server not responding correctly 
# then it help to take to increase the waiting time when traffic too much but it decrease the efficiency
# and performance of application..
import time

waiting_time=1 
max_retries=5
attempt=0

while attempt<max_retries:
    print("Attempt ", attempt+1,"-wait time ", waiting_time)
    time.sleep(waiting_time)
    waiting_time*=2
    attempt+=1


output:
Attempt  1 -wait time  1
Attempt  2 -wait time  2
Attempt  3 -wait time  4
Attempt  4 -wait time  8
Attempt  5 -wait time  16
