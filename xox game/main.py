import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=0, column=0, rowspan=3, columnspan=3)
        self.draw_grid()

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font='normal 20 bold', width=5, height=2, 
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)
        
        self.reset_button = tk.Button(self.root, text="Reset", font='normal 12 bold', command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3)

    def draw_grid(self):
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, fill='black', width=3)
            self.canvas.create_line(i * 100, 0, i * 100, 300, fill='black', width=3)

    def on_button_click(self, i, j):
        index = i * 3 + j
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, 
                                       fg="black" if self.current_player == "X" else "red")
            if self.check_winner():
                self.draw_winner_line()
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif None not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_indices = [i for i, val in enumerate(self.board) if val is None]
        move = random.choice(empty_indices)
        i, j = divmod(move, 3)
        self.on_button_click(i, j)

    def check_winner(self):
        self.win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                               (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                               (0, 4, 8), (2, 4, 6)]
        for condition in self.win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == self.current_player:
                self.winning_combo = condition
                return True
        return False

    def draw_winner_line(self):
        line_coords = [
            (50, 10, 50, 290), (150, 10, 150, 290), (250, 10, 250, 290),  # Vertical lines
            (10, 50, 290, 50), (10, 150, 290, 150), (10, 250, 290, 250),  # Horizontal lines
            (10, 10, 290, 290), (10, 290, 290, 10)  # Diagonal lines
        ]
        for i, condition in enumerate(self.win_conditions):
            if condition == self.winning_combo:
                self.canvas.create_line(*line_coords[i], fill='yellow', width=5)

    def reset_game(self):
        self.board = [None] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")
        self.canvas.delete("all")
        self.draw_grid()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
