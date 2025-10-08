from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

class SudokuBoardWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(9, 9, parent)
        self.init_board()

    def init_board(self):
        self.setFixedSize(454, 454)
        self.setEditTriggers(self.AllEditTriggers)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        validator = QIntValidator(1, 9, self)
        for i in range(9):
            self.setColumnWidth(i, 50)
            self.setRowHeight(i, 50)
            for j in range(9):
                item = QTableWidgetItem("")
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(i, j, item)
                # Asigna un QLineEdit con validador a cada celda
                editor = QLineEdit(self)
                editor.setValidator(validator)
                editor.setAlignment(Qt.AlignCenter)
                self.setCellWidget(i, j, editor)

    def get_board(self):
        """Devuelve el tablero como una lista de listas de enteros."""
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                widget = self.cellWidget(i, j)
                text = widget.text() if widget else ""
                try:
                    val = int(text)
                    if 1 <= val <= 9:
                        row.append(val)
                    else:
                        row.append(0)
                except ValueError:
                    row.append(0)
            board.append(row)
        return board

    def set_board(self, board):
        """Carga un tablero (lista de listas) en el widget."""
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                widget = self.cellWidget(i, j)
                if widget:
                    widget.setText(str(val) if val != 0 else "")
                    # Colorea el fondo según el bloque 3x3
                    block_row = i // 3
                    block_col = j // 3
                    if (block_row + block_col) % 2 == 0:
                        color = "#ffffff"  # Blanco
                    else:
                        color = "#e0e0e0"  # Gris claro
                    widget.setStyleSheet(f"background-color: {color}; border: none;")