import os

text = open("FF1 Digsites.txt", "wt")
text.close()
text = open("FF1 Digsites.txt", "at")
for root, dirs, files in os.walk("m/bin"):
    for file in files:
        if (file == "0.bin"):
            f = open(os.path.join(root, file), "rb")
            r = f.read()
            f.close()
            numTables = int.from_bytes(r[0x50:0x54], "little")
            point = int.from_bytes(r[0x54:0x58], "little")
            mapN = os.path.join(root, file).split("\\")[-2]
            mf = open("ff1_mapNames.txt", "rt")
            lines = list(mf.read().split("\n")).copy()
            for t in lines:
                if (t != ""):
                    nums = list(t.split(":")[0].replace(", ", ",").split(",")).copy()
                    for n in nums:
                        if (int(mapN.split(" [")[0]) == int(n)):
                            mapN = mapN + " [" + t.split(": ")[1] + "]"
            f = open("ff1_vivoNames.txt", "rt")
            vivoNames = [""] + list(f.read().split("\n")).copy()
            f.close()
            realP = []
            loc = point
            for i in range(numTables):
                realP.append(int.from_bytes(r[loc:(loc + 4)], "little"))
                loc = loc + 4
            check = 0
            for val in realP:
                index = int.from_bytes(r[(val + 4):(val + 8)], "little")
                if (index == 0):
                    continue
                else:
                    if (check == 0):
                        check = 1
                        text.write(mapN + ":\n")
                text.write("\tZone " + str(index).zfill(2) + ":\n")
                chip = int.from_bytes(r[(val + 8):(val + 12)], "little")
                if (chip in [0x6F, 0x70, 0x71]):
                    chip = str(chip - 0x6F)
                else:
                    chip = "0x" + hex(chip).upper()[2:]
                maxFos = int.from_bytes(r[(val + 12):(val + 16)], "little")
                text.write("\t\tFossil Chips Needed: " + chip + "\n")
                text.write("\t\tMax Spawns: " + str(maxFos) + "\n")
                numSpawns = int.from_bytes(r[(val + 0x28):(val + 0x2C)], "little")
                point3 = int.from_bytes(r[(val + 0x2C):(val + 0x30)], "little")
                for i in range(numSpawns):
                    point4 = int.from_bytes(r[(val + point3 + (i * 4)):(val + point3 + (i * 4) + 4)], "little")
                    vivoNum = int.from_bytes(r[(val + point4):(val + point4 + 4)], "little")
                    chance = int.from_bytes(r[(val + point4 + 4):(val + point4 + 8)], "little")
                    parts = [
                        int.from_bytes(r[(val + point4 + 16):(val + point4 + 20)], "little"),
                        int.from_bytes(r[(val + point4 + 20):(val + point4 + 24)], "little"),
                        int.from_bytes(r[(val + point4 + 24):(val + point4 + 28)], "little"),
                        int.from_bytes(r[(val + point4 + 28):(val + point4 + 32)], "little")
                    ]
                    s = "\t\t" + "[0x" + hex(val + point4).upper()[2:] + "] " + vivoNames[vivoNum] + ": " + str(chance) + "% "
                    s = s + "(Part 1: " + str(parts[0]) + "%, Part 2: " + str(parts[1]) + "%, Part 3: " + str(parts[2])
                    s = s + "%, Part 4: " + str(parts[3]) + "%)\n"
                    text.write(s)
            if (check == 1):
                text.write("\n")
text.close()
                
                