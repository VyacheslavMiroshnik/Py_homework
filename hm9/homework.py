from datetime import datetime
import sys
from contextlib import contextmanager
class Time_work():
     def __init__(self,file_path,open_type = "r", encoding_type = "utf-8"):
         self.file_path = file_path
         self.file_time = open(file_path, open_type, encoding = encoding_type)
         self.start_work = datetime.now()
     def __enter__ (self):
         return self    
     def __exit__(self,exc_t, exc_val, exc_tb):
         self.end_work = datetime.now()
         self.file_time.close()    

def
@contextmanager
def Time_write(file_path):
    try:
        file = open(file_path,"a",encoding='utf-8')
        yield file
    finally:
        file.close()




with Time_work("file.txt") as f:
    print(f.start_work)
    s=0
    for i in range(1000):
       s+=i 
   