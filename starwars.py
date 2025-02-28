class ImperialStarDestroyer:
    def __init__(self, name, crew, damage):
        self.name = name
        self.crew = crew
        self.health = 1000
        self.speed = 15
        self.damage = damage
        self._location = "Courscant"
        self._destination = None
    
    def __str__(self):
        return f"{self.name} is at {self._location} with {self.crew} crew members"
    

    @property
    def location(self):
        return self._location

    def new_location(self, Location):
        self._location = Location
    
    @property
    def destination(self):
        return self._destination
    
    def new_destination(self, new_destination):
        self._destination = new_destination

    def attack(self, target):
        target.health -= self.damage
        if target.health <= 0:
            return f"{target.name} is destroyed"
        return f"{self.name} attacked {target.name} and now {target.name}'s health is: {target.health}"        

class TieFighter(ImperialStarDestroyer):
    def __init__(self, name, crew, damage):
        super().__init__(name, crew, damage)
        self.speed = 100
        self._location = None
        self.health = 150
        self.damage = damage


    def __str__(self):
        return f"{self.name} is at {self._location} with {self.crew} crew members"

def main():
    #Imperial Star Destroyer
    ImperialStarDestroyer1 = ImperialStarDestroyer("Imperial Star Destroyer", 1000, 250)
    ImperialStarDestroyer1.new_location("Death Star")
    ImperialStarDestroyer1.new_destination("Tatooine")
    print(ImperialStarDestroyer1)
    print(f"Actual Location = {ImperialStarDestroyer1.location}")
    print(f"Destination = {ImperialStarDestroyer1.destination}")

    ImperialStarDestroyer1.new_destination("Alderaan")

    print(f"New Destination = {ImperialStarDestroyer1.destination}")
    print("\n")

    #Mandalorian Star Destroyer
    MandalorianDestroyer = ImperialStarDestroyer("Mandalorian Star Dstroyer", 500, 250)
    MandalorianDestroyer.new_location("Mandalore")
    MandalorianDestroyer.new_destination("Endor")

    print(MandalorianDestroyer)
    print(f"Actual Location = {MandalorianDestroyer.location}")
    print(f"Destination = {MandalorianDestroyer.destination}")
    print("\n")
    #TieFighter

    tiefighter = TieFighter("Tie Fighter", 1, 100)
    tiefighter.new_location("Death Star")
    tiefighter.new_destination("Coruscant")

    print(f"Location = {tiefighter.location}")

    print(tiefighter)


    print(tiefighter.attack(ImperialStarDestroyer1))

if __name__ == "__main__":
    main()