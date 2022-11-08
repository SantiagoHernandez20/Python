#1.	Modifique el programa POO, teniendo en cuenta: que, SI el empleado gana mas de 3600000, se le descuenta el 3,5% debe mostrar cuanto se le descuenta y cuanto es el total a ganar.



class Persona:
    def __init__(self):
        self.nombre=input("Ingrese nombre: ")
        self.edad=int(input("Ingrese edad: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: " , self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))

    def mostrar(self):
        super().mostrar()
        print("Sueldo: ", self.sueldo)
    
    #operacion
    def operacion(self):
        descuento = self.sueldo *0.35
        df = self.sueldo - descuento
        if self.sueldo > 3600000:
            print("El Destuento es: ",df)
        else:
            print()
       


 

persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.operacion()
