# -*- coding: utf-8 -*-
import os
from Automata import Estado
from Automata import Transcicion
from Automata import Automata

listaAutomatas = list()

    


def verificarExistencia(lista,objeto):
    for ob in lista:
        if ob.Nombre==objeto:
            return True

def Existe(lista,objeto):
    for ob in lista:
        if ob==objeto:
            return True

def ElimiarInicial(lista):
    for ob in lista:
        if ob.Inicial:
            ob.Inicial=False

def ExisteTransicion(lista,inicial,simbolo,final):
    for element in lista:
        if ((element.EstadoInicial==inicial and element.Simbolo==simbolo) and element.EstadoFinal==final) or element.Simbolo=='':
            return True


def MenuA():
    nombreAuto = str(input("Ingrese el nombre del Automata: "))
    os.system("cls")
    op = 0
    listaEstados = list()
    alfabeto = list()
    listaTrans = list()
    while op!= 7:
        os.system('cls')
        print("################## MENU AFD ##################")
        print("################ "+nombreAuto+" ################")
        print("(1) Ingresar Estados")
        print("(2) Ingresar alfabeto")
        print("(3) Estado Inicial")
        print("(4) Estados de Aceptacion")
        print("(5) Transiciones")
        print("(6) Ayuda")
        print("(7) Salir")
        op = int(input("####################Seleccione su opcion: "))
        if op==1:
            os.system('cls')
            seguir=''
            while seguir!='N':
                stdo=""
                stdo = str(input("Ingrese Estado: "))
                if verificarExistencia(listaEstados,stdo):
                    print("El estado "+stdo+" ya existe")
                else:
                    NuevoEstado = Estado(stdo)
                    listaEstados.append(NuevoEstado)
                seguir = str(input("¿Contunuar?(S/N): "))
            for estado in listaEstados:
                print(estado.Nombre) #Eliminar linea
        elif op==2:
            os.system('cls')
            se=' '
            while se!='':
                se=""
                se= str(input("Ingrese caracter: "))
                if Existe(alfabeto,se):
                    print(se+" ya existe en el alfabeto")
                else:
                    alfabeto.append(se)
            alfabeto.pop()
            for letra in alfabeto:
                print(letra) #Elimiar
        elif op==3:
            os.system('cls')
            print("Escoja Estado Inicial")
            estdo = str(input("Nombre: "))
            if verificarExistencia(listaEstados,estdo):
                ElimiarInicial(listaEstados)
                for estado in listaEstados:
                    if estado.Nombre==estdo:
                        estado.Inicial=True
            else:
                print(estdo+" no existe")
            for estado in listaEstados:
                if estado.Inicial:
                    print("El estado inicial es "+estado.Nombre)
        elif op==4:
            os.system('cls')
            ace=' '
            print("Escriba los estados de aceptacion")
            while ace!='':
                ace = str(input("Nombre del Estado: "))
                if verificarExistencia(listaEstados,ace):
                    for estado in listaEstados:
                        if estado.Nombre==ace:
                            estado.Aceptacion=True
                else:
                    print(ace+" no existe")
                    for estado in listaEstados:
                        if estado.Aceptacion:
                            print(estado.Nombre+" Aceptacion")
        elif op==5:
            os.system('cls')
            print("-----------Tansiciones----------")
            print("Formato: Eo,Ef;Simbolo")
            entrada=' '
            while entrada!='':
                entrada = str(input("Ingrese la transicion: "))
                transi = entrada.replace(';',',')
                transi = transi.split(',')
                if transi[0]=='':
                    break
                if ExisteTransicion(listaTrans,transi[0],transi[2],transi[1]):
                    print("No es posible hacer la transcicion")
                else:
                    NuevaTransicion = Transcicion(transi[0],transi[1],transi[2])
                    listaTrans.append(NuevaTransicion)
                for tr in listaTrans:
                    print("De "+tr.EstadoInicial+" a "+tr.EstadoFinal+" Con "+tr.Simbolo)
        elif op==7:
            print("Desea Guardar los cambios?")
            guardar = str(input("(S/N)/(s/n): "))
            if guardar=='s' or guardar=='S':
                NuevoAutomata = Automata(nombreAuto,listaEstados,listaTrans,alfabeto)
                listaAutomatas.append(NuevoAutomata)


def esEA(state,nombreAuto):
    for automata in listaAutomatas:
        for estado in automata.ListaEstados:
            if state==estado.Nombre:
                if estado.Aceptacion:
                    return True




def valAuto(cadena,nombreAuto):
    state=""
    for automata in listaAutomatas:
        if automata.Nombre==nombreAuto:
            for estado in automata.ListaEstados:
                if estado.Inicial:
                    state=estado.Nombre
    for automata in listaAutomatas:
        if automata.Nombre==nombreAuto:
            for letra in cadena:
                for tr in automata.ListaTransciciones:
                    if (tr.EstadoInicial==tr.EstadoFinal) and (tr.EstadoInicial==state):
                        if letra==tr.Simbolo:
                            state=tr.EstadoFinal
                            break
                    if state==tr.EstadoInicial:
                        if tr.Simbolo==letra:
                            state=tr.EstadoFinal
                            break
    if esEA(state,nombreAuto):
        return "valida"
    else:
        return "no valida"

def RutaAFD(cadena,nombreAuto):
    print("Ruta AFD: ",end="")
    state=""
    for automata in listaAutomatas:
        if automata.Nombre==nombreAuto:
            for estado in automata.ListaEstados:
                if estado.Inicial:
                    state=estado.Nombre
    for automata in listaAutomatas:
        if automata.Nombre==nombreAuto:
            for letra in cadena:
                for tr in automata.ListaTransciciones:
                    if (tr.EstadoInicial==tr.EstadoFinal) and (tr.EstadoInicial==state):
                        if letra==tr.Simbolo:
                            print(tr.EstadoInicial+","+tr.EstadoFinal+";"+tr.Simbolo+" ",end="")
                            state=tr.EstadoFinal
                            break
                    if state==tr.EstadoInicial:
                        if tr.Simbolo==letra:
                            print(tr.EstadoInicial+","+tr.EstadoFinal+";"+tr.Simbolo+" ",end="")
                            state=tr.EstadoFinal
                            break
    print(valAuto(cadena,nombreAuto))


def EvaluarCadena(cadena,nombreAuto):
    validar=True
    if validar:
        return valAuto(cadena,nombreAuto)
    else:
        return"No se encuentra en el alfabeto"
            


def esVerdadero(palabra):
    if palabra=='true':
        return True
    else:
        return False

def cargarArchivo(nombre):
    os.system('cls')
    ruta=nombre+".afd"
    arch=open(ruta,'r')
    lectura = arch.read()
    #lectura=lectura.replace(';',',')
    arch.close()
    lectura = lectura.split('\n')
    listaEstados = list()
    alfabeto = list()
    listaTrans = list()
    auxiliar=""
    auxiliarAcep=""
    for trans in lectura:
        print(trans)
        trans=trans.replace(';',',')
        trans=trans.split(',')
        print(trans)
        auxiliar=trans[0]
        auxiliarAcep=esVerdadero(trans[3])
        print(auxiliar+"  ...")
        break
    NuevoEstado = Estado(auxiliar)
    listaEstados.append(NuevoEstado)
    for state in listaEstados:
        if auxiliar==state.Nombre:
            state.Aceptacion=auxiliarAcep
            break
    for state in listaEstados:
        if auxiliar==state.Nombre:
            state.Inicial=True
            break
    for trans in lectura:
        print(trans)
        trans=trans.replace(';',',')
        trans=trans.split(',')
        if ExisteTransicion(listaTrans,trans[0],trans[2],trans[1]) or trans[0]=='':
            print("No es posible hacer la transcicion")
        else:
            NuevaTransicion = Transcicion(trans[0],trans[1],trans[2])
            listaTrans.append(NuevaTransicion)
        """for tr in listaTrans:
            print("De "+tr.EstadoInicial+" a "+tr.EstadoFinal+" Con "+tr.Simbolo)"""
        if verificarExistencia(listaEstados,trans[0]):
            print("El estado "+trans[0]+" ya existe")
        else:
            NuevoEstado = Estado(trans[0])
            listaEstados.append(NuevoEstado)
    for trans in lectura:
        print(trans)
        trans=trans.replace(';',',')
        trans=trans.split(',')
        if Existe(alfabeto,trans[2]):
            print("ya exisste"+trans[2])
        else:
            alfabeto.append(trans[2])
    for trans in lectura:
        print(trans)
        trans=trans.replace(';',',')
        trans=trans.split(',')
        if verificarExistencia(listaEstados,trans[1]):
            print("El estado "+trans[1]+" ya existe")
        else:
            NuevoEstado = Estado(trans[1])
            listaEstados.append(NuevoEstado)
    for trans in lectura:
        trans=trans.replace(';',',')
        trans=trans.split(',')
        for stado in listaEstados:
            if trans[0]==stado.Nombre:
                stado.Aceptacion=esVerdadero(trans[3])
            elif trans[1]==stado.Nombre:
                stado.Aceptacion=esVerdadero(trans[4])
            else:
                continue
    print("alfabeto-----------")
    print(str(alfabeto))
    NuevoAutomata = Automata(nombre,listaEstados,listaTrans,alfabeto)
    listaAutomatas.append(NuevoAutomata)

