""" 7-Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos"""
"""8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta"""

# Se crea la clase Persona. Se le pide nombre,edad,dni.
class Persona :
    def __init__(self,nombre,edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
# Se crea la clase Cuenta(con titular,cantidad) y se hereda de Persona(nombre,edad,dni)
class Cuenta(Persona):
    def __init__(self,nombre,edad,dni,cantidad):
        super(). __init__(nombre,edad,dni)

        self.__cantidad = cantidad
    #METODO PARA SABER SI ES MAYOR.
    def mayor_edad(self):
        if edad > 18 and edad < 25:
            return  "Si"
        else:
            return  "No"    
    #METODO PARA MOSTRAR
    def Mostrar(self):
        return print(f"""
                    NOMBRE:{nombre}
                    EDAD:{edad}
                    DNI:{dni}
                    TITULAR:{self.mayor_edad()}
                    CANTIDAD:{cantidad}""")
    #METODO INGRESAR PLATA
    def IngresarSaldo(self,ingreso):
        self.__ingreso= ingreso
        self.__cantidad = self.__cantidad + self.__ingreso
        return print(f"SALDO ACTUAL: {self.__cantidad}")
    #METODO SACAR PLATA
    def Retirar(self,retirar):
        if retirar > cantidad:
            return print("Saldo insuficiente")
        else:
            self.__retirar = retirar
            self.__cantidad = self.__cantidad - self.__retirar
            return print(f"SALDO ACTUAL: {self.__cantidad}")

while True:
    print("--------BIENVENIDO A SU BANCO PERSONAL-------")
    #VALIDACION DE OPCION
    while True:
        try:
            opcion  = int(input("Ingrese una opcion:\n[1]-Ingresar Usuario.\n[2]-Salir.\n-->"))
            if opcion == 1 or opcion == 2:
                break
            else:
                print("-"*10,"OPCION INCORRECTA" ,"-"*10)
        except ValueError:
            print("-"*10,"ERROR. INGRESO SE INGRESO UNA LETRA","-"*10,"\nVuelva a ingresar Opcion")
#SALIDA DEL PROGRAMA SEGUN OPCION
    if opcion == 2 :
        break
    else:
        #SOLICITUD DE DATOS
        nombre= input("Ingrese su nombre--> ")
        edad= int(input("Ingrese su edad--> "))
        dni= input("Ingrese su dni--> ")
        cantidad = int(input("Ingrese cantidad de dinero--> "))
        cuenta_1=Cuenta(nombre,edad,dni,cantidad)
        cuenta_1.Mostrar()
        if cuenta_1.mayor_edad() == "Si":
            
            while True :
                try:
                    opcion = int(input("INGRESE UNA OPCION:\n[1]-INGRESAR DINERO \n[2]-RETIRAR DINERO\n-->"))
                    if opcion == 1 or opcion == 2:
                        break
                    else:
                        print("-"*10,"OPCION INCORRECTA" ,"-"*10)
                except ValueError:
                    print("\nERROR. INGRESO INCORRECTO\nVuelva a ingresar Opcion")
                    
            if opcion == 1 :
                ingreso = int(input("INGRESE EL MONTO A INGRESAR--> "))
                cuenta_1.IngresarSaldo(ingreso)
            elif opcion == 2 : 
                retirar = int(input("INGRESE EL MONTO A RETIRAR-->"))
                cuenta_1.Retirar(retirar)
        else:
            print("No puede retirar plata\nNo cuenta con el tipo de titularidad.")
    while True:
        try:
            opcion=int(input("DESEA REALIZAR OTRA OPERACION?\n[1]SI\n[2]NO\n-->"))
            if opcion == 1 or opcion == 2:
                break
            print("-"*10,"OPCION INCORRECTA" ,"-"*10)
        except ValueError:
            print("\nERROR. INGRESO INCORRECTO\nVuelva a ingresar Opcion")
    if opcion == 2:
        break
            
            
    
print("::::::::::GRACIAS POR UTILIZAR EL PROGRAMA::::::::")

