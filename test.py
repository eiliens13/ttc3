class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad        
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print(f"Soy un {self.especie} del tipo", type(self).__name__)


class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño

    def mostrar(self):
        print(f"El dueño de este {self.especie} es {self.dueño}")

    def describeme(self):
        return super().describeme()

#
# m = Animal('mamifero', '2')
# m.describeme()

n = Perro("mamifero","3","Daily")
n.mostrar()