from PyQt5.QtCore import Qt


class SokobanController:

    def __init__(self):

        # Initialisation des paramètres du controller.
        self.__model = None
        self.__view = None
        self.__countOK = 1
        self.__pas = 0
        self.__winner = None

    def setModel(self, model):
        # Setter du model.
        self.__model = model

    def setView(self, view):
        # Setter de la view.
        self.__view = view

    def getPas(self):
        # Getter du nombre de déplacements.
        return self.__pas

    def play(self,key):
        # Action réalisé lors d'un appui de touche.

        if self.__winner:
            return

        direction = self.__model.getDirection()

        # Boucle pour vérifier les conditions lors d'un appui de la flèche droite.
        if key == Qt.Key_Right:
            if self.__model.get(direction[0], direction[1]+1) == 1:
                return
            elif self.__model.get(direction[0], direction[1]+1) == 2:
                if self.__model.get(direction[0], direction[1]+2) == 1 or self.__model.get(direction[0], direction[1]+2) == 2 or self.__model.get(direction[0], direction[1]+2) == 3:
                    return
                else:
                    self.__model.set(direction[0], direction[1]+1, 0)
                    if self.__model.get(direction[0], direction[1]+2) == 4:
                        self.__model.set(direction[0], direction[1]+2, 3)
                        self.__countOK += 1
                    else:
                        self.__model.set(direction[0], direction[1]+2, 2)
                    if self.__model.get(direction[0], direction[1]) == 6:
                        self.__model.set(direction[0], direction[1], 4)
                    else:
                        self.__model.set(direction[0], direction[1], 0)
                    direction[1] += 1
                    self.__model.set(direction[0], direction[1], 5)
            elif self.__model.get(direction[0], direction[1]+1) == 3:
                if self.__model.get(direction[0], direction[1]+2) == 1 or self.__model.get(direction[0], direction[1]+2) == 2 or self.__model.get(direction[0], direction[1]+2) == 3:
                    return
                else:
                    self.__model.set(direction[0], direction[1]+1, 0)
                    self.__model.set(direction[0], direction[1]+2, 2)
                    self.__countOK -= 1                    
                    self.__model.set(direction[0], direction[1], 0)
                    direction[1] += 1
                    self.__model.set(direction[0], direction[1], 6)
            elif self.__model.get(direction[0], direction[1]+1) == 4:
                self.__model.set(direction[0], direction[1], 0)
                direction[1] += 1
                self.__model.set(direction[0], direction[1], 6)
            else:
                if self.__model.get(direction[0], direction[1]) == 6:
                    self.__model.set(direction[0], direction[1], 4)
                else:
                    self.__model.set(direction[0], direction[1], 0)
                direction[1] += 1
                self.__model.set(direction[0], direction[1], 5)

        # Boucle pour vérifier les conditions lors d'un appui de la flèche gauche.
        elif key == Qt.Key_Left:
            if self.__model.get(direction[0], direction[1]-1) == 1:
                return
            elif self.__model.get(direction[0], direction[1]-1) == 2:
                if self.__model.get(direction[0], direction[1]-2) == 1 or self.__model.get(direction[0], direction[1]-2) == 2 or self.__model.get(direction[0], direction[1]-2) == 3:
                    return
                else:
                    self.__model.set(direction[0], direction[1]-1, 0)
                    if self.__model.get(direction[0], direction[1]-2) == 4:
                        self.__model.set(direction[0], direction[1]-2, 3)
                        self.__countOK += 1
                    else:
                        self.__model.set(direction[0], direction[1]-2, 2)
                    if self.__model.get(direction[0], direction[1]) == 6:
                        self.__model.set(direction[0], direction[1], 4)
                    else:
                        self.__model.set(direction[0], direction[1], 0)
                    direction[1] -= 1
                    self.__model.set(direction[0], direction[1], 5)
            elif self.__model.get(direction[0], direction[1]-1) == 3:
                if self.__model.get(direction[0], direction[1]-2) == 1 or self.__model.get(direction[0], direction[1]-2) == 2 or self.__model.get(direction[0], direction[1]-2) == 3:
                    return
                else:
                    self.__model.set(direction[0], direction[1]-1, 0)
                    self.__model.set(direction[0], direction[1]-2, 2)
                    self.__countOK -= 1                    
                    self.__model.set(direction[0], direction[1], 0)
                    direction[1] -= 1
                    self.__model.set(direction[0], direction[1], 6)
            elif self.__model.get(direction[0], direction[1]-1) == 4:
                self.__model.set(direction[0], direction[1], 0)
                direction[1] -= 1
                self.__model.set(direction[0], direction[1], 6)
            else:
                if self.__model.get(direction[0], direction[1]) == 6:
                    self.__model.set(direction[0], direction[1], 4)
                else:
                    self.__model.set(direction[0], direction[1], 0)
                direction[1] -= 1
                self.__model.set(direction[0], direction[1], 5)

        # Boucle pour vérifier les conditions lors d'un appui de la flèche du haut.
        elif key == Qt.Key_Up:
            if self.__model.get(direction[0]-1, direction[1]) == 1:
                return
            elif self.__model.get(direction[0]-1, direction[1]) == 2:
                if self.__model.get(direction[0]-2, direction[1]) == 1 or self.__model.get(direction[0]-2, direction[1]) == 2 or self.__model.get(direction[0]-2, direction[1]) == 3:
                    return
                else:
                    self.__model.set(direction[0]-1, direction[1], 0)
                    if self.__model.get(direction[0]-2, direction[1]) == 4:
                        self.__model.set(direction[0]-2, direction[1], 3)
                        self.__countOK += 1
                    else:
                        self.__model.set(direction[0]-2, direction[1], 2)
                    if self.__model.get(direction[0], direction[1]) == 6:
                        self.__model.set(direction[0], direction[1], 4)
                    else:
                        self.__model.set(direction[0], direction[1], 0)
                    direction[0] -= 1
                    self.__model.set(direction[0], direction[1], 5)
            elif self.__model.get(direction[0]-1, direction[1]) == 3:
                if self.__model.get(direction[0]-2, direction[1]) == 1 or self.__model.get(direction[0]-2, direction[1]) == 2 or self.__model.get(direction[0]-2, direction[1]) == 3:
                    return
                else:
                    self.__model.set(direction[0]-1, direction[1], 0)
                    self.__model.set(direction[0]-2, direction[1], 2)
                    self.__countOK -= 1
                    self.__model.set(direction[0], direction[1], 0)
                    direction[0] -= 1
                    self.__model.set(direction[0], direction[1], 6)
            elif self.__model.get(direction[0]-1, direction[1]) == 4:
                self.__model.set(direction[0], direction[1], 0)
                direction[0] -= 1
                self.__model.set(direction[0], direction[1], 6)
            else:
                if self.__model.get(direction[0], direction[1]) == 6:
                    self.__model.set(direction[0], direction[1], 4)
                else:
                    self.__model.set(direction[0], direction[1], 0)
                direction[0] -= 1
                self.__model.set(direction[0], direction[1], 5)

        # Boucle pour vérifier les conditions lors d'un appui de la flèche du bas.
        elif key == Qt.Key_Down:
            if self.__model.get(direction[0]+1, direction[1]) == 1:
                return
            elif self.__model.get(direction[0]+1, direction[1]) == 2:
                if self.__model.get(direction[0]+2, direction[1]) == 1 or self.__model.get(direction[0]+2, direction[1]) == 2 or self.__model.get(direction[0]+2, direction[1]) == 3:
                    return
                else:
                    self.__model.set(direction[0]+1, direction[1], 0)
                    if self.__model.get(direction[0]+2, direction[1]) == 4:
                        self.__model.set(direction[0]+2, direction[1], 3)
                        self.__countOK += 1
                    else:
                        self.__model.set(direction[0]+2, direction[1], 2)
                    if self.__model.get(direction[0], direction[1]) == 6:
                        self.__model.set(direction[0], direction[1], 4)
                    else:
                        self.__model.set(direction[0], direction[1], 0)
                    direction[0] += 1
                    self.__model.set(direction[0], direction[1], 5)
            elif self.__model.get(direction[0]+1, direction[1]) == 3:
                if self.__model.get(direction[0]+2, direction[1]) == 1 or self.__model.get(direction[0]+2, direction[1]) == 2 or self.__model.get(direction[0]+2, direction[1]) == 3:
                    return
                else:
                    self.__model.set(direction[0]+1, direction[1], 0)
                    self.__model.set(direction[0]+2, direction[1], 2)
                    self.__countOK -= 1
                    self.__model.set(direction[0], direction[1], 0)
                    direction[0] += 1
                    self.__model.set(direction[0], direction[1], 6)
            elif self.__model.get(direction[0]+1, direction[1]) == 4:
                self.__model.set(direction[0], direction[1], 0)
                direction[0] += 1
                self.__model.set(direction[0], direction[1], 6)
            else:
                if self.__model.get(direction[0], direction[1]) == 6:
                    self.__model.set(direction[0], direction[1], 4)
                else:
                    self.__model.set(direction[0], direction[1], 0)
                direction[0] += 1
                self.__model.set(direction[0], direction[1], 5)
        
        self.__pas += 1

        # Condition de victoire, réalisé si toutes les caisses sont sur les torches.
        if self.__countOK == 7:
            self.__winner = True

    def getWinner(self):
        # Getter du booléen de victoire.
        return self.__winner

    def restartGame(self):
        # Réinitialisation des paramètres.
        self.__model.clear()
        self.__view.cleanView()
        self.__model.start()
        self.__model.setDirection([2,3])
        self.__pas = 0
        self.__countOK = 1
        self.__winner = None

