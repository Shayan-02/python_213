import tkinter as tk

def click(item):
    cur = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, cur + str(item))
       
def clear():
    entry_field.delete(0, tk.END)
       
def equal():
    exp = entry_field.get()
    if expression(exp):
        try:
            result = str(eval(exp))
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, result)
        except ZeroDivisionError:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "cannot divide by 0")
    else:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "error")
                 
def expression(exp):
    valid_chars = "0123456789+-/*()"
    for char in exp:
        if char not in valid_chars:
            return False
    return True
       
w = tk.Tk()
w.title("Calculator")
w.configure(bg="#fef1f4")

entry_field = tk.Entry(w, font=('Arial', 18), bd=10, insertwidth=4, width=14)
entry_field.grid(row=0, column=0, columnspan=4)              
color_digit = "#f8baca"
color_operator = "#f17b99"
color_clear = "#ffffff"

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "C":
        tk.Button(w, text=button, padx=20, pady=20, font=('arial', 18), command=clear, bg=color_clear).grid(row=row, column=col)
    elif button == "=":
        tk.Button(w, text=button, padx=20, pady=20, font=('arial', 18), command=equal, bg=color_operator).grid(row=row, column=col)
    else:
        tk.Button(w, text=button, padx=20, pady=20, font=('arial', 18), command=lambda item=button: click(item), bg=color_digit).grid(row=row, column=col)
           
    col += 1
    if col > 3:
        col = 0
        row += 1
            
w.mainloop()
