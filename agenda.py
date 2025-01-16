tarefas = []

def add_tarefa ():
    nome = input("insira o nome da tarefa: ")
    descricao = input("insira a descrição da tarefa: ")
    prioridade = input("insira o nivel de prioridade da tarefa: ")
    categoria = input("insira a categoria da tarefa: ")
    tarefa ={
        'nome' : nome,
        'descrição' : descricao,
        'prioridade' : prioridade,
        'categoria' : categoria,
        'status' : 'pendente'
        }
    tarefas.append(tarefa)
    print("tarefa adicionada")

def concluir_tarefa (nome_tarefa): 
    for tarefa in tarefas:
        if tarefa['nome'] == nome_tarefa:
            tarefa['status'] = 'concluida'
            print(f'tarefa {nome_tarefa} concluida')
            return
        print("tarefa não encontrada")
        
def listar_tarefas ():
    if not tarefas:
        print("não há nenhuma tarefa")
    else:
        for tarefa in tarefas:
            print(f'''
                   ______________________________________
                  |               Tarefas                |
                  |--------------------------------------|
                  |Nome:{tarefa['nome']}                 |
                  |Descrição: {tarefa['descrição']}      |
                  |prioridade: {tarefa['prioridade']}    |
                  |categoria: {tarefa['categoria']}      |
                  |status: {tarefa['status']}            |
                  |______________________________________|
                  ''')

    while True:
        print('''
               ______________________________________
              |            lista de tarefas          |
              |--------------------------------------|
              |0.encerrar programa                   | 
              |1.adicionar tarefa                    |
              |2.listar tarefas                      |
              |3.marcar tarefa como concluida        |
              |______________________________________|
              ''')