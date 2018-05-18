import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont #Modulo para trabajar con fuentes 
from PyQt5.QtCore import Qt # modulo para modificar el cursor
import ctypes #GetSystemMetrics permite saber el tamano del escritorio


#Clase heredada de QMainWindows(constructor de ventana)
class Ventana(QMainWindow):
    #Metodo constructor de la clase
    def __init__(self):
        #Iniciar el objeto QmainWindows
        QMainWindow.__init__(self)
        #Cargar la configuracion del archivo .uic en el objeto
        uic.loadUi("main_windows.ui", self)
        self.setWindowTitle("Ventana Principal")
        #Mostar la ventana maximizada
        self.showMaximized()
        #Fijar el tamano de la ventana
        #fijar el tamao minimo
        self.setMinimumSize(500,500)
        #Fijar el tamano maximo
        self.setMaximumSize(500,500)
        # mover la ventana y centrarla en el escritorio
        resolucion =ctypes.windll.user32
        resolucion_ancho= resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2 )
        top = (resolucion_alto / 2) - (self.frameSize().height() / 2)
        self.move(left, top)
        #Desactivar la ventana
        #self.setEnabled(False)
        #ASignar un tipo de fuente
        qfont = QFont("Arial", 12, QFont.Bold)
        self.setFont(qfont)
        #Asignar un tipo de cursor
        self.setCursor(Qt.SizeAllCursor)
        #Asignar estilos CSS
        #self.setStyleSheet("Background-color: #000; color: #fff;")
        #Modificar el boton
        self.boton.setStyleSheet("Background-color: #000; color: #fff; font-size: 14px;")

    #Dar Mensaje de bienvenida al abrir ventana
    def showEvent(self, event):
        self.bienvenida.setText("Bienvenido!!!")
    
    #Dar mensaje de advertyencia al cerrar la ventana
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir ...", "Seguro que quieres salir de la apliacion?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #
    def moveEvent(self, event):
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.posicion.setText("x:" + str(x) + "y: " + str(y) )

#instancia para iniciar una aplicacion
app = QApplication(sys.argv)
_ventana = Ventana()
#mostrar la ventana
_ventana.show()
#ejecutar la aplicacion
app.exec_()
