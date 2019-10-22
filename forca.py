class Palavra:
    def __init__(self):
        self.palavra "peixeeletrico"
        self.palavra = self.palavra.upper()
        self.esconder()
    def esconder(self)
        self.palavra_misterio = []
        for letra in self.palavra:
            self.palavra_misterio.append('_')
    def revelar(elf, letra):
        for posicao, letra_palavra in  enumerate(self.palavra):
            if letra == letra_palavra:
                self.palavra_misterioa[posicao] = letra 
    def esta_completa(self):
        if '_' in self.palavra_misterio:
            return False
        else:    
            return True               


    def tem_letra(self, letra):
        if letra in self.palavra:  
            return True
        else:    
            return False   
   

class Jogo:
    def _init_(self):
    self.vidas = 6
    self.chutes = 0
    self.palavra_escondida = Palavra()
    self.histrico _chutes = []

    def chutar(self, letra):
       self.chutes += 1 
       letra = letra.upper()
       if self.eh_valido(letra):
           if self.adiciona_historico(letra):
               if self.palavra_escondida.tem_letra(letra):
                   self.palavra_escondida.revelar(letra)
                else:
                   self.vidas -= 1   
    def ganhou(self):
        if self.palavra_escondida.esta_completa():
            return True
        else:
            return False
    def perdeu(self):  
        if self.vidas <= 0:
            return True
        else:
            return False                      



    def adiciona_historico(self, letra):
        if letra in self.historico_chutes:
            return False
        else:
            self.historico_chutes.append(letra)    

    def eh_valido(self, letra):
       if len(letra) == 1 and letra.isapha():
           return True 
        else:
            return False         

if _name_ =="_main_":
    jogo = jogo()
    while not jogo.ganhou() and  jogos.pedeu()):
        print("-------------------")
        print(f"vidas: {jogo.vidas}")
        print(jogo.palavra_escondida)
        print(f"chutes: {jogo.historico_chutes}")
        print("----------------------")
        letra = input("Digite uma letra")
        jogo.chutar (letra)
        if jogo.ganhou()
            print("voca ficou vivo desa vez")
        elif jogo.perdeu()
              print("chegou a sua hora!")




