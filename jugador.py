from random import randrange
from tkinter import END

import graficador


class Jugador:
    arregloDados = {}

    def __init__(self, nombre, color, fichas, GanoJugador=False, UltimaFicha=None):

        self.nombre = nombre
        self.color = color
        self.fichas = fichas
        self.UltimaFicha = UltimaFicha
        self.GanoJugador = False
        self.Posicion=0



    def DefinirUltimaFicha(self, jugadorActual, Ficha):  # Cada jugador tendra una ultima ficha
        self.UltimaFicha = Ficha # Busca indice de la lista de fichas


    def TirarUnDado(self,desa, caja_entrada_dados, L_DADOS1, L_DADOS2, Panel):  # Para saber quien empieza
        x = 0
        mod = 3

        if not desa:
            caja_entrada_dados.config(state="normal")
            caja_entrada_dados.delete(0, END)
            caja_entrada_dados.insert(0, "%s presione continuar" % self.nombre)
            caja_entrada_dados.config(state="readonly")
            inp = ""
            while inp == "":
                inp = self.obtenerDadosIngresados(caja_entrada_dados)
            x = randrange(1, 7)
            Panel.update()

        if mod > 1:
            L_DADOS1.config(image=Jugador.arregloDados[x], bg="red")
            L_DADOS1.img = Jugador.arregloDados[x]
            L_DADOS2.config(image=None, bg="white")
            Panel.update()  # Actualizar la interfaz gráfica

        return x

    def TirarDosDados(self,desa, caja_entrada_dados, L_DADOS1, L_DADOS2, Panel):
        x = 0
        y = 0
        mod = 3
        if not desa:
                caja_entrada_dados.config(state="normal")
                caja_entrada_dados.delete(0,END)
                caja_entrada_dados.insert(0,"%s presione continuar"%self.nombre)
                caja_entrada_dados.config(state="readonly")
                inp=""
                texto_ingresado=""
                while inp == "":
                    inp = self.obtenerDadosIngresados(caja_entrada_dados)
                Panel.update()  # Actualizar la interfaz gráfica
                x = randrange(1, 7)
                y = randrange(1, 7)

        if mod>1:
            L_DADOS1.config(image = Jugador.arregloDados[x],bg="green")
            L_DADOS1.img = Jugador.arregloDados[x]
            L_DADOS2.config(image = Jugador.arregloDados[y],bg="green")
            L_DADOS2.img = Jugador.arregloDados[y]
            Panel.update()  # Actualizar la interfaz gráfica
        return (x, y)

    def obtenerDadosIngresados(self, caja_entrada_dados):
        caja_entrada_dados.get()


