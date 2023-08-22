# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia)

palabra = ""
cadena = "HOLA COMO ESTAS "
for i in cadena:
    if i == " ":
        print(palabra)
        palabra = ""
        continue
    
    palabra = palabra + i
        
    
print(palabra)
cont=0
if palabra in cadena:
    cont += 1 
    
print(cont)