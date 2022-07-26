#Este es mi primer programa en Python
text = "world!"
num = 13

print("Hello " + text + " " + str(num)) # Hello world! 13

print(num) # 13
print(num + len(text)) # 19
print(str(num) + str(len(text))) # 136

print("Las dos primeras letras del texto son: " + text[0:2]) # wo
print("La palabra tiene " + str(len(text)) + " carácteres")