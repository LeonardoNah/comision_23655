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
        print(f"""
        NOMBRE={self.nombre}
        EDAD = {self.edad}
        TITULAR ={self.mayor_edad()}    
            """)
        
persona1=Persona("Paula",42)
persona1.mostrar()