f = open("Config.txt", "r")
lines = f.readlines()
for line in lines:
    #print(line)
    if("ValidatorID") in line:
        ValidatorID = line.split("=")[1].strip()
        print(ValidatorID)
    if("Discord_Web_Hock") in line:
        Discord_Web_Hock  = line.split("=")[1].strip()
        print(Discord_Web_Hock)
