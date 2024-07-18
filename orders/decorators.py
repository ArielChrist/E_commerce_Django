
def decorator(func):
    def wrapper(request, *args, **kwargs):
        #traitement avant l'éxécution de la vue
        print("avant la vue decorateur ")
        response = func(request, **args, **kwargs)
        #traitement après l'éxécution de la vue
        print("après la vue decorateur")
        
        return response
    return wrapper