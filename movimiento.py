import tkinter
from tkinter import END

from ficha import Ficha
from jugador import Jugador
from tablero_mario import Tablero_Mario


class Movimiento:


    def GameOver(self, Jugadores):
        """
        @param Jugadores: List ob object of class 'Jugador'

        """
        numberWonPlayers = 0  # Counts the number of players that have already won
        for jugadorActual in Jugadores:
            if jugadorActual.GanoJugador:
                numberWonPlayers += 1
        if (numberWonPlayers == len(Jugadores) - 1 and len(Jugadores) > 1) or (
                numberWonPlayers == 1 and len(Jugadores) == 1):
            global POSICION
            jugadorFaltante = [jug for jug in Jugadores if not jug.GanoJugador]
            if not len(jugadorFaltante) == 0:
                jugadorFaltante[0].Posicion = POSICION
            return True
        return False

    def posiblesMovimientos(self, JugadorActual: list[Jugador], resultadoDado, ListaJugadores):

        listaPosiblesMovimientos = []
        # Esto se va a cambiar de funcion
        listaCasillasCarcel = [69, 70, 71, 72]
        numeros = {}
        numeros2 = {}
        for jugador in ListaJugadores:
            for ficha in jugador.fichas:
                casillaActual = ficha.espacioActual.numeroEspacio
                if casillaActual in numeros and not casillaActual in listaCasillasCarcel:
                    numeros[casillaActual][1] += 1
                    if numeros[casillaActual][0].colorFicha != ficha.colorFicha and casillaActual in [5, 22, 39, 56]:
                        numeros2[casillaActual] = [numeros[casillaActual][0], ficha]
                elif not casillaActual in listaCasillasCarcel:
                    numeros[casillaActual] = [ficha, 1]

        listaBloqueos = [item for item, valor in numeros.items() if valor[1] == 2]
        listaConUnaFicha = [(item, valor[0]) for item, valor in numeros.items() if valor[1] == 1]
        tuplaCasillasUnaFicha = tuple([valor for valor, ficha in listaConUnaFicha])
        dat = {"rojo": 5, "verde": 22, "amarillo": 39, "azul": 56}
        diccionarioSeguros = {"rojo": 68, "verde": 17, "amarillo": 34,
                              "azul": 51}  # Seguros donde inician las casillas especiales de cada color
        diccionarioPrimeraEspecial = {"rojo": 73, "verde": 80, "amarillo": 87, "azul": 94}  # Primera casilla especial

        numeroSeguroSalida = diccionarioSeguros[JugadorActual.color]
        numeroPrimeraEspecial = diccionarioPrimeraEspecial[JugadorActual.color]
        numeroDiccionarioSeguros = diccionarioSeguros[JugadorActual.color]

        colorJugador = JugadorActual.color

        for fichaActual in JugadorActual.fichas:
            bloqueo = False
            casillaFicha = fichaActual.espacioActual.numeroEspacio
            nombreFicha = fichaActual.nombreFicha
            posicionFinal = casillaFicha + resultadoDado
            if casillaFicha in listaCasillasCarcel and resultadoDado != 5:  # Evalua si la casilla esta en la ficha y saca diferente de 5
                continue
            if casillaFicha in listaCasillasCarcel and resultadoDado == 5:  # Si el dado da 5 y hay una casilla en la carcel sale automaticamente
                if not (dat[colorJugador] in listaBloqueos and not dat[colorJugador] in numeros2):
                    if (dat[colorJugador] in tuplaCasillasUnaFicha and numeros[dat[colorJugador]][
                        0].colorFicha != fichaActual.colorFicha):
                        return ([(nombreFicha + " sale de la carcel a la casilla: %d. Captura a %s." % (
                            dat[colorJugador], numeros[dat[colorJugador]][0].nombreFicha), fichaActual,
                                  numeros[dat[colorJugador]][0])])
                    elif dat[colorJugador] in numeros2:
                        if numeros2[dat[colorJugador]][0].colorFicha != fichaActual.colorFicha and \
                                numeros2[dat[colorJugador]][1].colorFicha == fichaActual.colorFicha:
                            return ([(nombreFicha + " sale de la carcel a la casilla: %d. Captura a %s." % (
                                dat[colorJugador], numeros2[dat[colorJugador]][0].nombreFicha), fichaActual,
                                      numeros2[dat[colorJugador]][0])])
                        elif numeros2[dat[colorJugador]][1].colorFicha != fichaActual.colorFicha and \
                                numeros2[dat[colorJugador]][0].colorFicha == fichaActual.colorFicha:
                            return ([(nombreFicha + " sale de la carcel a la casilla: %d. Captura a %s." % (
                                dat[colorJugador], numeros2[dat[colorJugador]][1].nombreFicha), fichaActual,
                                      numeros2[dat[colorJugador]][1])])
                        else:
                            continue
                    else:
                        return (
                        [(nombreFicha + " sale de la carcel a la casilla: %d." % dat[colorJugador], fichaActual)])
                else:
                    continue
            else:
                #  Condición 3
                for x in range(casillaFicha + 1, posicionFinal + 1):
                    if (casillaFicha <= numeroSeguroSalida and x > numeroSeguroSalida) or (
                            colorJugador == "verde" and casillaFicha >= 51 and casillaFicha <= 68 and x > 85):
                        if (colorJugador == "verde" and casillaFicha >= 51 and casillaFicha <= 68 and x > 85):
                            if x % 68 + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1 in listaBloqueos:
                                bloqueo = True
                                break
                            elif x % 68 + (
                                    numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1 > numeroPrimeraEspecial + 7:
                                bloqueo = True
                                break
                        else:
                            if x + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1 in listaBloqueos:
                                bloqueo = True
                                break
                            elif x + (numeroPrimeraEspecial - numeroDiccionarioSeguros) - 1 > numeroPrimeraEspecial + 7:
                                bloqueo = True
                                break
                    elif casillaFicha <= 68 and x <= 68 and x in listaBloqueos:
                        bloqueo = True
                        break
                    elif x % 68 in listaBloqueos:
                        bloqueo = True
                        break
                    elif x in listaBloqueos or x > numeroPrimeraEspecial + 7:  #:()
                        bloqueo = True
                        break

            CasillaEspecial = 0
            ListaCasillasSeguro = (12, 17, 29, 34, 46, 51, 63, 68)
            ListaCasillasSalida = (5, 22, 39, 56)
            if (casillaFicha <= numeroSeguroSalida and posicionFinal > numeroSeguroSalida) or (
                    colorJugador == "verde" and casillaFicha >= 51 and casillaFicha <= 68 and posicionFinal > 85):
                if (colorJugador == "verde" and casillaFicha >= 51 and casillaFicha <= 68 and posicionFinal > 85):
                    CasillaEspecial = posicionFinal % 68 + (numeroPrimeraEspecial - numeroSeguroSalida - 1)
                else:
                    CasillaEspecial = posicionFinal + (numeroPrimeraEspecial - numeroSeguroSalida - 1)
                if CasillaEspecial == numeroPrimeraEspecial + 7:
                    CasillaEspecial = 101

            if not bloqueo:
                if CasillaEspecial == 101 or posicionFinal == numeroPrimeraEspecial + 7:
                    textoRespuesta = '{} corona'.format(nombreFicha)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

                elif posicionFinal <= 68 and posicionFinal in tuplaCasillasUnaFicha and CasillaEspecial == 0:
                    fichaCapturada = numeros[posicionFinal][0]
                    if fichaCapturada.colorFicha != colorJugador and not posicionFinal in ListaCasillasSeguro and not posicionFinal in ListaCasillasSalida:
                        textoRespuesta = '{} captura a {} en casilla {}'.format(nombreFicha, fichaCapturada.nombreFicha,
                                                                                posicionFinal)
                        listaPosiblesMovimientos.append((textoRespuesta, fichaActual, fichaCapturada))
                    else:
                        textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal)
                        listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

                elif posicionFinal > 68 and (
                        posicionFinal % 68 in tuplaCasillasUnaFicha) and CasillaEspecial == 0 and casillaFicha <= 68:
                    fichaCapturada_2 = numeros[posicionFinal % 68][0]
                    if fichaCapturada_2.colorFicha != colorJugador and not posicionFinal % 68 in ListaCasillasSeguro and not posicionFinal % 68 in ListaCasillasSalida:
                        textoRespuesta = '{} captura a {} en casilla {}'.format(nombreFicha,
                                                                                fichaCapturada_2.nombreFicha,
                                                                                posicionFinal % 68)
                        listaPosiblesMovimientos.append((textoRespuesta, fichaActual, fichaCapturada_2))
                    else:
                        textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal % 68)
                        listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

                elif CasillaEspecial != 0:
                    textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, CasillaEspecial)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

                elif posicionFinal <= 68:
                    textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

                elif posicionFinal > 68 and casillaFicha > 68:
                    textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))

                elif posicionFinal > 68:
                    textoRespuesta = '{} mueve a casilla {}'.format(nombreFicha, posicionFinal % 68)
                    listaPosiblesMovimientos.append((textoRespuesta, fichaActual))
        if len(listaPosiblesMovimientos) == 0:
            return None
        return listaPosiblesMovimientos

    def realizarMovimiento(self, movimientoRealizar, tablero, jugadorActual,
                           Jugadores, caja_entrada_dados, boton_entrada_dados, Pan):  # Añadimos parametro jugador actual para poder definir la ultima ficha de cada jugador
        """
        Actualiza las posiciones de las fichas en el tablero


        @param movimientoRealizar: Es la tupla que contiene
        1. El movimiento a realizar (String)
        2. Objeto ficha a mover
        3. Objeto ficha capturado (String vacío si no captura)

        """
        mod = 3
        if movimientoRealizar == None:
            return
        FichaCapturada = None
        listaCasillasCarcel = {'rojo': 69, 'verde': 70, 'amarillo': 71, 'azul': 72}
        listaCasillasSalida = {'rojo': 5, 'verde': 22, 'amarillo': 39, 'azul': 56}
        FichaMover = movimientoRealizar[1]
        descripcionMovimiento = movimientoRealizar[0]

        if len(movimientoRealizar) == 3:
            FichaCapturada = movimientoRealizar[2]
        if 'sale' in descripcionMovimiento:
            if "Captura" in descripcionMovimiento:
                FichaCapturada = movimientoRealizar[2]
                FichaCapturada.estadoJuego = "inicio"
                casillaCarcel = listaCasillasCarcel[FichaCapturada.colorFicha]
                FichaCapturada.cambiarPosicion(tablero[casillaCarcel - 1])
                FichaMover.cambiarPosicion(tablero[listaCasillasSalida[FichaMover.colorFicha] - 1])
                FichaMover.estadoJuego = "activo"
                listaMovi = movimientoRealizar.posiblesMovimientos(jugadorActual, 20, Jugadores)
                if mod > 1:
                    tkinter.messagebox.showinfo("Captura",
                                                FichaMover.nombreFicha + " captura a " + FichaCapturada.nombreFicha)
                    tkinter.messagebox.showinfo("Salida", FichaMover.nombreFicha + " sale de la carcel.")
                if listaMovi and len(listaMovi) == 1:
                    movimientoRealizar.realizarMovimiento(listaMovi[0], tablero, jugadorActual, Jugadores, caja_entrada_dados , boton_entrada_dados, Pan)
                elif listaMovi and len(listaMovi) > 1:
                    movimientoRealizar.realizarMovimiento(movimientoRealizar.opciones(listaMovi, jugadorActual, caja_entrada_dados, boton_entrada_dados, Pan), tablero, jugadorActual, Jugadores, caja_entrada_dados , boton_entrada_dados, Pan)
            else:
                FichaMover.cambiarPosicion(tablero[listaCasillasSalida[FichaMover.colorFicha] - 1])
                FichaMover.estadoJuego = "activo"
                if mod > 1:
                    tkinter.messagebox.showinfo("Salida", FichaMover.nombreFicha + " sale de la carcel.")
        elif 'captura' in descripcionMovimiento:
            posicionFinal = int(descripcionMovimiento.split()[-1])
            casillaCarcel = listaCasillasCarcel[FichaCapturada.colorFicha]
            FichaCapturada.cambiarPosicion(tablero[casillaCarcel - 1])  # Cambia de posición
            FichaCapturada.estadoJuego = "inicio"
            FichaMover.cambiarPosicion(tablero[posicionFinal - 1])
            listaMovi = movimientoRealizar.posiblesMovimientos(jugadorActual, 20, Jugadores)
            if mod > 1:
                tkinter.messagebox.showinfo("Captura",
                                            FichaMover.nombreFicha + " captura a " + FichaCapturada.nombreFicha)
            if listaMovi and len(listaMovi) == 1:
                movimientoRealizar.realizarMovimiento(listaMovi[0], tablero, jugadorActual, Jugadores, caja_entrada_dados , boton_entrada_dados, Pan)
            elif listaMovi and len(listaMovi) > 1:
                movimientoRealizar.realizarMovimiento(movimientoRealizar.opciones(listaMovi, jugadorActual, caja_entrada_dados, boton_entrada_dados, Pan), tablero, jugadorActual, Jugadores, caja_entrada_dados , boton_entrada_dados, Pan)
        elif 'mueve' in descripcionMovimiento:
            posicionFinal = int(descripcionMovimiento.split()[-1])
            FichaMover.cambiarPosicion(tablero[posicionFinal - 1])  # Cambia posicion de la ficha
        elif 'corona' in descripcionMovimiento:
            if mod > 1:
                FichaMover.eliminarFicha()
            jugadorActual.fichas.remove(FichaMover)
            if len(jugadorActual.fichas) == 0:
                global POSICION
                jugadorActual.Posicion = POSICION
                POSICION += 1
                jugadorActual.GanoJugador = True
            if mod > 1:
                tkinter.messagebox.showinfo("Corona", FichaMover.nombreFicha + " corona.")
            listaMovi = movimientoRealizar.posiblesMovimientos(jugadorActual, 10, Jugadores)
            if listaMovi and len(listaMovi) == 1:
                movimientoRealizar.realizarMovimiento(listaMovi[0], tablero, jugadorActual, Jugadores, caja_entrada_dados, boton_entrada_dados, Pan)
            elif listaMovi and len(listaMovi) > 1:
                movimientoRealizar.realizarMovimiento(movimientoRealizar.opciones(listaMovi, jugadorActual, caja_entrada_dados, boton_entrada_dados, Pan), tablero, jugadorActual, Jugadores, caja_entrada_dados, boton_entrada_dados, Pan)
            Pan.update()
            return
        jugadorActual.DefinirUltimaFicha(jugadorActual, FichaMover)

    def imprimirEstado(self, Jugador):
        for ficha in Jugador.fichas:
            print(ficha.imprimirPropiedades())

    def seleccionarOpcion(self):
        seleccion = True

    def opciones(self, Lista, JugadorActual, caja_entrada_dados, boton_entrada_dados, Pan):
        eleccion = 0
        mod = 3
        seleccion = False
        if mod == 3:
            clicked = tkinter.StringVar(Pan)
            caja_entrada_dados.config(state="normal")
            caja_entrada_dados.delete(0, tkinter.END)
            caja_entrada_dados.insert(0,
                                      f"{JugadorActual.nombre} seleccione una opción de la lista y oprima continuar.")
            caja_entrada_dados.config(state="readonly")
            if Lista is not None:
                options = [opcion[0] for opcion in Lista]
            else:
                options = []
            clicked.set("Seleccione una opción")
            drop = tkinter.OptionMenu(Pan, clicked, *options)
            drop.place(x=0, y=600, width=700, height=50)
            boton_entrada_dados.config(command=self.seleccionarOpcion)
            while not seleccion:
                if clicked.get() != "Seleccione una opción":
                    seleccion = True
                Pan.update()
            eleccion = options.index(clicked.get()) + 1
            boton_entrada_dados.config(command=lambda: self.obtenerDadosIngresados(caja_entrada_dados))
            drop.destroy()
        Pan.update()
        return Lista[eleccion - 1]

    def FuncDados(self, etiqueta, accion):
        global dadoSeleccionado
        if accion == 0:
            etiqueta.config(bg="red")
        elif accion == 1:
            etiqueta.config(bg="green")
        elif accion == 2:
            dadoSeleccionado = 1
        elif accion == 3:
            dadoSeleccionado = 2

    def obtenerDadosIngresados(self, caja_entrada_dados):
        caja_entrada_dados.get()









