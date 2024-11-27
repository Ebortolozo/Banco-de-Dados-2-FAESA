-- Inserindo alunos na tabela ALUNOS
INSERT INTO ALUNOS (id, nome, idade, turma, curso) VALUES (ALUNOS_ID_SEQ.NEXTVAL, 'Joao Silva', 20, 'Turma A', 'Engenharia');
INSERT INTO ALUNOS (id, nome, idade, turma, curso) VALUES (ALUNOS_ID_SEQ.NEXTVAL, 'Maria Oliveira', 22, 'Turma B', 'Administracao');
INSERT INTO ALUNOS (id, nome, idade, turma, curso) VALUES (ALUNOS_ID_SEQ.NEXTVAL, 'Carlos Santos', 21, 'Turma A', 'Engenharia');
INSERT INTO ALUNOS (id, nome, idade, turma, curso) VALUES (ALUNOS_ID_SEQ.NEXTVAL, 'Ana Pereira', 23, 'Turma C', 'Direito');
INSERT INTO ALUNOS (id, nome, idade, turma, curso) VALUES (ALUNOS_ID_SEQ.NEXTVAL, 'Lucas Costa', 19, 'Turma B', 'Administracao');

-- Inserindo notas na tabela NOTAS
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 1, 8.5);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 2, 7.2);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 3, 9.0);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 4, 6.8);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 5, 8.0);

-- Inserindo mais notas para os mesmos alunos
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 1, 7.9);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 2, 6.5);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 3, 8.7);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 4, 7.0);
INSERT INTO NOTAS (id, aluno_id, nota) VALUES (NOTAS_ID_SEQ.NEXTVAL, 5, 9.1);
