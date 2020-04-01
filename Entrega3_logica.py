import tkinter as tk
import random

triqui = tk.Tk()
triqui.title("Triqui")
triqui.geometry("360x360")
triqui.config(bg = "grey")

class Tree:
    def __init__(self, l, izq, der):
        self.label = l
        self.left = izq
        self.right = der

def string2tree(A, LetrasProposicionales):
    conectivos = ["O", "Y", ">"]
    pila = []
    for c in A:
        if c in LetrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == "-":
            formulaaux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaaux)
        elif c in conectivos:
            formulaaux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaaux)
    return pila[-1]

def VI(f, I):
    if f.right == None:
        return I[f.label]
    elif f.label == "-":
        return 1 - VI(f.right, I)
    elif f.label == "Y":
        return VI(f.right, I) * VI(f.left, I)
    elif f.label == "O":
        return max(VI(f.left, I), VI(f.right, I))
    elif f.label == ">":
        return max(1 - VI(f.left, I), VI(f.right, I))
    elif f.label == "=":
        return 1 - (VI(f.left, I) - VI(f.right, I))**2
    else:
        return "Hay algun error en el planteamiento"

def interpretaciones(LetrasProposicionales):
    interps = []
    aux = {}
    for a in LetrasProposicionales:
        aux[a] = 1
    interps.append(aux)
    for a in LetrasProposicionales:
        interps_aux = [i for i in interps]
        for i in interps_aux:
            aux1 = {}
            for b in LetrasProposicionales:
                if a == b:
                    aux1[b] = 1 - i[b]
                else:
                    aux1[b] = i[b]
            interps.append(aux1)
    return interps

def grafico(I):
    if I["a"] == 1 and I["b"] == 1:
        C1 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["a"] == 1 and I["d"] == 1:
        C1 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["b"] == 1 and I["c"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["b"] == 1 and I["e"] == 1:
        C1 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui,  width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["c"] == 1 and I["f"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["d"] == 1 and I["e"] == 1:
        C1 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["f"] == 1 and I["e"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["h"] == 1 and I["e"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["f"] == 1 and I["i"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["g"] == 1 and I["d"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["g"] == 1 and I["h"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["i"] == 1 and I["h"] == 1:
        C1 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(triqui,   width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(triqui, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(triqui, text =  "X", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

LetrasProposicionales = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "A", "B", "C", "D", "E", "F", "G", "H", "I"]

R1 = "i-h-g-f-e-d-c-baYYYYYYYY"
R2 = "i-h-g-f-e-c-b-daYYYYYYYY"
R3 = "i-h-g-f-d-c-a-ebYYYYYYYY"
R4 = "i-h-g-f-e-d-a-cbYYYYYYYY"
R5 = "i-h-g-e-d-b-a-fcYYYYYYYY"
R6 = "i-h-g-f-c-b-a-edYYYYYYYY"
R7 = "i-h-f-e-c-b-a-gdYYYYYYYY"
R8 = "i-h-g-d-c-b-a-feYYYYYYYY"
R9 = "i-g-f-d-c-b-a-heYYYYYYYY"
R10 = "h-g-e-d-c-b-a-ifYYYYYYYY"
R11 = "i-f-e-d-c-b-a-hgYYYYYYYY"
R12 = "g-f-e-d-c-b-a-ihYYYYYYYY"

RP1 = R1+R2+R3+R4+R5+R6+R7+R8+R9+R10+R11+R12+"OOOOOOOOOOO"

R13 = "EDObaY>"
R14 = "EBOdaY>"
R15 = "FDOCOAOebY>"
R16 = "FEOcbY>"
R17 = "EBOfcY>"
R18 = "HEOgdY>"
R19 = "HGOBOAOedY>"
R20 = "HEOifY>"
R21 = "FEOihY>"
R22 = "IHOCOBOfeY>"
R23 = "IGOFODOheY>"
R24 = "EDOhgY>"

RP2 = R13+R14+R15+R16+R17+R18+R19+R20+R21+R22+R23+R24+"YYYYYYYYYYY"

REGLA_FINAL = RP1+RP2+"Y"

formula_global = string2tree(REGLA_FINAL, LetrasProposicionales)
interpretaciones_form = interpretaciones(LetrasProposicionales)
interpretaciones_form_aux = []
for i in interpretaciones_form:
    aux = VI(formula_global, i)
    if (aux == 1):
        interpretaciones_form_aux.append(i)

index = random.randrange(0, len(interpretaciones_form_aux) - 1)
grafico(interpretaciones_form_aux[index])
triqui.mainloop()

print("Imprime")