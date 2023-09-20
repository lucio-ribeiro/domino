import random
import os


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def __str__(self):
        return f"Peças do jogador {self.nome} : {', '.join(str(peca) for peca in self.mao)}"

    def jogar_peca(self, peca):
        self.mao.remove(peca)

    def mostrar_mao(self):
        print(f"Peças do {self.nome}: ")
        for i, domino in enumerate(self.mao):
            print(f"{i+1}: {domino}")


class DominoPeca:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return f"[{self.side1}|{self.side2}]"


class DominoGame:
    def __init__(self):
        self.tabuleiro = []
        self.jogadores = []

    def criar_pecas(self):
        domino = []
        for i in range(7):
            for j in range(i, 7):
                domino.append((i, j))
        return domino

    def embaralha_pecas(self):
        pecas = self.criar_pecas()
        random.shuffle(pecas)
        return pecas

    def adiciona_jogador(self, jogador):
        self.jogadores.append(jogador)

    def inicia_jogo(self):
        pecas = self.embaralha_pecas()
        for i, jogador in enumerate(self.jogadores):
            for j in range(7):
                peca = pecas[i]
                jogador.mao.append(pecas[i])
                pecas.remove(peca)

        return pecas
    
    def verificapeca(self, peca):
        
        if (len(self.tabuleiro) > 0 ):

            ultimapeca = self.tabuleiro[len(self.tabuleiro) - 1]
            primeirapeca = self.tabuleiro[0]


            if (peca[0] == ultimapeca[1]):
                self.tabuleiro.append(peca)
                return True
            
            elif (peca[1] == ultimapeca[1]):
                nova_peca = (peca[1], peca[0])
                self.tabuleiro.append(nova_peca)
                return True
            
            elif(peca[1] == primeirapeca[0]):
                self.tabuleiro.insert(0, peca)
                return True
            
            elif(peca[0] == primeirapeca[0]):
                nova_peca = (peca[1], peca[0])  
                self.tabuleiro.insert(0, nova_peca)
                return True
            
            else:
                print("PEÇA INVALIDA")
                return False
        else:
            self.tabuleiro.append(peca)
            return True


    def alguem_venceu(self):
        for jogador in self.jogadores:
            if (len(jogador.mao)==0):
                return False
            else:
                return True
 


    
def main():    
    

    num_jogadores = int(input("Digite o número de Jogadores: "))
    while num_jogadores < 2 or num_jogadores > 4:
        print("O número de jogadores deve ser entre 2 e 4.")
        num_jogadores = int(input("Digite o número de Jogadores novamente: "))
        
    jogo = DominoGame()
    

    for i in range(num_jogadores):
        nome = input("Digite o nome do jogador: ")
        jogadorteste = Jogador(nome)
        jogo.adiciona_jogador(jogadorteste)


    pecascomprar = jogo.inicia_jogo()
    jogadores = jogo.jogadores


    while (jogo.alguem_venceu()):
        for jogador in jogadores:
            mesa = jogo.tabuleiro
            print("\nMesa de dominó:")
            print(mesa)
            jogador.mostrar_mao()
            escolha = int(input("Escolha uma peça para jogar (digite o número da peça ou '0' para comprar uma nova): "))
            peca = jogador.mao[escolha - 1]
            
            while True:
               if (escolha > len(jogador.mao)):
                    print("\nMesa de dominó:")
                    print(mesa)
                    jogador.mostrar_mao()
                    escolha = int(input("Escolha uma peça para jogar (digite o número da peça ou '0' para comprar uma nova): "))
                    peca = jogador.mao[escolha - 1]
            
               elif(escolha==0):
                   if (len(pecascomprar) > 0 ):
                     
                     random.shuffle(pecascomprar)
                     jogador.mao.append(pecascomprar[0])
                     pecascomprar.remove(pecascomprar[0])

                     print("\nMesa de dominó:")
                     print(mesa)
                     jogador.mostrar_mao()
                     escolha = int(input("Escolha uma peça para jogar (digite o número da peça ou '0' para comprar uma nova): "))
                     peca = jogador.mao[escolha - 1]


                   else:
                       print("Acabaram as pecas para comprar, sua vez será passada!")
                       break;
               
               elif (jogo.verificapeca(peca)):
                   break;
               else:
                    print("\nMesa de dominó:")
                    print(mesa)
                    jogador.mostrar_mao()
                    escolha = int(input("Escolha uma peça para jogar (digite o número da peça ou '0' para comprar uma nova): "))
                    peca = jogador.mao[escolha - 1]

            jogador.jogar_peca(peca)
            os.system('cls' if os.name == 'nt' else 'clear')
            if (jogo.alguem_venceu() == False):
                jogadorcampeao = jogador
                break;
            

    print("Fim do jogo! Jogador Vencedor : " ,jogadorcampeao.nome)

if __name__ == "__main__":
    main()
