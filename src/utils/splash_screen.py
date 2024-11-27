from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_alunos = config.QUERY_COUNT.format(tabela="alunos")
        self.qry_total_notas = config.QUERY_COUNT.format(tabela="notas")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Ewerton Júnior"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"

    def get_total_alunos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_alunos)["total_alunos"].values[0]

    def get_total_notas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_notas)["total_notas"].values[0]

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
