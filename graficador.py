from tkinter import *
from PIL import Image, ImageTk

from builder_tablero_dc import Builder_tablero_dc
from builder_tablero_marvel import Builder_tablero_marvel
from ficha import Ficha
from jugador import Jugador
from builder_tablero_mario import Builder_tablero_mario



class Graficador:

    global LABEL_NOMBRE_ESPACIO

    def __init__(self):
        self.Panel = Tk()
        self.Panel.configure(bg="blue")
        self.Panel.state('zoomed')
        self.Panel.title('PRINCIPAL')
        self.imgFichas = Ficha.imgFichas
        self.arregloDados = Jugador.arregloDados
        self.tableroMario = Builder_tablero_mario()
        self.tableroMarvel = Builder_tablero_marvel()
        self.tablerodc = Builder_tablero_dc()
        #arregloDados = {}
        fondo = Image.open("img_mario\\fondo_mario.gif")
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

        self.BTN = Button(self.Panel, text="INICIAR", font=("Comic Sans MS", 40), width=8, height=1, command=self.menu_tablero, borderwidth=10)
        self.BTN.pack(pady=100)

        self.BTN.bind("<Enter>", self.cambiar_color_rojo)
        self.BTN.bind("<Leave>", self.cambiar_color_normal)

        self.BTN_creditos = Button(self.Panel, text="Créditos", font=("Comic Sans MS", 40), width=8, height=1, command=self.mostrar_creditos, borderwidth=10)
        self.BTN_creditos.pack(pady=50)

        self.BTN_creditos.bind("<Enter>", self.cambiar_color_rojo_creditos)
        self.BTN_creditos.bind("<Leave>", self.cambiar_color_normal_creditos)


    def menu_tablero(self):
       self.LB.destroy()
       self.BTN.destroy()
       self.BTN_creditos.destroy()
       self.etiqueta_titulo = Label(self.Panel, text="SELECCIONE UN TABLERO", font=("Comic Sans MS", 40), bg="blue")
       self.etiqueta_titulo.pack(pady=10)

       self.boton_tab_mario = Button(self.Panel, text="Mario", command=lambda: self.continuar_juego_mario(self.tableroMario.nombres),
                                               font=("Comic Sans MS", 20), width=8, height=1, borderwidth=10)
       self.boton_tab_mario.pack(pady=5)

       self.boton_tab_mario.bind("<Enter>", self.cambiar_color_btnMARIO)
       self.boton_tab_mario.bind("<Leave>", self.cambiar_color_normal_btnMARIO)

       self.boton_tab_marvel = Button(self.Panel, text="Marvel", command=lambda: self.continuar_juego_marvel(self.tableroMarvel.nombres),
                                     font=("Comic Sans MS", 20), width=8, height=1, borderwidth=10)
       self.boton_tab_marvel.pack(pady=5)

       self.boton_tab_marvel.bind("<Enter>", self.cambiar_color_btnMARVEL)
       self.boton_tab_marvel.bind("<Leave>", self.cambiar_color_normal_btnMARVEL)

       self.boton_tab_dc = Button(self.Panel, text="DC", command=lambda: self.continuar_juego_dc(self.tablerodc.nombres),
                                     font=("Comic Sans MS", 20), width=8, height=1, borderwidth=10)
       self.boton_tab_dc.pack(pady=5)

       self.boton_tab_dc.bind("<Enter>", self.cambiar_color_btnDC)
       self.boton_tab_dc.bind("<Leave>", self.cambiar_color_normal_btnDC)









    def cambiar_color_rojo(self, event):
        self.BTN.config(bg="red")

    def cambiar_color_normal(self, event):
        self.BTN.config(bg="SystemButtonFace")

    def cambiar_color_rojo_creditos(self, event):
        self.BTN_creditos.config(bg="red")

    def cambiar_color_normal_creditos(self, event):
        self.BTN_creditos.config(bg="SystemButtonFace")

    def cambiar_color_btnMARIO(self, event):
        self.boton_tab_mario.config(bg="blue")

    def cambiar_color_normal_btnMARIO(self, event):
        self.boton_tab_mario.config(bg="SystemButtonFace")

    def cambiar_color_btnMARVEL(self, event):
        self.boton_tab_marvel.config(bg="yellow")

    def cambiar_color_normal_btnMARVEL(self, event):
        self.boton_tab_marvel.config(bg="SystemButtonFace")

    def cambiar_color_btnDC(self, event):
        self.boton_tab_dc.config(bg="purple")

    def cambiar_color_normal_btnDC(self, event):
        self.boton_tab_dc.config(bg="SystemButtonFace")



    def mostrar_creditos(self):
        ventana_creditos = Toplevel()
        ventana_creditos.title("Créditos")
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


    def continuar_juego_mario(self, nombres_jugadores):
        self.etiqueta_titulo.destroy()
        self.boton_tab_mario.destroy()
        self.boton_tab_marvel.destroy()
        self.boton_tab_dc.destroy()

        nombres = [nombre.get() for nombre in nombres_jugadores]  # Obtener los nombres de las variables de control

        print("Lista de jugadores:")
        for i, nombre in enumerate(nombres):
            print(f"Jugador {i + 1}: {nombre}")

        self.tableroMario.crear_widgets(self.LB, self.BTN, self.BTN_creditos, self.Panel)
        #self.tableroMario.pintar_tablero(self.Panel)


    def continuar_juego_marvel(self, nombres_jugadores):
        self.etiqueta_titulo.destroy()
        self.boton_tab_mario.destroy()
        self.boton_tab_marvel.destroy()
        self.boton_tab_dc.destroy()

        nombres = [nombre.get() for nombre in nombres_jugadores]  # Obtener los nombres de las variables de control

        print("Lista de jugadores:")
        for i, nombre in enumerate(nombres):
            print(f"Jugador {i + 1}: {nombre}")

        self.tableroMarvel.crear_widgets(self.LB, self.BTN, self.BTN_creditos, self.Panel)


    def continuar_juego_dc(self, nombres_jugadores):
        self.etiqueta_titulo.destroy()
        self.boton_tab_mario.destroy()
        self.boton_tab_marvel.destroy()
        self.boton_tab_dc.destroy()

        nombres = [nombre.get() for nombre in nombres_jugadores]  # Obtener los nombres de las variables de control

        print("Lista de jugadores:")
        for i, nombre in enumerate(nombres):
            print(f"Jugador {i + 1}: {nombre}")

        self.tablerodc.crear_widgets(self.LB, self.BTN, self.BTN_creditos, self.Panel)








