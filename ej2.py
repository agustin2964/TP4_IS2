class laminador10m:

    def producir(self):
        print("Producida lamina de 10 metros")

class laminador5m:

    def producir(self):
        print("Producida lamina de 5 metros")

class laminadorBridge:

    def __init__(self, laminador, cantidad):
        self._laminador = laminador
        self._cantidad = cantidad
    
    def producir(self):
        for i in range(self._cantidad):
            self._laminador.producir()

laminador1 = laminadorBridge(laminador10m(), 3)
laminador1.producir()
laminador2 = laminadorBridge(laminador5m(), 2)
laminador2.producir()