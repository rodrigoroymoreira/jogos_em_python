import forca
import advinhacao
import jogoppt.py

print("********************************")
print("Escolha o seu jogo!")
print("********************************")


print("(1) Forca (2) Advinhacao (3) Pedra, Papel e Tesoura")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Advinhacao")
    advinhacao.jogar()
elif(jogo == 3):
    print("Jogando Pedra, Papel e Tesoura")
    jogoppt.jogar()