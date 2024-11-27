from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_aluno import Controller_Aluno
from controller.controller_nota import Controller_Nota

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_aluno = Controller_Aluno()
ctrl_nota = Controller_Nota()

def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_notas_por_alunos()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_media_por_turma()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_melhor_aluno_curso()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_rendimento_por_curso()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_notas_detalhadas()

def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        novo_aluno = ctrl_aluno.inserir_aluno()  
    elif opcao_inserir == 2:
        nova_nota = ctrl_nota.inserir_nota()  

def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_notas_detalhadas()
        aluno_atualizado = ctrl_aluno.atualizar_aluno()  
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_notas_detalhadas()  
        nota_atualizada = ctrl_nota.atualizar_nota()  

def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        relatorio.get_relatorio_notas_detalhadas()
        ctrl_aluno.excluir_aluno()  
    elif opcao_excluir == 2:
        relatorio.get_relatorio_notas_detalhadas()  
        ctrl_nota.excluir_nota()  

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1:  # Relatórios
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-4]: "))
            config.clear_console(1)

            reports(opcao_relatorio)
            config.clear_console(1)

        elif opcao == 2:  # Inserir Novos Registros
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)
            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3:  # Atualizar Registros
            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)
            config.clear_console()

        elif opcao == 4:  # Excluir Registros
            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)
            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:  # Sair
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
