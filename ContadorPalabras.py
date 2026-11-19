import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.ContarPalabras)

    def on_text_change(self):
        print("sd")

    def ContarPalabras(self):
        #Recuperar Texto
        texto = self.edtCaracteres.text()
        #separar las palabras
        textoSeparado = texto.split()
        print(textoSeparado)
        
        print("Se ha de presionar el boton")

        CantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"palabras: {CantidadPalabras}")
        num_caracteres=len(texto)
        totalCaracteres = 0
        for palabras in textoSeparado:
            totalCaracteres += len(palabras)
        self.tvCaracteres.setText(f"caracteres: {totalCaracteres}")

# Estas líneas deben ir fuera de la clase (sin espacios a la izquierda):
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())