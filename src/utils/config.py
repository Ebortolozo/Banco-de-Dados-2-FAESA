MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Notas por Alunos
2 - Relatório de Média por Turma
3 - Relatório de Melhor Aluno por Curso
4 - Relatório de Rendimento por Curso
5 - Relatório de Notas Detalhadas
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - ALUNOS
2 - NOTAS
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time: int = 3):
    '''
    Esse método limpa a tela após alguns segundos
    wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep

    sleep(wait_time)
    

    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

