import json

from kivy.network.urlrequest import UrlRequest


class HttpClient: # fonction au même nom que le fichier
    def get_pizza(self, on_complete, on_error):
        url = "https://comptedemoettests.pythonanywhere.com/api/GetPizzas"
        # important de copier/coller cette url pour la tester via un navigateur
        # FONCTION DE DESERIALISATION
        # La fonction est imbriquée dans la fonction get_pizza afin d'éviter
        # qu'elle puisse être appelée en dehors de celle-ci
        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = [pizza['fields'] for pizza in data]
            if on_complete:
                # test si on_complete n'est pas None
                # alors exécution de la fonction avec le dictionnaire
                on_complete(pizzas_dict)
        def data_error(req, error):
            print("data_error")
            if on_error:
                on_error(str(error))
        def data_failure(req, result):
            print("data_failure")
            if on_error:
                on_error("Erreur serveur : " + str(req.resp_status))
        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)