# Escribir una función que calcule el máximo común divisor entre dos números.

def mcd (a,b):
    if b == 0:
        return a 
    else:
        return mcd(b , a%b)
    
print(mcd(12,24))