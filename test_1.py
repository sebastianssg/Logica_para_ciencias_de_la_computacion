""" Programa que determina cuales interpretaciones hacen que una formula sea verdadera y cuales hacen que sea falsa """

class Tree(): # Se crea la Clase Tree con sus respectivos atributos
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label 

# Se inicializan los tres arboles con los que se trabajaran (A,B,C)
C = Tree('Y',(Tree('Y',(Tree('¬',None,(Tree('p',None,None)))),(Tree('>',(Tree('¬',None,(Tree('p',None,None)))),(Tree('¬',None,(Tree('q',None,None)))))))),(Tree('q',None,None)))        
Z = Tree ('O', (Tree('Y',(Tree ('j', None, None)),(Tree('Y',(Tree ('k', None, None)),(Tree ('l', None, None)))))), (Tree('Y',(Tree ('m', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('o', None, None)))))))
z = Tree ('O', (Tree('Y',(Tree ('p', None, None)),(Tree('Y',(Tree ('q', None, None)),(Tree ('r', None, None)))))), (Tree('Y',(Tree ('j', None, None)),(Tree('Y',(Tree ('m', None, None)),(Tree ('p', None, None)))))))
H = Tree ('O', (Tree('Y',(Tree ('k', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('q', None, None)))))), (Tree('Y',(Tree ('l', None, None)),(Tree('Y',(Tree ('o', None, None)),(Tree ('r', None, None)))))))
h = Tree ('O', (Tree('Y',(Tree ('j', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('r', None, None)))))), (Tree('Y',(Tree ('l', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('p', None, None)))))))
Va = Tree ('O',Z,z)
va = Tree ('O',H,h)
fin = Tree ('O',Va,va)

    
""" Esta seccion construye la tabla de verdad de las letras proposicionales dadas """

letrasProposicionales = ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'] # lista con las letras proposicionales

interps = [] # lista todas las posibles interpretaciones (diccionarios)

aux = {} # primera interpretacion


for a in letrasProposicionales:
    aux[a] = 1 # inicializamos la primera interpretacion con todo verdadero

interps.append(aux) # ... y la incluimos en interps

for a in letrasProposicionales:
    interps_aux = [i for i in interps] # lista auxiliar de nuevas interpretaciones

    for i in interps_aux:
        aux1 = {} # diccionario auxiliar para crear nueva interpretacion
        for b in letrasProposicionales:
            if a == b:
                aux1[b] = 1 - i[b] # Cambia el valor de verdad para b
            else:
                aux1[b] = i[b] # ... y mantiene el valor de verdad para las otras letras
        interps.append(aux1) # Incluye la nueva interpretacion en la lista

""" Funcion que halla en valor de verdad de un arbol binario de acuerdo a sus interpretaciones """

def V (f:Tree):
    
    if (f.right == None): # Hoja
        return i[f.label]
    
    elif (f.label == '¬'): # Negacion
        return 1-V (f.right)
    
    elif (f.label == 'Y'): # conjuncion 
        return V(f.left)*V(f.right)
    
    elif (f.label == 'O'): # disyuncion 
        if (V(f.left) >= V(f.right)):
            return V(f.left)
        elif (V(f.right) >= V(f.left)):
            return V(f.right)
    
    elif (f.label == '>'): # implicacion
        if ((1-V(f.left)) >= V(f.right)):
            return (1-V(f.left))
        elif (V(f.right)>= (1-V(f.left))):
            return V(f.right)
    
    elif (f.label == '<->'): # doble implicacion
        return 1-(V(f.left)-V(f.right))**2
    
""" Se imprimen las interpretaciones y su valor respecto a el arbol """

print('Interpretaciones de A: ','\n') # Arbol A
for i in interps:
    print(i)
    if (V(fin)==1): # Si el arbol evalua verdadero...
        print("Verdadero",'\n')
    else: # Si el arbol evalua falso...
        print ("Falso",'\n')
print ("////////////////////////////////",'\n')
        