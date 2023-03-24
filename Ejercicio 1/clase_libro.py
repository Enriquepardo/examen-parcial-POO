
# se define una clase libro con sus atributos y metodos

class Libro:
    def __init__(self, titulo, autor, genero, año, num_paginas, editorial):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.num_paginas = num_paginas
        self.editorial = editorial

    def descripcion(self):
        print('El libro {} fue escrito por {} en el año {} y tiene {} paginas'.format(self.titulo, self.autor, self.año, self.num_paginas))

    

libro_1 = Libro('El principito', 'Antoine de Saint-Exupéry', 'Infantil', 1943, 96, 'Salamandra')

libro_1.descripcion()
