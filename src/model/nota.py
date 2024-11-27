class Nota:
    def __init__(self, 
                 aluno_nome:str=None, 
                 turma:str=None, 
                 curso:str=None, 
                 nota:float=None):
        self.set_aluno_nome(aluno_nome)
        self.set_turma(turma)
        self.set_curso(curso)
        self.set_nota(nota)

    # Setters
    def set_aluno_nome(self, aluno_nome:str):
        self.aluno_nome = aluno_nome

    def set_turma(self, turma:str):
        self.turma = turma

    def set_curso(self, curso:str):
        self.curso = curso

    def set_nota(self, nota:float):
        self.nota = nota

    # Getters
    def get_aluno_nome(self) -> str:
        return self.aluno_nome

    def get_turma(self) -> str:
        return self.turma

    def get_curso(self) -> str:
        return self.curso

    def get_nota(self) -> float:
        return self.nota

    # Método para exibir dados da nota como string
    def to_string(self) -> str:
        return (f"Aluno: {self.get_aluno_nome()} | Turma: {self.get_turma()} | "
                f"Curso: {self.get_curso()} | Nota: {self.get_nota()}")
