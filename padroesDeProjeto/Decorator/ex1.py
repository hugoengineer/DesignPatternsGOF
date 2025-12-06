def DecoradorFunction(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Entrei no superior")
        print(f"Saindo do superior") 
        return original_function(*args, **kwargs)
    
    return wrapper_function

@DecoradorFunction
def funcao_decorada1(msg):
    print(f"Mensagem: {msg}")

@DecoradorFunction
def funcao_decorada2(nome):
    print(f"Nome: {nome}")

if __name__ == "__main__":
    funcao_decorada1("Olá, Mundo!")
    funcao_decorada2("Augusto")