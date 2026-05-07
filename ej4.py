class numeros:
    
    num1=0
    num2=0
    num3=0
    num4=0
    
    def calcular(self, num):
        self.num1=num
        self.num2=num+2
        self.num3=num*2
        self.num4=num/3
    
    def mostrar(self):
        print(f"Numero 1: {self.num1}")
        print(f"Numero 2: {self.num2}")
        print(f"Numero 3: {self.num3}")
        print(f"Numero 4: {self.num4}")

class chetoWrapper:

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def mostrar(self):
        print(f"numero chetardo1: {self._wrapped.num1}<----")
        print(f"numero chetardo2: {self._wrapped.num2}<----")
        print(f"numero chetardo3: {self._wrapped.num3}<----")
        print(f"numero chetardo4: {self._wrapped.num4}<----")

num= numeros()
num.calcular(9)
num.mostrar()
print()
cheto=chetoWrapper(num)
cheto.mostrar()