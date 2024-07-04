from tkinter import *
import math  # Importing math module for sqrt, log, etc.

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_field()
        text_result.insert("end", "Error: " + str(e))

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def create_round_button(canvas, x, y, text, command):
    r = 30  # reduced radius of the circle
    button = canvas.create_oval(x-r, y-r, x+r, y+r, fill="gray", outline="black")
    label = canvas.create_text(x, y, text=text, font=("Helvetica", 20), fill="white")
    canvas.tag_bind(button, "<Button-1>", lambda e: command())
    canvas.tag_bind(label, "<Button-1>", lambda e: command())

root = Tk()
root.title("Calculator v2.0")
root.geometry("400x600")

canvas = Canvas(root, width=400, height=600)
canvas.pack()

# Create text result area
text_result = Text(root, height=2, width=24, font=("Helvetica", 28), bd=0, bg="black", fg="white")
text_result_window = canvas.create_window(200, 50, window=text_result, anchor="center")

buttons = [
    ('7', lambda: add_to_calculation(7)),
    ('8', lambda: add_to_calculation(8)),
    ('9', lambda: add_to_calculation(9)),
    ('/', lambda: add_to_calculation('/')),
    ('4', lambda: add_to_calculation(4)),
    ('5', lambda: add_to_calculation(5)),
    ('6', lambda: add_to_calculation(6)),
    ('*', lambda: add_to_calculation('*')),
    ('1', lambda: add_to_calculation(1)),
    ('2', lambda: add_to_calculation(2)),
    ('3', lambda: add_to_calculation(3)),
    ('-', lambda: add_to_calculation('-')),
    ('C', clear_field),
    ('0', lambda: add_to_calculation(0)),
    ('=', evaluate_calculation),
    ('+', lambda: add_to_calculation('+')),
    ('x²', lambda: add_to_calculation('**2')),
    ('.', lambda: add_to_calculation('.')),
    ('(', lambda: add_to_calculation('(')),
    (')', lambda: add_to_calculation(')')),
    ('√', lambda: add_to_calculation('math.sqrt(')),
    ('^', lambda: add_to_calculation('**')),
    ('log', lambda: add_to_calculation('math.log(')),
    ('ln', lambda: add_to_calculation('math.log(')),
    ('sin', lambda: add_to_calculation('math.sin(')),
    ('cos', lambda: add_to_calculation('math.cos(')),
    ('tan', lambda: add_to_calculation('math.tan(')),
]

# Positions for buttons in grid layout
positions = [
    (70, 150), (150, 150), (230, 150), (310, 150),
    (70, 230), (150, 230), (230, 230), (310, 230),
    (70, 310), (150, 310), (230, 310), (310, 310),
    (70, 390), (150, 390), (230, 390), (310, 390),
    (70, 470), (150, 470), (230, 470), (310, 470),
    (70, 550), (150, 550), (230, 550), (310, 550),
]

for (text, command), (x, y) in zip(buttons, positions):
    create_round_button(canvas, x, y, text, command)

root.mainloop()
