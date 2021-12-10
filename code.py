import os
import time

Hours = float(input("Set The Time in hours ->  "))  
seconds = time.time() - (Hours*60*60*1000) 
def main():     
     if seconds <= Hours*60*60*1000:
        print("Do Your Homework")
while (True) :
  main()
