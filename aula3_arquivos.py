#arquivos
import os
def criar_arquivos():
    try:
        os.chdir(r"C:\Users\UNIVASSOURAS\Documents")

        with open("arquivo.txt", "w") as arquivo:
            arquivo.write("escrevendo alguma coisa\n")
            
        with open("arquivo.txt", "r") as arquivo:
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