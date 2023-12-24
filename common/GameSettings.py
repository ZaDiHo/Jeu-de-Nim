from utils.GameUtils import generateId

matches = 16 # Default value : 16
maxMatchesTaken = 3 # Default value : 3

firstPlayerId = generateId(5)
firstPlayerName = "PLAYER_" + "".join(map(str, firstPlayerId))

player = ""