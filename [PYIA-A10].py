import flet as ft 

def main(page: ft.Page):
    dados_formulario = []
    page.title = "Formulário de Contato"
    page.bgcolor = "#1E1E1E"
    
    lista_envios = ft.ListView(spacing=10, expand=True,  height=400)  
#---------------------------------------------------------------------------------------------------------------------------------------------------#   
    def listar_contatos(e):
        lista_envios.controls.clear()
        for i, contato in enumerate(dados_formulario):
            bloco = ft.Container(
                content=ft.Column([
                    ft.Text(f"Nome: {contato['Nome']}", color="WHITE", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Email: {contato['Email']}", color="WHITE", size=14),
                    ft.Text(f"Mensagem: {contato['Mensagem']}", color="WHITE", size=14),
                ], spacing=5),
                bgcolor="#333333",
                padding=10,
                border_radius=10
            )
            lista_envios.controls.append(bloco)
        page.update()
    
    def salvar_dados(e):
        if nome.value and email.value and mensagem.value:
            dados = {
                "Nome": nome.value,
                "Email": email.value,
                "Mensagem": mensagem.value
            }
            dados_formulario.append(dados)
            
            snack_bar = ft.SnackBar(
                content=ft.Text("Enviado com sucesso!", color="WHITE"),
                bgcolor="green",
                duration=5000
            )
            page.show_snack_bar(snack_bar)
            
            nome.value = ""
            email.value = ""
            mensagem.value = ""
            page.update()
        else:
            snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos!", color="WHITE"),
                bgcolor="red",
                duration=5000
            )
            page.show_snack_bar(snack_bar)
            page.update()
#---------------------------------------------------------------------------------------------------------------------------------------------------#
    titulo = ft.Text("Formulário de Contato", size=30, weight=ft.FontWeight.BOLD, color='#4169E1', text_align=ft.TextAlign.CENTER)
    nome = ft.TextField(label="Digite seu nome", expand=True, color='WHITE', focused_border_color='#4169E1')
    email = ft.TextField(label="Digite seu Email", expand=True, color='WHITE', focused_border_color='#4169E1')
    mensagem = ft.TextField(label="Digite sua mensagem", expand=True, color='WHITE', focused_border_color='#4169E1')
    enviar = ft.ElevatedButton('Enviar', bgcolor='#4169E1', color='WHITE', on_click=salvar_dados, width= 100 ,height= 40)
    btn1_list = ft.ElevatedButton('Listar Tarefas', bgcolor='#4169E1', color='WHITE', on_click=listar_contatos,width= 100 ,height= 40)
    
    titulo_container = ft.Container(
        content=titulo,
        alignment=ft.alignment.center
    )
    
    formulario = ft.Column(
        controls=[nome, email, mensagem, ft.Row([enviar, btn1_list])],
        spacing=30
    )
    
    page.add(titulo_container, formulario, lista_envios, )

ft.app(target=main)