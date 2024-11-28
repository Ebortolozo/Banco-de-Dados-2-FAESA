
# Sistema de Gestão de Alunos e Notas

Este projeto é um sistema de gestão de alunos e suas notas, desenvolvido em Python. Ele integra com o MongoDB para gerenciar informações sobre alunos e suas notas, e oferece funcionalidades para gerar relatórios detalhados de desempenho, como a média por turma, melhores alunos por curso, notas detalhadas e rendimento por curso.

## Pré-requisitos

- **Python 3.x**
- **Bibliotecas**:
  - `pandas` para manipulação de dados.
  - `pymongo` para integração com o MongoDB.

Você pode instalar as dependências utilizando o pip:

```bash
pip install pandas pymongo
```

- **Uma instância do MongoDB acessível para o sistema.**

## Configuração

1. **Instale as dependências necessárias**  
   Certifique-se de que as bibliotecas `pandas` e `pymongo` estejam instaladas. Utilize o seguinte comando:

   ```bash
   pip install pandas pymongo
   ```

2. **Criação do Banco de Dados MongoDB**  
   O sistema se conecta a um banco de dados MongoDB para armazenar as informações. Certifique-se de que sua instância do MongoDB esteja configurada e em funcionamento. A aplicação se conecta diretamente às coleções `alunos` e `notas`.

3. **Inicie o sistema**  
   Para executar a aplicação, basta rodar o script `relatorios.py`, onde são gerados os relatórios de desempenho dos alunos. A aplicação também está pronta para consultas detalhadas e agregações.

   ```bash
   python relatorios.py
   ```

## Funcionalidades

Este sistema permite realizar as seguintes operações e gerar os seguintes relatórios:

- **Relatório de Média por Turma**: Calcula a média das notas dos alunos agrupadas por turma.
- **Relatório de Melhor Aluno por Curso**: Identifica o aluno com a maior média de notas em cada curso.
- **Relatório de Notas Detalhadas**: Exibe as notas de todos os alunos, organizadas por curso e nome.
- **Relatório de Notas por Aluno**: Calcula a média das notas de cada aluno.
- **Relatório de Rendimento por Curso**: Calcula a média geral das notas dos alunos por curso.

## Uso

Uma vez que o sistema esteja em execução, você poderá visualizar os seguintes relatórios:

- **Relatório de Média por Turma**: Exibe a média das notas de todos os alunos por turma.
- **Relatório de Melhor Aluno por Curso**: Exibe o nome do melhor aluno de cada curso, com base na maior média de notas.
- **Relatório de Notas Detalhadas**: Exibe as notas de todos os alunos, listadas por curso e nome.
- **Relatório de Notas por Aluno**: Exibe o nome de cada aluno com sua média de notas.
- **Relatório de Rendimento por Curso**: Exibe a média de notas dos alunos de cada curso.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Veja o arquivo LICENSE para mais detalhes.
