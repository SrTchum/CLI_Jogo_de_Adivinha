import random

def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1. Fácil (10 tentativas)")
    print("2. Médio (7 tentativas)")
    print("3. Difícil (5 tentativas)")
    opcao = input("Opção: ")

    if opcao == "1":
        return 10
    elif opcao == "2":
        return 7
    elif opcao == "3":
        return 5
    else:
        print("Opção inválida. Usando dificuldade média (7 tentativas).")
        return 7

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = escolher_dificuldade() 
    
    print("\nBem-vindo ao Jogo de Adivinhação!")
    print(f"Tente adivinhar o número entre 1 e 100 em até {max_tentativas} tentativas.\n")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Dica: Tente um número MAIOR.")
            elif palpite > numero_secreto:
                print("Dica: Tente um número MENOR.")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                return
        except ValueError:
            print("Por favor, digite um número válido.")

    print(f"Fim do jogo! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogar()