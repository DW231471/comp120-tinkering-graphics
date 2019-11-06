import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))

print("Select a terrain variant:")


def option(x):
    print(x)


#list of variants

option("grass")
option("dirt")
option("dirt_rocky")
option("dirt_dry")
option("leaves_hedge")
option("leaves_autumn")
option("marble")
option("wood")
option("snow")
option("ice")

choice = input()

#users selection being used for image

if choice in "grass":
    picture = pygame.image.load('grass.png')
elif choice in "dirt":
    picture = pygame.image.load('dirt.png')
elif choice in "dirt_rocky":
    picture = pygame.image.load('dirt_rocky.png')
elif choice in "dirt_dry":
    picture = pygame.image.load('dirt_dry.png')
elif choice in "leaves_hedge":
    picture = pygame.image.load('leaves_hedge.png')
elif choice in "leaves_autumn":
    picture = pygame.image.load('leaves_autumn.png')
elif choice in "marble":
    picture = pygame.image.load('marble.png')
elif choice in "wood":
    picture = pygame.image.load('wood.png')
elif choice in "snow":
    picture = pygame.image.load('snow.png')
elif choice in "ice":
    picture = pygame.image.load('ice.png')
else:
    print("Input not accepted, please ensure you have selected an option from the list")


while True:
    screen.blit(screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
