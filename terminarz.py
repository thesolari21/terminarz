# Terminarz

# Zaimportuj plik .txt z drużynami
# Wymieszaj
# Ustal harmonogram 'kazdy z kazdym'
# Wypluj wyniki w .txt

import random

path = "teams.txt"
f =open(path, "r", encoding="utf-8")

teams = []

for line in f:
    line = line.strip("\n")
    teams.append(line)

for i in range(5):
    random.shuffle(teams)
    print(teams)




