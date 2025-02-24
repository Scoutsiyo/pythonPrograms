def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("How many times do you want the cat to meow? "))
print(meow(number))