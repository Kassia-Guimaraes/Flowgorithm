vertNumber = int(input("How many areas does your business have?"))
verts = dict()
for x in range(0, vertNumber):
    verts[input("select a distinct are of your business\n")] = dict()

for key in verts:
    for j in range(0,4):
        verts[key][j] = int(input(str(key)+ "\"s profit in trimester" + str(j+1) + "\n"))
        print(verts[key])
        print("\n")

bestVert = {"area": "",
            "profit": 0}

for key in verts: 
    print(key)
    vertTotal = 0 
    for j in range(0,4):
        print(verts[key][j])
        vertTotal = vertTotal + int(verts[key][j])
        if vertTotal > bestVert["profit"]:
            bestVert["area"] = key
            bestVert["profit"] = vertTotal
print("the most profitable area was " + str(bestVert["area"] + " with a total profit of " + str(bestVert["profit"])))