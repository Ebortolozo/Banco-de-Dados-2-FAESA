SELECT 
    a.nome, 
    a.curso, 
    n.nota
FROM 
    ALUNOS a
JOIN 
    NOTAS n ON a.id = n.aluno_id
ORDER BY 
    a.curso, a.nome