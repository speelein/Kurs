alter = 14
student = True
if alter >=18 and student:
    print("Du bist ein volljaeriger Student.")
if alter < 13 or student:
    print("Du bist entweder juenger als 13 oder ein Student.")
if not student:
    print("Du bist kein Student")
if (alter > 18 and student) or (alter < 13):
    print("Du bist entweder ein volljaeriger Student oder juenger als 13")