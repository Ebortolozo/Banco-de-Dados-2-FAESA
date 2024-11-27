class Aluno:
    def __init__(self, 
                 nome:str=None, 
                 idade:int=None, 
                 turma:str=None, 
                 curso:str=None):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_turma(turma)
        self.set_curso(curso)

    # Setters
    def set_nome(self, nome:str):
        self.nome = nome

    def set_idade(self, idade:int):
        self.idade = idade

    def set_turma(self, turma:str):
        self.turma = turma

    def set_curso(self, curso:str):
        self.curso = curso

    # Getters
    def get_nome(self) -> str:
        return self.nome

    def get_idade(self) -> int:
        return self.idade

    def get_turma(self) -> str:
        return self.turma

    def get_curso(self) -> str:
        return self.curso

    # Método para exibir dados do aluno como string
    def to_string(self) -> str:
        return (f"Nome: {self.get_nome()} | Idade: {self.get_idade()} | "
                f"Turma: {self.get_turma()} | Curso: {self.get_curso()}")
