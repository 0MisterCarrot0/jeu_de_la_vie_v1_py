# Ce script Python a été recopié du cours, il va être utilisé dans main.py pour utiliser
# les matrices

def dimensions(A):
    return (len(A),len(A[0]))

def colonne(A, co):
    return [A[li][co] for li in range(len(A))]

def est_matrice(A):
    if type(A) != list or A==[]:
        return False
    if type(A[0]) != list or A[0]==[]:
        return False
    for ligne in A:
        if type(ligne) != list or len(ligne) != len(A[0]):
            return False
    return True

def matrice_nulle(n,m):
    A=[]
    for ligne in range(n):
        L=[]
        for colonne in range(m):
            L.append(0)
        A.append(L)
    return A

def matrice_identité(n):
    A = matrice_nulle(n,n)
    for i in range(n):
        A[i][i]=1
    return A

def opposé(A):
    (n,m) = dimensions(A)
    B = matrice_nulle(n,m)
    for i in range(n):
        for j in range(m):
            B[i][j] = - A[i][j]
    return B

def trace(A):
    (n,m)=dimensions(A)
    if n != m :
        raise ValueError('Trace : matrice non carrée')
    tr = 0
    for i in range(n):
        tr = tr + A[i][i]
    return tr

def somme(A,B):
    (n,m) = dimensions(A)
    if (n,m) != dimensions(B):
        raise ValueError('Dimensions incompatibles')
    C = matrice_nulle(n,m)
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

def coefficient_produit(A,B,i,j):
    (n,m)=dimensions(A)
    c = 0
    for k in range(n):
        c = c + A[i][k]*B[k][j]
    return c

def produit(A,B):
    (la,ca) = dimensions(A) ; (lb,cb) = dimensions(B)
    if lb != ca:
        raise ValueError('Dimensions incompatibles')
    C = matrice_nulle(la,cb)
    for i in la:
        for j in cb:
            C[i][j] = coefficient_produit(A,B,i,j)
    return C