from model.nota import Nota
from conexion.oracle_queries import OracleQueries

class Controller_Nota:
    def __init__(self):
        pass

    def inserir_nota(self) -> Nota:
        '''Insere uma nova nota no banco de dados'''
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:  # Loop para permitir múltiplas inserções
            aluno_nome = input("Nome do aluno: ")
            nota = float(input("Nota: "))

            aluno_info = oracle.sqlToDataFrame(f"SELECT turma, curso FROM ALUNOS WHERE nome = '{aluno_nome}'")
            
            if aluno_info.empty:
                print(f"Aluno {aluno_nome} não encontrado.")
                return None
            
            turma = aluno_info.turma.values[0]
            curso = aluno_info.curso.values[0]

            oracle.write(f"INSERT INTO NOTAS (id, aluno_id, nota) "
                         f"SELECT NOTAS_ID_SEQ.NEXTVAL, id, {nota} FROM ALUNOS WHERE nome = '{aluno_nome}'")

            df_nota = oracle.sqlToDataFrame(f"SELECT aluno_id, nota FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{aluno_nome}')")
            nova_nota = Nota(aluno_nome, turma, curso, df_nota.nota.values[0])
            print(nova_nota.to_string())

            continuar = input("Deseja inserir mais uma nota? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

    def atualizar_nota(self) -> Nota:
        '''Atualiza uma nota existente'''
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:  # Loop para permitir múltiplas atualizações
            aluno_nome = input("Nome do aluno que deseja alterar a nota: ")

            # Verifica se a nota existe
            if not self.verifica_existencia_nota(oracle, aluno_nome):
                print(f"A nota para o aluno {aluno_nome} não existe.")
                return None

            # Solicita qual nota deseja alterar
            nota_atual = oracle.sqlToDataFrame(f"SELECT nota FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{aluno_nome}')")
            print(f"A nota atual de {aluno_nome} é: {nota_atual.nota.values[0]}")

            nova_nota = float(input("Nova nota: "))

            # Atualiza a nota
            oracle.write(f"UPDATE NOTAS SET nota = {nova_nota} WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{aluno_nome}')")

            # Recupera os dados atualizados
            df_nota = oracle.sqlToDataFrame(f"SELECT aluno_id, nota FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{aluno_nome}')")
            nota_atualizada = Nota(aluno_nome, None, None, df_nota.nota.values[0])
            print(nota_atualizada.to_string())

            continuar = input("Deseja atualizar a nota de outro aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

    def excluir_nota(self):
        '''Exclui uma nota do banco de dados'''
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:  # Loop para permitir múltiplas exclusões
            aluno_nome = input("Nome do aluno que deseja excluir a nota: ")

            # Verifica se a nota existe
            if not self.verifica_existencia_nota(oracle, aluno_nome):
                print(f"A nota para o aluno {aluno_nome} não existe.")
                return None

            # Remove a nota
            oracle.write(f"DELETE FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{aluno_nome}')")
            print(f"Nota do aluno {aluno_nome} removida com sucesso!")

            continuar = input("Deseja excluir a nota de outro aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

    def verifica_existencia_nota(self, oracle:OracleQueries, aluno_nome:str) -> bool:
        '''Verifica se uma nota já existe no banco de dados'''
        df_nota = oracle.sqlToDataFrame(f"SELECT aluno_id FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{aluno_nome}')")
        return not df_nota.empty

