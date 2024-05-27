from espacio import Espacio
from tablero import Tablero
from tkinter import *

class Tablero_dc(Tablero):

    def crearTablero(self, Pan):

        mod = 3
        tablero = []
        for x in range(68):
            labelF = ""
            labelI = ""
            orientacion = ""
            xF = 0
            yF = 0
            if mod > 1:
                if x + 1 in [y1 for y1 in range(1, 9)]:
                    orientacion = "vertical"
                    z = x
                    if x + 1 == 5:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=z * 18, y=252, width=18, height=54)
                        labelI = Label(Pan, bg="#ED0D0D", borderwidth=0)            # 250 - 252   rojo
                        labelI.place(x=z * 18 + 2, y=254, width=14, height=50)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=z * 18, y=252, width=18, height=54)
                        labelI = Label(Pan, bg="white", borderwidth=0)
                        labelI.place(x=z * 18 + 2, y=254, width=14, height=50)
                    xF = z * 18 + 2
                    yF = 4 # 4
                elif x + 1 in [y1 for y1 in range(9, 17)]:
                    orientacion = "horizontal"
                    z = x - 8
                    if x + 1 == 12:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=144, y=z * 18 + 306, width=54, height=18)
                        labelI = Label(Pan, bg="#ED0D0D", borderwidth=0)
                        labelI.place(x=146, y=z * 18 + 308, width=50, height=14)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=144, y=z * 18 + 306, width=54, height=18)
                        labelI = Label(Pan, bg="white", borderwidth=0)              #394 -- 396
                        labelI.place(x=146, y=z * 18 + 308, width=50, height=14)
                    xF = 146
                    yF = z * 18 + 308
                elif x + 1 == 17:
                    orientacion = "horizontal"
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=198, y=432, width=54, height=18)
                    labelI = Label(Pan, bg="#04B112", borderwidth=0)    #448 -- 450  verde
                    labelI.place(x=200, y=434, width=50, height=14)
                    xF = 200
                    yF = 434
                elif x + 1 in [y1 for y1 in range(18, 26)]:
                    orientacion = "horizontal"
                    z = x - 17
                    if x + 1 == 22:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=252, y=432 - z * 18, width=54, height=18)
                        labelI = Label(Pan, bg="#04B112", borderwidth=0)
                        labelI.place(x=254, y=434 - z * 18, width=50, height=14)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=252, y=432 - z * 18, width=54, height=18)
                        labelI = Label(Pan, bg="white", borderwidth=0)              #502 -- 504
                        labelI.place(x=254, y=434 - z * 18, width=50, height=14)
                    yF = 434 - z * 18
                    xF = 254
                elif x + 1 in [y1 for y1 in range(26, 34)]:
                    orientacion = "vertical"
                    z = x - 25
                    if x + 1 == 29:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=z * 18 + 306, y=252, width=18, height=54)
                        labelI = Label(Pan, bg="#04B112", borderwidth=0)
                        labelI.place(x=z * 18 + 308, y=254, width=14, height=50)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=z * 18 + 306, y=252, width=18, height=54)
                        labelI = Label(Pan, bg="white", borderwidth=0)              # 556 --- 558 amarillo
                        labelI.place(x=z * 18 + 308, y=254, width=14, height=50)
                    yF = 254
                    xF = z * 18 + 308
                elif x + 1 == 34:
                    orientacion = "vertical"
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=432, y=198, width=18, height=54)
                    labelI = Label(Pan, bg="#ECC811", borderwidth=0)                # 682 -- 684
                    labelI.place(x=434, y=200, width=14, height=50)
                    yF = 200
                    xF = 434
                elif x + 1 in [y1 for y1 in range(35, 43)]:
                    orientacion = "vertical"
                    z = x - 34
                    if x + 1 == 39:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=432 - z * 18, y=144, width=18, height=54)
                        labelI = Label(Pan, bg="#ECC811", borderwidth=0)
                        labelI.place(x=434 - z * 18, y=146, width=14, height=50)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=432 - z * 18, y=144, width=18, height=54)
                        labelI = Label(Pan, bg="white", borderwidth=0)              # 682 --- 684 azul
                        labelI.place(x=434 - z * 18, y=146, width=14, height=50)
                    yF = 146
                    xF = 434 - z * 18
                elif x + 1 in [y1 for y1 in range(43, 51)]:
                    orientacion = "horizontal"
                    z = x - 42
                    if x + 1 == 46:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=252, y=126 - z * 18, width=54, height=18)
                        labelI = Label(Pan, bg="#ECC811", borderwidth=0)
                        labelI.place(x=254, y=128 - z * 18, width=50, height=14)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=252, y=126 - z * 18, width=54, height=18)
                        labelI = Label(Pan, bg="white", borderwidth=0)                  # 502 -- 504
                        labelI.place(x=254, y=128 - z * 18, width=50, height=14)
                    yF = 128 - z * 18
                    xF = 254
                elif x + 1 == 51:
                    orientacion = "horizontal"
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=198, y=0, width=54, height=18)                       # 448 -- 450
                    labelI = Label(Pan, bg="#2926DA", borderwidth=0)
                    labelI.place(x=200, y=2, width=50, height=14)
                    yF = 2
                    xF = 200
                elif x + 1 in [y1 for y1 in range(52, 60)]:
                    orientacion = "horizontal"
                    z = x - 51
                    if x + 1 == 56:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=144, y=z * 18, width=54, height=18)
                        labelI = Label(Pan, bg="#2926DA", borderwidth=0)
                        labelI.place(x=146, y=z * 18 + 2, width=50, height=14)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=144, y=z * 18, width=54, height=18)
                        labelI = Label(Pan, bg="white", borderwidth=0)                  # 394 -  396
                        labelI.place(x=146, y=z * 18 + 2, width=50, height=14)
                    yF = z * 18 + 2
                    xF = 146
                elif x + 1 in [y1 for y1 in range(60, 68)]:
                    orientacion = "vertical"
                    z = x - 59
                    if x + 1 == 63:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=126 - z * 18, y=144, width=18, height=54)
                        labelI = Label(Pan, bg="#2926DA", borderwidth=0)
                        labelI.place(x=128 - z * 18, y=146, width=14, height=50)
                    else:
                        labelF = Label(Pan, bg="black", borderwidth=0)
                        labelF.place(x=126 - z * 18, y=144, width=18, height=54)
                        labelI = Label(Pan, bg="white", borderwidth=0)                     # 376 -- 378
                        labelI.place(x=128 - z * 18, y=146, width=14, height=50)
                    yF = 146
                    xF = 128 - z * 18
                elif x + 1 == 68:
                    orientacion = "vertical"
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=0, y=198, width=18, height=54)
                    labelI = Label(Pan, bg="#ED0D0D", borderwidth=0)                        #250 -- 252
                    labelI.place(x=2, y=200, width=14, height=50)
                    yF = 200
                    xF = 252
            if x + 1 in [5, 22, 39, 56]:
                NuevaCasilla = Espacio(x + 1, labelI, xF, yF, "salida", "ninguno", orientacion)
            elif x + 1 in [12, 17, 29, 34, 46, 51, 63, 68]:
                NuevaCasilla = Espacio(x + 1, labelI, xF, yF, "seguro", "ninguno", orientacion)
            else:
                NuevaCasilla = Espacio(x + 1, labelI, xF, yF, 'normal', "ninguno", orientacion)
            tablero.append(NuevaCasilla)
        label = ""
        if mod > 1:
            label = Label(Pan, bg="#ED0D0D", borderwidth=0)
            label.place(x=0, y=306, height=144, width=144)
            label = Label(Pan, bg="white", borderwidth=0)           #250 --- 255    cuadro inicio rojo
            label.place(x=5, y=311, height=134, width=134)
        tablero.append(Espacio(69, label, 255, 311, "inicio", "rojo"))
        if mod > 1:
            label = Label(Pan, bg="#04B112", borderwidth=0)         # 556 --- 561   cuadro inicio verde
            label.place(x=306, y=306, height=144, width=144)
            label = Label(Pan, bg="white", borderwidth=0)
            label.place(x=311, y=311, height=134, width=134)
        tablero.append(Espacio(70, label, 561, 311, "inicio", "verde"))
        if mod > 1:
            label = Label(Pan, bg="#ECC811", borderwidth=0)
            label.place(x=306, y=0, height=144, width=144)
            label = Label(Pan, bg="white", borderwidth=0)           # 556 --- 561   cuadro inicio amarillo
            label.place(x=311, y=5, height=134, width=134)
        tablero.append(Espacio(71, label, 561, 5, "inicio", "amarillo"))
        if mod > 1:
            label = Label(Pan, bg="#2926DA", borderwidth=2)
            label.place(x=0, y=0, height=144, width=144)
            label = Label(Pan, bg="white", borderwidth=0)           #250 --- 255    cuadro inicio azul
            label.place(x=5, y=5, height=134, width=134)
        tablero.append(Espacio(72, label, 255, 5, "inicio", "azul"))
        for x in range(28):
            if x < 7:
                z = x
                if mod > 1:
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=z * 18 + 18, y=198, width=18, height=54)     #Casillas recta final rojo
                    labelF = Label(Pan, bg="#ED0D0D", borderwidth=0)
                    labelF.place(x=z * 18 + 20, y=200, width=14, height=50)
                NuevaCasilla = Espacio(72 + x + 1, labelF, z * 18 + 270, 200, "especial", "rojo", "vertical")
            elif x < 14:
                z = x - 7
                if mod > 1:
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=198, y=414 - z * 18, width=54, height=18)
                    labelF = Label(Pan, bg="#04B112", borderwidth=0)            #Casillas recta final verde
                    labelF.place(x=200, y=416 - z * 18, width=50, height=14)
                NuevaCasilla = Espacio(72 + x + 1, labelF, 450, 416 - z * 18, "especial", "verde", "horizontal")
            elif x < 21:
                z = x - 14
                if mod > 1:
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=414 - z * 18, y=198, width=18, height=54)
                    labelF = Label(Pan, bg="#ECC811", borderwidth=0)            #Casillas recta final amarillo
                    labelF.place(x=416 - z * 18, y=200, width=14, height=50)
                NuevaCasilla = Espacio(72 + x + 1, labelF, 666 - z * 18, 200, "especial", "amarillo", "vertical")
            else:
                z = x - 21
                if mod > 1:
                    labelF = Label(Pan, bg="black", borderwidth=0)
                    labelF.place(x=198, y=z * 18 + 18, width=54, height=18)
                    labelF = Label(Pan, bg="#2926DA", borderwidth=0)            #Casillas recta final azul
                    labelF.place(x=200, y=z * 18 + 20, width=50, height=14)
                NuevaCasilla = Espacio(72 + x + 1, labelF, 450, z * 18 + 20, "especial", "azul", "horizontal")
            tablero.append(NuevaCasilla)
        lab = ""
        if mod > 1:
            imagen = PhotoImage(file="img_dc\\dc_tab.gif")
            lab = Label(Pan, bg="black")
            lab.place(x=144, y=144, width=162, height=162)
            lab = Label(Pan, image=imagen)
            lab.img = imagen
            lab.place(x=149, y=149, width=152, height=152)

        tablero.append(Espacio(101, lab, 399, 149, "llegada"))
        #labelF.lift()

        return tablero