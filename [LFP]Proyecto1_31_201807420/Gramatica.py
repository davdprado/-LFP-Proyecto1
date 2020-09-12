class NoTerminal:
    def __init__(self,nombre):
        self.Nombre=nombre
        self.Inicial=False
        self.Aceptacion=False
        self.Producciones=[]


class Gramatica:
    def __init__(self,nombre,terminales,nterminales):
        self.Nombre=nombre
        self.ListaTerminales=terminales
        self.ListaNoTerminales=nterminales