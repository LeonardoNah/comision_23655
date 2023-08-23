"""while True:
    try:
        opcion = int(input("ingrese una opcion"))
        if opcion == 1 or opcion == 2:
            break
        else:
            print("OPCION INCORRECTA")
    except:
        print("ERROR; INGRESO LETRA")
"""
"""
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def mayor_edad(self):
        if self.edad > 18:
            return  "SI"
        else:
            return  "No"
            
    def mostrar(self):
        print(f"
NOMBRE={self.nombre}
EDAD = {self.edad}
TITULAR ={self.mayor_edad()}    
            ")
        
persona1=Persona("Paula",42)
persona1.mostrar()
"""

class Empleado : 
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    @property
    def nombre_Completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def salario(self):
        pass
    
em1=Empleado("Nahuel","Roldan")
print(em1.nombre_Completo)
em1.nombre = "Gaston"
print(em1.nombre_Completo)