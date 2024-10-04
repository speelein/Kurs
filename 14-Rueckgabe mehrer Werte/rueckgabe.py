def berechne(a, b):
    summe = a +b
    differenz = a - b
    return summe, differenz

ergebnis = berechne(10, 5)
print(ergebnis)


summe, differenz = berechne(10, 5)
print("Summe ", summe)
print("Differenz ", differenz)

def finde_extreme(zahlen):                  # mit Liste
    return [min(zahlen), max(zahlen)]

extreme = finde_extreme([1, 2, 3, 4, 5, 8, 12, 7])
print(extreme)

def analysiere(zahlen):                     # mit dictionary
    return {
        'minimum' : min(zahlen),
        'maximum' : max(zahlen),
        'durchschnitt' :sum(zahlen)/len(zahlen)
    }

ergebnis = analysiere([1, 2, 3, 4, 5, 12])
print(ergebnis)