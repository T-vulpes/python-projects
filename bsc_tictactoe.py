import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe ")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.player = "X"

        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root, text="", font=("Arial", 40), width=5, height=2,
                    command=lambda r=row, c=col: self.player_move(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        if self.board[row][col] == "" and self.check_winner() is None:
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled")
            if self.check_winner():
                self.end_game("Oyuncu (X) kazandı!")
                return
            elif self.is_board_full():
                self.end_game("Berabere!")
                return
            self.root.after(500, self.computer_move)

    def computer_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3)
                       if self.board[r][c] == ""]
        if not empty_cells:
            return
        row, col = random.choice(empty_cells)
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O", state="disabled")

        if self.check_winner():
            self.end_game("Bilgisayar (O) kazandı!")
        elif self.is_board_full():
            self.end_game("Berabere!")

    def check_winner(self):
        b = self.board
        # Satırlar ve sütunlar
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]
        # Çaprazlar
        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]
        return None

    def is_board_full(self):
        return all(self.board[row][col] != ""
                   for row in range(3) for col in range(3))

    def end_game(self, message):
        messagebox.showinfo("Oyun Bitti", message)
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

