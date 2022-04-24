import os
r = open('tmp.txt', 'w')
os.system("whoami >> tmp.txt")
r.close()
f = open("tmp.txt", "r")
print(f.readline())
f.close()
os.remove("tmp.txt")