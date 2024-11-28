import pandas as pd
from model.nota import Nota
from bson.objectid import ObjectId
from conexion.mongo_queries import MongoQueries


class Controller_Nota:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_nota(self) -> Nota:
        '''Insere uma nova nota no MongoDB'''
        self.mongo.connect()
        
        aluno_nome = input("Nome do aluno: ")
        nota = float(input("Nota: "))

        # Verifica se o aluno existe
        aluno_info = pd.DataFrame(
            self.mongo.db["alunos"].find({"nome": aluno_nome}, {"_id": 1, "nome": 1, "turma": 1, "curso": 1})
        )
        
        if aluno_info.empty:
            print(f"Aluno {aluno_nome} não encontrado.")
            self.mongo.close()
            return None

        aluno_id = aluno_info["_id"].values[0]
        turma = aluno_info["turma"].values[0]
        curso = aluno_info["curso"].values[0]

        # Insere a nota na coleção "notas"
        nova_nota = {
            "aluno_id": aluno_id,
            "nota": nota
        }
        self.mongo.db["notas"].insert_one(nova_nota)

        # Cria o objeto Nota e exibe as informações
        nova_nota_obj = Nota(aluno_nome, turma, curso, nota)
        print(nova_nota_obj.to_string())

        self.mongo.close()
        return nova_nota_obj

    def atualizar_nota(self) -> Nota:
        '''Atualiza uma nota existente no MongoDB'''
        self.mongo.connect()
        
        aluno_nome = input("Nome do aluno que deseja alterar a nota: ")

        # Verifica se o aluno existe
        aluno_info = pd.DataFrame(
            self.mongo.db["alunos"].find({"nome": aluno_nome}, {"_id": 1, "nome": 1, "turma": 1, "curso": 1})
        )
        
        if aluno_info.empty:
            print(f"A nota para o aluno {aluno_nome} não existe.")
            self.mongo.close()
            return None

        aluno_id = aluno_info["_id"].values[0]
        turma = aluno_info["turma"].values[0]
        curso = aluno_info["curso"].values[0]

        # Obtém a nota atual
        nota_atual = self.mongo.db["notas"].find_one({"aluno_id": aluno_id})["nota"]
        print(f"A nota atual de {aluno_nome} é: {nota_atual}")

        nova_nota = float(input("Nova nota: "))

        # Atualiza a nota no MongoDB
        self.mongo.db["notas"].update_one({"aluno_id": aluno_id}, {"$set": {"nota": nova_nota}})

        # Cria o objeto Nota atualizado e exibe as informações
        nota_atualizada_obj = Nota(aluno_nome, turma, curso, nova_nota)
        print(nota_atualizada_obj.to_string())

        self.mongo.close()
        return nota_atualizada_obj

    def excluir_nota(self):
        '''Exclui uma nota do MongoDB'''
        self.mongo.connect()
        
        aluno_nome = input("Nome do aluno que deseja excluir a nota: ")

        # Verifica se o aluno existe
        aluno_info = pd.DataFrame(
            self.mongo.db["alunos"].find({"nome": aluno_nome}, {"_id": 1, "nome": 1})
        )
        
        if aluno_info.empty:
            print(f"A nota para o aluno {aluno_nome} não existe.")
            self.mongo.close()
            return None

        aluno_id = aluno_info["_id"].values[0]

        # Exclui a nota do MongoDB
        self.mongo.db["notas"].delete_one({"aluno_id": aluno_id})
        print(f"Nota do aluno {aluno_nome} removida com sucesso!")

        self.mongo.close()

    def verifica_existencia_nota(self, aluno_nome: str) -> bool:
        '''Verifica se uma nota já existe no MongoDB para o aluno'''
        self.mongo.connect()
        aluno_info = pd.DataFrame(
            self.mongo.db["alunos"].find({"nome": aluno_nome}, {"_id": 1})
        )
        
        if aluno_info.empty:
            self.mongo.close()
            return False

        aluno_id = aluno_info["_id"].values[0]
        nota = self.mongo.db["notas"].find_one({"aluno_id": aluno_id})

        self.mongo.close()
        return nota is not None
