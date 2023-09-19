import glob
import os

newFile = open("FFC Teams.txt", "wt")
newFile.close()
newFile = open("FFC Teams.txt", "at")
names = open("ffc_vivoNames.txt", "rt").read()
enemyNamesF = list(open("ffc_enemyNames.txt", "rt").read().split("\n"))

order = []
for file in glob.glob("./battle_param/bin/**/0.bin", recursive = True):
    order.append(file.split("_")[-1].split(".")[0][0:-2].zfill(4))
order.sort()
for file in order:
    data = open("./battle_param/bin/battle_param_defs_" + str(int(file)) + "/0.bin", "rb")
    full = data.read()
    shift = full[0x38] + 2 - 0x46
    nameID = full[0x46 + shift] - 0x4D
    reading = full[(112 + shift):]
    newFile.write("\n" + file + ":" + "\n")

    newFile.close()
    newFile = open("FFC Teams.txt", "ab")   
    text = "Name: " + enemyNamesF[nameID - 1] + " (" + str(nameID).zfill(2) + ")\n"
    newFile.write(text.encode("UTF-8", errors = "ignore"))
    newFile.close()
    newFile = open("FFC Teams.txt", "at")
    
    maxi = full[0x58 + shift]
    for i in range(maxi):
        vivo = int.from_bytes(reading[(i * 12):(i * 12 + 2)], "little")
        level = int.from_bytes(reading[(i * 12 + 2):(i * 12 + 4)], "little")
        superF = int.from_bytes(reading[(i * 12 + 6):(i * 12 + 8)], "little")
        sfTable = { "0": "None", "900": "Silver Head", "901": "Silver Body", "902": "Silver Arms", "903": "Silver Legs", "904": "Gold" }
        newFile.write(names.split("\n")[vivo - 1] + ": Level = " + str(level) + ", Super Fossil = " + str(sfTable[str(superF)]))
        newFile.write("\n")
    data.close()
    