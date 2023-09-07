import glob
import os

newFile = open("FF1 Teams.txt", "wt")
newFile.close()
newFile = open("FF1 Teams.txt", "at")
names = open("ff1_vivoNames.txt", "rt").read()

for file in glob.glob("./battle/bin/**/0.bin", recursive = True):
    data = open(file, "rb")
    full = data.read()
    nameID = int.from_bytes(full[100:102], "little")
    reading = full[148:]
    newFile.write("\n" + file[-10:-6] + ":" + "\n")

    newFile.close()
    newFile = open("FF1 Teams.txt", "ab")   
    for root, dirs, files in os.walk("./bin/japanese/textFiles"):
        for file2 in files:
            if (int(file2[0:4]) == nameID):
                nameF = open("./bin/japanese/textFiles/" + file2, "rb")
                text = "Name: " + nameF.read().decode("UTF-8", errors = "ignore").replace("\0", "") + " (" + str(nameID) + ")\n"
                newFile.write(text.encode("UTF-8", errors = "ignore"))
                nameF.close()
    newFile.close()
    newFile = open("FF1 Teams.txt", "at")
    
    maxi = full[0x5C]
    for i in range(maxi):
        vivo = int.from_bytes(reading[(i * 12):(i * 12 + 4)], "little")
        level = int.from_bytes(reading[(i * 12 + 4):(i * 12 + 8)], "little")
        padding = int.from_bytes(reading[(i * 12 + 8):(i * 12 + 12)], "little")
        res = names.split("\n")[vivo - 1] + ": Level = " + str(level) + ", Moves = " + str(reading[20 * maxi + 4 * i])
        res = res + ", AI = " + str(int.from_bytes(reading[(12 * maxi + 4 * i):(12 * maxi + 4 * i + 4)], "little"))
        newFile.write(res)
        newFile.write("\n")
    data.close()
    