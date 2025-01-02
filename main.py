import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x350")
        self.window.resizable(False, False)

        self.current_player = "X"

        self.board = ["" for _ in range(9)]
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        # Title label
        title = tk.Label(self.window, text="Tic Tac Toe", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Game board
        board_frame = tk.Frame(self.window)
        board_frame.pack()

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    board_frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda idx=(i * 3 + j): self.make_move(idx)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        # Reset button
        reset_button = tk.Button(self.window, text="Reset", font=("Arial", 12), command=self.reset_game)
        reset_button.pack(pady=10)

    def make_move(self, idx):
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
