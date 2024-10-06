# Indexsierung, Slicing, unterstuetzen verschiedene Datentypel
# feste Datensaetze zB. Koordinaten

meine_liste = [1, 2, 3, 4]
mein_tuple = (1, 2, 3, 4)

# Index haben beide - 0,1,2 bei Null beginnend Achtung immer eckige Klammer
print(meine_liste[1])
print(mein_tuple[2])

# Slicing herausschneiden 1-> Index 3-> bis 3 oder 4
print(meine_liste[1:4])
print(mein_tuple[1:3]) 

# Unterschied: Listen sind Veraenderlich, Tuples nicht!!!!!!!

meine_liste[0] = 100

print(meine_liste)

# Tuple nicht moeglich

# append anhaengen Liste ja Tuple nein

meine_liste.append(5)
print(meine_liste)
