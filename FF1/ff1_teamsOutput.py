import glob
import os
newFile = open("Battle Files Teams.txt", "at")
names = open("ff1_vivoNames.txt", "rt").read()

for file in glob.glob("./battle/bin/**/0.bin", recursive = True):
    data = open(file, "rb")
    full = data.read()
    nameID = int.from_bytes(full[100:102], "little")
    reading = full[148:]
    newFile.write("\n" + file[-10:-6] + ":" + "\n")

    newFile.close()
    newFile = open("Battle Files Teams.txt", "ab")   
    for root, dirs, files in os.walk("./bin/japanese/textFiles"):
        for file2 in files:
            if (int(file2[0:4]) == nameID):
                nameF = open("./bin/japanese/textFiles/" + file2, "rb")
                text = "Name: " + nameF.read().decode("UTF-8", errors = "ignore").replace("\0", "\n")
                newFile.write(text.encode("UTF-8", errors = "ignore"))
                nameF.close()
    newFile.close()
    newFile = open("Battle Files Teams.txt", "at")
    
    maxi = 0
    for i in [2, 1, 0]:
        vivo = int.from_bytes(reading[(i * 12):(i * 12 + 4)], "little")
        level = int.from_bytes(reading[(i * 12 + 4):(i * 12 + 8)], "little")
        padding = int.from_bytes(reading[(i * 12 + 8):(i * 12 + 12)], "little")
        if (vivo > 0) and (vivo < 116):
            if (level > 0) and (level < 13):
                if (padding <= 2):
                    if (maxi == 0):
                        maxi = i + 1
                    finalPad = (maxi - 1) * 12 + 8
                    newFile.write(names.split("\n")[vivo - 1] + ": Level = " + str(level) + ", Moves = " + str(reading[finalPad + 4 + 8 * maxi + 4 * i]))
                    newFile.write("\n")
    data.close()
    