import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height = 380, width = 350)

def to_O_C1():
    global casilla_1
    
    if (casilla_1['text'] == 'X'):
            casilla_1['text'] = 'O'
    else:
        casilla_1['text'] = 'X'
        
    
def to_O_C2():
    global casilla_2
    
    if (casilla_2['text'] == 'X'):
            casilla_2['text'] = 'O'
    else:
        casilla_2['text'] = 'X'
    
def to_O_C3():
    global casilla_3
    
    if (casilla_3['text'] == 'X'):
            casilla_3['text'] = 'O'
    else:
        casilla_3['text'] = 'X' 
        
        
def to_O_C4():
    global casilla_4
    
    if (casilla_4['text'] == 'X'):
            casilla_4['text'] = 'O'
    else:
        casilla_4['text'] = 'X' 
        
        
def to_O_C5():
    global casilla_5
    
    if (casilla_5['text'] == 'X'):
            casilla_5['text'] = 'O'
    else:
        casilla_5['text'] = 'X'

    
def to_O_C6():
    global casilla_6
    
    if (casilla_6['text'] == 'X'):
            casilla_6['text'] = 'O'
    else:
        casilla_6['text'] = 'X'
        
        
def to_O_C7():
    global casilla_7
    
    if (casilla_7['text'] == 'X'):
            casilla_7['text'] = 'O'
    else:
        casilla_7['text'] = 'X'
    
def to_O_C8():
    global casilla_8
    
    if (casilla_8['text'] == 'X'):
            casilla_8['text'] = 'O'
    else:
        casilla_8['text'] = 'X'
    
def to_O_C9():
    global casilla_9
    
    if (casilla_9['text'] == 'X'):
            casilla_9['text'] = 'O'
    else:
        casilla_9['text'] = 'X'    
    

instruccion = tk.Label(root, text = "Doble click para cambiar de X a O.", width = 30, height = 7)
casilla_1 = tk.Button(root, width = 15, height = 7, command = to_O_C1)
casilla_2 = tk.Button(root, width = 15, height = 7, command = to_O_C2)
casilla_3 = tk.Button(root, width = 15, height = 7, command = to_O_C3)
casilla_4 = tk.Button(root, width = 15, height = 7, command = to_O_C4)
casilla_5 = tk.Button(root, width = 15, height = 7, command = to_O_C5)
casilla_6 = tk.Button(root, width = 15, height = 7, command = to_O_C6)
casilla_7 = tk.Button(root, width = 15, height = 7, command = to_O_C7)
casilla_8 = tk.Button(root, width = 15, height = 7, command = to_O_C8)
casilla_9 = tk.Button(root, width = 15, height = 7, command = to_O_C9)

instruccion.place(x = 70, y = 310)

canvas.pack()

casilla_1.place(x = 0, y = 0)
casilla_2.place(x = 120, y = 0)
casilla_3.place(x = 240, y = 0)
casilla_4.place(x = 0, y = 120)
casilla_5.place(x = 120, y = 120)
casilla_6.place(x = 240, y = 120)
casilla_7.place(x = 0, y = 240)
casilla_8.place(x = 120, y = 240)
casilla_9.place(x = 240, y = 240)

root.mainloop()

 

