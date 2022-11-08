#3.	Elabore un programa POO, en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular con estos dos valores la suma, resta, multiplicación y división. Utilizar un método para cada una de las operaciones e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
class calculadora:

    def __init__(self):
        self.valor1=int(input("Ingrese un numero:"))
        self.valor2=int(input("Ingrese un numero: "))

    def sumar(self):
        su=self.valor1+self.valor2
        print("El resultado de suma es: ",su)

    def restar(self):
        re=self.valor1-self.valor2
        print("El resultado de resta es: ",re)

    def multiplicar(self):
        pro=self.valor1*self.valor2
        print("El resultado de multiplicacion es",pro)

    def division(self):
        divi=self.valor1/self.valor2
        print("El resultado de division2",divi)


# bloque principal

operacion1=calculadora()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.division()