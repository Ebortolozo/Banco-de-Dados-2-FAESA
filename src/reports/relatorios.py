from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_media_por_turma.sql") as f:
            self.query_relatorio_media_por_turma = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_melhor_aluno_curso.sql") as f:
            self.query_relatorio_melhor_aluno_curso = f.read()
        
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_notas_detalhadas.sql") as f:
            self.query_relatorio_notas_detalhadas = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_notas_por_alunos.sql") as f:
            self.query_relatorio_notas_por_alunos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_rendimento_por_curso.sql") as f:
            self.query_relatorio_rendimento_por_curso = f.read()

    def get_relatorio_media_por_turma(self):
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_media_por_turma))
        input("Pressione Enter para Sair do Relatório de Média por Turma")

    def get_relatorio_melhor_aluno_curso(self):
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_melhor_aluno_curso))
        input("Pressione Enter para Sair do Relatório de Melhor Aluno por Curso")
    
    def get_relatorio_notas_detalhadas(self):
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_notas_detalhadas))
        input("Pressione Enter para Sair do Relatório das Notas Detalhadas")

    def get_relatorio_notas_por_alunos(self):
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        oracle.connect()
        
        # Verifique o conteúdo da consulta antes de executá-la
        # print("Consulta SQL: ", self.query_relatorio_notas_por_alunos)
    
        # Recupera os dados transformando em um DataFrame
        try:
            df = oracle.sqlToDataFrame(self.query_relatorio_notas_por_alunos)
            print(df)
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
    
        input("Pressione Enter para Sair do Relatório de Notas por Aluno")



    def get_relatorio_rendimento_por_curso(self):
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_rendimento_por_curso))
        input("Pressione Enter para Sair do Relatório de Rendimento por Curso")
