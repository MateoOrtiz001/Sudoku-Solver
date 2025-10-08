from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer
from .sudokuBoard import SudokuBoardWidget
from .estilos import *

class StepByStepWindow(QDialog):
    def __init__(self, board, acciones, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resolución paso a paso")
        self.setFixedSize(500, 650)
        self.acciones = acciones
        self.board = [row[:] for row in board]
        self.step = 0

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.sudoku_board = SudokuBoardWidget()
        self.sudoku_board.set_board(self.board)
        self.sudoku_board.setDisabled(True)
        layout.addWidget(self.sudoku_board)

        self.info_label = QLabel(f"Paso 0 de {len(self.acciones)}")
        set_label_color(self.info_label, color="#FFF")
        layout.addWidget(self.info_label)

        self.next_btn = QPushButton("Siguiente paso")
        self.next_btn.clicked.connect(self.next_step)
        set_button_style(self.next_btn)
        layout.addWidget(self.next_btn)

        self.last_btn = QPushButton("Sudoku Resuelto")
        self.last_btn.clicked.connect(self.last_step)
        set_button_style(self.last_btn)
        layout.addWidget(self.last_btn)

        self.back_btn = QPushButton("Volver")
        self.back_btn.clicked.connect(self.close)
        set_button_style(self.back_btn)
        layout.addWidget(self.back_btn)

    def next_step(self):
        if self.step < len(self.acciones):
            i, j, value = self.acciones[self.step]
            self.board[i][j] = value
            self.sudoku_board.set_board(self.board)
            self.step += 1
            self.info_label.setText(f"Paso {self.step} de {len(self.acciones)}")
        if self.step == len(self.acciones):
            self.next_btn.setDisabled(True)
            self.info_label.setText("¡Sudoku resuelto!")
            
    def last_step(self):
        while self.step < len(self.acciones):
            i, j, value = self.acciones[self.step]
            self.board[i][j] = value
            self.step += 1
        self.sudoku_board.set_board(self.board)
        self.next_btn.setDisabled(True)
        self.last_btn.setDisabled(True)
        self.info_label.setText("¡Sudoku resuelto!")