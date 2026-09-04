#timer that can count backwards
import time
countto = int(input("Enter the time in seconds : "))

for y in range(countto, 0, -1):
    seconds = y % 60
    minutes = int(y / 60) % 60
    hours = int(y / 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print(" ")
print("FINISH !!")
