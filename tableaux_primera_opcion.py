#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

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
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
	#def String2Tree (A, LetrasProposicionales):
    Conectivos = ['O','Y','>']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c == '-':
            FormulaAux = Tree (c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree (c, Pila[-1], Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
    return Pila[-1]


#print(Inorder(StringtoTree('pqY')))
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

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

def par_complementario(h):
    for x in h:
        for y in h:
            if len(x)==1:
                if y=="-"+x:
                    return True
            else:
                if y==x[1]:
                    return True
    return False
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
	

def es_literal(i):
	# Esta función determina si el árbol i es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
    if i.right == None:
        return True
    elif i.label =='-':
        if i.right.right==None:
            return True
        else:
            return False
    else:
        return False

#print(es_literal(StringtoTree('p-')))
    

def solo_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
    
    for j in l:
        x = StringtoTree(j)
        if es_literal(x) == False:
            return False
    return True
#s [p, q], [¬p, q], [p, ¬¬q], [¬¬p, ¬(p∧q)]. 
#print(solo_literales(['p-','q-']))

def  Alfa_o_Beta (f):
    if (f.label == '-'):
        if (f.right.label == '-'):
            return '1Alfa'
        
    if (f.label == 'Y'):
        return '2Alfa'
    
    if (f.label == '-'):
        if (f.right.label == 'O'):
            return '3Alfa'
        
    if (f.label == '-'):
        if (f.right.label == '>'):
            return '4Alfa'
        
    if (f.label == '-'):
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
    A = StringtoTree(f)
    if A.label=='-':
        if A.right.label == '-':
            listaHojas.append(Inorder(A.right.right))
            # 1ALFA
        elif A.right.label == 'O':
            listaHojas.append('-'+Inorder(A.right.left))
            listaHojas.append('-'+Inorder(A.right.right))
            # 3ALFA
        elif A.right.label == '>':
            listaHojas.append(Inorder(A.right.left))
            listaHojas.append('-'+Inorder(A.right.right))
            # 4ALFA
        elif A.right.label == 'Y':
            listaHojas.append(['-'+Inorder(A.right.left)])
            listaHojas.append(['-'+Inorder(A.right.right)])
            #return '1BETA'
    elif A.label=='Y':
        listaHojas.append(Inorder(A.left))
        listaHojas.append(Inorder(A.right))
        #return '2ALFA'
    elif A.label == 'O':
        listaHojas.append([Inorder(A.left)])
        listaHojas.append([Inorder(A.right)])
        #return '2BETA'
    elif A.label == '>':
        listaHojas.append(['-'+Inorder(A.left)])
        listaHojas.append([Inorder(A.right)])
        #return '3BETA'
    
print(clasifica_y_extiende('pqYpO'))
print(listaHojas)

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = StringtoTree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
