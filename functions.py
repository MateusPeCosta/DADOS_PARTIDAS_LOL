import csv
import time

linha1 = ["'matchId'", "'gameCreation'", "'gameDuration'", "'gameId'", 
    "'gameVersion'", "'mapId'", "'queueId'", "'summonerName'",
    "'championName'", "'lane'", "'role'", "'individualPosition'", "'teamPosition'",
    "'puuid'", "'allInPings'", "'assistMePings'", "'assists'", 
    "'baitPings'", "'baronKills'", "'basicPings'", "'bountyLevel'", "'12AssistStreakCount'", 
    "'abilityUses'", "'acesBefore15Minutes'", "'alliedJungleMonsterKills'", "'baronTakedowns'", 
    "'blastConeOppositeOpponentCount'", "'bountyGold'", "'buffsStolen'", "'completeSupportQuestInTime'", 
    "'controlWardsPlaced'", "'damagePerMinute'", "'damageTakenOnTeamPercentage'", 
    "'dancedWithRiftHerald'", "'deathsByEnemyChamps'", "'dodgeSkillShotsSmallWindow'", 
    "'doubleAces'", "'dragonTakedowns'", "'earliestBaron'", "'earliestDragonTakedown'", 
    "'earliestElderDragon'", "'earlyLaningPhaseGoldExpAdvantage'", "'effectiveHealAndShielding'", 
    "'elderDragonKillsWithOpposingSoul'", "'elderDragonMultikills'", "'enemyChampionImmobilizations'", 
    "'enemyJungleMonsterKills'", "'epicMonsterKillsNearEnemyJungler'", "'epicMonsterKillsWithin30SecondsOfSpawn'", 
    "'epicMonsterSteals'", "'epicMonsterStolenWithoutSmite'", "'fastestLegendary'", "'flawlessAces'", 
    "'fullTeamTakedown'", "'gameLength'", "'getTakedownsInAllLanesEarlyJungleAsLaner'", 
    "'goldPerMinute'", "'hadOpenNexus'", "'immobilizeAndKillWithAlly'", "'initialBuffCount'", 
    "'initialCrabCount'", "'jungleCsBefore10Minutes'", "'junglerTakedownsNearDamagedEpicMonster'", 
    "'kTurretsDestroyedBeforePlatesFall'", "'kda'", "'killAfterHiddenWithAlly'", "'killParticipation'", 
    "'killedChampTookFullTeamDamageSurvived'", "'killingSprees'", "'killsNearEnemyTurret'", "'killsOnOtherLanesEarlyJungleAsLaner'", 
    "'killsOnRecentlyHealedByAramPack'", "'killsUnderOwnTurret'", "'killsWithHelpFromEpicMonster'", 
    "'knockEnemyIntoTeamAndKill'", "'landSkillShotsEarlyGame'", "'laneMinionsFirst10Minutes'", 
    "'laningPhaseGoldExpAdvantage'", "'legendaryCount'", "'lostAnInhibitor'", "'maxCsAdvantageOnLaneOpponent'", 
    "'maxKillDeficit'", "'maxLevelLeadLaneOpponent'", "'moreEnemyJungleThanOpponent'", "'multiKillOneSpell'", 
    "'multiTurretRiftHeraldCount'", "'multikills'", "'multikillsAfterAggressiveFlash'", "'mythicItemUsed'", 
    "'outerTurretExecutesBefore10Minutes'", "'outnumberedKills'", "'outnumberedNexusKill'", 
    "'perfectDragonSoulsTaken'", "'perfectGame'", "'pickKillWithAlly'", "'playedChampSelectPosition'", 
    "'poroExplosions'", "'quickCleanse'", "'quickFirstTurret'", "'quickSoloKills'", "'riftHeraldTakedowns'", 
    "'saveAllyFromDeath'", "'scuttleCrabKills'", "'skillshotsDodged'", "'skillshotsHit'", "'snowballsHit'", 
    "'soloBaronKills'", "'soloKills'", "'soloTurretsLategame'", "'stealthWardsPlaced'", "'survivedSingleDigitHpCount'", 
    "'survivedThreeImmobilizesInFight'", "'takedownOnFirstTurret'", "'takedowns'", "'takedownsAfterGainingLevelAdvantage'", 
    "'takedownsBeforeJungleMinionSpawn'", "'takedownsFirstXMinutes'", "'takedownsInAlcove'", 
    "'takedownsInEnemyFountain'", "'teamBaronKills'", "'teamDamagePercentage'", "'teamElderDragonKills'", 
    "'teamRiftHeraldKills'", "'threeWardsOneSweeperCount'", "'tookLargeDamageSurvived'", 
    "'turretPlatesTaken'", "'turretTakedowns'", "'turretsTakenWithRiftHerald'", "'twentyMinionsIn3SecondsCount'", 
    "'unseenRecalls'", "'visionScoreAdvantageLaneOpponent'", "'visionScorePerMinute'", "'wardTakedowns'", 
    "'wardTakedownsBefore20M'", "'wardsGuarded'", 
    "'champExperience'", "'champLevel'", "'championId'",
    "'championTransform'", "'commandPings'", "'consumablesPurchased'", 
    "'damageDealtToBuildings'", "'damageDealtToObjectives'", "'damageDealtToTurrets'", 
    "'damageSelfMitigated'", "'dangerPings'", "'deaths'", "'detectorWardsPlaced'", 
    "'doubleKills'", "'dragonKills'", "'eligibleForProgression'", "'enemyMissingPings'", 
    "'enemyVisionPings'", "'firstBloodAssist'", "'firstBloodKill'", "'firstTowerAssist'", 
    "'firstTowerKill'", "'gameEndedInEarlySurrender'", "'gameEndedInSurrender'", 
    "'getBackPings'", "'goldEarned'", "'goldSpent'", "'holdPings'", 
    "'inhibitorKills'", "'inhibitorTakedowns'", "'inhibitorsLost'", "'item0'", "'item1'", 
    "'item2'", "'item3'", "'item4'", "'item5'", "'item6'", "'itemsPurchased'", "'killingSprees'", 
    "'kills'", "'largestCriticalStrike'", "'largestKillingSpree'", "'largestMultiKill'", 
    "'longestTimeSpentLiving'", "'magicDamageDealt'", "'magicDamageDealtToChampions'", 
    "'magicDamageTaken'", "'needVisionPings'", "'neutralMinionsKilled'", "'nexusKills'", 
    "'nexusLost'", "'nexusTakedowns'", "'objectivesStolen'", "'objectivesStolenAssists'", 
    "'onMyWayPings'", "'participantId'", "'pentaKills'", "'physicalDamageDealt'", 
    "'physicalDamageDealtToChampions'", "'physicalDamageTaken'", "'profileIcon'", 
    "'pushPings'", "'quadraKills'",
    "'sightWardsBoughtInGame'", "'spell1Casts'", "'spell2Casts'", "'spell3Casts'", 
    "'spell4Casts'", "'summoner1Casts'", "'summoner1Id'", "'summoner2Casts'", 
    "'summoner2Id'", "'summonerLevel'", 
    "'teamEarlySurrendered'", "'teamId'", "'timeCCingOthers'", 
    "'timePlayed'", "'totalDamageDealt'", "'totalDamageDealtToChampions'", 
    "'totalDamageShieldedOnTeammates'", "'totalDamageTaken'", "'totalHeal'", 
    "'totalHealsOnTeammates'", "'totalMinionsKilled'", "'totalTimeCCDealt'", 
    "'totalTimeSpentDead'", "'totalUnitsHealed'", "'tripleKills'", "'trueDamageDealt'", 
    "'trueDamageDealtToChampions'", "'trueDamageTaken'", "'turretKills'", 
    "'turretTakedowns'", "'turretsLost'", "'unrealKills'", "'visionClearedPings'", 
    "'visionScore'", "'visionWardsBoughtInGame'", "'wardsKilled'", "'wardsPlaced'", "'win'", 
    "'bansAliados'", "'bansInimigos'", "'baronFirstAliado'", 
    "'championFirstAliado'", "'dragonFirstAliado'", "'inhibitorFirstAliado'", "'riftHeraldFirstAliado'", 
    "'towerFirstAliado'", "'baronFirstInimigo'", "'championFirstInimigo'", "'dragonFirstInimigo'", 
    "'inhibitorFirstInimigo'", "'riftHeraldFirstInimigo'", "'towerFirstInimigo'", "'baronKillsAliado'", 
    "'championKillsAliado'", "'dragonKillsAliado'", "'inhibitorKillsAliado'", "'riftHeraldKillsAliado'", 
    "'towerKillsAliado'", "'baronKillsInimigo'", "'championKillsInimigo'", "'dragonKillsInimigo'", 
    "'inhibitorKillsInimigo'", "'riftHeraldKillsInimigo'", "'towerKillsInimigo'"]

comparar = ['12AssistStreakCount', 
    'abilityUses', 'acesBefore15Minutes', 'alliedJungleMonsterKills', 'baronTakedowns', 
    'blastConeOppositeOpponentCount', 'bountyGold', 'buffsStolen', 'completeSupportQuestInTime', 
    'controlWardsPlaced', 'damagePerMinute', 'damageTakenOnTeamPercentage', 
    'dancedWithRiftHerald', 'deathsByEnemyChamps', 'dodgeSkillShotsSmallWindow', 
    'doubleAces', 'dragonTakedowns', 'earliestBaron', 'earliestDragonTakedown', 
    'earliestElderDragon', 'earlyLaningPhaseGoldExpAdvantage', 'effectiveHealAndShielding', 
    'elderDragonKillsWithOpposingSoul', 'elderDragonMultikills', 'enemyChampionImmobilizations', 
    'enemyJungleMonsterKills', 'epicMonsterKillsNearEnemyJungler', 'epicMonsterKillsWithin30SecondsOfSpawn', 
    'epicMonsterSteals', 'epicMonsterStolenWithoutSmite', 'fastestLegendary', 'flawlessAces', 
    'fullTeamTakedown', 'gameLength', 'getTakedownsInAllLanesEarlyJungleAsLaner', 
    'goldPerMinute', 'hadOpenNexus', 'immobilizeAndKillWithAlly', 'initialBuffCount', 
    'initialCrabCount', 'jungleCsBefore10Minutes', 'junglerTakedownsNearDamagedEpicMonster', 
    'kTurretsDestroyedBeforePlatesFall', 'kda', 'killAfterHiddenWithAlly', 'killParticipation', 
    'killedChampTookFullTeamDamageSurvived', 'killingSprees', 'killsNearEnemyTurret', 'killsOnOtherLanesEarlyJungleAsLaner', 
    'killsOnRecentlyHealedByAramPack', 'killsUnderOwnTurret', 'killsWithHelpFromEpicMonster', 
    'knockEnemyIntoTeamAndKill', 'landSkillShotsEarlyGame', 'laneMinionsFirst10Minutes', 
    'laningPhaseGoldExpAdvantage', 'legendaryCount', 'lostAnInhibitor', 'maxCsAdvantageOnLaneOpponent', 
    'maxKillDeficit', 'maxLevelLeadLaneOpponent', 'moreEnemyJungleThanOpponent', 'multiKillOneSpell', 
    'multiTurretRiftHeraldCount', 'multikills', 'multikillsAfterAggressiveFlash', 'mythicItemUsed', 
    'outerTurretExecutesBefore10Minutes', 'outnumberedKills', 'outnumberedNexusKill', 
    'perfectDragonSoulsTaken', 'perfectGame', 'pickKillWithAlly', 'playedChampSelectPosition', 
    'poroExplosions', 'quickCleanse', 'quickFirstTurret', 'quickSoloKills', 'riftHeraldTakedowns', 
    'saveAllyFromDeath', 'scuttleCrabKills', 'skillshotsDodged', 'skillshotsHit', 'snowballsHit', 
    'soloBaronKills', 'soloKills', 'soloTurretsLategame', 'stealthWardsPlaced', 'survivedSingleDigitHpCount', 
    'survivedThreeImmobilizesInFight', 'takedownOnFirstTurret', 'takedowns', 'takedownsAfterGainingLevelAdvantage', 
    'takedownsBeforeJungleMinionSpawn', 'takedownsFirstXMinutes', 'takedownsInAlcove', 
    'takedownsInEnemyFountain', 'teamBaronKills', 'teamDamagePercentage', 'teamElderDragonKills', 
    'teamRiftHeraldKills', 'threeWardsOneSweeperCount', 'tookLargeDamageSurvived', 
    'turretPlatesTaken', 'turretTakedowns', 'turretsTakenWithRiftHerald', 'twentyMinionsIn3SecondsCount', 
    'unseenRecalls', 'visionScoreAdvantageLaneOpponent', 'visionScorePerMinute', 'wardTakedowns', 
    'wardTakedownsBefore20M', 'wardsGuarded', 
]

def escrever_na_ultima_linha(arquivo_csv, nova_linha):

    with open(arquivo_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nova_linha)


def ultima_linha(arquivo_csv):

    with open(arquivo_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            last_row = row

    return last_row

def dados(partidadata,arquivo,num):
    for dadoInfo in (partidadata['info']['participants']):
        if(dadoInfo['summonerName'] == 'ComandZ'):

            dados = [f"'{partidadata['metadata']['matchId']}'", partidadata['info']['gameCreation'], 
                    partidadata['info']['gameDuration'], partidadata['info']['gameId'], 
                    num, partidadata['info']['mapId'], partidadata['info']['queueId'], 
                    f"'{dadoInfo['summonerName']}'", f"'{dadoInfo['championName']}'", 
                    f"'{dadoInfo['lane']}'", f"'{dadoInfo['role']}'", 
                    f"'{dadoInfo['individualPosition']}'", f"'{dadoInfo['teamPosition']}'", 
                    f"'{dadoInfo['puuid']}'"]

            dadoInfo.pop('perks')
            dadoInfo.pop('riotIdName')
            dadoInfo.pop('riotIdTagline')
            dadoInfo.pop('teamPosition')
            dadoInfo.pop('individualPosition')
            dadoInfo.pop('lane')
            dadoInfo.pop('championName')
            dadoInfo.pop('role')
            dadoInfo.pop('summonerName')
            dadoInfo.pop('puuid')
            dadoInfo.pop('summonerId')
        

            apend1 = []
            
            for nn in comparar:
                if nn in dadoInfo['challenges']:
                    apend1.append(dadoInfo['challenges'][nn])
                else:
                    apend1.append(0)

            apend2 = [valor for valor in dadoInfo.values()] #indece 8 ao adicionar

            apend3 = []

            dados.extend(apend2[:7])
            dados.extend(apend1)
            dados.extend(apend2[8:])

            for team in (partidadata['info']['teams']):
                bansA = []
                bansI = []
                aux1 = []
                aux2 = []

                if (team['teamId'] == dadoInfo['teamId']):
                
                    for obj in (team['objectives'].keys()):
                        apend3.append([team['objectives'][obj]['first']])
                    for obj in (team['objectives'].keys()):
                        apend3.append([team['objectives'][obj]['kills']])

                    for bnsA in (team['bans']):
                        bansA.append(bnsA['championId'])
                    aux1.append(bansA)
                    dados.extend(aux1)

                    
                else:
                    for obj in (team['objectives'].keys()):
                        apend3.append([team['objectives'][obj]['first']])
                    for obj in (team['objectives'].keys()):
                        apend3.append([team['objectives'][obj]['kills']])

                    for bnsI in (team['bans']):          
                        bansI.append(bnsI['championId'])
                    aux2.append(bansI)
                    dados.extend(aux2)
            
            dados.extend(apend3)
            
    escrever_na_ultima_linha(arquivo, dados)
    time.sleep(1)