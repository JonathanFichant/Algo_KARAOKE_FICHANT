

# Exercice A

print("Diagramme de classe visible dans le code en commentaire")

"""
Diagramme de classe Player
    -str Pseudo
    -int[] scores
    _____________
    +str getPseudo()
    +int getScore()
    +int getScores(int)
    +int getSommeScores()
    +int getMoyenneScores()
    +int getPireScore()
    +int getBestScore()
    +int addScore(int,int)
"""

class Player:
    def __init__(self,pseudo,scores):
        self.__pseudo = pseudo
        self.__scores = scores

    def getPseudo(self):
        return self.__pseudo

    def getScore(self,i):
        print("Score de la chanson " + str(i) + " : "+ str(self.__scores[i]))

    def getScores(self):
        print("")
        print("Scores de " + self.__pseudo + " : ")
        print("CHANSON 0 : " + str(self.__scores[0]))
        print("CHANSON 1 : " + str(self.__scores[1]))
        print("CHANSON 2 : " + str(self.__scores[2]))
        print("CHANSON 3 : " + str(self.__scores[3]))
        print("CHANSON 4 : " + str(self.__scores[4]))
        print("")

    def getSommeScores(self):
        temp = 0
        for i in range(5):
            temp += self.__scores[i]
        print("Somme des scores : " + str(temp))

    def getMoyenneScores(self):
        temp = 0
        moy = 0
        for i in range(5):
            if (self.__scores[i] > 0):
                temp += self.__scores[i]
                moy += 1
        print("Moyenne des scores enregistrés : " + str(temp/moy))

    def getPireScore(self):
        temp = 50
        temp2 = 0
        temp3 = 0
        for i in range(5):
            temp3 += self.__scores[i]
            if (self.__scores[i] > 0): # on ne compte que les chansons jouées
                if (temp > self.__scores[i]):
                    temp = self.__scores[i]
                    temp2 = i
        if (temp3 > 0): # on vérifie si au moins une chanson a été jouée
            print("Pire score de " + str(self.__pseudo) + " : Chanson " + str(temp2) + " : " + str(temp))
        else:
            print("Pas de chansons jouées pour le moment pour " + str(self.__pseudo) + ".")
            
    def getBestScore(self):
            temp = 0
            temp2 = 0
            for i in range(5):
                if (self.__scores[i] > 0): # on ne compte que les chansons jouées
                    if (temp < self.__scores[i]):
                        temp = self.__scores[i]
                        temp2 = i
            if (temp > 0): # on vérifie si au moins une chanson a été jouée
                print("Meilleur score de " + str(self.__pseudo) + " : Chanson " + str(temp2) + " : " + str(temp))
            else:
                print("Pas de chansons jouées pour le moment pour " + str(self.__pseudo) + ".")
        
    def addScore(self,newScore,numChanson):
        if (self.__scores[numChanson] < newScore and newScore >= 50):
            self.__scores[numChanson] = newScore
            print("Nouveau meilleur score ! Chanson " + str(numChanson) + " : " + str(newScore) ) 


Kyle = Player("Kyle",[0,30,0,70,0])
Jake = Player("Jake",[0,0,0,0,0])


Kyle.getScores()
Jake.getScore(2)

print("")

Kyle.getSommeScores()
Kyle.getMoyenneScores()

print("")

Kyle.getPireScore()
Jake.getPireScore()

print("")

Kyle.getBestScore()
Jake.getBestScore()

Kyle.getScores()


# score minimum 50 / 100
# 0 / 100 signifie que la chanson n'a pas été essayé par le joueur

while(True):

    print("Que voulez-vous faire ? :")
    print("Ajouter un joueur : 1 ")
    print("Afficher un score précis d'un joueur: 2 ")
    print("Afficher tous les scores d'un joueur : 3 ")
    print("Afficher la somme des scores d'un joueur : 4 ")
    print("Afficher la moyenne des scores enregistrés d'un joueur : 5 ")
    print("Afficher le pire score d'un joueur : 6 ")
    print("Afficher le meilleur score d'un joueur : 7 ")
    print("Ajouter un score : 8 ")
    choix = input()

    #Pas eu le temps d'implémenter la suite
    if (choix == "1"):
        var3 = input("Nom du nouveau joueur : ")
        var3 = Player(var3,[0,0,0,0,0])


    if (choix == "8"):
        var0 = (input("Nom du Joueur : "))
        var1 = int(input("Nouveau score : "))
        var2 = int(input("Numéro de la chanson : "))
        
        #var0.addScore(var1,var2)
        
    break

# Exercice B

"""
Diagramme de la classe Karaoké
    -str[] chansons
    -str[] players
    ________________
    +str[] addPlayer
    +str[] retirePlayer
    +int getBestScore(int)
    +str getBestPlayer
    +int getBestScoreAll
    +int getBestMoy

Diagramme de la classe Player modifiée
    -str pseudo
    ...


"""


"""class Karaoke:
    def __init__(self,chansons[0],players):
        self.__chansons = chansons
        self.__players = players

    def getBestScoreAll(i):
        temp = 0
        temp2 = 0
        for i in range(len(self.__chansons)):
            if (self.__scores[i] > 0): # on ne compte que les chansons jouées
                if (temp < self.__scores[i]):
                    temp = self.__scores[i]
                    temp2 = i
        if (temp > 0): # on vérifie si au moins une chanson a été jouée
            print("Meilleur score sur la chanson " + str(temp2) + " : " + str(temp))
        else:
            print("Pas de chansons jouées pour le moment.")"""


class Players:
    def __init__(self,pseudo):
        self.__pseudo = pseudo


#Pas eu le temps pour la suite


#min 1 player
#chaque chanson a un nom
#possibilité d'ajouter ou retirer des players sauf si reste qu'1
#fonction pour voir le meilleur score d'une chanson
#fonction pour voir le meilleur joueur (meilleur score total)
#fonction pour voir le meilleur score toutes chansons confondues
#fonction pour voir la meilleure moyenne