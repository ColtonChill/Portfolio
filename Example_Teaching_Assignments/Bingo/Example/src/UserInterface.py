from Deck import Deck
import Menu


class UserInterface():
    def __init__(self):
        self.deck = Deck

    def run(self):
        """Present the main mainMenu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        mainMenu = Menu.Menu("Main")
        mainMenu.addOption("C", "Create a new deck")

        keepGoing = True
        while keepGoing:
            command = mainMenu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __getDeckSpecs(self):
        while True:
            n = input("Please enter the Size [3,15] of the cards: ")
            if str.isnumeric(n):
                n = int(n)
                if 2 < int(n) < 16:
                    break
                else:
                    print("Invalid range")
            else:
                print("Entry must be a number")
        while True:
            m = input("Please enter the number [3,10000] of cards: ")
            if str.isnumeric(m):
                m = int(m)
                if 2 < int(m) < 10001:
                    break
                else:
                    print("Invalid range")
            else:
                print("Entry must be a number")
        while True:
            r = input(f"Please enter the maximum number[{2 * int(n) * int(n)},{4 * int(n) * int(n)}] possible on the cards: ")
            if str.isnumeric(r):
                r = int(r)
                if 2 * int(n) * int(n) <= int(r) <= 4 * int(n) * int(n):
                    break
                else:
                    print("Invalid range")
            else:
                print("Entry must be a number")
        self.deck = Deck(n, m, r)

    def __createDeck(self):
        """Command to create a new Deck"""
        self.__getDeckSpecs()
        self.__deckMenu()

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.deck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __printCard(self):
        """Command to print a single card"""
        n = input(f"Please enter the Card number[{1},{self.deck.getCardCount()}] to print: ")
        if str.isnumeric(n):
            n = int(n)
            if 1 <= int(n) <= self.deck.getCardCount():
                cardToPrint = self.deck.getCard(n)
                print()
                cardToPrint.print()
            else:
                print("Invalid range")
        else:
            print("Entry must be a number")

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = input(f"Please enter the file destination: ")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            with open(fileName, 'w') as outputStream:
                self.deck.print(outputStream)
            outputStream.close()
            print("Done!")  
