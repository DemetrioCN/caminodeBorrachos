import random


# Clase para generar distintos tipos de borrachos
class Borracho:
    
    def __init__(self, nombre):
        self.nombre = nombre


# El borracho tradicional se mueve en 4 posibles direcciones
# con igualdad de probabilidad [derecha, izquierda, arriba, abajo]
class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])


