def hourMax(namePassenger, hour, minute):
    if minute < 30:
        if hour < 1: 
            hour = 24
        hourMaximum = hour -1
        valueMinute = 30 + minute
        print("A hora máxima que deve ser apresentar à fila da segurança é às " + str(hour-1) +":"+ str(valueMinute))
    else: 
        valueMinute = minute - 30
        print("A hora máxima que deve ser apresentar à fila da segurança é às " + str(hour) +":"+ str(valueMinute))
    return

def hourMin(namePassenger, hour, minute):
    if hour == 0:
        hour = 24
    else:
        if hour == 1:
            hour == 25
    
    if minute < 30:
        print(namePassenger + ", pode ser apresentar á fila da segurança a partir de " + str(hour-2) + ":00")
    else:
        print(namePassenger + ", pode ser apresentar á fila da segurança a partir de " + str(hour-2) + ":30")
    return

print("Digite seu nome")
namePassenger = input()
print("Olá, "+ namePassenger + ". Estou aqui para ajudar você a se organizar para o seu voo. \nDigite o número de identificação do seu passaporte")
identPassenger = input()
print("Qual o horário do seu voo?")
timePlane = input()
time = timePlane.split(":")
hour = int(time[0])
minute = int(time[1])
print("Qual o número do voo?")
numberPlane = input()
hourMin(namePassenger, hour, minute)
hourMax(namePassenger, hour, minute)