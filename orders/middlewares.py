class HeaderMiddleware:
    
    def __init__(self, get_response):
        #get_response correspond à la vue à exécuter
        self.get_response = get_response
        
    def __call__(self, request):
        # traitement à effectuer avant la vue
        print("avant la vue middleware ")
        response = self.get_response(request)
        #traitement après l'éxécution de la vue
        print("après la vue middleware ")
        return response