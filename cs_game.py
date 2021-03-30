from clash import Clash
from warrior_factory import WarriorFactory
import random
from datetime import datetime
random.seed(datetime.now())


class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.wins = 0

    @staticmethod
    def intro():
        print("the  C O C K Y   S T R O L L E R \n"
              "Here is a small intro. \n"
              "You are a daring vagabond. You wade through the woods coming into sudden clashes and covering your name "
              "with glory or shame.")

    def choose_your_destiny(self):
        self.message_select_character()
        while True:
            try:
                player_id = int(input())
                if player_id in range(1, 5):
                    self.player1 = WarriorFactory.create_by_id(player_id)
                    print(f"You chose the {self.player1.name}'s way.\n")
                    break
                else:
                    print("Choose your destiny (1 to 4):")
                    pass
            except ValueError:
                print("Choose your destiny (1 to 4):")
            finally:
                pass

    def select_opponent(self):
        player_id = random.randint(1, 4)
        self.player2 = WarriorFactory.create_by_id(player_id)

    def start(self):
        self.choose_your_destiny()
        while True:
            self.player1.regen()
            self.select_opponent()
            if self.player2.name == self.player1.name:
                self.player2.name = 'Dark ' + self.player2.name
            clash = Clash(self.player1, self.player2)
            result = clash.start()
            if result == 2:         # you won
                self.wins += 1
                self.message_victory()
                pass
            elif result == 1:       # you died
                self.message_failure()
                return self.restart()
            else:                   # you ran
                pass

    @staticmethod
    def message_select_character():
        print("\nSelect your character: \n"
              "1 - Knight \n"
              "2 - Ogre \n"
              "3 - Goblin \n"
              "4 - Dragon (you bloody cheater!)")

    def message_victory(self):
        print(f"\n🚩 Congratulations, brave {self.player1.name}! "
              f"You've overcame the {self.player2.name} 🚩\n"
              f"Trophy count: '{self.wins}'.\n")

    def message_failure(self):
        print(f"\n💀 You've been killed.\n"
              f"{'':3}Game over.\n"
              f"{'':3}You achieved '{self.wins}' victories. 💀")

    def restart(self):
        print("\nRestart? (y) / (n)")
        while True:
            restart = input()
            if restart.casefold() == 'y':
                self.wins = 0
                return self.start()
            elif restart.casefold() == 'n':
                break
            else:
                print('Choose: "yes" (y) or "no" (n)?')
                pass


if __name__ == '__main__':
    game = Game()
    game.intro()
    game.start()
