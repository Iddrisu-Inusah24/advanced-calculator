import tkinter as tk
from tkinter import ttk, messagebox
from modules import Mat_utils, sci_utils

def insert_text(value):
    display_var.set(display_var.get() + str(value))

def clear_display():
    display_var.set("")


def backspace():
    current = display_var.get()
    display_var.set(current[:-1])

def calculate_expression():
    try:
        expr = display_var.get()
        # For now, eval() will handle it
        result = eval(expr)
        display_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def insert_ans():
    if last_answer is not None:
        entry.insert(tk.END, str(last_answer))

# --- GUI ---
root = tk.Tk()
root.title("Calculator (Step 2)")
root.geometry("300x400")

# Display
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10)

# Buttons frame
btn_frame = ttk.Frame(root)
btn_frame.pack()


# buttons styling
style = ttk.Style()
style.theme_use("clam")

style.configure("Digit.TButton", font=("Arial", 14), padding=10)
style.configure("Op.TButton", font=("Arial", 14, "bold"), padding=10, foreground="blue")
style.configure("Sci.TButton", font=("Arial", 12, "italic"), padding=10, foreground="green")
style.configure("Action.TButton", font=("Arial", 14, "bold"), padding=10, foreground="red")

# Button layout (digits + operators + scientific)
ans_button = ttk.Button(root, text="Ans", command=insert_ans)
buttons = [
    # Row 1: Clear + Backspace + Divide + Multiply
    ("C", 1, 0), ("⌫", 1, 1), ("/", 1, 2), ("*", 1, 3),

    # Row 2: Square root, power, factorial, modulus
    ("√", 2, 0), ("^", 2, 1), ("!", 2, 2), ("%", 2, 3),

    # Row 3: sin, cos, tan, parentheses
    ("sin", 3, 0), ("cos", 3, 1), ("tan", 3, 2), ("()", 3, 3),

    # Row 4: 7, 8, 9, Minus
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("-", 4, 3),

    # Row 5: 4, 5, 6, Plus
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("+", 5, 3),

    # Row 6: 1, 2, 3, Equals
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("=", 6, 3),

    # Row 7: 0 (spans 2 cols), ., Ans
    ("0", 7, 0 ), (".", 7, 1), ("Ans", 7, 2, 2),
]


# Configure grid weights so buttons expand evenly
for i in range(8):   # rows
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):   # columns
    btn_frame.columnconfigure(j, weight=1)



for btn in buttons:
    if len(btn) == 3:
        text, row, col = btn
        colspan = 1
    else:
        text, row, col, colspan = btn

    # Assign style
    if text.isdigit() or text == ".":
        btn_style = "Digit.TButton"
    elif text in ["+", "-", "*", "/", "="]:
        btn_style = "Op.TButton"
    elif text in ["√", "^", "!", "sin", "cos", "tan"]:
        btn_style = "Sci.TButton"
    else:  # C, ⌫
        btn_style = "Action.TButton"

    # Actions
    if text == "=":
        action = calculate_expression
    elif text == "C":
        action = clear_display
    elif text == "⌫":
        action = backspace
    else:
        action = lambda t=text: insert_text(t)

    ttk.Button(
        btn_frame, text=text, command=action, style=btn_style
    ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)
root.mainloop()