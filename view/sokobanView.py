from PyQt5.QtWidgets import QMainWindow, QGridLayout, QMenu, QAction, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound

class SokobanView(QMainWindow):


    def __init__(self):

        super().__init__()

        # Initialisation des paramètres pour le view.
        self.__seconds = "0"
        self.__minutes = "0"
        self.setWindowTitle("Sokoban")
        self.setFixedSize(900, 900)
        self.statusBar().showMessage("Timer : " + self.__minutes + " : " + self.__seconds +" | Déplacement : 0")

        self.__window = QLabel()
        self.setCentralWidget(self.__window)
        self.__gridLayout = QGridLayout()
        self.__window.setLayout(self.__gridLayout)
        self.__gridLabel = []
        self.__song = QSound("songs/C418.wav")
        self.__fireworks = QSound("songs/Fireworks.wav")
        self.__song.play()

        self.__model = None
        self.__controller = None

        # Création de l'onglet Jeu.
        menuBar = self.menuBar()
        gameMenu = QMenu("&Jeu", self)
        
        menuBar.addMenu(gameMenu)

        # Option restart.
        restart = QAction(self)
        restart.setText("&Restart")
        restart.setShortcut(Qt.Key_R)
        gameMenu.addAction(restart)
        restart.triggered.connect(self.restart)

        # Option quit.
        exitProgram = QAction(self)
        exitProgram.setText("&Quit")
        exitProgram.setShortcut(Qt.Key_Escape)
        gameMenu.addAction(exitProgram)
        exitProgram.triggered.connect(self.close)

        # Dimension des labels.
        rect = self.geometry()
        w = rect.width() / 9
        h = rect.height() / 9

        # Récupération des images.
        mur = QImage("images/Mur.png", 'png').copy(0, 0, 32, 32)
        sol = QImage("images/Sol.png", 'png').copy(0, 0, 32, 32)
        caisse = QImage("images/Caisse.png", 'png').copy(0, 0, 32, 32)
        caisseOK = QImage("images/CaisseOK.png", 'png').copy(0, 0, 32, 32)
        torche = QImage("images/Torche.png", 'png').copy(0, 0, 32, 32)
        personnage = QImage("images/Personnage.png", 'png').copy(0, 0, 32, 32)
        win = QImage("images/Victory.png", 'png').copy(0, 0, 502, 502)

        # Mise à l'échelle des images.
        self.__mur = QPixmap.fromImage(mur).scaled(w, h)
        self.__sol = QPixmap.fromImage(sol).scaled(w, h)
        self.__caisse = QPixmap.fromImage(caisse).scaled(w, h)
        self.__caisseOK = QPixmap.fromImage(caisseOK).scaled(w, h)
        self.__torche = QPixmap.fromImage(torche).scaled(w, h)
        self.__personnage = QPixmap.fromImage(personnage).scaled(w, h)
        self.__win = QPixmap.fromImage(win).scaled(rect.width(), rect.height())

        self.setWindowIcon(QIcon(self.__caisse))

        # Création du plateau de jeu.
        for i in range(9):
            tmp = []
            for j in range(9):
                label = QLabel()
                label.setStyleSheet(
                    "background-color:rgba(0,0,0,0)")
                label.setFixedSize(w, h)
                tmp.append(label)
                self.__gridLayout.addWidget(label, i, j)

            self.__gridLabel.append(tmp)

    def setModel(self, model):
        # Setter du model + lancement du timer.
        self.__model = model
        self.__model.start()

    def maj(self):
        # Récupération du temps.
        currentTime = self.__model.elapsed()

        self.__seconds = str((currentTime // 60000) % 60)
        self.__minutes = str((currentTime // 60000 // 60) % 60)

    def setPlateau(self):
        # Placement des images du jeu.
        for i in range(9):
            for j in range(9):
                if self.__model.get(i,j) == 0:
                    self.__gridLabel[i][j].setPixmap(self.__sol)
                if self.__model.get(i,j) == 1:
                    self.__gridLabel[i][j].setPixmap(self.__mur)
                if self.__model.get(i,j) == 2:
                    self.__gridLabel[i][j].setPixmap(self.__caisse)
                if self.__model.get(i,j) == 3:
                    self.__gridLabel[i][j].setPixmap(self.__caisseOK)
                if self.__model.get(i,j) == 4:
                    self.__gridLabel[i][j].setPixmap(self.__torche)
                if self.__model.get(i,j) == 5 or self.__model.get(i,j) == 6:
                    self.__gridLabel[i][j].setPixmap(self.__personnage)


    def cleanView(self):
        # Suppression des images du plateau.
        self.__window.setPixmap(QPixmap())
        for llabel in self.__gridLabel:
            for label in llabel:
                label.setPixmap(QPixmap())

    def restart(self):
        # Recharger la partie.
        self.__controller.restartGame()
        self.__minutes = "0"
        self.__seconds = "0"
        self.setWindowIcon(QIcon(self.__caisse))
        self.__song.play()
        self.setPlateau()
        self.statusBar().showMessage("Timer : " + self.__minutes + " : " + self.__seconds +" | Déplacement : 0")

    def setController(self, controller):
        # Setter du controller.
        self.__controller = controller

    def updateView(self):
        # Maj du jeu.
        self.setPlateau()
        self.update()
    
    def keyPressEvent(self,e):
        # Action réalisé après réception d'un appui de touche.
        self.__controller.play(e.key())
        self.maj()
        pas = self.__controller.getPas()
        self.statusBar().showMessage("Timer : " + self.__minutes + " : " + self.__seconds + " | Déplacement(s) : " + str(pas))
        self.updateView()
        if self.__controller.getWinner() == True:
            # Action réalisé si le joueur a gagné.
            self.__model.stop()
            self.setWindowIcon(QIcon(self.__caisseOK))
            self.cleanView()
            self.__song.stop()
            self.__fireworks.play()
            self.__window.setPixmap(self.__win)
            self.statusBar().showMessage("Félicitation, tu as réussi à finir le jeu en " + self.__minutes + " m et " + self.__seconds + " s avec " + str(pas) + " déplacements !")



