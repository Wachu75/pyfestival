import os
import pendulum

dt = pendulum.now()

pathToFolder = "./"

fileOut = ""
for file in os.listdir(pathToFolder):
    if file.endswith(".txt"):
        print(os.path.join("/", file))
        with open(file) as tempfile:
            line = tempfile.readline()
            print(line) # typu string
            print(line[2])
            # pominąc { na początku i na końcu a wynik dodać do fileout
            line = line.replace('{','').replace('}','').replace(' ', '')
            print(line)  # typu string
            fileOut = fileOut + "," +line
            #fileOut.removeprefix(',')
            fileOut = fileOut.lstrip(',')

temp = dt.format('DDMMYYYY', locale='pl')
file = ""+ temp + ".t" # rozszerzenie .t aby po ponownym uruchomieniu nie czytał tego pliku i nie dodawał do samego siebie

with open(file, 'w') as handler:
    handler.writelines(fileOut)

print(fileOut)

