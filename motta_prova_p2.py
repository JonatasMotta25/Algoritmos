museu = []

def cadastrar_obra(título, data_criação, tema, estilo_artístico, descrição, técnica_utilizada, autor, localizacao):
  obra = {
    'título': título,
    'data_criação': data_criação,
    'tema': tema,
    'estilo_artístico': estilo_artístico,
    'descrição': descrição,
    'técnica_utilizada': técnica_utilizada,
    'autor': autor,
    'localizacao': localizacao
    }
  
  museu.append(obra)
  print(f"Obra '{título}' cadastrada com sucesso!")

def cadastrar_artista(nome, data_nascimento, biografia, estilos_artisticos):
  artista = {
  'nome': nome,
  'data_nascimento': data_nascimento,
  'biografia': biografia,
  'estilos_artisticos': estilos_artisticos
  } 
  print(f"Artista '{nome}' cadastrado com sucesso!")

def cadastrar_estilo_artistico(denominacao, periodo_influencia, caracteristicas_predominantes, escola_representativa):
  estilo_artistico = {
  'denominacao': denominacao,
  'periodo_influencia': periodo_influencia,
  'caracteristicas_predominantes': caracteristicas_predominantes,
  'escola_representativa': escola_representativa
  }
  print(f"Estilo artístico '{denominacao}' cadastrado com sucesso!")

def pesquisar_obras(tema=None, estilo_artistico=None, autor=None):
  resultado = []
  for obra in museu:
    if (tema is None or obra['tema'] == tema) and (estilo_artistico is None or obra['estilo_artístico'] == estilo_artistico) and (autor is None or obra['autor'] == autor):
      resultado.append(obra)
  return resultado

def realizar_emprestimo_obra(título_obra, nome_responsavel, evento, data_emprestimo):
  for obra in museu:
    if obra['título'] == título_obra:
      with open('registro_emprestimo.txt', 'a') as file:
        file.write(f"{data_emprestimo} - {nome_responsavel} - {evento} - {título_obra}\n")
        print(f"Empréstimo realizado com sucesso para a obra '{título_obra}'!")
        
def ordernar_obras():
  n = len(museu)
  for i in range(n):
    for j in range (0, n-i-1):
        ano_atual = int(museu[j]['data_criação'].split('-')[0])
        ano_proximo =  int(museu[j+1]['data_criação'].split('-')[0])
        
        if ano_atual < ano_proximo:
            museu[j], museu[j+1], = museu[j+1], museu[j]
  print("Obras ordenadas por ano de criação (descrescente):")
  for obra in museu:
    print(f"{obra['título']} - {obra['data_criação']}")
  
def menu():
  while True:
    print("Museu de Saquarema")
    print("1. Cadastrar obra")
    print("2. Cadastrar artista")
    print("3. Cadastrar estilo artístico")
    print("4. Pesquisar obras")
    print("5. Realizar empréstimo de obra")
    print("6. Ordenar obras")
    print("7. Sair")
    
    opcao = int(input("Digite a opção desejada: "))

    try:
        if opcao == 1:
          título = input("Digite o título da obra: ")
          data_criação = input("Digite a data de criação: ")
          tema = input("Digite o tema da obra: ")
          estilo_artístico = input("Digite o estilo artístico: ")
          descrição = input("Digite a descrição da obra: ")
          técnica_utilizada = input("Digite a técnica utilizada: ")
          autor = input("Digite o nome do autor: ")
          localizacao = input("Digite a localização da obra: ")
          cadastrar_obra(título, data_criação, tema, estilo_artístico, descrição, técnica_utilizada, autor, localizacao)

        elif opcao == 2:
          nome = input("Digite o nome do artista: ")
          data_nascimento = input("Digite a data de nascimento do artista: ")
          biografia = input("Digite a biografia do artista: ")
          estilos_artisticos = input("Digite os estilos artísticos do artista (separados por vírgula): ").split(",")
          cadastrar_artista(nome, data_nascimento, biografia, estilos_artisticos)

        elif opcao == 3:
          denominacao = input("Digite a denominação do estilo artístico: ")
          periodo_influencia = input("Digite o período de influência do estilo artístico: ")
          caracteristicas_predominantes = input("Digite as características predominantes: ")
          escola_representativa = input("Digite a escola representativa: ")
          cadastrar_estilo_artistico(denominacao, periodo_influencia, caracteristicas_predominantes, escola_representativa)


        elif opcao == 4:
          tema = input("Digite o tema para pesquisa (deixe em branco para todos): ") or None
          estilo_artistico = input("Digite o estilo artístico para pesquisa (deixe em branco para todos): ") or None
          autor = input("Digite o autor para pesquisa (deixe em branco para todos): ") or None
          obras_encontradas = pesquisar_obras(tema, estilo_artistico, autor)
          if obras_encontradas:
            for obra in obras_encontradas:
              print(obra)
          else:
              print("Nenhuma obra encontrada!")

        elif opcao == 5:
          título_obra = input("Digite o título da obra para empréstimo: ")
          nome_responsavel = input("Digite o nome do responsável pelo empréstimo: ")
          evento = input("Digite o evento para o empréstimo: ")
          data_emprestimo = input("Digite a data do empréstimo: ")
          realizar_emprestimo_obra(título_obra, nome_responsavel, evento, data_emprestimo)
        
        elif opcao == 6:
            ordernar_obras()

        elif opcao == 7:
          print("Saindo...")
          break

        else:
          print("Opção inválida, por favor escolha novamente.")

    except Exception as e:
      print(f"Erro ao executar a opção: {e}")

if __name__ == "__main__":
  try:
    menu()
  except Exception as e:
    print(f"Erro geral ao executar o programa: {e}")
  finally:
    print("Programa encerrado.")
  
  
  
  

  
  
