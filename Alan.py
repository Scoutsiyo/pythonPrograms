def bomb():
    bomb = ["BANG","BOOM","POW","CRASH","KABOOM","BAM","WHAM","ZAP","ZOWIE","ZONK","ZLOPP","ZOW","ZOT","ZIT","ZIP","ZAP","ZAM"]
    print(*bomb)



def turtle_square():
    import turtle
    t = turtle.Turtle()
    d = 50
    while True:
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        t.forward(d)

def turtle_circle():
    import turtle
    t = turtle.Turtle()
    t.circle(100)

def turtle_lines():
    import turtle
    t = turtle.Turtle()
    for i in range(20):
        while i < 19:
            t.right(170)
            t.forward(100)
            t.left(170)
            t.forward(100)
            t.pensize(5)
            t.speed("fastest")
    turtle.bye()        

def gun():
    import string as ammo

    gun = list(ammo.ascii_uppercase)

    print(gun.pop())

def stats():
    import matplotlib.pyplot as plt
    import numpy as np
    
    val = np.random.randint(1,10,10)
    print(val)
    print(type(val))

    plt.figure(figsize=(10,5))
    plt.errorbar(range(len(val)), val, val, fmt = "o", capsize=6)
    help(plt.errorbar)
    plt.title('Error Bar Plot')
    plt.plot(range(len(val)), val , color = 'red')
    plt.show()

def square_game():
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Square Game")
    clock = pygame.time.Clock()
    sq
    pygame.quit()

square_game()