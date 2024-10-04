zahlen = [1,2,3,4,5]
for zahl in zahlen:  # alle die zutreffen
    print(zahl)

i = 1               # while solange bis
while i <= 5:
    print(i)
    i += 1

for zahl in zahlen:
    if zahl == 3:
        continue
    print(zahl)

    if zahl == 4:
        break

for i in range(1, 3):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}") # wird in ..... erklaert, im Bereich von...