Criação do banco para funcionar com o código presente nesse diretório:
1. Acesse e faça o login: "https://account.mongodb.com/account/login"
2. Crie um projeto
3. Vá em Database, click em Creat-> Shared-> GoogleCloud-> southamerica-east1-> M0 Sandbox-> e coloque um nome
4. Vá em Network Access, click em Add IP address-> Coloque seu IP-> Coloque uma identificação-> Confirm
5. Aproveite e insira o IP 0.0.0.0
6. Volte para Database, click em Connect-> Drivers-> Escolha o Driver(linguagem de programação)-> Escolha a versão-> Habilite View full code sample-> copie o código
7. No código você tem que alterar a string uri colocando a senha da seu projeto no lugar do <password>
8. Depois disso pode fazer a conexão com o banco
9. Para criar tabela vá em Browse Collections-> Create Database-> Escolha um nome para a base-> Escolha um nome para a tabela-> coloque Capped Collection-> Coloque o tamanho em bytes da sua tabela.
10. Agora no código de conexão é possivel acessar a tabela e fazer CRUD nela.
