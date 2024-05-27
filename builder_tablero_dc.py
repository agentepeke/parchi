import time
from tkinter import messagebox
from PIL import ImageTk, Image

from ficha import Ficha
from jugador import Jugador
from builder import Builder
from tkinter import *

from movimiento import Movimiento
from tablero_dc import Tablero_dc



class Builder_tablero_dc(Builder):

    def __init__(self):

        self.nombres = []

    def pintar_tablero(self, Panel):
        Panel.destroy()
        self.Panel = Tk()
        self.Panel.configure(bg="blue")
        self.Panel.state('zoomed')
        self.Panel.title('PARCHIS MARIO')
        nom = tuple(self.pedirDatos())
        d1 = PhotoImage(file="dados\\Dado1.gif")
        d2 = PhotoImage(file="dados\\Dado2.gif")
        d3 = PhotoImage(file="dados\\Dado3.gif")
        d4 = PhotoImage(file="dados\\Dado4.gif")
        d5 = PhotoImage(file="dados\\Dado5.gif")
        d6 = PhotoImage(file="dados\\Dado6.gif")
        Fi_super = PhotoImage(file="img_dc\\superman.gif")
        Fi_bat = PhotoImage(file="img_dc\\Batman.gif")
        Fi_LV = PhotoImage(file="img_dc\\LV.gif")
        Fi_MM = PhotoImage(file="img_dc\\MM.gif")

        Ficha.imgFichas["rojo"] = Fi_super
        Ficha.imgFichas["verde"] = Fi_bat
        Ficha.imgFichas["amarillo"] = Fi_LV
        Ficha.imgFichas["azul"] = Fi_MM
        Jugador.arregloDados[1] = d1
        Jugador.arregloDados[2] = d2
        Jugador.arregloDados[3] = d3
        Jugador.arregloDados[4] = d4
        Jugador.arregloDados[5] = d5
        Jugador.arregloDados[6] = d6
        fondo = ImageTk.Image.open("img_dc\\DCCOMICS.gif")
        fondo = fondo.resize((self.Panel.winfo_screenwidth(), self.Panel.winfo_screenheight()))
        fondo = ImageTk.PhotoImage(fondo)

        LF = Label(self.Panel, image=fondo)
        LF.configure(bg="blue")
        LF.place(x=0, y=0, relwidth=1, relheight=1)

        LF.image = fondo

        # Espacio donde se colocaran los dados
        self.LABEL_DADO1 = Label(self.Panel, bg="white")
        self.LABEL_DADO1.place(x=1050, y=90, width=175, height=175)
        self.LABEL_DADO2 = Label(self.Panel, bg="white")
        self.LABEL_DADO2.place(x=1050, y=290, width=175, height=175)
        self.LABEL_TABLEO = Label(self.Panel, bg="blue", fg="white")

        self.LABEL_TABLEO.place(x=456, y=50, width=455, height=455)

        self.BTN_regresar = Button(self.Panel, text="Regresar", font=("Comic Sans MS", 20), width=8, height=1,
                                   command=self.volver_menu, borderwidth=10)
        self.BTN_regresar.place(x=1200, y=600)

        self.BTN_regresar.bind("<Enter>", self.cambiar_color_rojo_regresar)
        self.BTN_regresar.bind("<Leave>", self.cambiar_color_normal_regresar)

        self.LABEL_NOMBRE_JUGADOR = Label(self.Panel, bg="RED", fg="white", text="TURNO DE: -----",
                                          font=("Comic Sans MS", 20))
        self.LABEL_NOMBRE_JUGADOR.place(x=50, y=50)

        self.LABEL_ESPACIO = Label(self.Panel, bg="yellow", fg="black", text="NUMERO DE ESPACIO:",
                                   font=("Comic Sans MS", 20))
        self.LABEL_ESPACIO.place(x=50, y=100)

        self.LABEL_NOMBRE_ESPACIO = Label(self.Panel, bg="yellow", fg="black", width=5, font=("Comic Sans MS", 20))
        self.LABEL_NOMBRE_ESPACIO.place(x=50, y=150)

        self.CAJA_ENTRADA = Entry(self.Panel, font=("Comic Sans MS", 20), borderwidth=0)
        self.CAJA_ENTRADA.place(x=350, y=530, width=700, height=50)
        self.BTN_ENTRADA = Button(self.Panel, text='Continuar', font=("Comic Sans MS", 20), fg="white",
                                  command=self.continuar_juegos, bg="green", borderwidth=0)
        self.BTN_ENTRADA.place(x=100, y=530, width=150, height=50)
        # --------------------------------------------------------------------------------------------------------------------------------------------
        TABLEROM = Tablero_dc()
        tablero1 = Tablero_dc.crearTablero(TABLEROM, self.LABEL_TABLEO)
        for espacio in tablero1:
            espacio.etiqueta.bind("<Enter>", lambda event, num=espacio.numeroEspacio: self.actualizar_label(num))
            espacio.etiqueta.bind("<Leave>", lambda event: self.LABEL_NOMBRE_ESPACIO.config(text="---"))
            print()
        Jugadores = self.CrearJugadoresYFichas(tablero1, len(nom), nom)
        indicePrimerJugador = self.OrdenDeJuego(Jugadores)

        desa = False
        mod = 3
        movimiento = Movimiento()
        while not movimiento.GameOver(Jugadores):
            # TABLEROM.config(state="readonly")

            repetirLanzamiento = True
            contadorParesSeguidos = 0  # contador de 3 seguidos
            jugadorActual = Jugadores[indicePrimerJugador % len(Jugadores)]
            if jugadorActual.GanoJugador: continue
            messagebox.showinfo("TIRAR DADOS", "Turno de " + jugadorActual.nombre + ". presione ENTER para tirar los dados")
            while repetirLanzamiento:

                resultadoDado1, resultadoDado2 = jugadorActual.TirarDosDados(desa, self.CAJA_ENTRADA,
                                                                             self.LABEL_DADO1, self.LABEL_DADO2,
                                                                             self.Panel)
                self.LABEL_NOMBRE_JUGADOR.config(text=f'TURNO DE: {jugadorActual.nombre}')
                if resultadoDado1 == resultadoDado2:
                    repetirLanzamiento = True
                    contadorParesSeguidos += 1
                    if contadorParesSeguidos == 3:
                        listaCasillasCarcel = {'rojo': 69, 'verde': 70, 'amarillo': 71, 'azul': 72}
                        UltimaFichaJugador = jugadorActual.UltimaFicha  # Invocamos la ultima ficha del jugador actual
                        nombreFicha = UltimaFichaJugador.nombreFicha  # Invocamos su nombre
                        posicionFinal = listaCasillasCarcel[
                            UltimaFichaJugador.colorFicha]  # Sacamos la llave de su posicion en la carcel
                        movimiento.realizarMovimiento(
                            ['{} mueve a casilla {}'.format(nombreFicha, posicionFinal), UltimaFichaJugador], tablero1,
                            jugadorActual, Jugadores, self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                        UltimaFichaJugador.estadoJuego = 'inicio'
                        repetirLanzamiento = False
                        contadorParesSeguidos = 0
                        # imprimirEstado(jugadorActual)
                        continue
                else:
                    contadorParesSeguidos = 0
                    repetirLanzamiento = False
                if resultadoDado1 + resultadoDado2 == 5:
                    ListaMovi = movimiento.posiblesMovimientos(jugadorActual, 5, Jugadores)
                    if ListaMovi and len(ListaMovi) == 1 and "sale" in ListaMovi[0][0]:
                        movimiento.realizarMovimiento(ListaMovi[0], tablero1, jugadorActual, Jugadores,
                                                      self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                        continue
                ListaMovi1 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                ListaMovi2 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                ListaMoviF = ""
                if ListaMovi1 and 'sale' in ListaMovi1[0][0]:
                    movimiento.realizarMovimiento(ListaMovi1[0], tablero1, jugadorActual, Jugadores,
                                                  self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                    ListaMovi2 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                    ListaMoviF = ListaMovi2
                elif ListaMovi2 and "sale" in ListaMovi2[0][0]:
                    movimiento.realizarMovimiento(ListaMovi2[0], tablero1, jugadorActual, Jugadores,
                                                  self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                    ListaMovi1 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                    ListaMoviF = ListaMovi1
                if type(ListaMoviF) != list:

                    if ListaMovi1:
                        if len(ListaMovi1) == 1:
                            movimiento.realizarMovimiento(ListaMovi1[0], tablero1,
                                                          jugadorActual, Jugadores, self.CAJA_ENTRADA,
                                                          self.BTN_ENTRADA, self.Panel)
                            movimiento.imprimirEstado(jugadorActual)
                        else:
                            movimiento.realizarMovimiento(
                                movimiento.opciones(ListaMovi1, jugadorActual, self.CAJA_ENTRADA,
                                                    self.BTN_ENTRADA, self.Panel), tablero1,
                                jugadorActual, Jugadores, self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                            # imprimirEstado(jugadorActual)
                    elif ListaMovi2:
                        if len(ListaMovi2) == 1:
                            movimiento.realizarMovimiento(ListaMovi2[0], tablero1, jugadorActual, Jugadores,
                                                          self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                        else:
                            movimiento.realizarMovimiento(
                                movimiento.opciones(ListaMovi1, jugadorActual, self.CAJA_ENTRADA,
                                                    self.BTN_ENTRADA, self.Panel), tablero1,
                                jugadorActual, Jugadores, self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                elif ListaMoviF and len(ListaMoviF) == 1:
                    movimiento.realizarMovimiento(ListaMoviF[0], tablero1, jugadorActual, Jugadores,
                                                  self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                    movimiento.imprimirEstado(jugadorActual)
                elif ListaMoviF and len(ListaMoviF) > 1:
                    movimiento.realizarMovimiento(
                        movimiento.opciones(ListaMovi1, jugadorActual, self.CAJA_ENTRADA,
                                            self.BTN_ENTRADA, self.Panel), tablero1,
                        jugadorActual, Jugadores, self.CAJA_ENTRADA, self.BTN_ENTRADA, self.Panel)
                    movimiento.imprimirEstado(jugadorActual)

            indicePrimerJugador += 1  # Defines the infinite cycle
        if mod > 1:
            self.Panel.quit()
        Jugadores.sort(key=lambda x: x.Posicion)
        for x in Jugadores:
            print(x.nombre + " terminó en posición: %d" % x.Posicion)

        self.Panel.quit()

        self.Panel.mainloop()

    def crear_widgets(self, LB, BTN, BTN_creditos, Panel):
        LB.destroy()
        BTN.destroy()
        BTN_creditos.destroy()
        self.etiqueta_titulo = Label(Panel, text="Registro de Jugadores", font=("Comic Sans MS", 40))
        self.etiqueta_titulo.pack(pady=10)

        self.label_jugadores = Label(Panel, text="Número de jugadores (2-4):", font=("Comic Sans MS", 20))
        self.label_jugadores.pack()

        self.entry_numero_jugadores = Entry(Panel, font=("Comic Sans MS", 20))
        self.entry_numero_jugadores.pack(pady=5)

        self.boton_confirmar_jugadores = Button(Panel, text="Confirmar", command=lambda:self.confirmar_jugadores(Panel),
                                                font=("Comic Sans MS", 20))
        self.boton_confirmar_jugadores.pack(pady=5)

    def confirmar_jugadores(self, Panel):
        self.numero_jugadores = self.entry_numero_jugadores.get()

        if self.numero_jugadores.isdigit():
            numero_jugadores = int(self.numero_jugadores)
            if 2 <= numero_jugadores <= 4:
                self.mostrar_ingreso_jugadores(numero_jugadores, Panel )

        self.entry_numero_jugadores.delete(0, END)

    def mostrar_ingreso_jugadores(self, numero_jugadores, Panel):
        self.label_jugadores.pack_forget()
        self.entry_numero_jugadores.pack_forget()
        self.boton_confirmar_jugadores.pack_forget()

        self.nombres = []  # Reinicializar la lista de nombres

        for i in range(numero_jugadores):
            label_jugador = Label(Panel, text=f"Ingrese el nombre del Jugador {i + 1}:",
                                  font=("Comic Sans MS", 20))
            label_jugador.pack(pady=5)

            nombre_jugador = StringVar()  # Variable de control para el nombre del jugador
            entry_jugador = Entry(Panel, font=("Comic Sans MS", 20), textvariable=nombre_jugador)
            entry_jugador.pack(pady=5)

            self.nombres.append(nombre_jugador)  # Guardar la variable de control en la lista

        boton_continuar = Button(Panel, text="Continuar", command=lambda: self.pintar_tablero(Panel),
                                 font=("Comic Sans MS", 20))
        boton_continuar.pack(pady=10)

        return self.nombres

    def pedirDatos(self):
        nombres_jugadores = [nombre.get() for nombre in self.nombres]  # Obtener los nombres de las variables de control

        print("Lista de jugadores:")
        for i, nombre in enumerate(nombres_jugadores):
            print(f"Jugador {i + 1}: {nombre}-------------------")
        return nombres_jugadores


    def CrearJugadoresYFichas(self, tablero, numeroJugadores, nombres):

        jugadores = []
        for x in range(numeroJugadores):  # Itera en el número de jugadores que hayan ingresado
            fichas = []
            if x == 0:  # Si x es 0, sera el primer jugador, y por ende fichas rojas

                for z in range(4):  # Crea las 4 fichas rojas
                    NuevaFicha = Ficha(self.LABEL_TABLEO, "rojo%d" % (z + 1), "rojo", tablero[68])  # Le asigna el número de ficha con su posición
                    fichas.append(NuevaFicha)  # Lo agrega en una lista de fichas
                jugadores.append(Jugador(nombres[0], "rojo", fichas))  # Crea un objeto jugador y lo agrega a una lista
                jugadores[0].UltimaFicha = jugadores[0].fichas[3]
            elif x == 1:
                for z in range(4):
                    NuevaFicha = Ficha(self.LABEL_TABLEO, "verde%d" % (z + 1), "verde", tablero[69])
                    fichas.append(NuevaFicha)
                jugadores.append(Jugador(nombres[1], "verde", fichas))
                jugadores[1].UltimaFicha = jugadores[1].fichas[3]
            elif x == 2:
                for z in range(4):
                    NuevaFicha = Ficha(self.LABEL_TABLEO, "amarillo%d" % (z + 1), "amarillo", tablero[70])
                    fichas.append(NuevaFicha)
                jugadores.append(Jugador(nombres[2], "amarillo", fichas))
                jugadores[2].UltimaFicha = jugadores[2].fichas[3]
            elif x == 3:
                for z in range(4):
                    NuevaFicha = Ficha(self.LABEL_TABLEO, "azul%d" % (z + 1), "azul", tablero[71])
                    fichas.append(NuevaFicha)
                jugadores.append(Jugador(nombres[3], "azul", fichas))
                jugadores[3].UltimaFicha = jugadores[3].fichas[3]
        self.LABEL_TABLEO.lift()
        return jugadores

    def OrdenDeJuego(self, ListaJugadores):
        desa = False
        aux = ListaJugadores[:]

        # Iterar sobre los jugadores
        for x in aux:
            # Establecer la variable de control como False al inicio de cada turno del jugador
            #self.dado_clickeado = False

            # Mostrar un mensaje para indicar al jugador que debe hacer clic
            messagebox.showinfo("Aviso", "Turno de " + x.nombre + ". Haz clic para tirar el dado.")
            x.valor = x.TirarUnDado(desa, self.CAJA_ENTRADA, self.LABEL_DADO1, self.LABEL_DADO2, self.Panel)

        aux2 = []
        for x in aux:
            if not (x.valor != self.ObtenerMayor(aux)):
                aux2.append(x)
        aux = aux2

        messagebox.showinfo("Aviso", aux[0].nombre + " es el primero en iniciar")
        return ListaJugadores.index(aux[0])


    def ObtenerMayor(self, listaJugadores):
        arreglo = []
        for i in range(len(listaJugadores)):
            arreglo.append(listaJugadores[i].valor)
        return max(arreglo)

    def continuar_juegos(self):
        self.dado_clickeado = True

    def volver_menu(self):
        self.Panel.destroy()
        return self.__init__()
    def cambiar_color_rojo_regresar(self, event):
        self.BTN_regresar.config(bg="green")

    def cambiar_color_normal_regresar(self, event):
        self.BTN_regresar.config(bg="SystemButtonFace")

    def actualizar_label(self, numero_espacio):
        self.LABEL_NOMBRE_ESPACIO.config(text=str(numero_espacio))
        print(numero_espacio)