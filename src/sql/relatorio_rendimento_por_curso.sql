SELECT 
    a.curso, 
    AVG(n.nota) AS media_rendimento
FROM 
    ALUNOS a
JOIN 
    NOTAS n ON a.id = n.aluno_id
GROUP BY 
    a.curso