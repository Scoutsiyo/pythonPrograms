

class ImperialStarDestroyer:
    def __init__(self, name, crew, weapons):
        self._name = name
        self._crew = crew
        self._weapons = weapons
        self._health = 1000
        self._speed = 15
        self._location = "Courscant"
        self._destination = None
        self._is_hyperspace = False
        self._is_shield_up = True
        self._is_engine_on = False
        self._is_weapon_ready = True
        self._is_firing = False
        self._is_moving = False
    
    def __str__(self):
        return f"{self._name} is at {self._location} with {self._crew} crew members"
    

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

class TieFighter(ImperialStarDestroyer):
    def __init__(self, name, crew, weapons, speed):
        super().__init__(name, crew, weapons)
        self._speed = speed
        self._location = None
        self._is_engine_on = True
        self._is_moving = True
        self._health = 100
    
    def __str__(self):
        return f"{self._name} is at {self._location} with {self._crew} crew members"


#Imperial Star Destroyer
ImperialStarDestroyer1 = ImperialStarDestroyer("Imperial Star Destroyer", 1000, 100)
ImperialStarDestroyer1.new_location("Death Star")
ImperialStarDestroyer1.new_destination("Tatooine")
print(ImperialStarDestroyer1)
print(f"Actual Location = {ImperialStarDestroyer1.location}")
print(f"Destination = {ImperialStarDestroyer1.destination}")

ImperialStarDestroyer1.new_destination("Alderaan")

print(f"New Destination = {ImperialStarDestroyer1.destination}")
print("\n")

#Mandalorian Star Destroyer
MandalorianDestroyer = ImperialStarDestroyer("Mandalorian Star Dstroyer", 500, 50)
MandalorianDestroyer.new_location("Mandalore")
MandalorianDestroyer.new_destination("Endor")

print(MandalorianDestroyer)
print(f"Actual Location = {MandalorianDestroyer.location}")
print(f"Destination = {MandalorianDestroyer.destination}")
print("\n")
#TieFighter

tiefighter = TieFighter("Tie Fighter", 1, 2, 100)
tiefighter.new_location("Death Star")
tiefighter.new_destination("Coruscant")

print(f"Location = {tiefighter.location}")

print(tiefighter)


