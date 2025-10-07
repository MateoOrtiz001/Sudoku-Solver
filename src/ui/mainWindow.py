from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, solver_agent):
        super().__init__()
        self.solver_agent = solver_agent
        self.current_board = None
        self.init_ui()
        self.connect_signals()
        
    def init_ui(self):
        self.setWindowTitle("Solucionador de Sudoku - Agente A*")
        self.setGeometry(100, 100, 900, 700)
    