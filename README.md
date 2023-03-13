# DADOS_PARTIDAS_LOL

Este projeto não é endossado pela Riot Games e não reflete os pontos de vista ou opiniões da Riot Games ou de qualquer pessoa oficialmente envolvida na produção ou gerenciamento das propriedades da Riot Games. Riot Games e todas as propriedades associadas são marcas comerciais ou marcas registradas da Riot Games, Inc.

********* ATENÇÃO *********
Devo dizer que antes de utilizar qualquer serviço da API Riot Games ou ainda copiar alguma parte do código desse projeto, consulte toda a documentação e requesitos para usar a API no site deles: https://developer.riotgames.com/docs/portal

Um projeto simples utilizando Python, algumas bibliotecas e a API da Riot Games para coleta de dados de partidas de um jogador, informando seu nickname ao programa.

O autor com esse projeto tem o objetivo de aprender novos métodos e aperfeiçoar a capacidade em programação, coleta e manipulação de dados.

Em resumo:

O projeto tem uma lógica bem simples. É pedido o nome de invocador do jogador que deseja procurar suas partidas, logo em seguida utilizamos essa informação para buscar os dados desse jogador como: id e puuid. A partir disso verificamos se já existe um arquivo com partidas desse jogador, se existir apenas adiconaremos as novas partidas, agora se não existir criaremos o arquivo e buscaremos as partidas desse jogador para armazena-las. 
No nosso caso usaremos o dado 'puuid' para acessar o historico com os ids das ultimas 100 partidas jogadas por ele. Percorremos o historico procurando partidas rankeadas para então começarmos o processo de escolha e armazenamento dos dados.

Um ponto a se ressaltar é que a coleta e o armazenamento dos dados não foram feitos por completo e como estão nos dados das partidas retirados diretamente da API. Alguns dados foram escolhidos, retirados e outros foram movidos de lugar na database para se adaptar ao projeto, isso tudo por total escolha do autor.
