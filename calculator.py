import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#1e1e2e")  # background color

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Function to handle button clicks
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        action = button_clear
    else:
        action = lambda x=text: button_click(x)
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
              bg="#3a3a4a", fg="white", command=action).grid(row=row, column=col, padx=5, pady=5)

# Equal button
tk.Button(root, text="=", width=22, height=2, font=("Arial", 14),
          bg="#4caf50", fg="white", command=button_equal).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the app
root.mainloop()
