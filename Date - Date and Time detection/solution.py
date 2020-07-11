import time
seconds = time.time()	
local_time = time.ctime(seconds)
print("Local time:", local_time)
list1=local_time.split(" ")
print(f"Date: {list1[2]} {list1[1]} {list1[4]}")
print(f"Time: {list1[3]}")