import random

card_dict = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# Player class
# This will control all operations relating to player actions
class Player:
    def __init__(self, player):
        self.player = player
        self.cards = {}
        self.total = 0
    
    # Determines whether to end the game
    def check_total(self):
        print("You now have {} points.".format(self.total))
        if self.total == 21:
            print("BLACKJACK!")
            return False
        if self.total > 21:
            print("BUST!")
            return True
        else:
            return False

    # If "Hit" is selected
    def add_card(self):
        print("Selecting a card...")
        face, value = random.choice(list(card_dict.items()))
        print("You drew a {}!".format(face))
        
        # If the card drawn is an ace, the user will be able to select whether to add 1 or 11 points
        if face == 'A':
            done = False
            while not done:
                ace = input("How many points would you like to add?\nCurrent score: {}\n1) 1\n2) 11\n".format(self.total))
                if not ace.isnumeric():
                    print("Invalid input. Please try again.\n")
                elif int(ace) < 1 or int(ace) > 2:
                    print("Invalid input. Please try again.\n")
                elif int(ace) == 1:
                    print("Adding 1 point...")
                    self.total += 1
                    done = True
                elif int(ace) == 2:
                    print("Adding 11 points...")
                    self.total += 11
                    done = True
        else:
            print("Adding {} points...".format(value))
            self.total += value
        
    
    # If "View hand" is selected
    def view_hand(self):
        statement = "Your hand is as follows:\n"
        for face in self.cards.keys():
            statement += face + " "
        statement += "\nTotal: {}\n".format(self.total)
        print(statement)
        self.check_total()





print("===================\n")
print("     BLACKJACK     \n")
print("===================\n\n")

# First prompt
ready = False
while not ready:
    num = input("How many people will be playing? (1-4): ")
    if not num.isnumeric():
        print("Invalid input. Please try again.\n")
    elif int(num) < 1 or int(num) > 4:
        print("Invalid input. Please try again.\n")
    else:
        ready = True

# Initialize player list
players = []
player1 = Player(1)
players.append(player1)
if int(num) > 1:
    player2 = Player(2)
    players.append(player2)
if int(num) > 2:
    player3 = Player(3)
    players.append(player3)
if int(num) > 3:
    player4 = Player(4)
    players.append(player4)

for entrant in players:
    bust = False
    print("\nPlayer {}\'s turn!".format(entrant.player))
    while not bust:
        choice = input("\nWhat would you like to do?\n1) Hit\n2) Stay\n3) Fold\n4) View hand\n")
        if not choice.isnumeric():
            print("Invalid input. Please try again.")
            continue
        elif int(choice) < 1 or int(choice) > 3:
            print("Invalid input. Please try again.")
            continue
        elif int(choice) == 1:
            entrant.add_card()
            bust = entrant.check_total()
        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            pass
        elif int(choice) == 4:
            entrant.view_hand()
            continue