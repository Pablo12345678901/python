# GESTION TAILLE FENÊTRE DE JEU AU DEMARRAGE
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

# IMPORTS
from kivy import platform
from kivy.core.window import Window
from kivy.app import App
from kivy.properties import Clock, ObjectProperty, StringProperty
from kivy.graphics import Color, Line, Quad, Triangle
from kivy.lang import Builder
from kivy.properties import NumericProperty
from random import randint
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.audio import SoundLoader


Builder.load_file("menu.kv")


# CREATION DU MAIN WIDGET
class MainWidget(RelativeLayout):
    from transforms import transform, transform_2D, transform_perspective # import des fonctions de transformation du fichiers transforms.py
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up

    menu_widget = ObjectProperty()
    # initialisation de 2 propriétés numérique pour les coordonnées du
    # point de perspective
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 8
    V_LINES_SPACING = .25 # valeur transformée plus tard en pourcentage de l'écran
    vertical_lines = []

    H_NB_LINES = 8
    H_LINES_SPACING = .15 # valeur transformée plus tard en pourcentage de l'écran
    horizontal_lines = []

    current_offset_y = 0
    SPEED = 0.005 # pour la vitesse en y de défilement - sera transformé en proportion de l'écran plus tard
    SPEED_X = .02 # pour la vitesse de décallage sur appui des touches / appui sur l'écran
    current_speed_x = 0
    current_offset_x = 0

    current_y_loop = 0
    NB_TILES = 10 # nombre de tiles
    tiles = [] # création d'une liste qui contiendra les tiles
    tiles_coordinates = [] # qui contiendra la liste des coordonnées des tiles en ti_x et ti_y = index
    NB_TILES_STRAIGHT_RIGHT = 16

    # VAISSEAU
    ship = None
    SHIP_WIDTH = 0.1 # il fera 10% de largeur
    SHIP_HEIGHT = 0.035 # il fera 3.5% de hauteur
    SHIP_BASE_Y = 0.04 # il sera à 4% de hauteur
    ship_coordinates_before_transformation = [(0, 0), (0, 0), (0, 0)] # 3 coordonnées du triangle ship initialisées à 0,0

    state_game_over = False # la variable passera à True si game over
    state_game_has_started = False # la variable passera à True lors du lancement du jeu

    menu_title = StringProperty("G   A   L   A   X   Y")
    menu_button_title = StringProperty("START")

    score_txt = StringProperty() # initialisation de la variable de gestion du score

    # SONS
    sound_begin = None # initialisé à None
    sound_galaxy = None
    sound_gameover_impact = None
    sound_gameover_voice = None
    sound_music1 = None
    sound_restart = None

    # CREATION FONCTION INIT
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_audio() # chargement des sons dans les variables de class
        self.init_vertical_lines() # appel de la fonction pour générer des lignes verticales
        self.init_horizontal_lines() # appel de la fonction pour générer des lignes horizontales
        self.init_tiles()
        self.init_ship()
        self.pre_fill_titles_coordinates()
        self.generate_tiles_coordinates()

        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self) # appelle keyboard_closed lorsqu'il se ferme
            self.keyboard.bind(on_key_down=self.on_keyboard_down) # en cas d'appui sur touche
            self.keyboard.bind(on_key_up=self.on_keyboard_up) # en cas de relachement de touche

        Clock.schedule_interval(self.update, 1.0/60.0) # appel de la fonction update 60fps
        self.sound_galaxy.play()  # son d'entrée de jeu

    # FONCTION DE CHARGEMENT DES SONS
    # les sons sont stockés dans des variables pour réutilisation ultérieure
    def init_audio(self):
        self.sound_begin = SoundLoader.load("RESSOURCES/audio/begin.wav")
        self.sound_galaxy = SoundLoader.load("RESSOURCES/audio/galaxy.wav")
        self.sound_gameover_impact = SoundLoader.load("RESSOURCES/audio/gameover_impact.wav")
        self.sound_gameover_voice = SoundLoader.load("RESSOURCES/audio/gameover_voice.wav")
        self.sound_music1 = SoundLoader.load("RESSOURCES/audio/music1.wav")
        self.sound_restart = SoundLoader.load("RESSOURCES/audio/restart.wav")
        # DEFINITION DU VOLUME POUR CHAQUE SON
        self.sound_music1.volume = .25 # volume à 100%
        self.sound_begin.volume = .25 # volume à 25%
        self.sound_galaxy.volume = .25
        self.sound_gameover_voice.volume = .25
        self.sound_restart.volume = .25
        self.sound_gameover_impact.volume = .6

    # FONCTION DE REINITIALISATION DE VARIABLE (UTILE APRES LE GAME OVER)
    # ACTIVE LORS DU CLIC SUR LE BOUTON POUR (RE)DEMARRER LE JEU
    def reset_game(self):
        #FUN self.SPEED = 0.005 # remise à la valeur initiale car accélération y dans le jeu au fil du temps
        #FUN self.SPEED_X = .01 # remise à la valeur initiale car accélération de déplacement x dans le jeu au fil du temps
        self.current_offset_y = 0 # remise à 0 du décalage sur l'axe y
        self.current_y_loop = 0 # remise à 0 de la boucle pour les coordonnées y
        self.current_offset_x = 0 # remise à 0 du décalage sur l'axe x
        self.current_speed_x = 0 # remise à 0 de la vitesse x, au cas où on était en déplacement x lorsqu'on a perdu
        self.tiles_coordinates = []  # vidage des coordonnées des index de tiles
        self.pre_fill_titles_coordinates() # pour les remplir avec une ligne droite de tiles
        self.generate_tiles_coordinates() # puis de continuer à générer des tiles
        self.score_txt = "SCORE : " + str(self.current_y_loop)
        self.state_game_over = False # remis à False à la fin car sinon le jeu commence alors que les variables ne sont pas réinitialisées

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'): # test si le nom de la plateforme est ordinateur
            return True # retourne True si ordinateur
        return False # retourne False si non ordinateur

    def get_line_x_from_index(self, index):  # pour les lignes verticales > afin d'obtenir le x
        central_line_x = self.perspective_point_x  # cordonnée x de la ligne centrale du point de perspective - pour permettre des évolution plus faciles si souhaitées
        spacing = self.V_LINES_SPACING * self.width  # donne la valeur à partir de la proportion
        offset = index - 0.5  # car l'index 0 est la ligne à gauche du milieu de l'écran, décallé de 0.5 index > utilisé ensuite pour multiplié le spacing
        line_x = central_line_x + offset * spacing + self.current_offset_x  # en prenant en compte le décallage pour toujours obtenir la bonne positions
        return int(line_x) # retourne la coordonnée x de la ligne selon l'index

    def get_line_y_from_index(self, index):
        spacing_y = self.H_LINES_SPACING * self.height  # donne la valeur à partir de la proportion
        line_y = index * spacing_y - self.current_offset_y  # en prenant en compte le décallage pour toujours obtenir la bonne position
        return line_y  # retourne la coordonnée y de la ligne selon l'index

    def get_tile_coordinates(self, ti_x, ti_y): # Fonction qui obtiendra les coordonnées des 4 coins basées sur son indexage
        ti_y = ti_y - self.current_y_loop # réduction de l'index y par le nombre de boucle faite
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y

    # FONCTION DE GENERATION DU TRIANGLE = SHIP
    def init_ship(self):
        with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle() # ajout du triange sans coordonnées

    # FONCTION DE GENERATION DE TILES
    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_TILES):
                self.tiles.append(Quad()) # ajout des tiles avec quad vide

    # FONCTION DE GENERATION DE TILES EN LIGNES DROITE
    def pre_fill_titles_coordinates(self):
        for i in range(0, self.NB_TILES_STRAIGHT_RIGHT): # bouclera x fois
            self.tiles_coordinates.append((0, i)) # en ligne droite au centre, avec x = 0

    def generate_tiles_coordinates(self):
        last_x = 0
        last_y = 0 # initialisation de la valeur de l'index y de la derniere paire de coordonnées créées
        # SUPPRESSION DES COORDONNES SORTIE
        # condition : ti_y < self.current_y_loop
        for i in range(len(self.tiles_coordinates)-1, -1, -1): # on boucle sur tous les éléments en partant du dernier pour éviter les problèmes d'index en cas de suppression
            # self.tiles_coordinates)-1 car on sort du tableau sinon
            # deuxième "-1" : pour que l'élément en index 0 soit atteint, sinon jamais atteint et la boucle se stoppe à l'index 1
            # troisième "-1" : pour boucler en sens inverse
            if self.tiles_coordinates[i][1] < self.current_y_loop:
                del self.tiles_coordinates[i]
        if len(self.tiles_coordinates) > 0: # réajustement du last_y
            last_coordinates = self.tiles_coordinates[-1] # au y de la dernière paire de coordonnées créées
            last_y = last_coordinates[1] + 1 # et ajout de +1
            # sinon par défaut, le last_y est remis à 0 à chaque appel de la fonction generate_tiles_coordinates
            last_coordinates = self.tiles_coordinates[-1]  # au y de la dernière paire de coordonnées créées
            last_x = last_coordinates[0] # adaptation du last x selon les dernières coordonnées produites
        for i in range(len(self.tiles_coordinates), self.NB_TILES): # départ depuis la longueur des tuples de coordonnées
            # ainsi si le tuple des coordonnées et plus petit que le nombre de tiles alors cela déclenche la création d'un nouveau tile
            r = randint(0, 2)  # valeur min et max sont incluses x2 dans les résultats
            # 0 -> en avant : simple case
            # 1 -> droite : L inversé
            # 2 -> gauche : L
            start_index = -int(self.V_NB_LINES / 2) + 1  # calcul de l'index de la ligne la plus à gauche
            end_index = start_index + self.V_NB_LINES  # calcul de l'index de la ligne la plus à droite
            self.tiles_coordinates.append((last_x, last_y))  # ajout de coordonnées (index de tile) pour futurement créer une ligne
            if (r == 1) and (last_x < (end_index-2)): # "-2" : aller à droite sauf si on est sur la dernière case de droite
                last_x += 1 # décalage d'un case vers la droite
                self.tiles_coordinates.append((last_x, last_y)) # ajout du tile décalé à droite
                last_y += 1 # décalage du last_y d'une case vers le haut
                self.tiles_coordinates.append((last_x, last_y)) # ajout du tile décalé en haut
            elif (r == 2) and (last_x > start_index): # aller à gauche sauf si on est sur la dernière case de gauche
                last_x -= 1  # décalage d'un case vers la droite
                self.tiles_coordinates.append((last_x, last_y))
                last_y += 1  # décalage du last_y d'une case vers le haut
                self.tiles_coordinates.append((last_x, last_y))  # ajout du tile décalé en haut
            last_y += 1  # augmentation du dernier index à chaque fois que de nouvelles coordonnées sont créées


    # FONCTION DE GENERATION DE LIGNES
    def init_vertical_lines(self):
        #DEBUG print("INIT V")
        with self.canvas:
            Color(1, 1, 1)
            # boucle pour créer le nombre de lignes
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
                # peut importe la valeur de celle-ci car elles seront adaptées par la suite

    def init_horizontal_lines(self):
        #DEBUG print("INIT H")
        with self.canvas:
            Color(1, 1, 1)
            # boucle pour créer le nombre de lignes
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())
                # peut importe la valeur de celle-ci car elles seront adaptées par la suite

    # FONCTION D'ADAPTATION DES COORDONNEES DU VAISSEAU
    def update_tiles(self):
        for i in range(0, self.NB_TILES):
            tile = self.tiles[i] # lien vers l'objet dans l'index i
            tile_coordinates = self.tiles_coordinates[i] # récupération des coordonnées sous forme de tuple
            xmin, ymin = self.get_tile_coordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.get_tile_coordinates(tile_coordinates[0] + 1, tile_coordinates[1] + 1)
            # schéma des points
            #   2       3
            #
            #   1       4
            # TRANFORMATION EN PERPSECTIVE
            x1, y1 = self.transform(xmin, ymin)
            x2, y2 = self.transform(xmin, ymax)
            x3, y3 = self.transform(xmax, ymax)
            x4, y4 = self.transform(xmax, ymin)
            tile.points = [x1, y1, x2, y2, x3, y3, x4, y4] # liste 3 coins du triangle > mis à jour à chaque intervalle
            # afin que si redimensionnement de la taille de la fenêtre, le vaisseau aussi soit redimensionné

    def update_vertical_lines(self):
        start_index = -int(self.V_NB_LINES/2) + 1 # calcul de l'index de la ligne la plus à gauche
        end_index = start_index + self.V_NB_LINES # calcul de l'index de la ligne la plus à droite
        for i in range(start_index, end_index): # implémentation des extrême
            line_x = self.get_line_x_from_index(i) # voir fonction ci-dessus
            x1, y1 = self.transform(line_x, 0) # transformation des valeurs x1, y1
            x2, y2 = self.transform(line_x, self.height) # idem x2, y2
            self.vertical_lines[i].points = [x1, y1, x2, y2]

    def update_horizontal_lines(self):
        start_index = -int(self.V_NB_LINES / 2) + 1  # calcul de l'index de la ligne la plus à gauche
        end_index = start_index + self.V_NB_LINES  # calcul de l'index de la ligne la plus à droite
        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index - 1) # "-1" on ne va pas à l'index de fin, on s'arrête juste avant voir la fonction "get_line_x_from_index"
        for i in range(0, self.H_NB_LINES):
            #line_y = i * spacing_y - self.current_offset_y # la hauteur de la ligne sera incrémentée de i * spacing à chaque boucle
            line_y = self.get_line_y_from_index(i)
            # et de l'offset à chaque intervalle
            x1, y1 = self.transform(xmin, line_y) # transformation des valeurs x1, y1
            x2, y2 = self.transform(xmax, line_y) # idem x2, y2
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update_ship(self):
        half_width = self.SHIP_WIDTH * self.width / 2 # moitié de la largeur du vaisseau
        height = self.SHIP_HEIGHT * self.height # hauteur du vaisseau
        base_y = self.SHIP_BASE_Y * self.height # position du vaisseau en hauteur
        center_x = self.width / 2
        # SCHEMA DES POINTS
        #       2
        #   1       3
        # 1 : coin en bas à gauche
        self.ship_coordinates_before_transformation[0] = (center_x - half_width, base_y) # conservation des coordonnées du ship dans la variable de class
        x1, y1 = self.transform(*self.ship_coordinates_before_transformation[0])  # expansion des 2 paramètres - unpack le tuple + transformation en perspective
        # 2 : la pointe d'en haut
        self.ship_coordinates_before_transformation[1] = (center_x, base_y + height)
        x2, y2 = self.transform(*self.ship_coordinates_before_transformation[1])
        # 3 : coin en bas à droite
        self.ship_coordinates_before_transformation[2] = (center_x + half_width, base_y)
        x3, y3 = self.transform(*self.ship_coordinates_before_transformation[2]) # mise en perspective
        self.ship.points = [x1, y1, x2, y2, x3, y3]

    # FONCTION DE CONTROLE DE COLLISION AVEC TOUS LES TILES
    def check_ship_collisions(self):
        for i in range(0, len(self.tiles_coordinates)): # on boucle sur tous les tiles
            ti_x, ti_y = self.tiles_coordinates[i] # récupération des coordonnées
            if ti_y > self.current_y_loop + 1: # si ti_y ne fait partie des 2 première rangée - il est plus grand
                return False # on économise le programme de boucles inutiles - il n'y a pas eu de collision
            else:
                if self.check_ship_collision_with_tile(ti_x, ti_y):
                    return True
        return False # si on n'a fini de boucler mais qu'on a pas eu True, alors forcément collision = False


    # FONCTION DE CONTRÔLE SI COLISION ENTRE LE SHIP ET UN TILE
    def check_ship_collision_with_tile(self, ti_x, ti_y):
        # récupération des coordonnées des 4 coins du tiles
        x_min, y_min = self.get_tile_coordinates(ti_x, ti_y)
        x_max, y_max = self.get_tile_coordinates(ti_x + 1, ti_y + 1)
        for i in range(0, 3):
            px, py = self.ship_coordinates_before_transformation[i]
            if (x_min <= px <= x_max) and (y_min <= py <= y_max):
                return True # Si au moins un des points du ship est dedans la tile
        return False # sinon False

    def update(self, dt):
        #DEBUG print("dt : " + str(dt) + "- 1/60 " + str(1.0/60.0))
        time_factor = dt * 60.0 # devrait être 1 - mais si prend plus de temps, sera plus grand que 1 et si prend moins de temps, sera plus petit que 1 - sert à ajuster la vitesse proportionnellement
        self.update_vertical_lines() # appeler la fonction d'update 60x/sec
        self.update_horizontal_lines() # appeler la fonction d'update 60x/sec
        self.update_tiles() # appeler la fonction d'update 60x/sec
        self.update_ship()
        if not self.state_game_over and self.state_game_has_started: # tant que pas GAME OVER et que le jeu a démarré, on permet l'avancement
            speed_y = self.SPEED * self.height # adaptation de la vitesse en proportion de la taille de l'écran
            self.current_offset_y += speed_y * time_factor # accroissement de l'offset à chaque intervalle
            # on avance de la vitesse * le facteur temps qui dépend du delta time
            # ainsi le jeu semble avancer à la même vitesse sur toute machine
            spacing_y = self.H_LINES_SPACING * self.height # reprise du code de la fonction update_horizontal_lines pour obtenir l'espacement entre 2 lignes
            while self.current_offset_y >= spacing_y: # tant que le décallage dépasse ou est égal à une ligne (un écart entre deux lignes)
                self.current_offset_y -= spacing_y # alors on soustrait une ligne - cela équivaut presque à remettre le décallage à 0
                self.current_y_loop += 1 # adaptation d'une variable qui compte le nombre de boucle pour décaller le tile d'un cran à chaque boucle
                self.score_txt = "SCORE : " + str(self.current_y_loop) # adaptation de la valeur de score_txt à chaque tour de boucle
                self.generate_tiles_coordinates()
                #FUN self.SPEED *= (1 + (1/100)) # accélération à chaque tile
                #FUN self.SPEED_X *= (1 + (1/100)) # accélération à chaque tile
            speed_x = self.current_speed_x * self.width # adaptation de la vitesse en proportion de la taille de l'écran
            self.current_offset_x += speed_x * time_factor # le décallage x  dépend du current_speed et pas du speed
        if not self.check_ship_collisions() and not self.state_game_over: # si pas de collision (= négatif) et que pas encore eu le GAME OVER
            # rappel : collision = collision avec un tile du chemin = positif
            # si pas de collision = négatif = sorti du chemin
            self.state_game_over = True # si GAMEOVER, la variable passe à True
            self.menu_title = "G  A  M  E     O  V  E  R" # modification du titre du menu
            self.menu_button_title = "RE-START" # modification du titre du bouton
            self.menu_widget.opacity = 0.8
            self.sound_music1.stop() # arrêt de la musique après affichage du GAME OVER
            self.sound_gameover_impact.play() # bruit impact lors qu'on sort du chemin
            Clock.schedule_once(self.play_voice_game_over, 3) # la fonction du son ne sera appelé qu'une fois au bout de 3 secondes
            print("GAME OVER") #DEBUG

    def play_voice_game_over(self, dt):
        if self.state_game_over: # le son n'est jouer qu'en état GAME OVER
            # donc si le joueur clic vite sur re-start, le son ne sera pas joué
            self.sound_gameover_voice.play()  # voix qui dit "GAME OVER"

    # FONCTION QUI GERE LE CLIC SUR LE BOUTON DU MENU
    def on_menu_button_pressed(self):
        if self.state_game_over: # si GAME OVER
            self.sound_gameover_impact.stop() # coupe le son impact qui est long
            # sinon si en début de jeu je me crash, le son n'est pas joué
            # car l'ancien son est encore en train d'être joué
            self.sound_restart.play() # alors son "restart
        else:
            self.sound_begin.play() # sinon son "begin"
        self.sound_music1.play()  # musique de jeu
        self.reset_game()
        self.state_game_has_started = True # Démarrage du jeu
        self.menu_widget.opacity = 0




# CREATION DE L'APP
class GalaxyApp(App):
    pass

# LANCEMENT DE L'APP
GalaxyApp().run()