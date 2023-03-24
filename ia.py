import math
import pygame
from dataclasses import *
import time

@dataclass
class Grille:
    pos:list[int] = field(default_factory=list)
    rec_pos:list = field(default_factory=list)
    valeur = 1
    
    def actualiser_grille(self,coordonnée,valeur):
        self.pos[coordonnée] = valeur
    
    def touch_case(self):
        position_souris = pygame.mouse.get_pos()
        for colonne in range(len(self.rec_pos)):
            for ligne in range(len(self.pos[colonne])):
                if self.rec_pos[colonne][ligne].collidepoint(position_souris):
                    if pygame.mouse.get_pressed()[0]:
                        if self.verif_colonne(colonne):
                            self.ajout(colonne,self.valeur)
                            time.sleep(0.5)
                            if self.valeur == 1:
                                self.valeur = 2
                                return True
                            else:
                                self.valeur = 1   
                                return True     
    def colision_grille(self):
        li = []
        for colonne in range(len(self.pos)):
            for ligne in range(len(self.pos[colonne])):
                li.append(pygame.Rect(position_dans_grille(colonne,ligne),(26,26)))
            self.rec_pos.append(li)
            li = []
    def verif_colonne(self,colonne):
        compteur = 0
        for i in self.pos[colonne]:
            if i == 0:
                compteur += 1
        if compteur != 0:
            return True
        else:
            return False
    
    def ajout(self,colonne,valeur):
        for ligne in range(5,-1,-1):
            if self.pos[colonne][ligne] == 0:
                self.pos[colonne][ligne] = valeur
                return self
    
    def remove(self,colonne):
        if self.pos[colonne] == [0,0,0,0,0,0]:
            return False
        elif self.verif_colonne(colonne) == False:
            self.pos[colonne][0] = 0
        else:
            for ligne in range(5,-1,-1):
                if self.pos[colonne][ligne] == 0:
                    self.pos[colonne][ligne+1] = 0
                    return True

def position_dans_grille(colonne,ligne):
    ycor = 0
    xcor = 0
    if colonne == 0:
        ycor = 5
    elif colonne == 1:
        ycor = 40
    elif colonne == 2:
        ycor = 75
    elif colonne == 3:
        ycor = 110
    elif colonne == 4:
        ycor = 143
    elif colonne == 5:
        ycor = 178
    elif colonne == 6:
        ycor = 213
    if ligne == 0:
        xcor = 5
    elif ligne == 1:
        xcor = 40
    elif ligne == 2:
        xcor = 75
    elif ligne == 3:
        xcor = 110
    elif ligne == 4:
        xcor = 143
    elif ligne == 5:
        xcor = 178
    return (ycor,xcor)
def verif_win(grille,z):
    for y in range(6):
        for i in range(4):
            if grille.pos[i][y] == z: 
                if grille.pos[i+1][y] == z :
                    if grille.pos[i+2][y] == z: 
                        if grille.pos[i+3][y] == z:
                            return True
    for y in range(7):
        for i in range(3):
            if grille.pos[y][i] == z: 
                if grille.pos[y][i+1] == z :
                    if grille.pos[y][i+2] == z: 
                        if grille.pos[y][i+3] == z:
                            return True
    if grille.pos[0][0] == z and grille.pos[1][1] == z and grille.pos[2][2] == z and grille.pos[3][3] == z:
        return True
    elif grille.pos[4][4] == z and grille.pos[1][1] == z and grille.pos[2][2] == z and grille.pos[3][3] == z:
        return True
    elif grille.pos[4][4] == z and grille.pos[5][5] == z and grille.pos[2][2] == z and grille.pos[3][3] == z:
        return True
    elif grille.pos[0][1] == z and grille.pos[1][2] == z and grille.pos[2][3] == z and grille.pos[3][4] == z:
        return True
    elif grille.pos[4][5] == z and grille.pos[1][2] == z and grille.pos[2][3] == z and grille.pos[3][4] == z:
        return True
    elif grille.pos[0][2] == z and grille.pos[1][3] == z and grille.pos[2][4] == z and grille.pos[3][5] == z:
        return True
    elif grille.pos[1][0] == z and grille.pos[2][1] == z and grille.pos[3][2] == z and grille.pos[4][3] == z:
        return True
    elif grille.pos[5][4] == z and grille.pos[2][1] == z and grille.pos[3][2] == z and grille.pos[4][3] == z:
        return True
    elif grille.pos[5][4] == z and grille.pos[6][5] == z and grille.pos[3][2] == z and grille.pos[4][3] == z:
        return True
    elif grille.pos[2][0] == z and grille.pos[3][1] == z and grille.pos[4][2] == z and grille.pos[5][3] == z:
        return True
    elif grille.pos[6][4] == z and grille.pos[3][1] == z and grille.pos[4][2] == z and grille.pos[5][3] == z:
        return True
    elif grille.pos[3][0] == z and grille.pos[4][1] == z and grille.pos[5][2] == z and grille.pos[6][3] == z:
        return True
    elif grille.pos[6][0] == z and grille.pos[5][1] == z and grille.pos[4][2] == z and grille.pos[3][3] == z:
        return True
    elif grille.pos[2][4] == z and grille.pos[5][1] == z and grille.pos[4][2] == z and grille.pos[3][3] == z:
        return True
    elif grille.pos[2][4] == z and grille.pos[1][5] == z and grille.pos[4][2] == z and grille.pos[3][3] == z:
        return True
    elif grille.pos[5][0] == z and grille.pos[4][1] == z and grille.pos[3][2] == z and grille.pos[2][3] == z:
        return True
    elif grille.pos[1][4] == z and grille.pos[4][1] == z and grille.pos[3][2] == z and grille.pos[2][3] == z:
        return True
    elif grille.pos[1][4] == z and grille.pos[0][5] == z and grille.pos[3][2] == z and grille.pos[2][3] == z:
        return True
    elif grille.pos[4][0] == z and grille.pos[3][1] == z and grille.pos[2][2] == z and grille.pos[1][3] == z:
        return True
    elif grille.pos[0][4] == z and grille.pos[3][1] == z and grille.pos[2][2] == z and grille.pos[1][3] == z:
        return True
    elif grille.pos[3][0] == z and grille.pos[2][1] == z and grille.pos[1][2] == z and grille.pos[0][3] == z:
        return True
    elif grille.pos[6][1] == z and grille.pos[5][2] == z and grille.pos[4][3] == z and grille.pos[3][4] == z:
        return True
    elif grille.pos[2][5] == z and grille.pos[5][2] == z and grille.pos[4][3] == z and grille.pos[3][4] == z:
        return True
    elif grille.pos[6][2] == z and grille.pos[5][3] == z and grille.pos[4][4] == z and grille.pos[3][5] == z:
        return True

def minimax(grille,profondeur,joueur):
    if verif_win(grille,1) == True:
        return 1
    elif verif_win(grille,2) == True:
        return -1
    elif profondeur == 0:
        return 0
    # elif profondeur == 0:
    #     return 0
    compteur = 0
    #Minimax(grille,profondeur+1,joueuropposé)
    if joueur == "ia":
        score:int
        bestscore = -math.inf
        for colonne in range(7):
            
            if grille.verif_colonne(colonne):
                grille.ajout(colonne,1)
                if grille.verif_colonne(colonne) == False:
                    if verif_win(grille,1) == True:
                        grille.remove(colonne)
                        return 1
                    elif verif_win(grille,2) == True:
                        grille.remove(colonne)
                        return -1
                    else:
                        
                        score = minimax(grille,profondeur-1,"joueur")
                        
                score = minimax(grille,profondeur-1,"joueur")
                grille.remove(colonne)
                bestscore = max(score,bestscore)
             
        
           
    else:
        score:int
        bestscore = math.inf
        for colonne in range(7):
            if grille.verif_colonne(colonne):
                grille.ajout(colonne,2)
                if grille.verif_colonne(colonne) == False:
                    if verif_win(grille,1) == True:
                        grille.remove(colonne)
                        return 1
                    elif verif_win(grille,2) == True:
                        grille.remove(colonne)
                        return -1
                    else:
                        
                        
                        score = minimax(grille,profondeur-1,"ia")
                score = minimax(grille,profondeur-1,"ia")
                grille.remove(colonne)
                bestscore = min(score,bestscore)
            
    return bestscore
    
    
def ia_hard(grille,valeur):
    score = -math.inf
    meilleur_score = -math.inf
    meilleur_coup:int
    for colonne in range(7):
        if grille.verif_colonne(colonne):
            grille.ajout(colonne,valeur)
            score = minimax(grille,5,"joueur")
            grille.remove(colonne)
            print(score)
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = colonne
    
    grille.ajout(meilleur_coup,valeur)
    
