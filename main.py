import tkinter as tk
import random

def play_game(player_choice):
    computer = random.choice([1, -1, 0])
    youDict = {"snake": 1, "water": -1, "gun": 0}
    reverseDict = {1: "snake", -1: "water", 0: "gun"}

    you = youDict[player_choice]
    result_text.set(f"You choose: {reverseDict[you]} \nComputer choose: {reverseDict[computer]}")

    if computer == you:
        result.set("Draw")
    else:
        if computer == -1 and you == 1:
            result.set("You win")
        elif computer == -1 and you == 0:
            result.set("You lose")
        elif computer == 1 and you == -1:
            result.set("You lose")
        elif computer == 1 and you == 0:
            result.set("You win")
        elif computer == 0 and you == 1:
            result.set("You lose")
        elif computer == 0 and you == -1:
            result.set("You win")

# Create the main window
window = tk.Tk()
window.title("Snake, Water, Gun Game")

# Variable to store result
result_text = tk.StringVar()
result = tk.StringVar()

# Create buttons for user choice
btn_snake = tk.Button(window, text="Snake", width=15, command=lambda: play_game("snake"))
btn_water = tk.Button(window, text="Water", width=15, command=lambda: play_game("water"))
btn_gun = tk.Button(window, text="Gun", width=15, command=lambda: play_game("gun"))

# Place buttons on the window
btn_snake.pack(pady=10)
btn_water.pack(pady=10)
btn_gun.pack(pady=10)

# Display the result
result_label = tk.Label(window, textvariable=result_text, font=("Helvetica", 14))
result_label.pack()

# Display the win/lose/draw result
final_result = tk.Label(window, textvariable=result, font=("Helvetica", 16, "bold"))
final_result.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
