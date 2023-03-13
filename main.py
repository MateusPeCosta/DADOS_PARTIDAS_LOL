#* This project is not endorsed by Riot Games and does not reflect the views or opinions of Riot Games 
#* or anyone officially involved in producing or managing Riot Games properties. Riot Games and all associated properties 
#* are trademarks or registered trademarks of Riot Games, Inc

import requests
import functions
import json
import os

# API Key
apikey = 'SUA_KEY_API'

# Nome de invocador (summoner name) do jogador
summonername = str(input("Digite seu nick de invocador com todos os caracteres minusculos: "))

# URL da API
url = f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonername}?api_key={apikey}"

# Fazendo a requisição à API
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:

    print("Requisição bem sucedida!!")
    
    # Convertendo o conteúdo da resposta em um dicionário
    summonerdata = json.loads(response.content)
    
    # Pegando o ID do jogador
    summonerpuuid = summonerdata['puuid']
    
    arquivo = f'./data{summonername}.csv'
    
    if os.path.isfile(arquivo):

        print("Parece que já temos partidas salvas referentes a esse invocador!!")
        pathAtual = int(input("Digite o path em que devemos procurar novas partidas: "))

        uLinha = functions.ultima_linha(arquivo)
        uLinha = uLinha[0]

        # URL da API para pegar as partidas do jogador
        matchhistoryurl = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{summonerpuuid}/ids?start=0&count=100&api_key={apikey}"
        
        # Fazendo a requisição à API
        matchhistoryresponse = requests.get(matchhistoryurl)

        # Verificando se a requisição foi bem-sucedida
        if matchhistoryresponse.status_code == 200:
            # Convertendo o conteúdo da resposta em um dicionário
            matchhistorydata = json.loads(matchhistoryresponse.content)

            print("Aguarde suas partidas estão sendo armazenadas!!")

            for i in range (len(matchhistorydata)-1,-1,-1):
                partida = matchhistorydata[i]

                part = f"https://americas.api.riotgames.com/lol/match/v5/matches/{partida}?api_key={apikey}"

                responsepartida = requests.get(part)

                    # Verificando se a requisição foi bem-sucedida
                if responsepartida.status_code == 200:
                    # Convertendo o conteúdo da resposta em um dicionário
                    partidadata = json.loads(responsepartida.content)

                    if(partidadata['metadata']['matchId'] != uLinha[1:15]):
                        continue

                    elif(partidadata['metadata']['matchId'] == uLinha[1:15]):

                        for j in range (i-1,-1,-1):
                            partida2 = matchhistorydata[j]

                            parti2 = f"https://americas.api.riotgames.com/lol/match/v5/matches/{partida2}?api_key={apikey}"

                            responsepartida2 = requests.get(parti2)

                            # Verificando se a requisição foi bem-sucedida
                            if responsepartida2.status_code == 200:
                                # Convertendo o conteúdo da resposta em um dicionário
                                partidadata_novo = json.loads(responsepartida2.content)


                                if(partidadata_novo['info']['queueId'] == 420 or partidadata_novo['info']['queueId'] == 430):

                                    versao = (partidadata_novo['info']['gameVersion'])
                                    num = int(versao[:2])

                                    if(num == pathAtual):

                                        functions.dados(partidadata,arquivo,num)

                                else:
                                    continue

    else:

        print("Parece que ainda não temos partidas referentes a esse invocador!!")
        pathAtual = int(input("Digite o path atual ou que deseja que os dados sejam procurados: "))

        functions.escrever_na_ultima_linha(arquivo,functions.linha1)       

        # URL da API para pegar as partidas do jogador
        matchhistoryurl = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{summonerpuuid}/ids?start=0&count=100&api_key={apikey}"

        # Fazendo a requisição à API
        matchhistoryresponse = requests.get(matchhistoryurl)

        # Verificando se a requisição foi bem-sucedida
        if matchhistoryresponse.status_code == 200:
            # Convertendo o conteúdo da resposta em um dicionário
            matchhistorydata = json.loads(matchhistoryresponse.content)
            
            print("Aguarde suas partidas estão sendo armazenadas!!")

            for i in range (len(matchhistorydata)-1,-1,-1):
                partida = matchhistorydata[i]

                part = f"https://americas.api.riotgames.com/lol/match/v5/matches/{partida}?api_key={apikey}"

                responsepartida = requests.get(part)

                    # Verificando se a requisição foi bem-sucedida
                if responsepartida.status_code == 200:
                    # Convertendo o conteúdo da resposta em um dicionário
                    partidadata = json.loads(responsepartida.content)

                    if(partidadata['info']['queueId'] == 420 or partidadata['info']['queueId'] == 430):

                        versao = (partidadata['info']['gameVersion'])
                        num = int(versao[:2])
                        
                        if(num == pathAtual):

                            functions.dados(partidadata,arquivo,num)

                    else:
                        continue