import tkinter as tk
import base_matrice as mat
from random import randint

root = tk.Tk()
root.title("Jeu de la vie")
menu=tk.Menu(root)
subMenu1=tk.Menu(menu)
subMenu2=tk.Menu(menu)
subMenu3=tk.Menu(menu)
root.config(menu=menu)
Hauteur=700
Largeur=Hauteur
(H,L,c)=(Hauteur,Largeur,'#596643')
Dessin=tk.Canvas(root,height=H,width=L,bg='white')
Dessin.pack()

# def case(x,y,nbCasesLargeur,nbCasesHauteur):
#     return (x*Largeur/nbCasesLargeur,y*Hauteur/nbCasesHauteur)

def case(x,y,nbCasesLargeur,nbCasesHauteur):
    return (y*Hauteur/nbCasesHauteur,x*Largeur/nbCasesLargeur)

# def inv_case(x,y,nbCasesLargeur,nbCasesHauteur):
#     return (int(x/Largeur*nbCasesLargeur),int(y/Hauteur*nbCasesHauteur))

def inv_case(x,y,nbCasesLargeur,nbCasesHauteur):
    return (int(y/Hauteur*nbCasesHauteur),int(x/Largeur*nbCasesLargeur))

def case_active(x,y,nbCasesLargeur,nbCasesHauteur):
    (x1,y1)=case(x,y,nbCasesLargeur,nbCasesHauteur)
    Dessin.create_rectangle((x1,y1),(x1+Largeur/nbCasesLargeur,y1+Hauteur/nbCasesHauteur),fill='black')

def voisins_case(matr,ligne,colonne):
    compteur=0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if 0<=ligne+i<len(matr) and 0<=colonne+j<len(matr[0]):
                compteur+=matr[ligne+i][colonne+j]
    return compteur

def prochaine_gen(matr):
    (n,m)=mat.dimensions(matr)
    nouv_matr=mat.matrice_nulle(n,m)
    for ligne in range(len(matr)):
        for colonne in range(len(matr[0])):
            voisins=voisins_case(matr,ligne,colonne)
            if ligne==0 and colonne==0 or ligne==len(matr)-1 and colonne==0 or ligne==0 and colonne==len(matr[0])-1 or ligne==len(matr)-1 and colonne==len(matr[0])-1:
                # Dans le cas du coins, il reste vivant si il a 2 ou 3 voisins. Et il naît si il a 3 voisins
                if matr[ligne][colonne]==0:
                    if voisins==3:
                        nouv_matr[ligne][colonne]=1
                    else:
                        nouv_matr[ligne][colonne]=0
                else:
                    if voisins==2:
                        nouv_matr[ligne][colonne]=1
                    else:
                        nouv_matr[ligne][colonne]=0
            elif ligne==0 or ligne==len(matr)-1 or colonne==0 or colonne==len(matr[0])-1:
                # Bord de la matrice
                if matr[ligne][colonne]==0:
                    if voisins==3:
                        nouv_matr[ligne][colonne]=1
                    else:
                        nouv_matr[ligne][colonne]=0
                else:
                    if voisins==2 or voisins==3:
                        nouv_matr[ligne][colonne]=1
                    else:
                        nouv_matr[ligne][colonne]=0
            else:
                # Intérieur de la matrice
                if matr[ligne][colonne]==0:
                    if voisins==3:
                        nouv_matr[ligne][colonne]=1
                    else:
                        nouv_matr[ligne][colonne]=0
                else:
                    if voisins==2 or voisins==3:
                        nouv_matr[ligne][colonne]=1
                    else:
                        nouv_matr[ligne][colonne]=0
    return nouv_matr

def grille_hasard(matr):
    (n,m)=mat.dimensions(matr)
    for i in range(n):
        for j in range(m):
            matr[i][j]=randint(0,1)
    return matr

class État():
    def __init__(self):
        self.casesL=10 # nombre cases sur la largeur
        self.casesH=self.casesL # nombre cases sur la hauteur
        self.matrice=mat.matrice_nulle(self.casesL,self.casesH)
        self.choix='hasard'
        #self.matrice=grille_hasard(self.matrice)
        self.affichage()

    def affichage(self):
        Dessin.delete('all')
        for i in range(self.casesL+1):
            Dessin.create_line((i*Largeur/self.casesL,0),(i*Largeur/self.casesL,Hauteur),fill='black')
            Dessin.create_line((0,i*Hauteur/self.casesH),(Largeur,i*Hauteur/self.casesH),fill='black')
        for ligne in range(len(self.matrice)):
            for colonne in range(len(self.matrice[0])):
                if self.matrice[ligne][colonne]==1:
                    case_active(ligne,colonne,self.casesL,self.casesH)

état=État()

def hasard():
    état.choix='hasard'
    unpack()
    pack()
    état.matrice=grille_hasard(état.matrice)
    état.affichage()

def planeur():
    état.choix='structure'
    unpack()
    pack()
    état.matrice[3][1]=1
    état.matrice[3][2]=1
    état.matrice[3][3]=1
    état.matrice[2][3]=1
    état.matrice[1][2]=1
    état.affichage()

def oscillateur():
    état.choix='structure'
    unpack()
    pack()
    (i,j)=inv_case(Largeur/2,Hauteur/2,état.casesL,état.casesH)
    état.matrice[j][i-2]=1
    état.matrice[j][i-1]=1
    état.matrice[j][i]=1
    état.matrice[j-1][i-1]=1
    état.matrice[j-1][i]=1
    état.matrice[j-1][i+1]=1
    état.affichage()

def canon():
    if état.casesL<38 or état.casesH<38:
        état.casesL=38
        état.casesH=38
        état.matrice=mat.matrice_nulle(état.casesL,état.casesH)
    état.choix='structure'
    unpack()
    pack()
    f_in=open('canon.txt', 'r', encoding='utf-8')
    for ligne in f_in:
        état.matrice[int(ligne[0])][int(ligne[2:])]=1
    état.affichage()

def horloge():
    if état.casesL<14 or état.casesH<14:
        état.casesL=14
        état.casesH=14
        état.matrice=mat.matrice_nulle(état.casesL,état.casesH)
    état.choix='structure'
    unpack()
    pack()
    f_in=open('horloge.txt', 'r', encoding='utf-8')
    for ligne in f_in:
        if ligne[1]!=' ':
            état.matrice[int(ligne[0])*10+int(ligne[1])][int(ligne[3:])]=1
        else:
            état.matrice[int(ligne[0])][int(ligne[2:])]=1
    état.affichage()

def prochain_bouton():
    état.matrice=prochaine_gen(état.matrice)
    état.affichage()

def prochain_touche(event):
    état.matrice=prochaine_gen(état.matrice)
    état.affichage()

def reinitialisation():
    état.matrice=mat.matrice_nulle(état.casesL,état.casesH)
    état.affichage()

def valeur_nb_case(x):
    (état.casesL,état.casesH)=(int(x),int(x))
    état.matrice=mat.matrice_nulle(int(x),int(x))
    état.affichage()

def raj_enl_case(event):
    (position_x,position_y)=inv_case(event.x,event.y,état.casesL,état.casesH)
    if état.matrice[position_x][position_y]==0:
        état.matrice[position_x][position_y]=1
    elif état.matrice[position_x][position_y]==1:
        état.matrice[position_x][position_y]=0
    état.affichage()

bouton_hasard=tk.Button(root, text='Hasard', command=hasard, width=9)
bouton_generation=tk.Button(root, text='Prochain', command=prochain_bouton, width=9)
bouton_reinitialisation=tk.Button(root, text='Réinitialisation', command=reinitialisation, width=9)
curseur_case=tk.Scale(root, orient='horizontal', length=3*Largeur/4, label='Nombre de cases',command=valeur_nb_case, from_=10, to=100)
avertissement=tk.Label(text="'a' permet d'activer ou désactiver une case pointée par la souris.")
avertissement2=tk.Label(text="La flèche de droite permet de passer à le prochaine génération.")

menu.add_cascade(label='Hasard', menu=subMenu1)
subMenu1.add_command(label='Hasard',command=hasard)
menu.add_cascade(label='Structure', menu=subMenu2)
subMenu2.add_command(label='Planeur', command=planeur)
subMenu2.add_command(label='Oscillateur', command=oscillateur)
subMenu2.add_command(label='Canon', command=canon)
subMenu2.add_command(label='Horloge',command=horloge)

def pack():
    avertissement.pack()
    avertissement2.pack()
    if état.choix=='hasard':
        bouton_hasard.pack()
    bouton_generation.pack()
    bouton_reinitialisation.pack()
    curseur_case.pack()

def unpack():
    bouton_hasard.pack_forget()
    bouton_generation.pack_forget()
    bouton_reinitialisation.pack_forget()
    curseur_case.pack_forget()
    avertissement.pack_forget()

root.bind('<Right>',prochain_touche)
root.bind('<Key-a>',raj_enl_case)

pack()

root.mainloop()