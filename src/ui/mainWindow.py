from PyQt5.QtWidgets import QHBoxLayout, QFrame, QMainWindow, QWidget,QGridLayout,QLabel, QPushButton, QMessageBox, QSlider
from .sudokuBoard import SudokuBoardWidget
from .moduloSolucionador import StepByStepWindow
from .estilos import *
from src.sudokuClase.problem import SudokuProblem
from src.agentes.astar import aStarSearch
from src.agentes.heuristica import sudokuHeuristic
import sudoku, time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_board = None
        self.dificultad = 0.5
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Solucionador de Sudoku")
        self.setFixedSize(900, 700)
        self.setStyleSheet("background-color: #393939;")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)

        titulo_frame = QFrame()
        titulo_frame.setStyleSheet("background-color: #1E1E1E; border-radius: 2px;height: 40px;")
        titulo_layout = QHBoxLayout(titulo_frame)
        #titulo_layout.setContentsMargins(10, 10, 10, 10)
        titulo_layout.setAlignment(Qt.AlignCenter)
        titulo_frame.setFixedHeight(130)

        titulo = QLabel("Sudoku Solver")
        set_label_font(titulo, font_family="Verdana", font_size=35, bold=True)
        set_label_color(titulo, color="#ffffff")
        set_label_alignment(titulo, alignment="center")
        set_label_margin(titulo, margin=5)
        titulo_layout.addWidget(titulo)
        layout.addWidget(titulo_frame, 0, 0, 1, 2) 
        
        layout.setColumnStretch(0, 3)
        layout.setColumnStretch(1, 1)
        self.sudoku_board = SudokuBoardWidget()
        self.sudoku_board.setStyleSheet("border: 2px solid #1E1E1E;")  
        self.sudoku_board.set_board([[0]*9 for _ in range(9)])  # Tablero vacío inicial
        layout.addWidget(self.sudoku_board, 1, 0, 6, 1)  # Tablero de Sudoku

        texto = QLabel("Introduce un Sudoku y presiona 'Resolver'\n o 'Generar Nuevo' para un nuevo puzzle. ")
        set_label_font(texto, font_family="Arial", font_size=12)
        set_label_color(texto, color="#FFF")
        set_label_alignment(texto, alignment="center")
        set_label_margin(texto, margin=5)
        layout.addWidget(texto, 1, 1, 1, 1) 
        
        self.slider_label = QLabel("Dificultad: Media (0.5)")
        set_label_font(self.slider_label, font_family="Arial", font_size=12)
        set_label_color(self.slider_label, color="#FFF")
        set_label_alignment(self.slider_label, alignment="center")
        layout.addWidget(self.slider_label, 2, 1, 1, 1)

        self.dificultad_slider = QSlider(Qt.Horizontal)
        self.dificultad_slider.setMinimum(10)
        self.dificultad_slider.setMaximum(95)
        self.dificultad_slider.setValue(50)
        self.dificultad_slider.setTickInterval(5)
        self.dificultad_slider.setTickPosition(QSlider.TicksBelow)
        self.dificultad_slider.valueChanged.connect(self.actualizar_dificultad)
        layout.addWidget(self.dificultad_slider, 3, 1, 1, 1)

        # Botón Generar Sudoku
        boton_generar = QPushButton("Generar Nuevo")
        set_button_style(boton_generar)
        layout.addWidget(boton_generar, 4, 1)
        boton_generar.clicked.connect(self.generar_sudoku)
        
        boton_resolver = QPushButton("Resolver")
        set_button_style(boton_resolver)
        layout.addWidget(boton_resolver, 5, 1) 
        boton_resolver.clicked.connect(self.resolver_sudoku)
        
    def resolver_sudoku(self):
        board = self.sudoku_board.get_board()
        problem = SudokuProblem(startState=board)
        acciones = aStarSearch(problem, sudokuHeuristic)
        if not acciones:
            QMessageBox.warning(self, "Sin solución", "No se pudo encontrar una solución para este Sudoku.")
            return
        paso_a_paso = StepByStepWindow(board, acciones, parent=self)
        paso_a_paso.exec_()
        
    def generar_sudoku(self):
        seed = int(time.time())
        puzzle = sudoku.Sudoku(3, 3,seed=seed).difficulty(self.dificultad)  # 0.5 es dificultad media
        board = puzzle.board
        board = [[cell if cell is not None else 0 for cell in row] for row in board]
        self.sudoku_board.set_board(board)
        
    def actualizar_dificultad(self, value):
        self.dificultad = value / 100
        if self.dificultad < 0.33:
            nivel = "Fácil"
        elif self.dificultad < 0.66:
            nivel = "Media"
        else:
            nivel = "Difícil"
        self.slider_label.setText(f"Dificultad: {nivel} ({self.dificultad:.2f})")
