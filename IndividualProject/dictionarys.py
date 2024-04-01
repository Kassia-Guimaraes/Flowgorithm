dayPlanes = int(input("Quantas aeronoaves têm no dia? "))
arrayPlanes = []
compPlane = []
destination = []
numberPlane = []
timePlane = []

for i in range(0, dayPlanes):
    compPlane.append(input("Qual a companhia aérea da aeronave " + str(i+1) + " ? "))
    destination.append(input("Qual o destino do voo? "))
    numberPlane.append(input("Qual o número do voo? "))
    timePlane.append(input("Qual a hora do voo? "))
    planes = {"Companhia Aerea": compPlane, "Destino": destination, "Numero Voo":numberPlane, "Hora do Voo":timePlane}
    arrayPlanes.append(planes)

for planes in arrayPlanes:
    print(planes)

info = input()
for x in range(0, len(planes["Companhia Aerea"])):
    if info == planes["Companhia Aerea"][x]:
        newInfo = []
        for key in planes:
            newInfo.append(planes[key][x]) 
        print(newInfo)