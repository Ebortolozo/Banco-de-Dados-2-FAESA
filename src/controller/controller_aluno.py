from model.alunos import Aluno
from conexion.mongo_queries import MongoQueries
import pandas as pd

class Controller_Aluno:
    def __init__(self):
        self.mongo = MongoQueries()

    def inserir_aluno(self) -> Aluno:
        '''Insere um novo aluno no MongoDB'''
        # Cria uma nova conexão com o banco
        self.mongo.connect()

        while True:  # Loop para permitir múltiplas inserções
            nome = input("Nome do aluno (Novo): ")
            idade = int(input("Idade do aluno (Novo): "))
            turma = input("Turma do aluno (Novo): ")
            curso = input("Curso do aluno (Novo): ")

            # Verifica se o aluno já existe
            if self.verifica_existencia_aluno(nome):
                print(f"Já existe um aluno com o nome {nome}. Tente novamente.")
                continue  # Continua o loop para permitir a inserção de outro aluno

            # Insere o novo aluno no MongoDB
            aluno_data = {
                "nome": nome,
                "idade": idade,
                "turma": turma,
                "curso": curso
            }
            self.mongo.db.alunos.insert_one(aluno_data)

            # Recupera os dados do aluno inserido
            df_aluno = self.recupera_aluno(nome)
            novo_aluno = Aluno(df_aluno.nome.values[0], df_aluno.idade.values[0], df_aluno.turma.values[0], df_aluno.curso.values[0])

            # Exibe os dados do aluno inserido
            print(novo_aluno.to_string())

            continuar = input("Deseja inserir mais um aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

        # Fecha a conexão com o MongoDB
        self.mongo.close()

    def atualizar_aluno(self) -> Aluno:
        '''Atualiza os dados de um aluno existente no MongoDB'''
        # Cria uma nova conexão com o banco
        self.mongo.connect()

        while True:  # Loop para permitir múltiplas atualizações
            nome = input("Nome do aluno que deseja alterar: ")

            # Verifica se o aluno existe
            if not self.verifica_existencia_aluno(nome):
                print(f"O aluno {nome} não existe.")
                return None

            # Solicita as novas informações
            nova_idade = int(input("Nova idade: "))
            nova_turma = input("Nova turma: ")
            novo_curso = input("Novo curso: ")

            # Atualiza os dados do aluno no MongoDB
            self.mongo.db.alunos.update_one(
                {"nome": nome},
                {"$set": {"idade": nova_idade, "turma": nova_turma, "curso": novo_curso}}
            )

            # Recupera os dados atualizados do aluno
            df_aluno = self.recupera_aluno(nome)
            aluno_atualizado = Aluno(df_aluno.nome.values[0], df_aluno.idade.values[0], df_aluno.turma.values[0], df_aluno.curso.values[0])

            # Exibe os dados do aluno atualizado
            print(aluno_atualizado.to_string())

            continuar = input("Deseja atualizar os dados de outro aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

        # Fecha a conexão com o MongoDB
        self.mongo.close()

    def excluir_aluno(self):
        '''Exclui um aluno do MongoDB'''
        # Cria uma nova conexão com o banco
        self.mongo.connect()

        while True:  # Loop para permitir múltiplas exclusões
            nome = input("Nome do aluno que deseja excluir: ")

            # Verifica se o aluno existe
            if not self.verifica_existencia_aluno(nome):
                print(f"O aluno {nome} não existe.")
                return None

            # Remove o aluno do MongoDB
            self.mongo.db.alunos.delete_one({"nome": nome})
            print(f"Aluno {nome} removido com sucesso!")

            continuar = input("Deseja excluir outro aluno? (Sim/Não): ").strip().lower()
            if continuar == "não":
                print("Voltando ao menu principal...")
                break  # Sai do loop e volta ao menu principal

        # Fecha a conexão com o MongoDB
        self.mongo.close()

    def verifica_existencia_aluno(self, nome: str) -> bool:
        '''Verifica se um aluno já existe no MongoDB'''
        # Recupera o aluno com o nome fornecido
        aluno = self.mongo.db.alunos.find_one({"nome": nome})
        return aluno is not None

    def recupera_aluno(self, nome: str) -> pd.DataFrame:
        '''Recupera os dados de um aluno no MongoDB e transforma em um DataFrame'''
        aluno = self.mongo.db.alunos.find_one({"nome": nome})
        # Converte os dados do aluno em um DataFrame
        return pd.DataFrame([aluno])
