import glob
import os

newFile = open("FFC Teams.txt", "wt")
newFile.close()
newFile = open("FFC Teams.txt", "at")
names = open("ffc_vivoNames.txt", "rt").read()

order = []
for file in glob.glob("./battle_param/bin/**/0.bin", recursive = True):
    order.append(file.split("_")[-1].split(".")[0][0:-2].zfill(4))
order.sort()
for file in order:
    data = open("./battle_param/bin/battle_param_defs_" + str(int(file)) + "/0.bin", "rb")
    full = data.read()
    if (full[71] == 16):
        shift = 0
        nameID = full[0x46] - 0x4D
    else:
        shift = full[0x6C] + 4
        nameID = full[0x46 + shift] - 0x4D
    reading = full[(112 + shift):]
    newFile.write("\n" + file + ":" + "\n")

    newFile.close()
    newFile = open("FFC Teams.txt", "ab")   
    for root, dirs, files in os.walk("./bin/text_battle_enemy_name/enemyNameFiles"):
        for file2 in files:
            if (int(file2[0:2]) == nameID):
                nameF = open("./bin/text_battle_enemy_name/enemyNameFiles/" + file2, "rb")
                text = "Name: " + nameF.read().decode("UTF-8", errors = "ignore").replace("\0", "") + " (" + str(nameID).zfill(2) + ")\n"
                newFile.write(text.encode("UTF-8", errors = "ignore"))
                nameF.close()
    newFile.close()
    newFile = open("FFC Teams.txt", "at")
    
    maxi = full[0x58]
    for i in range(maxi):
        vivo = int.from_bytes(reading[(i * 12):(i * 12 + 2)], "little")
        level = int.from_bytes(reading[(i * 12 + 2):(i * 12 + 4)], "little")
        superF = int.from_bytes(reading[(i * 12 + 6):(i * 12 + 8)], "little")
        sfTable = { "0": "None", "900": "Silver Head", "901": "Silver Body", "902": "Silver Arms", "903": "Silver Legs", "904": "Gold" }
        newFile.write(names.split("\n")[vivo - 1] + ": Level = " + str(level) + ", Super Fossil = " + str(sfTable[str(superF)]))
        newFile.write("\n")
    data.close()
    