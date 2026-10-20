class HeroCreator():

    number_of_characters = 0

    def __init__(self, Strength, Agility, Intellect):
        self.Strength = Strength
        self.Agility = Agility
        self.Intellect = Intellect
        HeroCreator.number_of_characters += 1

    @classmethod
    def printout_the_number(cls):
        print(cls.number_of_characters)

human_bard = HeroCreator(3, 7, 8)

print(HeroCreator.number_of_characters)

class WizardCreator(HeroCreator):
    def __init__(self, Strength, Agility, Intellect, ManaPool):
        super().__init__(Strength, Agility, Intellect)
        self.ManaPool = ManaPool

    def give_stats_report(self):
        print(f'This character has {self.Strength} point of strength, {self.Agility} points of agility, {self.Intellect} points of intellect and {self.ManaPool} point of mana')

ElfWizard = WizardCreator(2, 4, 9, 150)
ElfWizard.give_stats_report()
print(HeroCreator.number_of_characters)

