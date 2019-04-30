import pygame

bg_color = (0, 170, 0)
clock = pygame.time.Clock()

def load_images():
    image_list.append(pygame.image.load('./images/base.png').convert())
    image_list.append(pygame.image.load('./images/base.png').convert())
    image_list.append(pygame.image.load('./images/base.png').convert())

def place_initial_images():
    x = 0
    pos = [(0,0),(40,0),(80,0)]
    for i in image_list:
        screen.blit(i,pos[x])
        x += 1

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill(bg_color)
done = False

#Images
image_list = []
load_images()
place_initial_images()

y_test = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(bg_color)
    place_initial_images()
    screen.blit(image_list[0],(0, y_test))
    y_test += 40
        
    pygame.display.flip()
    clock.tick(2)

