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
