import time
# create a countdown timer


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,-1,-1):
    seconds = int (x % 60)
    minutes = int(x//60) % 60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}",end=" ",flush=True)
print()
print("Times up Buddy.")




sec = int(input("Enter the countdown Number you like: "))

for counter in range(sec,0,-1):
    time.sleep(1)
    print(f"{counter}")
print()
print("Happy New Year!!")
