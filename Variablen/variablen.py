x = 5         # int kann beliebig lang sein, speicherbegrenzt
name = "Max" # String
x=name       
print(name)

a, b, c, = 1,2,"Max"

k= 5 # Integer
b= 5.23 # Float
l= "max" # String
global_var = 3 #gilt auch in funk ????????
# locale Variable

def glob():
    local= 4 # ich bin local
    global_var = 3
    print(local)

print(global_var)
# print(local) geht nicht
