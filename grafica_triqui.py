import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height = 380, width = 350)


 #clase árbol binario
class Tree:
    def __init__(self, l, izq, der):
        self.label = l
        self.left = izq
        self.right = der

#valor interpretación
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
    
#convertir de polaca inversa a árbol
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

#imprimir árbol a string
def Inorder(A):
    if A.right == None:
        return A.label
    elif A.label == "-":
        return "-" + Inorder(A.right)
    elif A.label in ["Y", "O", ">"]:
        return "(" + Inorder(A.left) + A.label + Inorder(A.right) + ")"
    
    
#tabla de verdad de todas las proposiciones
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


#forma normal conjuntiva
def enFNC(A):
#    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 900)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    atomos = letrasProposicionalesA + letrasProposicionalesB
    L = []
    pila = []
    i = -1
    s = A[0]
    
    while len(A) > 0:
        if s in atomos and len(pila) > 0 and pila[-1] == "-":
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            L.append(atomo + "=" + "-" + s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ")":
            w = pila[-1]
            O = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila) - 4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo + "=" + "(" + v + O + w + ")")
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    
    B = ""
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    
    for X in L:
        Y = enFNC(X)
        B += "Y" + Y
    
    B = atomo + B
    return B

def Clausula(C):
    L = []
    while len(C) > 0:
        s = C[0]
        if s == "O":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L

def formaClausal(A):
    L = []
    i = 0
    while len(A) > 0:
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == "Y":
                L.append(Clausula(A[:i]))
                A = A[i + 1:]
                i = 0
            else:
                i += 1
    return L

    

def unitPropagate(S,I):
    unitaria = False
    C = []
    while len(S)!=0:
        for x in S:
            if len(x)==1:
                l = x
                unitaria = True
                break
            elif len(x)==2 and x[0]=='-':
                l = x
                unitaria = True
                break
        if unitaria == True:
            C = S[:]
            count = 0
            for m in S:
                C[count]=m
                for c in range(len(m)):
                    if len(l) == 1:
                        if (m[c] == '-' and m[c+1] == l):
                            yolo = len(m)
                            C[count] = C[count].replace('-'+C[count][c+1],'')
                            #C[count] = C[count].replace(C[count][c],'')
                            if len(C[count])<yolo:
                                break
                        elif m[c] == l:
                            C.remove(C[count])
                            count-=1

                    elif len(l) == 2:
                        if m[c] == l[1]:
                            yolo = len(m)
                            C[count]= C[count].replace(C[count][c],'')
                            if len(C[count])<yolo:
                                break
                        elif m[c] == '-' and m[c+1] == l[1]:
                            C.remove(C[count])
                            count-=1
                            break
                        
                            

                count+=1
            S = C[:]
            if len(l) == 1:
                I[l[0]]=1
            elif len(l)==2:
                I[x[1]]=0
            unitaria=False
        else:
            break
    return S,I



def DPLL(S,I):
    S,I = unitPropagate(S,I)
    clau_vacia = ""
    if clau_vacia in S:
        return "Insatisfacible" ,{}
    elif len(S)==0:
        return "Satisfacible" ,I
    S2 = S[:]
    count = 0
    for m in S:
        S2[count] = m
        for c in range(len(m)):
            if m[c] not in I.keys():
                if m[c] != '-':
                    l = m[c]
                    break
        break
    for m in S:
        for c in range(len(m)):
            if len(l) == 1:
                if (m[c] == '-' and m[c+1] == l):
                    yolo = len(m)
                    S2[count] = S2[count].replace('-'+S2[count][c+1],'')
                    if len(S2[count])<yolo:
                        break
                elif m[c] == l:
                    S2.remove(S2[count])
                    count-=1
        count+=1
    S = S2[:]
    if len(l) == 1:
        I[l]=1
    elif len(l)==2:
        I[l]=0
    
    #if DPLL(S2,I)== ("Satisfacible",I):
        #return "Satisfacible",I
    S,I = unitPropagate(S,I)
    if len(S)==0:
        return "Satisfacible" ,I
    else:
        S3 = S2[:]
        count = 0
        for m in S:
            S3[count] = m
            for c in range(len(m)):
                if m[c] not in I.keys():
                    if m[c] != '-':
                        l = m[c]
                        break
            break
        for m in S:
            S3[count] = m
            for c in range(len(m)):
                if len(l)==1:
                    if m[c] == l:
                        
                        yolo = len(m)
                        S3[count] = S3[count].replace(S3[count][c],'')
                        if len(S3[count])<yolo:
                            break
                    elif (m[c] == '-' and m[c+1] == l):
                        S3.remove(S3[count])
                        count-=1
                        break
                   
            count+=1
        S = S3[:]
        if len(l)==1:
            I[l]=0
        elif len(l)==2:

            I[l]=1
        return DPLL(S3,I)   
    

def to_O_C1(I):
    global casilla_1
    if casilla_1['text'] == 'X' or I["j"]==1:
        casilla_1['text'] = 'O'
    elif I["a"]==1:
        casilla_1['text'] = 'X'
        
    
def to_O_C2(I):
    global casilla_2
    if I["k"]==1:
        casilla_2['text'] = 'O'
    elif I["b"]==1:
        casilla_2['text'] = 'X'
    
def to_O_C3(I):
    global casilla_3
    if I["l"]==1:
        casilla_3['text'] = 'O'
    elif I["c"]==1:
        casilla_3['text'] = 'X' 
        
        
def to_O_C4(i):
    global casilla_4
    if I["m"]==1:
        casilla_4['text'] = 'O'
    elif I["d"]==1:
        casilla_4['text'] = 'X' 
        
        
def to_O_C5(I):
    global casilla_5
    if I["n"]==1:
        casilla_5['text'] = 'O'
    elif I["e"]==1:
        casilla_5['text'] = 'X'

    
def to_O_C6(I):
    global casilla_6
    if I["o"]==1 or I["f"]==0:
        casilla_6['text'] = 'O'
    elif I["f"]==1 or I["o"]==0:
        casilla_6['text'] = 'X'
        
        
def to_O_C7(I):
    global casilla_7
    if I["p"]==1:
        casilla_7['text'] = 'O'
    elif I["g"]==1:
        casilla_7['text'] = 'X'
    
def to_O_C8(I):
    global casilla_8
    if ["q"]==1 or I["h"]==0:
        casilla_8['text'] = 'O'
    elif I["h"]==1:
        casilla_8['text'] = 'X'
    
def to_O_C9(I):
    global casilla_9
    if  I["r"]==1:
        casilla_9['text'] = 'O'
    elif I["i"]==1:
        casilla_9['text'] = 'X'    
    

LetrasProposicionales = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"]


#REGLA 1
r1 = "k-bYb-kYO"
r2 = "l-cYc-lYO"
r3 = "m-dYd-mYO"
r4 = "n-eYe-nYO"
r5 = "o-fYf-oYO"
r6 = "p-gYg-pYO"
r7 = "q-hYh-qYO"
r8 = "r-iYi-rYO"
r9 = "j-aYa-jYO"
R1T=r1+r2+r3+r4+r5+r6+r7+r8+r9+"YYYYYYYY"

#REGLA2_X  horizontal

R21 = "abcYY"
R22 = "defYY"
R23 = "ghiYY"
R2X = R21+R22+R23+"OO"

#REGLA2_O horizontal

R21 = "jklYY"
R22 = "mnoYY"
R23 = "pqrYY"
R2O = R21+R22+R23+"OO"

#REGLA3_X  vertical

R21 = "adgYY"
R22 = "behYY"
R23 = "cfiYY"
R3X = R21+R22+R23+"OO"

#REGLA3_O vertical

R21 = "jmpYY"
R22 = "knpYY"
R23 = "lorYY"
R3O = R21+R22+R23+"OO"

#REGLA4_X diagonal

R21 = "gecYY"
R22 = "aeiYY"
R4X = R21+R22+"O"

RNU = "ceYgYieYaYO" # PRINCIPAL

#REGLA4_O diagonal

R41 = "jnrYY"
R42 = "lnpYY"
R4O = R41+R42+"O"

RNO = "lnYpYrnYjYO" # PRINCIPAL

#REGLA5

R5X = R3X+"-"+R2X+"Y"+R2X+"-"+R3X+"YO"
R5O = R3O+"-"+R2O+"Y"+R2O+"-"+R3O+"YO"

RNX = "lnYpYrnYjYOrqYpYonYmYlkYjYOOroYlYqnYkYpmYjYOOYceYgYieYaYOifYcYheYbYgdYaYOOYYY-ihYgYfeYdYcbYaYOO>"

RYX = "lnYpYrnYjYOrqYpYonYmYlkYjYOOroYlYqnYkYpmYjYOOYceYgYieYaYOifYcYheYbYgdYaYOOYYY-ihYgYfeYdYcbYaYOO>"

#REGLAS FINALES

RT1 = R1T+R2O+"aiYYY"  #HORIZONTAL LINEA DE O
RF = R1T+R5X+R5O+"aYY" #Horizontal linea de o
RT2 = R1T+R3X+"pYY"    #VERTICAL LINEA DE X
RT3 = R1T+RNU+"Y"      #DIAGONAL DE X

formula_global = string2tree(RT1, LetrasProposicionales)
form = Inorder(formula_global)
tseitin = Tseitin(form, LetrasProposicionales)
causal = formaClausal(tseitin)
par = causal[:]


count= 0
for x in par:
    par[count] = ''
    for y in x:
        par[count]  = par[count] + y
    count+=1



dpll = DPLL(par, {})
print(dpll)
I = dpll[1]


instruccion = tk.Label(root, text = "Doble click para cambiar de X a O.", width = 30, height = 7)
casilla_1 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C1(I))
casilla_2 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C2(I))
casilla_3 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C3(I))
casilla_4 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C4(I))
casilla_5 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C5(I))
casilla_6 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C6(I))
casilla_7 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C7(I))
casilla_8 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C8(I))
casilla_9 = tk.Button(root, width = 15, height = 7, command = lambda: to_O_C9(I))

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



