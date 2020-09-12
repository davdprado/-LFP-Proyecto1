# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from AFD import listaAutomatas
from Gramar import listaGramatica

def hacerpdf(nombre):
    w,h=A4
    c=canvas.Canvas(nombre+".pdf",pagesize=A4)
    c.drawString(50, 50, "El automata: "+nombre)
    c.drawString(50, h - 50,nombre)
    x = 120
    y = h - 45
    c.line(x, y, x + 100, y)
    contador=710
    for automata in listaAutomatas:
        if nombre==automata.Nombre:
            c.drawString(50,750, "--Alfabeto: "+str(automata.Alfabeto))
            c.drawString(50,730,"--Estados: ")
            for estado in automata.ListaEstados:
                if estado.Inicial and estado.Aceptacion:
                    c.drawString(50,contador,'----'+estado.Nombre+' INICIAL Y ACEPTACION')
                    contador=contador-20
                elif estado.Inicial or estado.Aceptacion:
                    if estado.Aceptacion:
                        c.drawString(50,contador,'----'+estado.Nombre+' ACEPTACION')
                        contador=contador-20
                    elif estado.Inicial:
                        c.drawString(50,contador,'----'+estado.Nombre+' INICIAL')
                        contador=contador-20
                else:
                    c.drawString(50,contador,'----'+estado.Nombre)
                    contador=contador-20
            c.drawString(50,contador,'--Transiciones: ')
            contador=contador-20
            for tr in automata.ListaTransciciones:
                c.drawString(50,contador,"----De "+tr.EstadoInicial+" a "+tr.EstadoFinal+" Con "+tr.Simbolo)
                contador=contador-20
    c.drawImage(nombre+".png",150,600,width=250, height=150)
    c.save()

def hacerpdf2(nombre):
    w,h=A4
    c=canvas.Canvas(nombre+".pdf",pagesize=A4)
    c.drawString(50, 50, ": "+nombre)
    c.drawString(50, h - 50,nombre)
    x = 120
    y = h - 45
    c.line(x, y, x + 100, y)
    contador=660
    for gramatica in listaGramatica:
        if nombre==gramatica.Nombre:
            c.drawString(50,700,"-"+gramatica.Nombre)
            c.drawString(50,680,"---Terminales"+str(gramatica.ListaTerminales))
            c.drawString(50,660,"Producciones: -------------------")
            contador=contador-20
            for nt in gramatica.ListaNoTerminales:
                c.drawString(50,contador,nt.Nombre)
                contador=contador-20
                for produc in nt.Producciones:
                    c.drawString(50,contador,"-->"+produc)
                    contador=contador-20
            for nt in gramatica.ListaNoTerminales:
                if nt.Inicial and nt.Aceptacion:
                    c.drawString(50,contador,'----'+nt.Nombre+' INICIAL Y ACEPTACION')
                    contador=contador-20
                elif nt.Inicial or nt.Aceptacion:
                    if nt.Aceptacion:
                        c.drawString(50,contador,'----'+nt.Nombre+' ACEPTACION')
                        contador=contador-20
                    elif nt.Inicial:
                        c.drawString(50,contador,'----'+nt.Nombre+' INICIAL')
                        contador=contador-20
    c.drawImage(nombre+".png",250,450,width=250, height=150)
    c.save()
