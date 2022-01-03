from PyQt5.QtCore import QTimer

class SokobanModel:

    def __init__(self):

        # Initialisation des paramètres du model.
        self.__counter = 0
        self.__running = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(0)
        self.__direction = [2,3]
        self.__views = []
        self.__plateau = [[0,0,0,1,1,1,1,1,1],
                          [1,1,1,1,0,0,0,1,1],
                          [1,1,4,5,2,0,0,1,1],
                          [1,1,1,1,0,2,4,1,1],
                          [1,1,4,1,1,2,0,1,1],
                          [1,1,0,1,0,4,0,1,1],
                          [1,1,2,0,3,2,2,4,1],
                          [1,1,0,0,0,4,0,0,1],
                          [1,1,1,1,1,1,1,1,1]]

    def clear(self):
        # Réinitialise le plateau.
        self.__plateau = [[0,0,0,1,1,1,1,1,1],
                          [1,1,1,1,0,0,0,1,1],
                          [1,1,4,5,2,0,0,1,1],
                          [1,1,1,1,0,2,4,1,1],
                          [1,1,4,1,1,2,0,1,1],
                          [1,1,0,1,0,4,0,1,1],
                          [1,1,2,0,3,2,2,4,1],
                          [1,1,0,0,0,4,0,0,1],
                          [1,1,1,1,1,1,1,1,1]]

    def addView(self, view):
        # Ajouter des view.
        self.__views.append(view)

    def getDirection(self):
        # Getter de la direction du joueur.
        return self.__direction

    def setDirection(self, direction):
        # Setter de la direction du joueur.
        self.__direction = direction

    def get(self, l, c):
        # Récupère la valeur de la case du plateau.
        assert l in (0, 1, 2, 3, 4, 5, 6, 7, 8) and c in (0, 1, 2, 3, 4, 5, 6, 7, 8)
        return self.__plateau[l][c]

    def set(self, l, c, v):
        # Remplace la valeur de la case du plateau.
        assert l in (0, 1, 2, 3, 4, 5, 6, 7, 8) and c in (0, 1, 2, 3, 4, 5, 6, 7, 8)

        self.__plateau[l][c] = v

    def start(self):
        # Relance le timer à 0.
        self.__counter = 0
        self.__running = True
        self.timer.start(0)

    def stop(self):
        # Stop le timer.
        self.__running = False

    def timerEvent(self):
        # Vérifie si le timer est arrêté.
        if self.__running:
            self.__counter += 1

    def elapsed(self):
        # Retourne le temps écoulé.
        return self.__counter


