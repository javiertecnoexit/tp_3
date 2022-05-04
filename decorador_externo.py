def decorador_externo(function):
    def wrapper():
        print(" soy un decorador externo y vine desde otro archivo")
        function()
        
    return wrapper