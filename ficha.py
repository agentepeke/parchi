from tkinter import Label, Tk, PhotoImage


class Ficha:  # Declara la clase ficha


    imgFichas = {}

    def __init__(self, Pan, nombreFicha, colorFicha, espacioActual,estadoJuego = "inicio"):

        #global mod
        self.colorFicha = colorFicha
        self.espacioActual = espacioActual
        self.estadoJuego = estadoJuego
        self.nombreFicha = nombreFicha
        self.espacioActual = espacioActual
        self.etiqueta = ""

        mod = 3


        if mod>1:
            self.etiqueta = Label(Pan, image = Ficha.imgFichas[colorFicha])
            self.etiqueta.img = Ficha.imgFichas[colorFicha]
            if self.espacioActual.NoFichas == 0:
                self.etiqueta.place(x = self.espacioActual.x - 210, y = self.espacioActual.y + 40,width = 14,height = 14)
                self.xI = self.espacioActual.x -210
                self.yI = self.espacioActual.y + 40
                print(self.espacioActual.x)
            elif self.espacioActual.NoFichas == 1:
                self.etiqueta.place(x=self.espacioActual.x - 170, y=self.espacioActual.y+40,width=14,height=14)
                self.xI = self.espacioActual.x - 170
                self.yI = self.espacioActual.y + 40
            elif self.espacioActual.NoFichas == 2:
                self.etiqueta.place(x=self.espacioActual.x - 210,y=self.espacioActual.y+80,width=14,height=14)
                self.xI = self.espacioActual.x - 210
                self.yI = self.espacioActual.y + 80
            elif self.espacioActual.NoFichas == 3:
                self.etiqueta.place(x=self.espacioActual.x - 170,y=self.espacioActual.y+80,width=14,height=14)
                self.xI = self.espacioActual.x - 170
                self.yI = self.espacioActual.y + 80
        self.espacioActual.NoFichas+=1
        self.etiqueta = self.etiqueta
        if mod>1:
            self.etiqueta.bind("<Enter>",self.Entra)
            self.etiqueta.bind("<Leave>",self.Sale)
        self.PosFicha = ""

    def Entra(self,event, L_NOMBRES):
        L_NOMBRES.config(text=self.nombreFicha)
    def Sale(self,event, L_NOMBRES):

        L_NOMBRES.config(text="NOMBRES")
    def imprimirPropiedades(self):
        """
        Returns the current state of the token
        @return: None
        """
        return "Ficha %s: color= %s espacio=%s estado=%s" % (
            self.nombreFicha, self.colorFicha, self.espacioActual.numeroEspacio, self.estadoJuego)
    def eliminarFicha(self):
        self.etiqueta.destroy()
    def cambiarPosicion(self, NuevoEspacio):
        """
        Actualiza la posicion
        """
        mod = 3
        self.espacioActual.NoFichas-=1
        if self.espacioActual.NoFichas==1 and self.PosFicha=="A":
          self.espacioActual.PosFicha="B"
        elif self.espacioActual.NoFichas==1 and self.PosFicha=="B":
          self.espacioActual.PosFicha="A"
        self.espacioActual = NuevoEspacio
        if self.espacioActual.tipoEspacio=="inicio":
            if mod>1:
                self.etiqueta.place(x=self.xI,y=self.yI)
        elif self.espacioActual.NoFichas==0 and self.espacioActual.orientacion=="vertical":
            if mod>1:
                self.etiqueta.place(x=self.espacioActual.x,y=self.espacioActual.y+7)
            self.espacioActual.PosFicha="A"
            self.PosFicha="A"
        elif self.espacioActual.NoFichas==0 and self.espacioActual.orientacion=="horizontal":
            if mod>1:
                self.etiqueta.place(x=self.espacioActual.x+7,y=self.espacioActual.y)
            self.espacioActual.PosFicha="A"
            self.PosFicha="A"
        elif self.espacioActual.NoFichas==1:
            if self.espacioActual.orientacion=="vertical" and self.espacioActual.PosFicha=="B":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x,y=self.espacioActual.y+7)
              self.PosFicha="A"
            elif self.espacioActual.orientacion=="vertical" and self.espacioActual.PosFicha=="A":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x,y=self.espacioActual.y+33)
              self.PosFicha="B"
            elif self.espacioActual.orientacion=="horizontal" and self.espacioActual.PosFicha=="B":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x+7,y=self.espacioActual.y)
              self.PosFicha="A"
            elif self.espacioActual.orientacion=="horizontal" and self.espacioActual.PosFicha=="A":
              if mod>1:
                  self.etiqueta.place(x=self.espacioActual.x+33,y=self.espacioActual.y)
              self.PosFicha="B"
        NuevoEspacio.NoFichas+=1
    def num(self):
        return self.nombreFicha