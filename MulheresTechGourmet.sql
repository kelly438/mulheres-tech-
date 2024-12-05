-- criando meu primeiro banco de dados
CREATE DATABASE pipoquinha;

-- criando minha primeira tabela/entidade
CREATE TABLE alunos(
	matricula INTEGER PRIMARY KEY,
    nome_aluno TEXT NOT NULL,
    genero TEXT NOT NULL
    );
    -- injeção de dados-teste
    INSERT INTO alunos VALUES (1, 'Marina','F');
    INSERT INTO alunos VALUES (2, 'Joana' , 'F');
    
    
    -- consultando as injeções realizadas
    SELECT * FROM alunos WHERE matricula=1
    
    -- ATIVIDADE: crie uma nova tabela chamada ' professores', com a mesma quantidade de caracteristicas de 'aluno',
    -- fazendo ao menos duas injecões de dados e uma consulta
    
    -- criando tabela professores
    CREATE TABLE professores(
		matricula INTEGER PRIMARY KEY,
        nome_professores TEXT NOT NULL,
        disciplina TEXT NOT NULL
        );
        -- injeção de dados-teste
        INSERT INTO professores VALUES (1, 'Jhony', 'TEOLOGIA');
        INSERT INTO professores VALUES (2, 'Felipe', ' FILOSOFIA');
     
     -- consultando as injeções realizadas
     SELECT * FROM professores WHERE matricula=1
     

        
        

    
    
    
    
    



			


