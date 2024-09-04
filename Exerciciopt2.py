lista_tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:
        id = max(x['id'] for x in lista_tarefas) + 1
    else:
        id = 1
        
    tarefas = {
        'id': id,
        'descricao': descricao,
        'status': status,
        'prioridade': prioridade
    }
    lista_tarefas.append(tarefas)
    
adicionar_tarefa(lista_tarefas, 'foi alguma coisa', 'pendente', 'baixa')

def visualizar_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print(f'ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}')

visualizar_tarefas(lista_tarefas)

def filtrar_tarefas(lista_tarefas):
    print('Filtrar por:')
    print('1. Status')
    print('2. Prioridade') 
    escolha = int(input('Escolha uma opção: '))  
    if escolha == 1:
        status = input('Qual status deseja filtrar?')
        tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa['status'] == status]
        visualizar_tarefas(tarefas_filtradas)
        
    elif escolha == 2:
        prioridade = input('Digite a prioridade: ')
        tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa['prioridade'] == prioridade]
        visualizar_tarefas(tarefas_filtradas)
    
    else:
        print('Opção inválida.')
        
        
filtrar_tarefas(lista_tarefas)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         