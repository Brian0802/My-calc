import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import math

calculation = ""

def add_to_calculation(symbol):
    global calculation
    if x_pow_y:
        print("yes")
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
        messagebox.showwarning(title="ERROR", message=f"Error: {e}")

def direct_calculation(operation):
    global calculation
    if calculation != "":
        try:
            if operation == 'sqrt':
                calculation = str(math.sqrt(eval(calculation)))
            elif operation == 'log':
                calculation = str(math.log10(eval(calculation)))
            elif operation == 'ln':
                calculation = str(math.log(eval(calculation)))
            elif operation == 'sin':
                calculation = str(math.sin(math.radians(eval(calculation))))
            elif operation == 'cos':
                calculation = str(math.cos(math.radians(eval(calculation))))
            elif operation == 'tan':
                calculation = str(math.tan(math.radians(eval(calculation))))
            elif operation == '**2':
                calculation = str(eval(calculation) ** 2)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        except Exception as e:
            clear_field()
            messagebox.showwarning(title="ERROR", message=f"{e}")

def x_pow_y():
    global calculation
    x = str(calculation)
    calculation = f"{x}**"
    text_result.delete(1.0, "end")
    return True

def backward():
    global calculation
    if calculation is not None:
        calculation = calculation[:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Initialize customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

window = ctk.CTk()
window.title("Calculator")
window.geometry("360x720")
window.resizable(False, False)

# Result display
text_result = ctk.CTkTextbox(window, 
                             height=50, 
                             width=320, 
                             font=("Arial", 30, "bold"), 
                             bg_color="black")
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Function to create custom buttons
def create_custom_button(text, command, row, column):
    button = ctk.CTkButton(window, 
                           text=text, 
                           command=command, 
                           font=("Arial", 20, "bold"), 
                           width=70, 
                           height=70)
    button.grid(row=row, column=column, padx=10, pady=10)

# Button Layout
buttons = [
    ('7', lambda: add_to_calculation(7)), ('8', lambda: add_to_calculation(8)), ('9', lambda: add_to_calculation(9)), ('/', lambda: add_to_calculation('/')),
    ('4', lambda: add_to_calculation(4)), ('5', lambda: add_to_calculation(5)), ('6', lambda: add_to_calculation(6)), ('*', lambda: add_to_calculation('*')),
    ('1', lambda: add_to_calculation(1)), ('2', lambda: add_to_calculation(2)), ('3', lambda: add_to_calculation(3)), ('-', lambda: add_to_calculation('-')),
    ('C', clear_field), ('0', lambda: add_to_calculation(0)), ('=', evaluate_calculation), ('+', lambda: add_to_calculation('+')),
    ('x²', lambda: direct_calculation('**2')), ('.', lambda: add_to_calculation('.')), ('(', lambda: add_to_calculation('(')), (')', lambda: add_to_calculation(')')),
    ('√', lambda: direct_calculation('sqrt')), ('log', lambda: direct_calculation('log')), ('ln', lambda: direct_calculation('ln')), ('sin', lambda: direct_calculation('sin')),
    ('cos', lambda: direct_calculation('cos')), ('tan', lambda: direct_calculation('tan')), ('x^y', lambda: x_pow_y()),('<-',lambda: backward())
]

for i, (text, cmd) in enumerate(buttons):
    create_custom_button(text, cmd, row=i//4+1, column=i%4)

window.bind("<Key-Escape>",lambda event: window.destroy())
window.bind("<c>", lambda event: clear_field())

if __name__ == '__main__':
    window.mainloop()
