import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

h=int(time.strftime("%H"))

m=int(time.strftime("%M"))

s=int(time.strftime("%S"))

if (h>=0 and h<=5 and m<=59 and s<=59):
    print("Good Night")

elif (h>=6 and h<=11 and m<=59 and s<=59):
    print("Good morning")

elif (h>=12 and h<=17 and m<=59 and s<=59):
    print("Good Afternoon")

elif (h>18 and h<=23 and m<=59 and s<=59):
     print("Good Evening")
