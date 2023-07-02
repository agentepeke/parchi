import tkinter
from tkinter import *
from tkinter import messagebox, font, Entry


from PIL import ImageTk, Image

from ficha import Ficha
from jugador import Jugador
from tablero_mario import Tablero_Mario
from movimiento import Movimiento

class Graficador:

    global LABEL_NOMBRE_ESPACIO

    def __init__(self):
        self.Panel = Tk()
        self.Panel.configure(bg="blue")
        self.Panel.state('zoomed')
        self.Panel.title('PRINCIPAL')
        self.imgFichas = Ficha.imgFichas
        self.arregloDados = Jugador.arregloDados
        #arregloDados = {}
        fondo = Image.open("fondo_mario.gif")
        fondo = fondo.resize((self.Panel.winfo_screenwidth(), self.Panel.winfo_screenheight()))
        fondo = ImageTk.PhotoImage(fondo)

        LF = Label(self.Panel, image=fondo)
        LF.configure(bg="blue")
        LF.place(x=0, y=0, relwidth=1, relheight=1)

        LF.image = fondo
        self.texto_ingresado: str
        self.TXT_ENTRADA = None

        self.etiquetas_colores = ["red", "green", "yellow", "blue"]
        self.nombres = []

        self.LB = Label(self.Panel, text="Parchis FLMCJ", font=("Comic Sans MS", 50))
        panel_bg = self.Panel["bg"]
        self.LB.config(bg=panel_bg)
        self.LB.pack(pady=10)

        self.BTN = Button(self.Panel, text="INICIAR", font=("Comic Sans MS", 40), width=8, height=1, command=self.crear_widgets, borderwidth=10)
        self.BTN.pack(pady=100)

        self.BTN.bind("<Enter>", self.cambiar_color_rojo)
        self.BTN.bind("<Leave>", self.cambiar_color_normal)

        self.BTN_creditos = Button(self.Panel, text="Créditos", font=("Comic Sans MS", 40), width=8, height=1, command=self.mostrar_creditos, borderwidth=10)
        self.BTN_creditos.pack(pady=50)

        self.BTN_creditos.bind("<Enter>", self.cambiar_color_rojo_creditos)
        self.BTN_creditos.bind("<Leave>", self.cambiar_color_normal_creditos)

        # Metodo para crear el panel donde se realizara el tablero


    def pintar_tablero(self):
        self.Panel.destroy()
        self.Panel = Tk()
        self.Panel.configure(bg="blue")
        self.Panel.state('zoomed')
        self.Panel.title('PARCHIS MARIO')
        nom = tuple(self.pedirDatos())
        d1 = PhotoImage(file="d1.gif")
        d2 = PhotoImage(file="d2.gif")
        d3 = PhotoImage(file="d3.gif")
        d4 = PhotoImage(file="d4.gif")
        d5 = PhotoImage(file="d5.gif")
        d6 = PhotoImage(file="d6.gif")
        fRo = PhotoImage(file="fRo.gif")
        fVe = PhotoImage(file="fVe.gif")
        fAm = PhotoImage(file="fAm.gif")
        fAz = PhotoImage(file="fAz.gif")

        Ficha.imgFichas["rojo"] = fRo
        Ficha.imgFichas["verde"] = fVe
        Ficha.imgFichas["amarillo"] = fAm
        Ficha.imgFichas["azul"] = fAz
        Jugador.arregloDados[1] = d1
        Jugador.arregloDados[2] = d2
        Jugador.arregloDados[3] = d3
        Jugador.arregloDados[4] = d4
        Jugador.arregloDados[5] = d5
        Jugador.arregloDados[6] = d6
        fondo = Image.open("fondo_mario.gif")
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
        self.LABEL_TABLEO = Label(self.Panel, fg="white")

        self.LABEL_TABLEO.place(x=456, y=50, width=455, height=455)

        TABLEROM = Tablero_Mario()
        tablero1 = TABLEROM.crearTablero( self.LABEL_TABLEO)

        self.BTN_regresar = Button(self.Panel, text="Regresar", font=("Comic Sans MS", 20), width=8, height=1,
                                       command=self.volver_menu, borderwidth=10)
        self.BTN_regresar.place(x=1200, y=600)

        self.BTN_regresar.bind("<Enter>", self.cambiar_color_rojo_regresar)
        self.BTN_regresar.bind("<Leave>", self.cambiar_color_normal_regresar)

        self.LABEL_NOMBRE_JUGADOR = Label(self.Panel, bg="RED", fg="white", text="TURNO DE: -----",font=("Comic Sans MS", 20))
        self.LABEL_NOMBRE_JUGADOR.place(x=50, y=50)

        self.LABEL_ESPACIO = Label(self.Panel, bg="yellow", fg="black", text="NUMERO DE ESPACIO:", font=("Comic Sans MS", 20))
        self.LABEL_ESPACIO.place(x=50, y=100)

        self.LABEL_NOMBRE_ESPACIO = Label(self.Panel, bg="yellow", fg="black", width=5, font=("Comic Sans MS", 20))
        self.LABEL_NOMBRE_ESPACIO.place(x=50, y=150)

        for espacio in tablero1:
            espacio.etiqueta.bind("<Enter>", lambda event, num=espacio.numeroEspacio: self.actualizar_label(num))
            espacio.etiqueta.bind("<Leave>", lambda event: self.LABEL_NOMBRE_ESPACIO.config(text="---"))
            print()

        self.caja_entrada_dados = Entry(self.Panel, font='Helvetica 20', borderwidth=0)
        self.caja_entrada_dados.place(x=0, y=500, width=550, height=50)
        self.boton_entrada_dados = Button(self.Panel, text='Continuar', font=("Times New Roman", 20), fg="white",
                                     command=self.obtenerDadosIngresados, bg="blue", borderwidth=0)
        self.boton_entrada_dados.place(x=550, y=500, width=150, height=50)
        #--------------------------------------------------------------------------------------------------------------------------------------------
        Jugadores = self.CrearJugadoresYFichas(tablero1, len(nom), nom)
        indicePrimerJugador = self.OrdenDeJuego(Jugadores)
        desa = False
        mod = 3
        movimiento = Movimiento()
        while not movimiento.GameOver(Jugadores):
            self.LABEL_TABLEO.update()
            repetirLanzamiento = True
            contadorParesSeguidos = 0  # contador de 3 seguidos
            jugadorActual = Jugadores[indicePrimerJugador % len(Jugadores)]
            if jugadorActual.GanoJugador: continue
            while repetirLanzamiento:
                resultadoDado1, resultadoDado2 = jugadorActual.TirarDosDados(desa, self.caja_entrada_dados, self.LABEL_DADO1, self.LABEL_DADO2, self.Panel)
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
                            jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
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
                        movimiento.realizarMovimiento(ListaMovi[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                        continue
                ListaMovi1 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                ListaMovi2 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                ListaMoviF = ""
                if ListaMovi1 and 'sale' in ListaMovi1[0][0]:
                    movimiento.realizarMovimiento(ListaMovi1[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                    ListaMovi2 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                    ListaMoviF = ListaMovi2
                elif ListaMovi2 and "sale" in ListaMovi2[0][0]:
                    movimiento.realizarMovimiento(ListaMovi2[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                    ListaMovi1 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                    ListaMoviF = ListaMovi1
                if type(ListaMoviF) != list:
                    if ListaMovi1 and ListaMovi2:
                        dadoSeleccionado = 0
                        if mod == 3:
                            self.caja_entrada_dados.config(state="normal")
                            self.caja_entrada_dados.delete(0, END)
                            self.caja_entrada_dados.insert(0, "%s seleccione uno de los dados" % jugadorActual.nombre)
                            self.caja_entrada_dados.config(state="readonly")
                            self.LABEL_DADO1.bind("<Enter>", lambda x: movimiento.FuncDados(self.LABEL_DADO1, 0))
                            self.LABEL_DADO2.bind("<Enter>", lambda x: movimiento.FuncDados(self.LABEL_DADO2, 0))
                            self.LABEL_DADO1.bind("<Button-1>", lambda x: movimiento.FuncDados(self.LABEL_DADO1, 2))
                            self.LABEL_DADO1.bind("<Leave>", lambda x: movimiento.FuncDados(self.LABEL_DADO1, 1))
                            self.LABEL_DADO2.bind("<Leave>", lambda x: movimiento.FuncDados(self.LABEL_DADO2, 1))
                            self.LABEL_DADO2.bind("<Button-1>", lambda x: movimiento.FuncDados(self.LABEL_DADO1, 3))
                            self.LABEL_DADO1.config(bg="green")
                            self.LABEL_DADO2.config(bg="green")
                            self.LABEL_DADO1.unbind("<Enter>")
                            self.LABEL_DADO2.unbind("<Enter>")
                            self.LABEL_DADO1.unbind("<Button-1>")
                            self.LABEL_DADO1.unbind("<Leave>")
                            self.LABEL_DADO2.unbind("<Leave>")
                            self.LABEL_DADO2.unbind("<Button-1>")
                        for x in range(2):
                            if dadoSeleccionado == 1 and not ListaMovi1:
                                continue
                            elif dadoSeleccionado == 2 and not ListaMovi2:
                                continue
                            elif dadoSeleccionado == 1 and len(ListaMovi1) == 1:
                                movimiento.realizarMovimiento(ListaMovi1[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                                ListaMovi2 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                                dadoSeleccionado = 2
                            elif dadoSeleccionado == 1 and len(ListaMovi1) > 1:
                                movimiento.realizarMovimiento(movimiento.opciones(ListaMovi1, jugadorActual, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel), tablero1,
                                                              jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                                ListaMovi2 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado2, Jugadores)
                                dadoSeleccionado = 2
                            elif dadoSeleccionado == 2 and len(ListaMovi2) == 1:
                                movimiento.realizarMovimiento(ListaMovi2[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                                ListaMovi1 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                                dadoSeleccionado = 1
                            elif dadoSeleccionado == 2 and len(ListaMovi2) > 1:
                                movimiento.realizarMovimiento(movimiento.opciones(ListaMovi1, jugadorActual, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel), tablero1,
                                                              jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                                ListaMovi1 = movimiento.posiblesMovimientos(jugadorActual, resultadoDado1, Jugadores)
                                dadoSeleccionado = 1
                            # imprimirEstado(jugadorActual)
                    elif ListaMovi1:
                        if len(ListaMovi1) == 1:
                            movimiento.realizarMovimiento(ListaMovi1[0], tablero1,
                                                          jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                            movimiento.imprimirEstado(jugadorActual)
                        else:
                            movimiento.realizarMovimiento(movimiento.opciones(ListaMovi1, jugadorActual, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel), tablero1,
                                                          jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                            # imprimirEstado(jugadorActual)
                    elif ListaMovi2:
                        if len(ListaMovi2) == 1:
                            movimiento.realizarMovimiento(ListaMovi2[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                        else:
                            movimiento.realizarMovimiento(movimiento.opciones(ListaMovi1, jugadorActual, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel), tablero1,
                                                          jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                elif ListaMoviF and len(ListaMoviF) == 1:
                    movimiento.realizarMovimiento(ListaMoviF[0], tablero1, jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                    movimiento.imprimirEstado(jugadorActual)
                elif ListaMoviF and len(ListaMoviF) > 1:
                    movimiento.realizarMovimiento(movimiento.opciones(ListaMovi1, jugadorActual, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel), tablero1,
                                                  jugadorActual, Jugadores, self.caja_entrada_dados, self.boton_entrada_dados, self.Panel)
                    movimiento.imprimirEstado(jugadorActual)

            indicePrimerJugador += 1  # Defines the infinite cycle
        if mod > 1:
            self.Panel.quit()
        Jugadores.sort(key=lambda x: x.Posicion)
        for x in Jugadores:
            print(x.nombre + " terminó en posición: %d" % x.Posicion)

        self.Panel.quit()

        self.Panel.mainloop()


    def cambiar_color_rojo(self, event):
        self.BTN.config(bg="red")

    def cambiar_color_normal(self, event):
        self.BTN.config(bg="SystemButtonFace")

    def cambiar_color_rojo_creditos(self, event):
        self.BTN_creditos.config(bg="red")

    def cambiar_color_normal_creditos(self, event):
        self.BTN_creditos.config(bg="SystemButtonFace")

    def cambiar_color_rojo_regresar(self, event):
        self.BTN_regresar.config(bg="green")

    def cambiar_color_normal_regresar(self, event):
        self.BTN_regresar.config(bg="SystemButtonFace")

    def mostrar_creditos(self):
        ventana_creditos = Toplevel()
        ventana_creditos.title("Créditos")

        #ventana_creditos.geometry("300x200")

        # Personalizar el fondo y la fuente
        ventana_creditos.configure(bg="lightblue")
        fuente = ("Comic Sans MS", 20)

        # Etiqueta de créditos
        etiqueta_creditos = Label(ventana_creditos,
                                  text="Desarrollado por:\n--Fernando Quiñonez--\n--Luis Gutierrez--"
                                       "\n--Marco de Leon--\n--Carlos Santisteban--\n--Jesus Queme--",
                                  bg="lightblue", fg="black", font=fuente)
        etiqueta_creditos.pack()
        ventana_creditos.update_idletasks()
        width = ventana_creditos.winfo_width()
        height = ventana_creditos.winfo_height()
        x = (ventana_creditos.winfo_screenwidth() // 2) - (width // 2)
        y = (ventana_creditos.winfo_screenheight() // 2) - (height // 2)
        ventana_creditos.geometry(f"{width}x{height}+{x}+{y}")



    def start(self):
        self.Panel.mainloop()

    def volver_menu(self):
        self.Panel.destroy()
        return self.__init__()

    def actualizar_label(self, numero_espacio):
        self.LABEL_NOMBRE_ESPACIO.config(text=str(numero_espacio))
        print(numero_espacio)


    def crear_widgets(self):
        self.LB.destroy()
        self.BTN.destroy()
        self.BTN_creditos.destroy()
        self.etiqueta_titulo = Label(self.Panel, text="Registro de Jugadores", font=("Comic Sans MS", 40))
        self.etiqueta_titulo.pack(pady=10)

        self.label_jugadores = Label(self.Panel, text="Número de jugadores (2-4):", font=("Comic Sans MS", 20))
        self.label_jugadores.pack()

        self.entry_numero_jugadores = Entry(self.Panel, font=("Comic Sans MS", 20))
        self.entry_numero_jugadores.pack(pady=5)

        self.boton_confirmar_jugadores = Button(self.Panel, text="Confirmar", command=self.confirmar_jugadores, font=("Comic Sans MS", 20))
        self.boton_confirmar_jugadores.pack(pady=5)

    def confirmar_jugadores(self):
        self.numero_jugadores = self.entry_numero_jugadores.get()

        if self.numero_jugadores.isdigit():
            numero_jugadores = int(self.numero_jugadores)
            if 2 <= numero_jugadores <= 4:
                self.mostrar_ingreso_jugadores(numero_jugadores)

        self.entry_numero_jugadores.delete(0, END)

    def mostrar_ingreso_jugadores(self, numero_jugadores):
        self.label_jugadores.pack_forget()
        self.entry_numero_jugadores.pack_forget()
        self.boton_confirmar_jugadores.pack_forget()

        self.nombres = []  # Reinicializar la lista de nombres

        for i in range(numero_jugadores):
            label_jugador = Label(self.Panel, text=f"Ingrese el nombre del Jugador {i + 1}:",
                                  font=("Comic Sans MS", 20))
            label_jugador.pack(pady=5)

            nombre_jugador = StringVar()  # Variable de control para el nombre del jugador
            entry_jugador = Entry(self.Panel, font=("Comic Sans MS", 20), textvariable=nombre_jugador)
            entry_jugador.pack(pady=5)

            self.nombres.append(nombre_jugador)  # Guardar la variable de control en la lista

        boton_continuar = Button(self.Panel, text="Continuar", command=lambda: self.continuar_juego(self.nombres),
                                 font=("Comic Sans MS", 20))
        boton_continuar.pack(pady=10)

        return self.nombres
    def pedirDatos(self):
        nombres_jugadores = [nombre.get() for nombre in self.nombres]  # Obtener los nombres de las variables de control

        print("Lista de jugadores:")
        for i, nombre in enumerate(nombres_jugadores):
            print(f"Jugador {i + 1}: {nombre}-------------------")
        return nombres_jugadores

    def continuar_juego(self, nombres_jugadores):

        nombres = [nombre.get() for nombre in nombres_jugadores]  # Obtener los nombres de las variables de control

        print("Lista de jugadores:")
        for i, nombre in enumerate(nombres):
            print(f"Jugador {i + 1}: {nombre}")
        self.pintar_tablero()

    def obtenerDadosIngresados(self):
        self.caja_entrada_dados.get()

    def CrearJugadoresYFichas(self, tablero, numeroJugadores, nombres):

        jugadores = []
        for x in range(numeroJugadores):  # Itera en el número de jugadores que hayan ingresado
            fichas = []
            if x == 0:  # Si x es 0, sera el primer jugador, y por ende fichas rojas
                """
                68-> Start position for red.
                69-> Start position for green.
                70-> Start position for yellow.
                71-> Start position for blue.
                """
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

        return jugadores

    def OrdenDeJuego(self, ListaJugadores):
        desa = False
        aux = ListaJugadores[:]
        while len(aux) != 1:
            for x in aux:
                x.valor = x.TirarUnDado(desa, self.caja_entrada_dados, self.LABEL_DADO1, self.LABEL_DADO2, self.Panel)
            aux2 = []
            for x in aux:
                if not (x.valor != self.ObtenerMayor(aux)):
                    aux2.append(x)
            aux = aux2

        tkinter.messagebox.showinfo("Aviso", aux[0].nombre + " es el primero en iniciar")
        return ListaJugadores.index(aux[0])

    def ObtenerMayor(self, listaJugadores):
        arreglo = []
        for i in range(len(listaJugadores)):
            arreglo.append(listaJugadores[i].valor)
        return max(arreglo)





