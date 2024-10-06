# Listenkompression Comprehanchen

# [ ausdruck for item in iterable if bedingung ]


quadrate = [x**2 for x in range(5)]
print(quadrate)

gerade_zahlen = [x for x in range(10) if x %2 == 0]
print(gerade_zahlen)

# verschachtelte Schleifen

kombinationen = [ (a, b) for a in [1, 2, 3] for b in [4, 5, 6] if a % 2 == 0 and b % 2 == 0]
print(kombinationen)