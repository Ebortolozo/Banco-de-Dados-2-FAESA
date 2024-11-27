from model.alunos import Aluno
from conexion.oracle_queries import OracleQueries

class Controller_Aluno:
    def __init__(self):
        pass

    def inserir_aluno(self) -> Aluno:
        '''Insere um novo aluno no banco de dados'''
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:  # Loop para permitir múltiplas inserções
            nome = input("Nome do aluno (Novo): ")
            idade = int(input("Idade do aluno (Novo): "))
            turma = input("Turma do aluno (Novo): ")
            curso = input("Curso do aluno (Novo): ")

            # Verifica se já existe um aluno com o mesmo nome
            if self.verifica_existencia_aluno(oracle, nome):
                print(f"Já existe um aluno com o nome {nome}. Tente novamente.")
                continue  # Continua o loop para permitir a inserção de outro aluno

            oracle.write(f"INSERT INTO ALUNOS (id, nome, idade, turma, curso) "
                         f"VALUES (ALUNOS_ID_SEQ.NEXTVAL, '{nome}', {idade}, '{turma}', '{curso}')")

            df_aluno = oracle.sqlToDataFrame(f"SELECT id, nome, idade, turma, curso FROM ALUNOS WHERE nome = '{nome}'")
            novo_aluno = Aluno(df_aluno.nome.values[0], df_aluno.idade.values[0], df_aluno.turma.values[0], df_aluno.curso.values[0])
            print(novo_aluno.to_string())

            continuar = input("Deseja inserir mais um aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

    def atualizar_aluno(self) -> Aluno:
        '''Atualiza os dados de um aluno existente'''
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:  # Loop para permitir múltiplas atualizações
            nome = input("Nome do aluno que deseja alterar: ")

            # Verifica se o aluno existe
            if not self.verifica_existencia_aluno(oracle, nome):
                print(f"O aluno {nome} não existe.")
                return None

            # Solicita as novas informações
            nova_idade = int(input("Nova idade: "))
            nova_turma = input("Nova turma: ")
            novo_curso = input("Novo curso: ")

            # Atualiza o aluno existente
            oracle.write(f"UPDATE ALUNOS SET idade = {nova_idade}, turma = '{nova_turma}', curso = '{novo_curso}' WHERE nome = '{nome}'")

            # Recupera os dados atualizados
            df_aluno = oracle.sqlToDataFrame(f"SELECT nome, idade, turma, curso FROM ALUNOS WHERE nome = '{nome}'")
            aluno_atualizado = Aluno(df_aluno.nome.values[0], df_aluno.idade.values[0], df_aluno.turma.values[0], df_aluno.curso.values[0])
            print(aluno_atualizado.to_string())

            continuar = input("Deseja atualizar os dados de outro aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

    def excluir_aluno(self):
        '''Exclui um aluno do banco de dados'''
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:  # Loop para permitir múltiplas exclusões
            nome = input("Nome do aluno que deseja excluir: ")

            # Verifica se o aluno existe
            if not self.verifica_existencia_aluno(oracle, nome):
                print(f"O aluno {nome} não existe.")
                return None

            # Verifica se o aluno possui notas associadas
            notas_existentes = oracle.sqlToDataFrame(f"SELECT * FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{nome}')")
            if not notas_existentes.empty:
                print(f"O aluno {nome} possui notas associadas.")

                # Pergunta ao usuário se deseja excluir as notas
                excluir_nota = input("Deseja excluir as notas associadas ao aluno? (Sim/Não): ").strip().lower()
                if excluir_nota == "sim":
                    # Exclui as notas associadas
                    oracle.write(f"DELETE FROM NOTAS WHERE aluno_id = (SELECT id FROM ALUNOS WHERE nome = '{nome}')")
                    print(f"As notas do aluno {nome} foram removidas com sucesso!")

                elif excluir_nota == "não":
                    print("Voltando ao menu principal...")
                    break  # Sai do loop e volta ao menu principal

            # Remove o aluno
            oracle.write(f"DELETE FROM ALUNOS WHERE nome = '{nome}'")
            print(f"Aluno {nome} removido com sucesso!")

            continuar = input("Deseja excluir outro aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

    def verifica_existencia_aluno(self, oracle:OracleQueries, nome:str) -> bool:
        '''Verifica se um aluno já existe no banco de dados'''
        df_aluno = oracle.sqlToDataFrame(f"SELECT nome FROM ALUNOS WHERE nome = '{nome}'")
        return not df_aluno.empty
