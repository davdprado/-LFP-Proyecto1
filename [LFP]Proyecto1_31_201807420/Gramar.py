# -*- coding: utf-8 -*-
from Gramatica import NoTerminal
from Gramatica import Gramatica
from AFD import verificarExistencia,Existe
from AFD import ElimiarInicial
import os
import AFD

listaGramatica = list()

def MenuG():
    nombreGramatica = str(input("Ingrese el nombre de la Gramatica: "))
    os.system("cls")
    op = 0
    listaNT = list()
    listaT = list()
    listaProducciones = list()
    while op!= 7:
        #os.system('cls')
        print("################## MENU GRAMATICA ##################")
        print("################ "+nombreGramatica+" ################")
        print("(1) Ingresar No Terminales")
        print("(2) Ingresar Terminales")
        print("(3) No Terminal Inicial ")
        print("(4) Producciones")
        print("(5) Mostrar Gramatica")
        print("(6) Ayuda")
        print("(7) Salir")
        op = int(input("####################Seleccione su opcion: "))
        if op==1:
            os.system('cls')
            NT=' '
            while NT!='':
                NT=""
                NT= str(input("Ingrese NT: "))
                if verificarExistencia(listaNT,NT) or Existe(listaT,NT):
                    print("El NT: "+NT+" ya existe")
                else:
                    NuevoNT = NoTerminal(NT)
                    listaNT.append(NuevoNT)
            listaNT.pop()
        elif op==2:
            os.system('cls')
            se=' '
            while se!='':
                se=""
                se= str(input("Ingrese Terminal: "))
                if Existe(listaT,se):
                    print(se+" ya existe")
                else:
                    listaT.append(se)
            listaT.pop()
        elif op==3:
            os.system('cls')
            print("Escoja NT Inicial")
            estdo = str(input("Nombre: "))
            if verificarExistencia(listaNT,estdo):
                ElimiarInicial(listaNT)
                for estado in listaNT:
                    if estado.Nombre==estdo:
                        estado.Inicial=True
            else:
                print(estdo+" no existe")
            for estado in listaNT:
                if estado.Inicial:
                    print("El estado inicial es "+estado.Nombre)
        elif op==4:
            os.system('cls')
            pr=' '
            while pr!='':
                pr = str(input("Ingrese Produccion: "))
                aux=pr
                aux=aux.split('>')
                for buscar in listaNT:
                    if buscar.Nombre==aux[0]:
                        if Existe(buscar.Producciones,aux[1]):
                            print("Ya existe esta produccion")
                        else:
                            buscar.Producciones.append(aux[1])
                for nt in listaNT:
                    for produc in nt.Producciones:
                        if produc=='epsilon':
                            nt.Aceptacion=True 
        elif op==7:
            print("Desea Guardar los cambios?")
            guardar = str(input("(S/N)/(s/n): "))
            if guardar=='s' or guardar=='S':
                NuevaGramatica = Gramatica(nombreGramatica,listaT,listaNT)
                listaGramatica.append(NuevaGramatica)




def cargarGram(nombre):
    os.system('cls')
    ruta=nombre+".grm"
    arch=open(ruta,'r')
    lectura = arch.read()
    #lectura=lectura.replace(';',',')
    arch.close()
    lectura = lectura.split('\n')
    listaNT = list()
    listaterminales = list()
    auxiliar=""
    for produccion in lectura:
        print(produccion)
        produccion=produccion.replace('>',' ')
        produccion = produccion.split(' ')
        print(produccion)
        auxiliar=produccion[0]
        print(auxiliar+"  ...")
        break
    NuevoNT = NoTerminal(auxiliar)
    listaNT.append(NuevoNT)
    for state in listaNT:
        if auxiliar==state.Nombre:
            state.Inicial=True
            break
    for terminal in lectura:
        print(terminal)
        terminal=terminal.replace('>',' ')
        terminal=terminal.split(' ')
        if AFD.verificarExistencia(listaNT,terminal[0]):
            print("ya exisste"+terminal[0])
        else:
            NuevoNT = NoTerminal(terminal[0])
            listaNT.append(NuevoNT)
            print("valor: "+terminal[1])
        if AFD.Existe(listaterminales,terminal[1]):
            print("ya exisste"+terminal[1])
        else:
            listaterminales.append(terminal[1])
    for produc in lectura:
        produc=produc.split('>')
        for buscar in listaNT:
            if produc[0]==buscar.Nombre:
                if AFD.Existe(buscar.Producciones,produc[1]):
                    print("la produccion ya existe")
                else:
                    buscar.Producciones.append(produc[1])
    print("NT--------------------")
    for nt in listaNT:
        print(nt.Nombre)
    print("Terminales--------------")
    for ter in listaterminales:
        print(ter)
    print("Producciones: -------------------")
    for nt in listaNT:
        print(nt.Nombre)
        for produc in nt.Producciones:
            print("     "+produc)
            if produc=='epsilon':
                nt.Aceptacion=True
    print("Aceptacion----------")
    for nt in listaNT:
        if nt.Aceptacion:
            print(nt.Nombre)
    NuevaGramatica = Gramatica(nombre,listaterminales,listaNT)
    listaGramatica.append(NuevaGramatica)


def AceptacionXD(nombre,nt):
    for gram in listaGramatica:
        if gram.Nombre==nombre:
            for NT in gram.ListaNoTerminales:
                if NT.Nombre==nt:
                    if NT.Aceptacion:
                        return True
                    else:
                        return False


def EvaluarCadena(cadena,nombreGramatica,rutaAFD,rutaGramatica):
    listaRuta=list()
    listaRutaG=list()
    State=""
    per=""
    for gramatica in listaGramatica:
        if nombreGramatica==gramatica.Nombre:
            for NT in gramatica.ListaNoTerminales:
                if NT.Inicial:
                    State=NT.Nombre
    for gramatica in listaGramatica:
        if nombreGramatica==gramatica.Nombre:
            for letra in cadena:
                per=per+letra
                cambia=False
                for NT in gramatica.ListaNoTerminales:
                    for produccion in NT.Producciones:
                        produccion= produccion.split(' ')
                        if produccion[0]=='epsilon':
                            continue
                        elif (State==NT.Nombre) and (NT.Nombre==produccion[1]):
                            if letra==produccion[0]:
                                listaRuta.append(State+","+produccion[1]+","+produccion[0]+"; ")
                                listaRutaG.append(State+"-->"+per+produccion[1])
                                State=produccion[1]
                                cambia=True
                                break
                        elif State==NT.Nombre:
                            if letra==produccion[0]:
                                listaRuta.append(State+","+produccion[1]+","+produccion[0]+"; ")
                                listaRutaG.append(State+"-->"+per+produccion[1]+" ")
                                State=produccion[1]
                                cambia=True
                                break
                    if cambia:
                        break
    if rutaAFD:
        print("Ruta AFD: ",end="")
        for ruta in listaRuta:
            print(str(ruta),end="")
    if rutaGramatica:
        print("Expansion Gramatica: ",end="")
        for ruta in listaRutaG:
            print(str(ruta),end="")
    if AceptacionXD(nombreGramatica,State):
        print("valida")
    else:
        print("no valida")


    