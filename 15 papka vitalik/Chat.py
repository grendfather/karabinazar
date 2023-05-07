import pygame

# Set the width and height of the screen (in pixels)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Maze Game")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the font for the text
font = pygame.font.Font(None, 36)

# Set the maze structure
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Define the player position
player_x = 1
player_y = 1

# Define the player speed
player_speed = 5

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the maze
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, WHITE, [j*50, i*50, 50, 50])
    
    # Draw the player
    pygame.draw.circle(screen, (255, 0, 0), (player_x*50+25, player_y*50+25), 20)
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if maze[player_y-1][player_x] == 0:
            player_y -= player_speed
    if keys[pygame.K_DOWN]:
        if maze[player_y+1][player_x] == 0:
            player_y += player_speed
    if keys[pygame.K_LEFT]:
        if maze[player_y][player_x-1] == 0:
            player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        if maze[player_y][player_x+1] == 0:
            player_x += player_speed
    
    # Update the screen
