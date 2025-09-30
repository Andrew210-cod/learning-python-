import pygame

pygame.init()

# Create window
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Image Example")

# Load and sclae image
player1 = pygame.image.load("image copy.png")
player1 = pygame.transform.scale(player1, (150, 150))

player2 = pygame.image.load("image.png")
player2 = pygame.transform.scale(player2, (150, 150))

x1, y1 = 200, 200
x2, y2 = 200, 400
speed1 = 2
speed2 = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x1 -= speed1
    if keys[pygame.K_d]:
        x1 += speed1
    if keys[pygame.K_w]:
        y1 -= speed1
    if keys[pygame.K_s]:
        y1 += speed1

    if keys[pygame.K_LEFT]:
        x2 -= speed2
    if keys[pygame.K_RIGHT]:
        x2 += speed2
    if keys[pygame.K_UP]:
        y2 -= speed2
    if keys[pygame.K_DOWN]:
        y2 += speed2
    
    screen.fill((0,0,0)) 
    screen.blit(player1, (x1,y1))
    screen.blit(player2, (x2,y2)) 
    pygame.display.update()

pygame.quit()
