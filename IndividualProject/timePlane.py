def hourMax(namePassenger, hour, minute):
    if minute < 30:
        if hour < 1:
            hour = 24
        hourMaximum = hour - 1
        valueMinute = 30 + minute
        print("A hora máxima que deve se apresentar para a segurança é às " + str(fabs(hourMaximum)) + ":" + str(valueMinute))
    else:
        valueMinute = minute - 30
        print("A hora máxima que deve se apresentar para a segurança é às " + str(hour) + ":" + str(valueMinute))

def hourMin(namePassenger, hour, minute):
    if hour == 0 or hour == 0:
        hour = 24
    else:
        if hour == 1 or hour == 1:
            hour = 25
    if minute < 30:
        print(namePassenger + ", pode se apresentar na fila para a segurança a partir das " + str(hour - 2) + ":00")
    else:
        print(namePassenger + ", pode se apresentar na fila para a segurança a partir das " + str(hour - 2) + ":30")

def numberofintances(hourPlane, item):
    qty = 1
    for count in range(0, len(hourPlane) - 1 + 1, 1):
        if hourPlane[count] == item:
            qty = qty + 1
    
    return qty

def slice(hourPlane, sliceOn, numberofitems, slicedList):
    counter = 0
    while counter != numberofitems:
        slicedList[counter] = ""
        for count in range(0, len(hourPlane) - 1 + 1, 1):
            if hourPlane[count] == sliceOn:
                counter = counter + 1
                slicedList[counter] = ""
            else:
                slicedList[counter] = slicedList[counter] + hourPlane[count]
        counter = counter + 1

def splitHourPlane(hourPlane):
    splitOn = ":"
    numberofitems = numberofintances(hourPlane, splitOn)
    slicedList = [""] * (numberofitems)

    slice(hourPlane, splitOn, numberofitems, slicedList)
    h1 = int(slicedList[0])
    
    return h1

def splitMinPlane(hourPlane):
    splitOn = ":"
    numberofitems = numberofintances(hourPlane, splitOn)
    slicedList = [""] * (numberofitems)

    slice(hourPlane, splitOn, numberofitems, slicedList)
    min1 = int(slicedList[1])
    
    return min1

# Main
print("Digite seu nome")
namePassenger = input()
print("Olá, " + namePassenger + "! Estou aqui para ajudar você a se organizar para seu voo.")
print("Digite o número de identificação do seu passaporte")
identPassenger = input()
print("Qual o horário do seu voo?")
hourPlane = input()
print("Qual o número do voo?")
numberPlane = str(input())
hour = splitHourPlane(hourPlane)
minute = splitMinPlane(hourPlane)
hourMin(namePassenger, hour, minute)
hourMax(namePassenger, hour, minute)
print(namePassenger + ", para passar pela segurança deve ter em mãos o seu passaporte, como documento de identificação e o número do voo. Faça uma boa viagem e até a próxima!")
