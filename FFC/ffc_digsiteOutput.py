import os

text = open("FFC Digsites.txt", "wt")
text.close()
text = open("FFC Digsites.txt", "at")
for root, dirs, files in os.walk("m/bin"):
    for file in files:
        if (file == "0.bin"):
            f = open(os.path.join(root, file), "rb")
            r = f.read()
            f.close()
            point = int.from_bytes(r[0x6C:0x70], "little")
            mapN = os.path.join(root, file).split("\\")[-2]
            f = open("ffc_kasekiNames.txt", "rt")
            vivoNames = list(f.read().split("\n")).copy()
            f.close()
            realP = [ int.from_bytes(r[point:(point + 4)], "little") ]
            loc = point + 4
            while (realP[-1] > 0):
                realP.append(int.from_bytes(r[loc:(loc + 4)], "little"))
                loc = loc + 4
            realP = realP[0:-1]
            check = 0
            for val in realP:
                index = int.from_bytes(r[(val + 2):(val + 4)], "little")
                if (index == 0):
                    continue
                else:
                    if (check == 0):
                        check = 1
                        text.write(mapN + ":\n")
                text.write("Zone " + str(index).zfill(2) + ":\n")
                # maxFos = int.from_bytes(r[(val + 12):(val + 16)], "little")
                # text.write("\tMax Spawns: " + str(maxFos) + "\n")
                numTables = int.from_bytes(r[(val + 12):(val + 16)], "little")
                point3 = int.from_bytes(r[(val + 16):(val + 20)], "little")
                for i in range(numTables):
                    text.write("\tFossil Chip " + str(i) + ":\n")
                    point4 = int.from_bytes(r[(val + point3 + (i * 4)):(val + point3 + (i * 4) + 4)], "little")
                    point5 = int.from_bytes(r[(val + point4 + 12):(val + point4 + 16)], "little")
                    numWeird = int.from_bytes(r[(val + point4 + point5 + 8):(val + point4 + point5 + 12)], "little")
                    numSpawns = int.from_bytes(r[(val + point4 + point5 + 16):(val + point4 + point5 + 20)], "little")
                    startSpawns = val + point4 + point5 + 24 + (numWeird * 2)
                    for j in range(numSpawns):
                        thisStart = startSpawns + (j * 8)
                        vivoNum = int.from_bytes(r[(thisStart + 2):(thisStart + 4)], "little")
                        # chance = int.from_bytes(r[(val + point4 + 4):(val + point4 + 8)], "little")
                        text.write("\t\t" + "[0x" + hex(thisStart + 2).upper()[2:] + "] " + vivoNames[vivoNum] + "\n")
            if (check == 1):
                text.write("\n")
text.close()
                
                