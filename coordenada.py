# Abstraccion de donde se encuentra nuestro borracho en
# el plano


class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Movemos al borracho aleatoriamente y su coordenada se actualiza
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    # Calcula distancia entre dos puntos
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5


