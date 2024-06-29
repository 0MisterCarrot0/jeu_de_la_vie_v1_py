INFORMATIONS :
Comme le jeu de la vie est codé sur une grille sans limite, et que je n'ai pas pu le faire pareil,
j'ai rajouté quelques règles,
	- Une case dans un coin reste vivante dans le cas où elle a 2 ou 3 voisins. Une case naît 
	si elle a exactement 3 voisins.
	- Une case sur un bord (coin exclu) reste vivante si elle a 2 ou 3 voisins. Une case naît 
	si elle a exactement 3 voisins.
	- Toute autre case reste vivante si elle a 2 ou 3 voisins et naît si elle a exactement 
	3 voisins.
	PS : J'ai laissé dans mon code la possibilité de changer ces règles pour les bords et les
	coins. C'est pour cela que je n'ai pas factorisé (Car en soit ce sont les mêmes règles
	pour toutes les cases).


ASTUCES :
- La touche 'a' permet d'activer ou de désactivé une case en mettant le curseur au niveau de la case.
- Pour le canon il faut être sur une grille d'au minimum 38 cases de côté.
- Pour l'horloge il faut être sur un grille d'au minimum 14 cases de côté.