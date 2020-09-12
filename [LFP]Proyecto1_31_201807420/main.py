# -*- coding: utf-8 -*-
import os
import AFD
import Gramar
import pdf
from AFD import listaAutomatas
from Gramar import listaGramatica
from Automata import Estado
from Automata import Transcicion
from AFD import EvaluarCadena
from probando import crearImagen

"""def evaluarCadena(cadena,listado):
    state=""
    print("la entrada es: "+cadena)
    for automata in listado:
        for estado in listado.ListaEstados:"""


def GenerarDot(nombre):
    arhivo= open('imagen.dot','w')
    arhivo.writelines('digraph '+nombre+' { \n')
    arhivo.writelines("rankdir=LR;")
    arhivo.writelines('node [shape = doublecircle];')
    for automata in listaAutomatas:
        if nombre==automata.Nombre:
            for state in automata.ListaEstados:
                if state.Aceptacion:
                    arhivo.writelines(' '+state.Nombre)
    arhivo.writelines(';\n')
    arhivo.writelines('node [shape = circle];')
    for automata in listaAutomatas:
        if nombre==automata.Nombre:
            for state in automata.ListaEstados:
                if state.Aceptacion==False:
                    arhivo.writelines(' '+state.Nombre)
    arhivo.writelines(';\n')
    arhivo.writelines('node [shape = point, color=white, fontcolor=white]; start;\n')
    arhivo.writelines('start ->')
    for automata in listaAutomatas:
        if nombre==automata.Nombre:
            for state in automata.ListaEstados:
                if state.Inicial:
                    arhivo.writelines(' '+state.Nombre)
    arhivo.writelines(';\n')
    for automata in listaAutomatas:
        if nombre==automata.Nombre:
            for tr in automata.ListaTransciciones:
                arhivo.writelines(tr.EstadoInicial+' -> '+tr.EstadoFinal+' [ label="'+tr.Simbolo+'"];\n')
    arhivo.writelines('}')
    arhivo.close()

def GenerarDotG(nombre):
    arhivo= open('imagen.dot','w')
    arhivo.writelines('digraph '+nombre+' { \n')
    arhivo.writelines("rankdir=LR;")
    arhivo.writelines('node [shape = doublecircle];')
    for gramatica in listaGramatica:
        if nombre==gramatica.Nombre:
            for NT in gramatica.ListaNoTerminales:
                if NT.Aceptacion:
                    arhivo.writelines(' '+NT.Nombre)
    arhivo.writelines(';\n')
    arhivo.writelines('node [shape = circle];')
    for gramatica in listaGramatica:
        if nombre==gramatica.Nombre:
            for NT in gramatica.ListaNoTerminales:
                if NT.Aceptacion==False:
                    arhivo.writelines(' '+NT.Nombre)
    arhivo.writelines(';\n')
    arhivo.writelines('node [shape = point, color=white, fontcolor=white]; start;\n')
    arhivo.writelines('start ->')
    for gramatica in listaGramatica:
        if nombre==gramatica.Nombre:
            for NT in gramatica.ListaNoTerminales:
                if NT.Inicial:
                    arhivo.writelines(' '+NT.Nombre)
    arhivo.writelines(';\n')
    for gramatica in listaGramatica:
        if nombre==gramatica.Nombre:
            for NT in gramatica.ListaNoTerminales:
                for produccion in NT.Producciones:
                    produccion = produccion.split(' ')
                    if produccion[0]=='epsilon':
                        continue
                    else:
                        arhivo.writelines(NT.Nombre+' -> '+produccion[1]+' [ label="'+produccion[0]+'"];\n')
    arhivo.writelines('}')
    arhivo.close()





def EscribirTF(valor):
    if valor:
        return "true"
    else:
        return "false"

def esAceptacion(lista,ob):
    for stado in lista:
        if stado.Nombre==ob:
            if stado.Aceptacion:
                return True
            else:
                return False


def crearArchivoA(nombreAFD):
    archivo = open('c://Proyecto1/Guardar/'+nombreAFD+".afd","w")
    for buscar in listaAutomatas:
        if buscar.Nombre==nombreAFD:
            for tr in buscar.ListaTransciciones:
                archivo.writelines(tr.EstadoInicial+","+tr.EstadoFinal+","+tr.Simbolo+";"+EscribirTF(esAceptacion(buscar.ListaEstados,tr.EstadoInicial))+","+EscribirTF(esAceptacion(buscar.ListaEstados,tr.EstadoFinal))+"\n")
    archivo.close()

def crearArchivoG(nombreGramatica):
    archivo=open('c://Proyecto1/Guardar/'+nombreGramatica+".grm","w")
    for buscar in listaGramatica:
        if buscar.Nombre==nombreGramatica:
            for NT in buscar.ListaNoTerminales:
                for pr in NT.Producciones:
                    archivo.writelines(NT.Nombre+">"+pr+'\n')
    archivo.close()

def MenuEva(nombre,esGramatica):
    op = 0
    os.system("cls")
    while op!= 5:
        print("################## MENU EVALUAR ##################")
        print("(1) Solo Validar")
        print("(2) Ruta en AFD")
        print("(3) Expandir Gramatica")
        print("(4) Ayuda")
        print("(5) Salir")
        op = int(input("####################Seleccione su opcion: "))
        if op==1:
            if esGramatica:
                cadena = str(input("Ingrese Cadena: "))
                Gramar.EvaluarCadena(cadena,nombre,False,False)
            else:
                cadena=str(input("Ingrese Cadena: "))
                print(AFD.EvaluarCadena(cadena,nombre))
        elif op==2:
            if esGramatica:
                cadena=str(input("Ingrese Cadena: "))
                Gramar.EvaluarCadena(cadena,nombre,True,False)
            else:
                cadena=str(input("Ingrese Cadena: "))
                AFD.RutaAFD(cadena,nombre)
        elif op==3:
            if esGramatica:
                cadena=str(input("Ingrese Cadena: "))
                Gramar.EvaluarCadena(cadena,nombre,False,True)




def Menucargar():
    op = 0
    while op!= 4:
        os.system('cls')
        print("################## MENU CARGAR ##################")
        print("(1) AFD")
        print("(2) Gramatica")
        print("(3) Ayuda")
        print("(4) Salir")
        op = int(input("####################Seleccione su opcion: "))
        if op==1:
            nombre = str(input("Nombre del archivo: "))
            try:
                AFD.cargarArchivo(nombre)
            except:
                print("Error")
        if op==2:
            nombre = str(input("Nombre del archivo: "))
            Gramar.cargarGram(nombre)


def MenuGuardar():
    op = 0
    os.system("cls")
    while op!= 2:
        print("################## MENU GUARDAR ##################")
        print("(1) Guardar")
        print("(2) Salir")
        op = int(input("####################Seleccione su opcion: "))
        if op==1:
            nombreAFD=str(input("Ingrese Nombre de Automata o Gramatica: "))
            for buscar in listaAutomatas:
                if nombreAFD==buscar.Nombre:
                    crearArchivoA(nombreAFD)
                    print("Se creo el archivo .afd")
                else:
                    print("no se encontro el automata")
            for buscar in listaGramatica:
                if nombreAFD==buscar.Nombre:
                    crearArchivoG(nombreAFD)
                    print("se creo el archivo .grm")
                else:
                    print("no existe Gramatica")


def mostrarAutomatas(listadoA):
    print("automatas:")
    for automata in listaAutomatas:
        print('-'+automata.Nombre)
        print("--Alfabeto: "+str(automata.Alfabeto))
        print("--Estados: ")
        for estado in automata.ListaEstados:
            if estado.Inicial and estado.Aceptacion:
                print('----'+estado.Nombre+' INICIAL Y ACEPTACION')
            elif estado.Inicial or estado.Aceptacion:
                if estado.Aceptacion:
                    print('----'+estado.Nombre+' ACEPTACION')
                elif estado.Inicial:
                    print('----'+estado.Nombre+' INICIAL')
            else:
                print('----'+estado.Nombre)
        print('--Transiciones: ')
        for tr in automata.ListaTransciciones:
            print("----De "+tr.EstadoInicial+" a "+tr.EstadoFinal+" Con "+tr.Simbolo)
    print("Gramaticas")
    for gramatica in listaGramatica:
        print("-"+gramatica.Nombre)
        print("---Terminales"+str(gramatica.ListaTerminales))
        print("Producciones: -------------------")
        for nt in gramatica.ListaNoTerminales:
            print(nt.Nombre)
            for produc in nt.Producciones:
                print("  "+produc)
        for nt in gramatica.ListaNoTerminales:
            if nt.Inicial and nt.Aceptacion:
                print('----'+nt.Nombre+' INICIAL Y ACEPTACION')
            elif nt.Inicial or nt.Aceptacion:
                if nt.Aceptacion:
                    print('----'+nt.Nombre+' ACEPTACION')
                elif nt.Inicial:
                    print('----'+nt.Nombre+' INICIAL')

def detalleGra(nombre):
    for gramatica in listaGramatica:
        if gramatica.Nombre==nombre:
            print("-"+gramatica.Nombre)
            print("---Terminales"+str(gramatica.ListaTerminales))
            print("Producciones: -------------------")
            for nt in gramatica.ListaNoTerminales:
                print(nt.Nombre)
                for produc in nt.Producciones:
                    print("  "+produc)
            for nt in gramatica.ListaNoTerminales:
                if nt.Inicial and nt.Aceptacion:
                    print('----'+nt.Nombre+' INICIAL Y ACEPTACION')
                elif nt.Inicial or nt.Aceptacion:
                    if nt.Aceptacion:
                        print('----'+nt.Nombre+' ACEPTACION')
                    elif nt.Inicial:
                        print('----'+nt.Nombre+' INICIAL')

    
def detalleAFD(nombre):
    for automata in listaAutomatas:
        if automata.Nombre==nombre:
            print('-'+automata.Nombre)
            print("--Alfabeto: "+str(automata.Alfabeto))
            print("--Estados: ")
            for estado in automata.ListaEstados:
                if estado.Inicial and estado.Aceptacion:
                    print('----'+estado.Nombre+' INICIAL Y ACEPTACION')
                elif estado.Inicial or estado.Aceptacion:
                    if estado.Aceptacion:
                        print('----'+estado.Nombre+' ACEPTACION')
                    elif estado.Inicial:
                        print('----'+estado.Nombre+' INICIAL')
                else:
                    print('----'+estado.Nombre)
            print('--Transiciones: ')
            for tr in automata.ListaTransciciones:
                print("----De "+tr.EstadoInicial+" a "+tr.EstadoFinal+" Con "+tr.Simbolo)


def MenucReportes():
    op = 0
    os.system("cls")
    while op!= 4:
        print("################## MENU REPORTES ##################")
        print("(1) Ver Detalle")
        print("(2) Generar Reporte")
        print("(3) Ayuda")
        print("(4) Salir")
        op = int(input("####################Seleccione su opcion: "))
        if op==1:
            nombreAFD=str(input("Ingrese Nombre de Automata o Gramatica: "))
            for buscar in listaAutomatas:
                if nombreAFD==buscar.Nombre:
                    a=""
                    while a!="s":
                        detalleAFD(nombreAFD)
                        a = str(input("Salir(s):"))
                        os.system('cls')
                else:
                    print("no se encontro el automata")
            for buscar in listaGramatica:
                if nombreAFD==buscar.Nombre:
                    a=""
                    while a!="s":
                        detalleGra(nombreAFD)
                        a = str(input("Salir(s):"))
                        os.system('cls')
                else:
                    print("no existe Gramatica")
        elif op==2:
            nombreAFD=str(input("Ingrese Nombre de Automata o Gramatica: "))
            for buscar in listaAutomatas:
                if nombreAFD==buscar.Nombre:
                    GenerarDot(nombreAFD)
                    crearImagen(nombreAFD)
                    print("Se creo el automata")
                    pdf.hacerpdf(nombreAFD)
                else:
                    print("no se encontro el automata")
            for buscar in listaGramatica:
                if nombreAFD==buscar.Nombre:
                    GenerarDotG(nombreAFD)
                    crearImagen(nombreAFD)
                    print("se creo el automata")
                    pdf.hacerpdf2(nombreAFD)
                else:
                    print("no existe Gramatica")

op=0
while op!= 7:
    os.system("cls")
    print("##################MENU REGULAR##################")
    print("(1) Crear AFD")
    print("(2) Crear Gramatica")
    print("(3) Evaluar Cadenas")
    print("(4) Reportes")
    print("(5) Cargar Archivo de Entrada")
    print("(6) Guardar")
    print("(7) Salir")
    op = int(input("####################Seleccione su opcion: "))
    if op==1:
        AFD.MenuA()
    elif op==2:
        Gramar.MenuG()
    elif op==3:
        nombre = str(input("Ingrese el nombre del Automata o Gramatica: "))
        if AFD.verificarExistencia(listaAutomatas,nombre):
            MenuEva(nombre,False)
        elif AFD.verificarExistencia(listaGramatica,nombre):
            MenuEva(nombre,True)
    elif op==4:
        MenucReportes()
    elif op==5:
        Menucargar()
    elif op==6:
        MenuGuardar()
    elif op==9:
        mostrarAutomatas(listaAutomatas)

