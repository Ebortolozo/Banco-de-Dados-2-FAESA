SELECT 
    a.nome, 
    AVG(n.nota) AS media_notas
FROM 
    ALUNOS a
JOIN 
    NOTAS n ON a.id = n.aluno_id
GROUP BY 
    a.nome