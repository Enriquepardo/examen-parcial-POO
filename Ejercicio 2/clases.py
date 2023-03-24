

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre 

    def comer(self):
        print('El animal come')


class Mamifero(Animal):
    def __init__(self, nombre, pelo):
        super().__init__(nombre)
        self.pelo = pelo

    def amamantar(self):
        print('El animal amamanta')
  

class Oviparo(Animal):
    def __init__(self, nombre, huevos):
        super().__init__(nombre)
        self.huevos = huevos

    def poner_huevos(self):
        print('El animal pone huevos')


# la clase gato heredaria de mamifero
# la clase pollo heredaria de oviparo
# la clase ornitorrnco heredaria de mamifero y oviparo

class Ornitorrinco(Mamifero, Oviparo):
    def __init__(self, nombre, pelo, huevos, pico):
        super().__init__(nombre, pelo)
        self.pico = pico

    def nadar(self):
        print('El ornitorrinco nada')

