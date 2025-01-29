import flet as ft 

def adicionar_tarefa(e, campo_tarefa, lista_tarefas, page):
    if campo_tarefa.value:
        lista_tarefas.controls.append(ft.Text(campo_tarefa.value))
        campo_tarefa.value = ""  
        page.update() 


def main(page: ft.Page):
    campo_tarefa = ft.TextField(label="Nova Tarefa", expand=True,color='white')
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=lambda e: adicionar_tarefa(e, campo_tarefa, lista_tarefas, page),bgcolor='green',color='white')
    lista_tarefas = ft.Column()
    
    page.add(ft.Row(controls=[campo_tarefa,botao_adicionar]),lista_tarefas)


ft.app(target=main)
