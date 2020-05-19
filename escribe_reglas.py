class Tree():
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label 
        

def Polaca_Inv(f:Tree): # Escribe la proposicion
    
    if (f.right == None): # Hoja
        return f.label
    
    elif (f.label == '-'): # Negacion
        return  Polaca_Inv(f.right) +'-'
    
    elif (f.label == 'Y' or f.label == 'O' or f.label == '>' or f.label == '<->'): # Conectores binarios
        return Polaca_Inv(f.right) + Polaca_Inv(f.left) + f.label
    
    
def Polaca(f:Tree): # Escribe la proposicion
    
    if (f.right == None): # Hoja
        return f.label
    
    elif (f.label == '-'): # Negacion
        return '-' + Polaca(f.right)
    
    elif (f.label == 'Y' or f.label == 'O' or f.label == '>' or f.label == '<->'): # Conectores binarios
        return Polaca(f.left) + f.label + Polaca(f.right)
    

def String2Tree (A, LetrasProposicionales):
    Conectivos = ['O','Y','>']
    Pila = []
    for c in A:
        if c in LetrasProposicionales:
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

def Inorder(f:Tree): # Escribe la proposicion
    
    if (f.right == None): # Hoja
        return f.label
    
    elif (f.label == '-'): # Negacion
        return '-' + Inorder(f.right)
    
    elif (f.label == 'Y' or f.label == 'O' or f.label == '>' or f.label == '='): # Conectores binarios
        return '(' + Inorder(f.left) + f.label + Inorder(f.right) + ')'

################################################### HORIZONTALES ####################################################
print ("Reglas Horizontales:")       
xr2 = Tree ('O', (Tree('Y',(Tree ('a', None, None)),(Tree('Y',(Tree ('b', None, None)),(Tree ('c', None, None)))))), (Tree('Y',(Tree ('d', None, None)),(Tree('Y',(Tree ('e', None, None)),(Tree ('f', None, None)))))))
xrr2 = Tree('Y',(Tree ('g', None, None)),(Tree('Y',(Tree ('h', None, None)),(Tree ('i', None, None)))))
Xh = Tree('O',xr2,xrr2)
print (Polaca_Inv(Xh))

or2 = Tree ('O', (Tree('Y',(Tree ('j', None, None)),(Tree('Y',(Tree ('k', None, None)),(Tree ('l', None, None)))))), (Tree('Y',(Tree ('m', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('o', None, None)))))))
orr2 = Tree('Y',(Tree ('p', None, None)),(Tree('Y',(Tree ('q', None, None)),(Tree ('r', None, None)))))
Oh = Tree('O',or2,orr2)
print (Polaca_Inv(Oh))

print("\n")
################################################### VERTICALES ####################################################
print ("Reglas Verticales:")
xr3 = Tree ('O', (Tree('Y',(Tree ('a', None, None)),(Tree('Y',(Tree ('d', None, None)),(Tree ('g', None, None)))))), (Tree('Y',(Tree ('b', None, None)),(Tree('Y',(Tree ('e', None, None)),(Tree ('h', None, None)))))))
xrr3 = Tree('Y',(Tree ('c', None, None)),(Tree('Y',(Tree ('f', None, None)),(Tree ('i', None, None)))))
Xv = Tree('O',xr3,xrr3)
print (Polaca_Inv(Xv))

or3 = Tree ('O', (Tree('Y',(Tree ('j', None, None)),(Tree('Y',(Tree ('m', None, None)),(Tree ('p', None, None)))))), (Tree('Y',(Tree ('k', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('q', None, None)))))))
orr3 = Tree('Y',(Tree ('l', None, None)),(Tree('Y',(Tree ('o', None, None)),(Tree ('r', None, None)))))
Ov = Tree('O',or3,orr3)
print (Polaca_Inv(Ov))
print("\n")
################################################### DIAGONALES ####################################################
print ("Reglas Diagonales:")
Xdr4 = Tree ('O', (Tree('Y',(Tree ('a', None, None)),(Tree('Y',(Tree ('e', None, None)),(Tree ('i', None, None)))))), (Tree('Y',(Tree ('g', None, None)),(Tree('Y',(Tree ('e', None, None)),(Tree ('c', None, None)))))))
print (Polaca_Inv(Xdr4))

Odr4 = Tree ('O', (Tree('Y',(Tree ('j', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('r', None, None)))))), (Tree('Y',(Tree ('p', None, None)),(Tree('Y',(Tree ('n', None, None)),(Tree ('l', None, None)))))))
print (Polaca_Inv(Odr4))
print("\n")

################################################### GRANDES (->) #################################################

""" X horizontal implica negacion de las demas """
print ("X horizontal implica negacion de las demas:")
neg1 = Tree ('Y', (Tree('Y',Xv, Xdr4)),(Tree('Y',Ov, Oh)))
neg11 = Tree ('Y', neg1, Odr4)

Xhimp = Tree ('>',Xh, (Tree('-',None, neg11)))

print (Polaca_Inv(Xhimp))
print("\n")

""" O horizontal implica negacion de las demas """
print ("O horizontal implica negacion de las demas:")
neg2 = Tree ('Y', (Tree('Y',Xv, Xdr4)),(Tree('Y',Ov, Xh)))
neg22 = Tree ('Y', neg2, Odr4)

Ohimp = Tree ('>',Oh, (Tree('-',None, neg22)))

print (Polaca_Inv(Ohimp))
print("\n")

""" X vertical implica negacion de las demas """
print ("X vertical implica negacion de las demas:")
neg3 = Tree ('Y', (Tree('Y',Xh, Xdr4)),(Tree('Y',Ov, Oh)))
neg33 = Tree ('Y', neg3, Odr4)

Xvimp = Tree ('>',Xv, (Tree('-',None, neg33)))

print (Polaca_Inv(Xvimp))
print("\n")

""" O vertical implica negacion de las demas """
print ("O vertical implica negacion de las demas:")
neg4 = Tree ('Y', (Tree('Y',Xh, Xdr4)),(Tree('Y',Xv, Oh)))
neg44 = Tree ('Y', neg4, Odr4)

Ovimp = Tree ('>',Ov, (Tree('-',None, neg44)))

print (Polaca_Inv(Ovimp))
print("\n")

""" X diagonal implica negacion de las demas """
print ("X diagonal implica negacion de las demas:")
neg5 = Tree ('Y', (Tree('Y',Xh, Xv)),(Tree('Y',Ov, Oh)))
neg55 = Tree ('Y', neg5, Odr4)

Xvimp = Tree ('>',Xdr4, (Tree('-',None, neg55)))

print (Polaca_Inv(Xvimp))
print("\n")

""" O diagonal implica negacion de las demas """
print ("O diagonal implica negacion de las demas:")
neg6 = Tree ('Y', (Tree('Y',Xh, Xv)),(Tree('Y',Ov, Oh)))
neg66 = Tree ('Y', neg6, Xdr4)

Xvimp = Tree ('>',Odr4, (Tree('-',None, neg66)))

print (Polaca_Inv(Xvimp))
print("\n")
