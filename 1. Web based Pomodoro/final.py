import time
import webbrowser

work_time = 25*60
rest_time = 5*60
rest_long_time = 15*60

cycle = int(input("Please enter number of cycle: "))

while cycle > 0:
    cycle -= 1
    print("Start your work")
    time.sleep(work_time)
    print("take a break")
    webbrowser.open_new('https://www.youtube.com/channel/UC-UAmJt6hHh1cX6D7zBcjPw')
    if cycle == 0:
        time.sleep(rest_long_time)