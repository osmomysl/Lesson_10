class Clash:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.escapes = 0
        self.result = 0

    def start(self):
        self.message_start()
        if not self.runaway():
            self.combat()
        return self.result

    def runaway(self):
        while True:
            your_choice = input()
            if your_choice.casefold() == 'f':
                return False        # go to the combat
            elif your_choice.casefold() == 'r':
                self.result = 0
                self.message_run(1)
                return True         # leave the combat
            else:
                self.message_run(2)
                pass

    def combat(self):
        while self.player1.is_alive() and self.player2.is_alive():
            p1_damage = self.player1.make_damage()
            self.player2.take_damage(p1_damage)
            p2_damage = self.player2.make_damage()
            self.player1.take_damage(p2_damage)
            if not self.low_hp():
                if self.player1.is_alive():
                    self.result = 2  # = 2 if you won
                else:
                    self.result = 1  # = 1 if you died
            else:
                break
        return self.result       # = 0 if you ran away

    def low_hp(self):
        if self.player1.is_alive() and self.player2.is_alive():
            if (self.player1.hp / self.player1.health < 0.5 and self.escapes == 0) or \
                    (self.player1.hp / self.player1.health < 0.15 and self.escapes == 1):
                self.escapes += 1
                self.message_low_hp()
                return self.runaway()
            else:
                pass

    def message_start(self):
        print(f"You have faced an enemy: {self.player2.name} ({self.player2.hp} HP) \n"
              f"What are you going to do: fight (f) or run away (r)?")

    @staticmethod
    def message_low_hp():
        print("\nYou are wounded and exhausted.\n"
              "Do you want to save your life by leaving the battle (r) or fight to the last breath (f)?")

    @staticmethod
    def message_run(step):
        if step == 1:
            print("You ran away from the enemy. \n"
                  "You're still alive, but you haven't gained any glory.\n")
        elif step == 2:
            print("Make your decision: \u2694 (f) or \U0001F3C3 (r)?")
