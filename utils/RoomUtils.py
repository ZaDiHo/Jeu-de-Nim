# Nom du fichier: RoomUtils.py
# Auteur: Thomas PROVOST
# Objectif: Utilitaire pour la gestion des salons
# Date dernière modification: 25/01/2021
# Version: 1.0

from utils.GameUtils import generateId

def createRoom(player):
    """
    Crée une salle de jeu
    
    Paramètres:
    * player: le joueur qui crée la salle
    """
    id = generateId(5)
    roomId = "ROOM_".join(map(str, id))
    key = generateId(6)
    roomKey = "".join(map(str, key))
    player.sendPacket(f"CREATE {player.getName()} {roomId} {roomKey}")