class Casa:
    def __init__(self):
        self.paredes = ""
        self.portas = ""
        self.janelas = ""
        self.telhado = ""
        self.garagem = ""

class CasaBuilder:
    def __init__(self):
        self.casa = Casa()    

    def construir_paredes(self):
        self.casa.paredes = "Paredes construídas\n"
        return self
    
    def construir_portas(self):
        self.casa.portas = "Portas instaladas\n"
        return self
    
    def construir_janelas(self):
        self.casa.janelas = "Janelas instaladas\n"
        return self
    
    def construir_telhado(self):
        self.casa.telhado = "Telhado construído\n"
        return self
    
    def construir_garagem(self):
        self.casa.garagem = "Garagem construída\n"
        return self
    
    def get_casa(self):
        return self.casa
    

if __name__ == "__main__":
    ObjCasa = (
        CasaBuilder()
        .construir_garagem()
        .construir_janelas() 
        .construir_portas()
        .construir_paredes()
        .construir_telhado()
        .get_casa()
    )

    print(f"{ObjCasa.paredes}\n{ObjCasa.portas}\n{ObjCasa.janelas}\n{ObjCasa.telhado}\n{ObjCasa.garagem}")