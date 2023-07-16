from cryptography.fernet import Fernet
from encryption import cipher, encrypt


global_password = None
people = list()

f = open("data.txt", "r")

#decrypt the data
data = f.read()
data = cipher.decrypt(data.encode()).decode()

#read the data
for line in data.split("\n"):
    if not line:
        continue
    if(line[0] == "#"):
        info = line[1:].split(" ")
        info = [" ".join(info[:-3]), info[-3], info[-2], info[-1]]
        if(len(info) >= 4):
            people.append(tuple(info))
        else:
            print("Error: invalid line in data.txt file")
            continue
    if(line[0] == "p"):
        global_password = line[1:]

#encrypt the data

f.close()

