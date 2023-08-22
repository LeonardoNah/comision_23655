"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona :
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        return f"NOMBRE : {self.nombre}. EDAD : {self.edad}. DNI: {self.dni}"
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
    
persona1 = Persona("Carlos",5,43243243)
print(persona1.mostrar())
persona1.es_mayor_de_edad()
    
    