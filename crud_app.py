import flet as ft
from pessoa import *
from manipulador import *

def main(page: ft.Page):
    page.title = 'Cadastro'
    # page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed="brown")
    page.scroll = 'adaptive'
 
    p = Pessoa(0,'','','','','','')
    m = Manipulador() 
    
#NOTE: usuarios_cadastrados   
    def usuarios_cadastrados(e):
        try:
                    usuario = {}
                    campos = ("nome", "cpf", "email", "profissao")
                    print(f"Arquivo aberto: {abrir_arquivo}.json\n")
                    for campo in campos:
                        usuario[campo] = input(f"Informe o campo {campo.capitalize()}: ")
                    usuario["codigo"] = len(usuarios)
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo)) 
        except Exception as e:
                    print(f"Não foi possível realizar a operação. {e}.")
        page.update()
        
#NOTE: abrir arquivos
    def abrir_arquivo(self, nome_arquivo):
            # desserializarndo objeto json em python
            with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
            return dados
        
        
#NOTE: salvar_dados
    def salvar_dados(self, usuarios, nome_arquivo):
            try:
                with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
                    json.dump(usuarios, f)
                return f"Dados gravados com sucesso."
            except Exception as e:
                return f"Não foi possível salvar os dados. {e}."
        

#NOTE: cadastrar
    def cadastrar(e):
        nome = ft.TextField(label="NOME")
        cpf = ft.TextField(label="CPF")
        email = ft.TextField(label="E-MAIL")
        profissao = ft.TextField(label="PROFISSÃO")
        end = ft.TextField(label="ENDEREÇO")
        tel = ft.TextField(label="TELEFONE")
        botao_cadastrar= ft.ElevatedButton('Cadastrar-se', width=200)
        page.add(
            ft.Row(
            [ft.Text('Cadastre-se', size=60, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [nome],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [cpf],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [email],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [profissao],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [end],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [tel],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [botao_cadastrar],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.update
    #NOTE: cadastrar-se
        # def cadastrar_se(e):
        #     try:
        #             usuarios = m.abrir_arquivo(abrir_arquivo)
        #             f'Arquivo aberto: {abrir_arquivo}.json.\n'
        #             for i in range(len(usuarios)):
        #                 for campo in usuarios[i]:
        #                     f'{campo.capitalize()}: {usuarios[i].get(campo)}.'
        #     except Exception as e:
        #             f'Não foi possível abrir o arquivo. {e}'
        # page.update()
        
    #def usuarios_cadastrados(e):
        
        
    page.update()
    
    usuarios = []
    ver_cadastrados = ft.ElevatedButton("Ver usuários", width=400, on_click= usuarios_cadastrados)
    cadastro= ft.ElevatedButton('Cadastrar', width=400, on_click=cadastrar)
    alterar_cadastro = ft.ElevatedButton('Alterar cadastro', width=400)
    excluir_usuario= ft.ElevatedButton('Excluir usuário', width=400)
    
    page.add(
        ft.Row(
            [ft.Text('Cadastro', size=60, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(),
        ft.Row(),
        ft.Row(),
        ft.Row(
            [ver_cadastrados],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [cadastro],
            alignment=ft.MainAxisAlignment.CENTER  
        ),
        ft.Row(
            [alterar_cadastro],
            alignment=ft.MainAxisAlignment.CENTER  
        ),
         ft.Row(
            [excluir_usuario],
            alignment=ft.MainAxisAlignment.CENTER  
        )
    )
        
    page.update

ft.app(main)