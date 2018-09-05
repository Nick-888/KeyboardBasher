class Main:
    def __init__(self):
        self.numberOfPlayers = 0
        self.playersNames = []
        self.numberOfRounds = 0

    def main(self):
        self.enterNumberOfPlayers()
        self.enterPlayerNames()
        self.enterNumberOfRounds()

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
        print("Number of rounds: " + (str(self.numberOfRounds)))


if __name__ == "__main__": 
  main = Main()
  main.main()