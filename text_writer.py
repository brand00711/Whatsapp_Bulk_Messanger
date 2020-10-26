import datetime 
  
# date in yyyy/mm/dd format 
d1 = datetime.datetime(2020, 8, 19)
d2 = datetime.datetime.now()

if d2>=d1:
    print("Exceeded Time")