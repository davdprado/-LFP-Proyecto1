
class Estado():
    def __init__(self,nombre):
        self.Nombre=nombre
        self.Inicial=False
        self.Aceptacion=False


class Transcicion():
    def __init__(self,Eo,Ef,s):
        self.EstadoInicial=Eo
        self.EstadoFinal=Ef
        self.Simbolo=s

class Automata():
    def __init__(self,nombre,estado,transicion,alfabeto):
        self.Nombre=nombre
        self.ListaEstados=estado
        self.Alfabeto=alfabeto
        self.ListaTransciciones=transicion