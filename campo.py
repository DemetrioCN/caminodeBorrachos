
class Campo:

    def __init__(self):
        # Guarda las coodenadas de los borrachos
        self.coordenadas_de_borrachos = {}


    # Anade al borracho con las coordenadas que venga
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

 
    # Mueve al borracho en el campo 
    def mover_borracho(self, borracho):
        # Regresa el x, y del paso
        delta_x, delta_y = borracho.camina()
        
        # Obtenemos la coordenada actual
        coordenada_actual = self.coordenadas_de_borrachos[borracho]

        # Actualiza la coordenada de borracho, sumando la coordenada
        # random con el metodo mover()
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        # Guarada la nueva coordenada en el diccionario
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    # Regresa las coordenadas guardadas en el diccionario
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]


