import tkinter as tk
import random 



#initialize the game
def initialize_game():
    board = [[0] * 4 for _ in range(4)]
    spawn_new_tile(board)
    spawn_new_tile(board)
    return board

#add a new tile (2 or 4) to a random free spot
def spawn_new_tile(board):
    empty_tiles = [(r,c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = random.choice([2,4])

def move_left(board):
    global score
    for r in range(4):
        #remove all the zeros from the row
        new_row = [x for x in board[r] if x != 0]
        #merge the tiles
        i=0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                score += new_row[i]  # Add the score when merging
                new_row.pop(i+1)
            i += 1
        board[r] = new_row + [0] * (4 - len(new_row))


# Move the tiles based on the direction
def move(board, direction):
    if direction == "Left":
        move_left(board)
    elif direction == "Right":
        # Reverse rows, move left, reverse rows back
        for r in range(4):
            board[r] = list(board[r])[::-1]  # Reverse each row
        move_left(board)
        for r in range(4):
            board[r] = list(board[r])[::-1]  # Reverse each row
    elif direction == "Up":
        # Transpose, move left, transpose back
        board[:] = [list(row) for row in zip(*board)]  # Convert tuples back to lists
        move_left(board)
        board[:] = [list(row) for row in zip(*board)]  # Convert tuples back to lists
    elif direction == "Down":
        # Transpose, reverse rows, move left, reverse rows, transpose back
        board[:] = [list(row) for row in zip(*board)]  # Convert tuples back to lists
        for r in range(4):
            board[r] = list(board[r])[::-1]  # Reverse each row
        move_left(board)
        for r in range(4):
            board[r] = list(board[r])[::-1]  # Reverse rows back
        board[:] = [list(row) for row in zip(*board)]  # Convert tuples back to lists


#check if the game is over
def is_game_over(board):
    #check for any empty spaces or possible moves
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return False
            if r<3 and board[r][c] == board[r + 1][c]:
                return False
            if r>1 and board[r][c] == board[r - 1][c]:
                return False
            if c<3 and board[r][c] == board[r ][c + 1]:
                return False
            if c>1 and board[r][c] == board[r ][c - 1]:
                return False
    return True

#handle keypress to move tiles
def on_keypress(event, board, canvas, score_label, high_score_label):
    global score, high_score
    direction = None
    if event.keysym == "Left":
        direction = "Left"
    elif event.keysym == "Right":
        direction = "Right"
    elif event.keysym == "Up":
        direction = "Up"
    elif event.keysym == "Down":
        direction = "Down"
    
    if direction:
        #print(direction)
        move(board, direction)
        spawn_new_tile(board)
        update_display(board, canvas, score_label, high_score_label)

        if is_game_over(board):
            canvas.delete("all")
            canvas.create_text(200,  200, text = "Game Over!", font = ("Arial", 32, "bold"), fill = "red")
    
         # Update the score label
        score_label.config(text=f"Score: {score}")

        # Update the high score if necessary
        if score > high_score:
            high_score = score
            high_score_label.config(text=f"High Score: {high_score}")

    


def update_display(board, canvas, score_label, high_score_label):
    canvas.delete("all")
    for r in range(4):
        for c in range(4):
            x1, y1 = c*100, r*100
            x2, y2 = x1 + 100, y1 + 100
            value = board[r][c]
            color = "lightgray" if value == 0 else "#eee4da" if value == 2 else "#ede0c8" if value == 4 else "#f2b179" if value == 8 else "#f59563" if value == 16 else "#f67c5f" if value == 32 else "#f65e3b" if value == 64 else "#edcf72" if value == 128 else "#edcc61" if value == 256 else "#edc850" if value == 512 else "#edb83d" if value == 1024 else "#ed9c2e" if value == 2048 else "#ccc0b3"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width = 2)
            if value !=0: #if not 0 then display the value
                canvas.create_text(x1 + 50, y1 + 50, text = str(value), font = ("Arial", 24, "bold"))





#tkinter setup
root = tk.Tk()
root.title("2048")

#create the canvas to display the grid
canvas = tk.Canvas(root, width = 400, height = 400)
canvas.pack()

# Create score and high score labels
score = 0
high_score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
score_label.pack()

high_score_label = tk.Label(root, text=f"High Score: {high_score}", font=("Arial", 16))
high_score_label.pack()

#initialize the game and set up the keyboard bindings
board = initialize_game()
update_display(board, canvas, score_label, high_score_label)
root.bind("<KeyPress>", lambda event: on_keypress(event, board, canvas, score_label, high_score_label))

root.mainloop()







