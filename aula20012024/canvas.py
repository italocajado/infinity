import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

canvas.create_rectangle(10, 10, 100, 60, fill='blue')

root.mainloop()
