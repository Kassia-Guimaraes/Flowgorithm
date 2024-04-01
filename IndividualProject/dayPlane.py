def infoPlanes():
    informationPlane = [""] * (4)

    print("Qual a companhia aérea do voo?")
    informationPlane[0] = input()
    print("Qual o destino do voo?")
    informationPlane[1] = input()
    print("Qual o número do voo?")
    informationPlane[2] = input()
    hourPlane()
    infoFlight = informationPlane[0] + ", " + informationPlane[1] + ", " + informationPlane[2] + ", " + informationPlane[3]
    
    return infoFlight

# Main
columns = 1
print("Quantas aeronoves têm no dia?")
lines = int(input())
airPlanes = [""] * (lines * columns)

for i in range(0, lines - 1 + 1, 1):
    airPlanes[i] = infoPlanes()
print("As aeronaves do dia são:")
for i in range(0, lines - 1 + 1, 1):
    print(airPlanes[i])
