from conexion.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:
    def __init__(self):
        pass

    def get_relatorio_media_por_turma(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].aggregate([
            {
                "$lookup": {
                    "from": "notas",
                    "localField": "_id",
                    "foreignField": "aluno_id",
                    "as": "notas_info"
                }
            },
            {
                "$unwind": "$notas_info"
            },
            {
                "$group": {
                    "_id": "$turma",
                    "media_notas_turma": { "$avg": "$notas_info.nota" }
                }
            },
            {
                "$project": {
                    "turma": "$_id",
                    "media_notas_turma": 1,
                    "_id": 0
                }
            }
        ])

        df_media_por_turma = pd.DataFrame(list(query_result))

        if df_media_por_turma.empty:
            print("Nenhum dado encontrado para o relatório de média por turma.")
        else:
            print(df_media_por_turma)

        mongo.close()

        input("Pressione Enter para Sair do Relatório de Média por Turma")

    def get_relatorio_melhor_aluno_curso(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].aggregate([
            {
                "$lookup": {
                    "from": "notas",
                    "localField": "_id",
                    "foreignField": "aluno_id",
                    "as": "notas_info"
                }
            },
            {
                "$unwind": "$notas_info"
            },
            {
                "$group": {
                    "_id": { "curso": "$curso", "nome": "$nome" },
                    "media_notas": { "$avg": "$notas_info.nota" }
                }
            },
            {
                "$sort": { "media_notas": -1 }
            },
            {
                "$group": {
                    "_id": "$_id.curso",
                    "top_students": { "$push": { "nome": "$_id.nome", "media_notas": "$media_notas" } }
                }
            },
            {
                "$project": {
                    "curso": "$_id",
                    "top_student": { "$arrayElemAt": ["$top_students", 0] }
                }
            },
            {
                "$project": {
                    "curso": 1,
                    "nome": "$top_student.nome",
                    "media_notas": "$top_student.media_notas"
                }
            },
            {
                "$sort": { "curso": 1 }
            }
        ])

        df_melhor_aluno_curso = pd.DataFrame(list(query_result))

        if df_melhor_aluno_curso.empty:
            print("Nenhum dado encontrado para o relatório de Melhor Aluno por Curso.")
        else:
            print(df_melhor_aluno_curso)

        mongo.close()

        input("Pressione Enter para Sair do Relatório de Melhor Aluno por Curso")

    def get_relatorio_notas_detalhadas(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].aggregate([
            {
                "$lookup": {
                    "from": "notas",
                    "localField": "_id",
                    "foreignField": "aluno_id",
                    "as": "notas_info"
                }
            },
            {
                "$unwind": "$notas_info"
            },
            {
                "$project": {
                    "nome": 1,
                    "curso": 1,
                    "nota": "$notas_info.nota"
                }
            },
            {
                "$sort": {
                    "curso": 1,
                    "nome": 1
                }
            }
        ])

        df_notas_detalhadas = pd.DataFrame(list(query_result))

        mongo.close()

        print(df_notas_detalhadas)
        input("Pressione Enter para Sair do Relatório de Notas Detalhadas")

    def get_relatorio_notas_por_alunos(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].aggregate([
            {
                "$lookup": {
                    "from": "notas",
                    "localField": "_id",
                    "foreignField": "aluno_id",
                    "as": "notas_info"
                }
            },
            {
                "$unwind": "$notas_info"
            },
            {
                "$group": {
                    "_id": "$nome",
                    "media_notas": { "$avg": "$notas_info.nota" }
                }
            },
            {
                "$project": {
                    "nome": "$_id",
                    "media_notas": 1
                }
            },
            {
                "$sort": { "media_notas": -1 }
            }
        ])
        
        df_notas_por_aluno = pd.DataFrame(list(query_result))
        
        mongo.close()

        print(df_notas_por_aluno)
        input("Pressione Enter para Sair do Relatório de Notas por Aluno")

    def get_relatorio_rendimento_por_curso(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].aggregate([
            {
                "$lookup": {
                    "from": "notas",
                    "localField": "_id",
                    "foreignField": "aluno_id",
                    "as": "notas_info"
                }
            },
            {
                "$unwind": "$notas_info"
            },
            {
                "$group": {
                    "_id": "$curso",
                    "rendimento": { "$avg": "$notas_info.nota" }
                }
            },
            {
                "$project": {
                    "curso": "$_id",
                    "rendimento": 1
                }
            },
            {
                "$sort": { "rendimento": -1 }
            }
        ])
        
        df_rendimento_por_curso = pd.DataFrame(list(query_result))
        
        mongo.close()

        print(df_rendimento_por_curso)
        input("Pressione Enter para Sair do Relatório de Rendimento por Curso")
