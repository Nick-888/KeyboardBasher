import string
import random
from player import Player

class Main:
    def __init__(self):
        self.numberOfPlayers = 0
        self.playersNames = []
        self.numberOfRounds = 0
        self.letterToPoints = dict()
        self.playerToPoints = dict()

    def main(self):
        self.enterNumberOfPlayers()
        self.enterPlayerNames()
        self.enterNumberOfRounds()
        self.keyboardBash()
        self.sortPlayerToPoints()

    #Ask user to enter number of players
    def enterNumberOfPlayers(self):
        while True:
            try:
                self.numberOfPlayers = int(input("How many players will be playing? "))
                if(self.numberOfPlayers == 0):
                    print("Number of players must be greater than 0 \n")
                    continue
            except ValueError:
                print("This is not an integer please try again \n")
                continue
            else:
                break
        print("Number of players: " + str(self.numberOfPlayers))
    
    #enter names for each player:
    def enterPlayerNames(self):
        self.playersNames = [None] * self.numberOfPlayers
        if self.numberOfPlayers > 1:
            currentPlayer = 1
            index = 0
            while currentPlayer <= self.numberOfPlayers:
                name = input("Player " + str(currentPlayer) + " name: ")
                if name and not name.isspace():
                    self.playersNames[index] = name
                    currentPlayer = currentPlayer + 1
                    index = index + 1
                else:
                    print("Name must not be empty \n")
                    continue        
        else:
            self.playersNames[0] = "You"
        print("Player names: " + str(self.playersNames))

    #enter number of rounds
    def enterNumberOfRounds(self):
        while True:
            try:
                self.numberOfRounds = int(input("How many rounds would you like to play? "))
                if(self.numberOfRounds == 0):
                    print("Number of rounds must be greater than 0 \n")
                    continue
            except ValueError:
                print("This is not an integer please try again \n")
                continue
            else:
                break

    #generate random number between -5 and 5 inclusive
    def generateRandomNumber(self):
        return random.randrange(-5,6)


    #map each character on keyboard to random value
    def createLetterToPoints(self):
        allChars = string.printable
        for char in allChars:
            self.letterToPoints[char] = self.generateRandomNumber()

    #let the user bash their keyboard
    def keyboardBash(self):
        currentRoundNumber = 0
        while currentRoundNumber < self.numberOfRounds:
            print("  ----------------ROUND " + str(currentRoundNumber + 1) + " ----------------")
            self.createLetterToPoints()
            for player in self.playersNames:
                playerAttempt = input(player + "'s turn. Bash the keyboard! ")
                playerScore = 0
                if player in self.playerToPoints:
                    playerScore = self.playerToPoints[player]

                roundScore = 0
                for character in playerAttempt:
                    roundScore = roundScore + self.letterToPoints[character]
                
                print(player + " scored: " + str(roundScore))
                playerScore = playerScore + roundScore
                self.playerToPoints[player] = playerScore
            currentRoundNumber = currentRoundNumber + 1

    #method to sort playerToPoints dictionary
    def sortPlayerToPoints(self):
        allPlayers = []
        for key in self.playerToPoints:
            player = Player(key,self.playerToPoints[key])
            allPlayers.append(player)
        allPlayers = sorted(allPlayers, key=lambda player: player.score, reverse=True)
        index = 1
        for player in allPlayers:
            print(str(index) + ": " + player.name + " with " + str(player.score) + " points")
            index = index + 1
            
if __name__ == "__main__": 
  main = Main()
  main.main()