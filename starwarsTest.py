from starwars import ImperialStarDestroyer, TieFighter

#def meow(n: int) -> str:
#    return "meow\n" * n

Imperial = ImperialStarDestroyer( "A-4", 1040, 250)
Mandalore = ImperialStarDestroyer("Mandalorian Star Destroyer",670, 250)
Tie = TieFighter("Tie-1", 2, 100)
Tie.new_location("Death Star")
Mandalore.new_location("Mandalore")




print(Imperial)
print(Mandalore)
print(Tie)

print(Mandalore.attack(Imperial))
print(Tie.attack(Imperial))
print(Imperial.attack(Mandalore))
