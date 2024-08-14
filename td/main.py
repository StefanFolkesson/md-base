import tkinter as tk
import functions as f
import time
import random

# Create a window
window = tk.Tk()

# Create a canvas
canvas = tk.Canvas(window, width=850, height=600)
canvas.pack()

# Get the time right now
timer = time.time()

# Create a label to display the timer
timer_label = tk.Label(window, text="00:00", font=("Arial", 24))
timer_label.pack()

# Define a function to update the timer
# general variables
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
       [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
       [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
       [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1],
       [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
       [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
points = [(1,1),(15,1),(15,9),(1,9),(1,3),(13,3),(13,7),(3,7),(3,5),(11,5)]
buttons=[]  #array to store the keys pressed
enemyarray = [] #array to store enemys
turretarray=[]

for i in range(10):
    y=random.randint(100,400)
    enemyarray.append({"sq":canvas.create_rectangle(100, y, 30, y+30, fill="blue"),"health":100,"speed":7,"targetpoint":0,"effect":["",0],"h_bar":canvas.create_rectangle(100, y-6, 30, y-1, fill="green")})    
# Create an array of 40 random points for the square to follow
#points = [(random.randint(100,600),random.randint(100,400)) for i in range(40)]



window.bind("<Key>",lambda event:f.on_key(event,buttons))
window.bind("<KeyRelease>",lambda event:f.on_key_up(event,buttons))
canvas.bind("<Button-1>",lambda event:f.on_click(event,enemyarray,turretarray,canvas,buttons))
window.after(100, f.update_timer, timer, timer_label)
window.after(100, f.move_square, canvas, enemyarray, points)
window.after(100, f.target, canvas, enemyarray, turretarray)
f.draw_map(canvas, map)
window.mainloop()
