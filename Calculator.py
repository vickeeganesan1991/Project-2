from tkinter import *
import math

expr = ""

# ================= 3D BUTTON CLASS =================
class Button3D(Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.default_relief = "raised"
        self.default_bd = 4

        self.config(
            relief=self.default_relief,
            bd=self.default_bd,
            bg="#e0e0e0",
            activebackground="#d0d0d0",
            font=("Calibri", 14, "bold")
        )

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.config(relief="sunken", bd=3)

    def on_release(self, event):
        self.config(relief="raised", bd=4)


def key_input(event):
    key = event.keysym

    # --------------- NUMBERS ----------------
    if key in ["0","1","2","3","4","5","6","7","8","9"]:
        press(key)

    # NUMPAD numbers
    elif key in ["KP_0","KP_1","KP_2","KP_3","KP_4",
                 "KP_5","KP_6","KP_7","KP_8","KP_9"]:
        press(key[-1])   # KP_5 → "5"

    # --------------- OPERATORS ----------------
    elif key in ["plus","KP_Add"]:
        press("+")

    elif key in ["minus","KP_Subtract"]:
        press("-")

    elif key in ["asterisk","KP_Multiply"]:
        press("*")

    elif key in ["slash","KP_Divide"]:
        press("/")

    # --------------- ENTER AS "=" -------------
    elif key in ["Return","KP_Enter"]:
        press("=")

    # --------------- BACKSPACE ----------------
    elif key == "BackSpace":
        press("⌫")

    # --------------- DELETE AS AC -------------
    elif key == "Delete":
        press("AC")

# ===================== CALCULATOR LOGIC =====================
def press(key):
    global expr
    try:
        # ----- STANDARD OPERATIONS -----
        if key == "=":
            # result = str(eval(expr))
            # display.set(result)
            # expr = result
            result = str(eval(expr))
            entry.configure(state="normal")
            display.set(result)
            entry.configure(state="readonly")
            expr = result


        elif key == "AC":
            expr = ""
            display.set("")

        elif key == "⌫":
            expr = expr[:-1]
            display.set(expr)

        elif key == "𝑥²":
            expr = str(eval(expr + "**2"))
            display.set(expr)

        elif key == "𝑥³":
            expr = str(eval(expr + "**3"))
            display.set(expr)

        elif key == "√𝑥":
            expr = str(math.sqrt(eval(expr)))
            display.set(expr)

        elif key == "∛𝑥":
            expr = str(eval(expr) ** (1/3))
            display.set(expr)

        elif key == "1/𝑥":
            expr = str(1 / eval(expr))
            display.set(expr)

        elif key == "log10":
            expr = str(math.log10(eval(expr)))
            display.set(expr)

        elif key == "eˣ":
            expr = str(math.exp(eval(expr)))
            display.set(expr)

        elif key == "π":
            expr += str(math.pi)
            display.set(expr)

        # ---------- Trigonometry ------------
        elif key == "sin":
            expr = str(math.sin(math.radians(eval(expr))))
            display.set(expr)

        elif key == "cos":
            expr = str(math.cos(math.radians(eval(expr))))
            display.set(expr)

        elif key == "tan":
            expr = str(math.tan(math.radians(eval(expr))))
            display.set(expr)

        elif key == "asin":
            expr = str(math.degrees(math.asin(eval(expr))))
            display.set(expr)

        elif key == "acos":
            expr = str(math.degrees(math.acos(eval(expr))))
            display.set(expr)

        elif key == "atan":
            expr = str(math.degrees(math.atan(eval(expr))))
            display.set(expr)

        # ---------- Programmer Mode ----------
        elif key == "BIN":
            expr = bin(int(eval(expr)))[2:]
            display.set(expr)

        elif key == "OCT":
            expr = oct(int(eval(expr)))[2:]
            display.set(expr)

        elif key == "HEX":
            expr = hex(int(eval(expr)))[2:].upper()
            display.set(expr)

        elif key == "BIN→DEC":
            expr = str(int(expr, 2))
            display.set(expr)

        elif key == "OCT→DEC":
            expr = str(int(expr, 8))
            display.set(expr)

        elif key == "HEX→DEC":
            expr = str(int(expr, 16))
            display.set(expr)

        # ----------------------------------------------------
        #                 UNIT CONVERSIONS
        # ----------------------------------------------------

        # Distance
        elif key == "M→FT":
            expr = str(float(expr) * 3.28084)
            display.set(expr)

        elif key == "FT→M":
            expr = str(float(expr) / 3.28084)
            display.set(expr)

        elif key == "IN→FT":
            expr = str(float(expr) / 12)
            display.set(expr)

        elif key == "FT→IN":
            expr = str(float(expr) * 12)
            display.set(expr)

        # Weight
        elif key == "KG→G":
            expr = str(float(expr) * 1000)
            display.set(expr)

        elif key == "G→KG":
            expr = str(float(expr) / 1000)
            display.set(expr)

        elif key == "KG→LB":
            expr = str(float(expr) * 2.20462)
            display.set(expr)

        elif key == "LB→KG":
            expr = str(float(expr) / 2.20462)
            display.set(expr)

        # Temperature
        elif key == "CEL→FAR":
            expr = str((float(expr) * 9/5) + 32)
            display.set(expr)

        elif key == "FAR→CEL":
            expr = str((float(expr) - 32) * 5/9)
            display.set(expr)

        elif key == "CEL→KEL":
            expr = str(float(expr) + 273.15)
            display.set(expr)

        elif key == "KEL→CEL":
            expr = str(float(expr) - 273.15)
            display.set(expr)

        # Append normal text
        else:
            expr += str(key)
            display.set(expr)

    except:
        display.set("error")
        expr = ""



# ================ BUTTON LAYOUT =======================
# ButtonList = [

#     # Row 1
#     ("√𝑥",1,0), ("𝑥²",1,1), ("𝑥³",1,2), ("∛𝑥",1,3), ("1/𝑥",1,4), ("π",1,5),

#     # Row 2
#     ("sin",2,0), ("cos",2,1), ("tan",2,2), ("asin",2,3), ("acos",2,4), ("atan",2,5),

#     # Row 3
#     ("7",3,0), ("8",3,1), ("9",3,2), ("*",3,3), ("log10",3,4), ("eˣ",3,5),

#     # Row 4
#     ("4",4,0), ("5",4,1), ("6",4,2), ("-",4,3), ("BIN",4,4), ("OCT",4,5),

#     # Row 5
#     ("1",5,0), ("2",5,1), ("3",5,2), ("+",5,3), ("HEX",5,4), ("BIN→DEC",5,5),

#     # Row 6
#     ("AC",6,0), ("⌫",6,1), ("0",6,2), ("/",6,3), ("=",6,4), ("OCT→DEC",6,5),

#     # Row 7 → Conversions
#     ("M→FT",7,0), ("FT→M",7,1), ("IN→FT",7,2), ("FT→IN",7,3), ("HEX→DEC",7,4),

#     # Row 8 → Weight
#     ("KG→G",8,0), ("G→KG",8,1), ("KG→LB",8,2), ("LB→KG",8,3), 

#     # Row 9 → Temperature
#     ("C→F",9,0), ("F→C",9,1), ("C→K",9,2), ("K→C",9,3),
# ]


ButtonList = [
    ("1/𝑥",1,0),("𝑥²",1,1), ("𝑥³",1,2),("√𝑥",1,3), ("∛𝑥",1,4),("BIN",1,5),("M→FT",1,6),("KG→LB",1,7),

    ("sin",2,0), ("cos",2,1), ("tan",2,2), ("sin⁻¹",2,3), ("cos⁻¹",2,4), ("OCT",2,5),("FT→M",2,6) ,("LB→KG",2,7),    

    ("7",3,0), ("8",3,1), ("9",3,2), ("*",3,3), ("tan⁻¹",3,4),("HEX",3,5),("IN→FT",3,6),("CEL→FAR",3,7),

    ("4",4,0), ("5",4,1), ("6",4,2), ("-",4,3), ("log10",4,4),("BIN→DEC",4,5),("FT→IN",4,6),("FAR→CEL",4,7),

    ("1",5,0), ("2",5,1), ("3",5,2), ("+",5,3), ("eˣ",5,4),("OCT→DEC",5,5),("KG→GR",5,6),("CEL→KEL",5,7),

    ("AC",6,0), ("⌫",6,1), ("0",6,2), ("/",6,3), ("=",6,4),("HEX→DEC",6,5),("GR→KG",6,6),("KEL→CEL",6,7),

]


# ===================== UI SETUP =======================
root = Tk()
root.title("Scientific + Unit Converter Calculator")
root.geometry("850x650")
root.config(bg="#868d5c")
root.resizable(False, False)
root.bind("<Key>", key_input)

display = StringVar()

entry = Entry(
    root,
    textvariable=display,
    font=("Segoe UI", 32),
    width=32,
    bd=0,
    justify="right",
    bg="white",
    fg="black",
    highlightthickness=2,
)
entry.grid(row=0, column=0, columnspan=9, padx=10, pady=20, ipady=20)
entry.configure(state = 'normal')
display.set(expr)
entry.configure(state = 'readonly')

# ======= Create 3D Buttons =======
for text, r, c in ButtonList:
    btn = Button3D(
        root,
        text=text,
        width=8,
        height=2,
        command=lambda x=text: press(x)
    )
    btn.grid(row=r, column=c, padx=6, pady=6)

root.mainloop()
