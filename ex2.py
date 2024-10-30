import os

with open("frase_usuario.txt", "w") as frase:
    frase.write(input("Digite uma frase: "))

with open("frase_usuario.txt", "r") as frase:
        conteudo = frase.read()
        print(conteudo)
        
   