WITH Ranking AS (
    SELECT 
        a.curso, 
        a.nome, 
        AVG(n.nota) AS media_notas,
        ROW_NUMBER() OVER (PARTITION BY a.curso ORDER BY AVG(n.nota) DESC) AS ranking
    FROM 
        ALUNOS a
    JOIN 
        NOTAS n ON a.id = n.aluno_id
    GROUP BY 
        a.curso, a.nome
)
SELECT 
    curso, 
    nome, 
    media_notas
FROM 
    Ranking
WHERE 
    ranking = 1
ORDER BY 
    curso
