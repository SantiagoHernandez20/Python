#2.	Realizar un programa POO que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Ingresar por teclado. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la calificación y si ha aprobado o no. Nota >=3 aprobó
class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=input("Ingrese su nombre: ")
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Su Nota es: ",self.nota)

    def mostrar_estado(self):
        if self.nota>=3:
            print("Aprobo")
        else:
            print("No aprobo")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("",4)
alumno1.imprimir()
alumno1.mostrar_estado()

