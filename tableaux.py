#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a¬z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listahojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '¬':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    
    #def String2Tree (A, LetrasProposicionales):
    Conectivos = ['O','Y','>']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c == '¬':
            FormulaAux = Tree (c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree (c, Pila[-1], Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
    return Pila[-1]


	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	#p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	#return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"


    
    
def par_complementario(l):
    
    # Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
    
    for x in l:
        for y in l:
            if x.label == '¬':
                if x.right.label == y.label:
                    return True
                if y.label == '¬':
                    if x.label == y.right.label:
                        return True
    return False



def es_literal(f):
    # Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
    
    if f.right == None:
        return True
    elif f.label =='¬':
        if f.right.right==None:
            return True
        else:
            return False
    else:
        return False
    
        
    

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
    
    for j in l:
        if es_literal(j) == False:
            return True
        else:
            return False
        
        
def  Alfa_o_Beta (f):
    # Clasifica una formuna en alfa o beta 
    
    if (f.label == '¬'):
        if (f.right.label == '¬'):
            return '1Alfa'
        
    if (f.label == 'Y'):
        return '2Alfa'
    
    if (f.label == '¬'):
        if (f.right.label == 'O'):
            return '3Alfa'
        
    if (f.label == '¬'):
        if (f.right.label == '>'):
            return '4Alfa'
        
    if (f.label == '¬'):
        if (f.right.label == 'Y'):
            return '1Beta'
        
    if (f.right.label == 'O'):
            return '2Beta'
        
    if (f.right.label == '>'):
            return '3Beta'


def clasifica_y_extiende(f):
    # clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas

    
    global listahojas
    
    if (f.label == '¬'):
        if (f.right.label == '¬'):
            for l in listahojas:
                for S in l:
                    if (S.right.label == f.right.label and S.right.left.label == f.right.left.label and S.right.right.label == f.right.right.label):
                        l.remove(S)
                        l.apend([f.right.right])
        elif f.right.label == 'O':
            for l in listahojas:
                for V in l:
                    if (V.right != None):
                        if (V.right.label == f.right.label and V.right.left.label == f.right.left.label and V.right.right.label == f.right.right.label):
                            l.remove(V)
                            l.append(Tree('¬',None,f.right.left))
                            l.append(Tree('¬',None,f.right.right))
        elif f.right.label == '>':
            for l in listahojas:
                for M in l:
                    if (M.right != None):
                        if (M.right.label == f.right.label and M.right.left.label == f.right.left.label and M.right.right.label == f.right.right.label):
                            l.remove(M)
                            l.append(f.right.left)
                            l.append(Tree('¬',None,f.right.right))
        elif f.right.label == 'Y':
            valores = []
            for l in listahojas:
                for Y in l:
                    valores.append(Y)
                    if (Y.right.label == f.right.label and Y.right.left.label == f.right.left.label and Y.right.right.label == f.right.right.label):
                        l.remove(Y)
                        valores = l[:]
                        l.append(Tree('¬',None,f.right.left))
                        valores.append(Tree('¬',None,f.right.right))
            listahojas.append(valores)

    elif f.label == 'Y':
        for l in listaHojas:
            for F in l:
                if (F.label == f.label and F.left.label == f.left.label and F.right.label==f.right.label):
                    l.remove(F)
                    l.append(f.left)
                    l.append(f.right)

    elif f.label == 'O':
        valores = []
        for l in listahojas:
            for A in l:
                if (A.label == f.label and A.left.label == f.left.label and A.right.label==f.right.label):
                    l.remove(A)
                    valores = l[:]
                    l.append(f.left)
                    valores.append(f.right)
        listahojas.append(valores)
    elif f.label == '>':
        valores = []
        for l in listahojas:
            for A in l:
                if (A.label == f.label and A.left.label == f.left.label and A.right.label==f.right.label):
                    l.remove(A)
                    valores = l[:]
                    l.append(Tree('¬',None,f.right.left))
                    valores.append(f.right.right)
                valores.append(A)
        listahojas.append(valores)
    
    print (listahojas)
    
    
    
def Tableaux(f):
    
    # Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f

    
    global listaHojas
    global listaInterpsVerdaderas
    A = StringtoTree(f)
    listaHojas = [[A]]

    while (len(listaHojas) > 0):
        hojas = choice(listaHojas)
       
        if not (no_literales(hojas)):
            
            for tree in hojas:
               
                clasifica_y_extiende(tree)
        else:
            if (par_complementario(hojas)):
                listaHojas.remove(hojas)
            else:
                listaInterpsVerdaderas.append(hojas)
                listaHojas.remove(hojas)
                
    return listaInterpsVerdaderas
    
    

SEC = Tree('Y',(Tree('Y',(Tree('¬',None,(Tree('p',None,None)))),(Tree('>',(Tree('¬',None,(Tree('p',None,None)))),(Tree('¬',None,(Tree('q',None,None)))))))),(Tree('q',None,None)))
print(clasifica_y_extiende(SEC))

   

       