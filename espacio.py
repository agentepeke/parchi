class Espacio():

    def __init__(self, numeroEspacio, etiqueta, x, y, tipoEspacio="normal", colorCasillaEspecial="ninguno", orientacion="Ninguna", label_nombre=None):

        self.colorCasillaEspecial = colorCasillaEspecial
        self.tipoEspacio = tipoEspacio
        self.numeroEspacio = numeroEspacio
        self.etiqueta = etiqueta
        self.label_nombre = label_nombre

        self.etiqueta.bind("<Enter>", self.Entra)
        self.etiqueta.bind("<Leave>", self.Sale)
        self.orientacion = orientacion
        self.NoFichas = 0
        self.PosFicha = ""
        self.x = x
        self.y = y

    def Entra(self, event):
        numero_espacio = self.numeroEspacio
        text = str(self.numeroEspacio)

        if self.label_nombre is not None:
            self.label_nombre.config(text=str(numero_espacio))


    def Sale(self, event):
        if self.label_nombre is not None:
            self.label_nombre.config(text="Espacio")