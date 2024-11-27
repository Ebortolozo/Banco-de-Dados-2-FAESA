SELECT
    a.turma, 
    AVG(n.nota) AS media_notas_turma
FROM
    ALUNOS a
JOIN
    NOTAS n ON a.id = n.aluno_id
GROUP BY
    a.turma