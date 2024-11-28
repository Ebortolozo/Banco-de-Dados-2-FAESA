from utils import config
from conexion.mongo_queries import MongoQueries

class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = "Ewerton Júnior"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"
        
        # Instância do MongoDB
        self.mongo = MongoQueries()

    def get_total_alunos(self):
        # Conecta ao MongoDB e retorna o total de alunos
        self.mongo.connect()
        total_alunos = self.mongo.db["alunos"].count_documents({})
        self.mongo.close()
        return total_alunos

    def get_total_notas(self):
        # Conecta ao MongoDB e retorna o total de notas
        self.mongo.connect()
        total_notas = self.mongo.db["notas"].count_documents({})
        self.mongo.close()
        return total_notas

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                SISTEMA DE GESTÃO DE ALUNOS               
        #                                                          
        #  TOTAL DE REGISTROS:                                    
        #      1 - ALUNOS:         {str(self.get_total_alunos()).rjust(5)}
        #      2 - NOTAS:          {str(self.get_total_notas()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
