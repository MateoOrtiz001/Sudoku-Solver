from src import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/icono.ico"))
    window = MainWindow()  
    window.show()
    sys.exit(app.exec_())