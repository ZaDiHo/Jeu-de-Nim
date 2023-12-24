from client.NimClient import openSession

# common/nim_game.py

class Player:
    def __init__(self, playerName):
        self.name = playerName

    def getName(self):
        return self.name
    
    def setClientSocket(self, client_socket):
        self.client_socket = client_socket

    def sendPacket(self, packet):
        if self.client_socket:
            self.client_socket.send(packet.encode('utf-8'))
        else:
            print("Erreur : Le socket client n'est pas défini.")


matches = 16
difficulty = 1
maxNumberOfMatchesTakeable = 3
mode = 1 #1 = Solo | 2 = Local | 3 = Online

def initValues():
    global matches, difficulty, maxNumberOfMatchesTakeable, mode
    matches = 21
    difficulty = 1
    maxNumberOfMatchesTakeable = 3
    mode = 1

def setMode(value):
    global mode
    mode = value

def getMode():
    global mode
    return mode

def setMatches(value):
    global matches
    matches = value

def setDifficulty(value):
    global difficulty
    difficulty = value

def setMaxNumberOfMatchesTakeable(value):
    global maxNumberOfMatchesTakeable
    maxNumberOfMatchesTakeable = value

def getMatches():
    global matches
    return matches

def getDifficulty():
    global difficulty
    return difficulty

def getMaxNumberOfMatchesTakeable():
    global maxNumberOfMatchesTakeable
    return maxNumberOfMatchesTakeable