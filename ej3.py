class composite_element():

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def mostrar(self, indent=0):
        print(' ' * indent + self.name)
        for child in self.children:
            child.mostrar((indent + 4))

class leaf_element():

    def __init__(self, name):
        self.name = name

    def mostrar(self, indent=0):
        print(' ' * indent + self.name)

producto=composite_element("Producto")
conjunto1=composite_element("Conjunto 1")
conjunto2=composite_element("Conjunto 2")
conjunto3=composite_element("Conjunto 3")
pieza1=leaf_element("pieza1")
pieza2=leaf_element("pieza2")
pieza3=leaf_element("pieza3")
pieza4=leaf_element("pieza4")
pieza5=leaf_element("pieza5")
pieza6=leaf_element("pieza6")
pieza7=leaf_element("pieza7")
pieza8=leaf_element("pieza8")
pieza9=leaf_element("pieza9")
conjunto1.add_child(pieza1)
conjunto1.add_child(pieza2)
conjunto1.add_child(pieza3)
conjunto2.add_child(pieza4)
conjunto2.add_child(pieza5)
conjunto2.add_child(pieza6)
conjunto3.add_child(pieza7)
conjunto3.add_child(pieza8)
conjunto3.add_child(pieza9)
producto.add_child(conjunto1)
producto.add_child(conjunto2)
producto.add_child(conjunto3)
producto.mostrar()
conjunto4=composite_element("Conjunto 4")
pieza10=leaf_element("pieza10")
pieza11=leaf_element("pieza11")
pieza12=leaf_element("pieza12")
pieza13=leaf_element("pieza13")
conjunto4.add_child(pieza10)
conjunto4.add_child(pieza11)
conjunto4.add_child(pieza12)
conjunto4.add_child(pieza13)
producto.add_child(conjunto4)
print("")
producto.mostrar()