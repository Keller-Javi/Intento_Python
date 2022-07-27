#Este es mi primer programa en Python
text = "world!"
num = 13
variable_bool = False

print("Hello " + text + " " + str(num) + " " + str(variable_bool)) # Hello world! 13

# Cuando no se imprime solo una variable es necesario hacerla un string para imprimirla con str(variable)
print(variable_bool) # 13
print(num + len(text)) # 19
print(str(num) + str(len(text))) # 136

print("Las dos primeras letras del texto son: " + text[0:2]) # wo
print("La palabra tiene " + str(len(text)) + " carácteres")

lista_de_numeros_primos = [1, 2, 3, 5, 7, 11, 13]
lista_random = [1, "Pedro", 13, 'Juan', True] # Las listas no necesitan ser del mismo tipo de dato

print("Esta es una lista: " + str(lista_random))
