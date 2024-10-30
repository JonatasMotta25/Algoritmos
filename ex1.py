import os

try:
    with open("mensagem.txt", "w") as arquivo:
        arquivo.write("Vasco maior do mundo.\n")
        
    with open("mensagem.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        
    print(os.getcwd())
    
except FileNotFoundError:
    print("Arquivo não encontrado")
    
except PermissionError:
    print("Você não tem permissão de leitura/escrita")
    
except Exception as e:
    print("Deu erro de: {e}")
    
finally:
    print("Até mais!!")