from warrior import Warrior


class WarriorFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_knight():    # the basic class
        knight = Warrior('Knight', 100, 40, 70, 50)
        return knight

    @staticmethod
    def create_ogre():      # strong but clumsy
        ogre = Warrior('Ogre', 150, 80, 20, 40)
        return ogre

    @staticmethod
    def create_goblin():    # agile but weak
        goblin = Warrior('Goblin', 70, 30, 90, 60)
        return goblin

    @staticmethod
    def create_dragon():    # the killer
        dragon = Warrior('Dragon', 300, 150, 10, 10)
        return dragon

    @staticmethod
    def create_by_id(player_id):
        if player_id == 1:
            return WarriorFactory.create_knight()
        elif player_id == 2:
            return WarriorFactory.create_ogre()
        elif player_id == 3:
            return WarriorFactory.create_goblin()
        elif player_id == 4:
            return WarriorFactory.create_dragon()
