# Sistema de Gestão de Alunos e Notas

Este projeto é um sistema de gestão de alunos e suas notas, desenvolvido em Python com uma conexão ao banco de dados Oracle. O sistema permite inserir, atualizar e excluir informações de alunos e notas.

## Pré-requisitos

- Python 3.x
- Biblioteca `cx_Oracle` para conexão com o banco de dados Oracle.
- Um banco de dados Oracle acessível para o sistema.

## Configuração

1. **Instale as dependências necessárias**. Certifique-se de que a biblioteca `cx_Oracle` esteja instalada. Você pode instalá-la usando pip:

   ```bash
   pip install cx_Oracle
   ```

2. **Crie o banco de dados**. Execute o script `create_tables_and_records.py` para criar as tabelas e inserir registros iniciais. Você pode executar o script a partir do terminal:

   ```bash
   python create_tables_and_records.py
   ```

   Certifique-se de que o script está configurado corretamente para se conectar ao seu banco de dados Oracle.

3. **Inicie o sistema**. Após a criação das tabelas e registros, execute o script `principal.py` para iniciar a aplicação:

   ```bash
   python principal.py
   ```

## Uso

Uma vez que a aplicação esteja em execução, você poderá realizar as seguintes operações:

- Inserir novos alunos e suas informações.
- Inserir notas para os alunos existentes.
- Atualizar informações de alunos e notas.
- Excluir alunos e notas do sistema.
- Verificar e listar informações de alunos e notas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request. (Definitivamente não feito por IA esse README)

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
