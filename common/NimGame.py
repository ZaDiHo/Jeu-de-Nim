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

