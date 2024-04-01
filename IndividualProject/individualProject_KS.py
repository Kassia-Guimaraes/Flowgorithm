def infoPlanes(i):
    # Informações do voo do dia no aeroporto, número de aeronaves pré-definida pelo funcionário
    informationPlane = [""] * (4)

    print("Qual a companhia aérea do voo " ,(i+1),"?")
    informationPlane[0] = input()
    print("Qual o destino do voo",(i+1),"?")
    informationPlane[1] = input()
    print("Qual o número do voo " ,(i+1),"?")
    informationPlane[2] = input()
    print("Qual o horário do voo " ,(i+1),"?")
    informationPlane[3] = input()

    # Declaração de variável com as informções do voo, sendo o return da função
    infoFlight = informationPlane[0] + ", " + informationPlane[1] + ", " + informationPlane[2] + ", " + informationPlane[3]
    
    return infoFlight

def hourMax(namePassenger, hour, minute):
    # Definição da hora máxima para passageiro ir para a fila da segurança
    # Hora máxima definida sendo 30 minutos antes do horário do voo
    if minute < 30:
        if hour < 1:
            hour = 24
        hourMaximum = hour - 1
        valueMinute = 30 + minute
        print("A hora máxima que deve se apresentar para a segurança é às " + str(hourMaximum) + ":" + str(valueMinute))
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
        airPlanes[i] = infoPlanes(i)
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
        print("Deseja realizar check-in?\n1 -> Sim\n2 -> Não")
        checkin = int(input())
        if checkin == 1:

            # declaração de variáveis com funções para imputs da identificação do passageiro, contendo condições condições
            namePassenger = namePassengerFunc()
            identPassenger = passaportNumberFunc()
            hourPlane = timePlaneFunc()
            numberPlane = numberPlaneFunc()

            # Separação da hora e minuto
            splitTime = hourPlane.split(":")
            hour = int(splitTime[0])
            minute = int(splitTime[1])
            hourMin(namePassenger, hour, minute)
            hourMax(namePassenger, hour, minute)
            print("Para passar pela segurança deve ter em mãos o seu passaporte, como documento de identificação e o número do voo. Faça uma boa viagem e até a próxima!")
            counter = counter + 1
        else:
            break
    percentCapacity = float(counter * 100) / capacityRoom
    print(str(counter) + " pessoas realizaram o check-in na fila, do total de " + str(capacityRoom) + ". A capacidade do salão de espera está em cerca de " + str(percentCapacity) + "% d e passageiros realizou check-in")
