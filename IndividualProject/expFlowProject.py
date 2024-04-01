def hourMax(namePassenger, hour, minute):
    # Definição da hora máxima para passageiro ir para a fila da segurança
    # Hora mínima definida sendo 30 minutos antes do horário do voo
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
    # Definição da hora mínima para passageiro ir para a fila da segurança. Definida como 2 horas antes do horário do voo
    if hour == 0 or hour == 0:
        hour = 24
    else:
        if hour == 1 or hour == 1:
            hour = 25
    if minute < 30:
        print("Pode se apresentar na fila para a segurança a partir das " + str(hour - 2) + ":00")
    else:
        print("Pode se apresentar na fila para a segurança a partir das " + str(hour - 2) + ":30")

def infoPlanes():
    # Informações do voo do dia no aeroporto, número de aeronaves pré-definida pelo funcionário
    informationPlane = [""] * (4)

    print("Qual a companhia aérea do voo?")
    informationPlane[0] = input()
    print("Qual o destino do voo?")
    informationPlane[1] = input()
    print("Qual o número do voo?")
    informationPlane[2] = input()
    print("Qual o horário do voo?")
    informationPlane[3] = input()

    # Declaração de variável com as informções do voo, sendo o return da função
    infoFlight = informationPlane[0] + ", " + informationPlane[1] + ", " + informationPlane[2] + ", " + informationPlane[3]
    
    return infoFlight

def namePassengerFunc():
    # Função com condicional para declaração do nome do passageiro
    print("Digite seu nome")
    namePassenger = input()

    # Número mínimo de caracteres para aceitar o nome do passageiro como válido
    while len(namePassenger) < 2:
        print("Nome inválido, por favor digite seu nome novamente")
        namePassenger = input()
    print("Olá, " + namePassenger + "! Estou aqui para ajudar você a se organizar para seu voo.")
    
    return namePassenger

def numberofintances(hourPlane, splitOn):
    # número de vezes que a função split deve rodar para conseguir seprar a hora, sendo a condição para o split ":"
    qty = 1
    for count in range(0, len(hourPlane) - 1 + 1, 1):

        # enquanto a variável alocada posição da hora do voo for diferente da condição do split (:), deve separar os elementos, entre xx:yy
        if hourPlane[count] == splitOn:

            # quando chega na posição em que o split (:) é declarado, faz a soma da contagem das instancias
            qty = qty + 1
    
    return qty

def numberPlaneFunc():
    # Função com condicional para declaração do número do voo
    print("Qual o número do voo? (ex: 14E26)")
    numberPlane = input()

    # pré-difinição do número de caracteres para o número do voo
    while len(numberPlane) != 5:
        print("Número de voo inválido, o número do voo deve conter 5 caracteres. Por favor digite novamente o número do voo (ex: 14E26)")
        numberPlane = input()
    
    return numberPlane

def passaportNumberFunc():
    # Função com condicional para declaração do número do passaporte
    print("Digite o número de identificação do seu passaporte. (ex: AB123456)")
    passaportNumber = input()

    # O número de identificação do passaporte deve conter 8 caracteres
    while len(passaportNumber) != 8:
        print("Valor inválido, o número do passaporte deve conter 2 letras seguido de 6 números. Por favor insira o número de seu passaporte novamente")
        passaportNumber = input()
    
    return passaportNumber

def slice(hourPlane, sliceOn, numberofitems, slicedList):
    counter = 0
    while counter != numberofitems:

        # enquanto o contador for diferente do número de instâncias
        slicedList[counter] = ""
        for count in range(0, len(hourPlane) - 1 + 1, 1):
            if hourPlane[count] == sliceOn:

                # quando, na contagem de elementos chegar no split (:) vai pular 1 casa, sem contar o ":" como importante para o resultado
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

    # Pega a parte da hora, separado pelo slice, e aloca numa variável para dar como retorno da função
    h1 = int(slicedList[0])
    
    return h1

def splitMinPlane(hourPlane):
    splitOn = ":"
    numberofitems = numberofintances(hourPlane, splitOn)
    slicedList = [""] * (numberofitems)

    slice(hourPlane, splitOn, numberofitems, slicedList)

    # Pega a parte do minuto, separado pelo slice, e aloca numa variável para dar como retorno da função
    min1 = int(slicedList[1])
    
    return min1

def timePlaneFunc():
    # Função com condicional para declaração do horário do voo
    print("Qual o horário do seu voo? (ex: 13:40)")
    timePlane = input()

    # Número mínimo de caracteres para aceitar como horário do voo
    while len(timePlane) != 5:
        print("Hora inválida, por favor digite novamente o horário de seu voo. (ex: 00:20)")
        timePlane = input()
    
    return timePlane

# Main
print("Para começarmos, digite sua password")
password = input()
capacityRoom = 10

# password fictícia para identificação de funcionário no Menu
if password == "employee123":

    # Área do funcionário
    print("Bem-vindo a área do funcionário.")
    print("Quantas aeronoves têm no dia?")
    lines = int(input())
    airPlanes = [""] * (lines)

    for i in range(0, lines - 1 + 1, 1):

        # Repetição para alocação de informações de voo em cada linha do Array
        airPlanes[i] = infoPlanes()
    print("As aeronaves do dia são:")
    for i in range(0, lines - 1 + 1, 1):

        # Output de todas as aeronaves do dia
        print(airPlanes[i])
else:

    # Área do passageiro
    print("Bem-vindo(a) a área do passageiro.")

    # contador para rodar o for
    counter = 0
    for i in range(0, capacityRoom - 1 + 1, 1):
        print("Deseja realizar check-in?" + chr(13) + "1 -> Sim" + chr(13) + "2 -> Não")
        checkin = int(input())
        if checkin == 1:

            # declaração de variáveis com funções para imputs da identificação do passageiro, contendo condições condições
            namePassenger = namePassengerFunc()
            identPassenger = passaportNumberFunc()
            hourPlane = timePlaneFunc()
            numberPlane = numberPlaneFunc()

            # Separação da hora e minuto
            hour = splitHourPlane(hourPlane)
            minute = splitMinPlane(hourPlane)
            hourMin(namePassenger, hour, minute)
            hourMax(namePassenger, hour, minute)
            print("Para passar pela segurança deve ter em mãos o seu passaporte, como documento de identificação e o número do voo. Faça uma boa viagem e até a próxima!")
            counter = counter + 1
        else:
            i = capacityRoom - 1
    percentCapacity = float(counter * 100) / capacityRoom
    print(str(counter) + " pessoas realizaram o check-in na fila, do total de " + str(capacityRoom) + ". A capacidade do salão de espera está em cerca de " + str(percentCapacity) + "% de passageiros realizou check-in")
