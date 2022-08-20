import hello

print("\n\n")
print("Esta es la lista de hello: " + str(hello.lista_random))

x = int (input("Ingrese un numero: "))

if x < 0:
    print ("El número es negativo")
elif x == 0:
    print ("Es cero")
elif x == 1:
    print ("Simples")
else:
    print ("No se ")

for v in hello.lista_random:
    print (v)


print("\n\n\n")

# Create a sample collection
users = {
    'Hans': 'active',
 'Éléonore': 'inactive',
  '景太郎': 'active'}

print (users)

print("\n\n\n")

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print (active_users)

for i in range(5):
    print (i)

for i in range(len(hello.lista_random)):
    print (i, hello.lista_random[i])

var = sum (range(0,10,3)) # range(0, 10, 3) = [0, 3, 6, 9] y sum (range(0,10,3)) = 0 + 3 + 6 + 9

