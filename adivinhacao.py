import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 50)) # 0.0 1.0
total_de_tentativas = 0
pontos = 100

print("Qual nível de dificuldade?")
print(" Nível(1) Fácil com 20 tentativas \n Nível(2) Médio com 10 tentativas \n Nível(3) Difícil com 5 tentativas")

nivel = int(input("Defina o nível da dificuldade 1, 2, ou 3: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 50: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez { } pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))




print("+++++++++++++++++++++++++++++++++")
print("++++++++++Fim do Jogo++++++++++++")
print("+++++++++++++++++++++++++++++++++")
