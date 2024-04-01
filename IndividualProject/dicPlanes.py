#dayPlanes = int(input("Quantas aeronoaves têm no dia? "))
arrayPlanes = []
compPlane = ["Tap1", "Tap2"]
destination = ["pt to fr", "pt to br"]
numberPlane = ["1234fr5", "175gt55"]
timePlane = ["13:30", "00:50"]

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