import os

def crearImagen(nombre):
    print("probando")
    comando="dot -Tpng imagen.dot -o "+nombre+".png"
    print(os.system(comando))
