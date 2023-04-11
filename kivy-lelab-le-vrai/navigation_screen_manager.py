from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager):
    # GESTION D'UNE LISTE D'ECRAN
    screen_stack = []

    # FONCTION POUR POUSSER UN ECRAN = L'AFFICHER
    def push(self, screen_name):
        # on change d'écran uniquement si
        # l'écran n'est pas dans la liste des écrans précédents
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name

    # FONCTION POUR RETIRER UN ECRAN DE LA LISTE
    def pop(self):
        # retour en arrière que si la liste contient des éléments
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name
