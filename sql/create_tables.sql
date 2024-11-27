-- Apagando os relacionamentos (FKs)
ALTER TABLE NOTAS DROP CONSTRAINT ALUNOS_NOTAS_FK;

/*Apagando as tabelas, se existirem*/
DROP TABLE NOTAS;
DROP TABLE ALUNOS;

-- Apagando as sequências, se existirem
DROP SEQUENCE ALUNOS_ID_SEQ;
DROP SEQUENCE NOTAS_ID_SEQ;

-- Criar tabela de alunos
CREATE TABLE ALUNOS (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    idade NUMBER NOT NULL,
    turma VARCHAR2(50) NOT NULL,
    curso VARCHAR2(100) NOT NULL
);

-- Criar tabela de notas
CREATE TABLE NOTAS (
    id NUMBER PRIMARY KEY,
    aluno_id NUMBER,
    nota NUMBER(5, 2) NOT NULL,
    CONSTRAINT ALUNOS_NOTAS_FK FOREIGN KEY (aluno_id) REFERENCES ALUNOS(id)
);


-- Criando sequência para a tabela de alunos
CREATE SEQUENCE ALUNOS_ID_SEQ;
CREATE SEQUENCE NOTAS_ID_SEQ;