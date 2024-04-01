def hourMax(hour, minute):
    if minute < 30:
        if hour < 1:
            hour = 24
        valueHour = hour -1
        valueMinute = minute + 30
        print("hourMax "+ str(valueHour) + ":"+ str(valueMinute))
    else: 
        valueMinute = minute - 30
        print("hourMax "+ str(hour) + ":" + str(valueMinute)) 
    return

def hourMin(hour, minute):
    if hour == 0:
        hour = 24
    else: 
        if hour == 1:
            hour = 25
    if minute < 30:
        print("hourMin "+ str(hour-2)+ ":00")
    else:
        print("hourMin "+ str(hour-2)+ ":30")
    return

timePlane = input()
time = timePlane.split(":")
hour = int(time[0])
minute = int(time[1]) 
hourMin(hour, minute)
hourMax(hour, minute)