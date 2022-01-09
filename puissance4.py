import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100
 
# This sets the margin between each cell
MARGIN = 10
PADDING = 50


multiplex = 'multiplex.ogg'

 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(15):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(15):
        grid[row].append(0)  # Append a cell
 
 
# Initialize pygame
pygame.init()

player = 1
 
# Set the HEIGHT and WIDTH of the screen
# WINDOW_SIZE = [785, 675]
WINDOW_SIZE = [860, 900]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Puissance 4")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


pygame.font.init()

font = pygame.font.SysFont("monospace", 75)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONUP and player == 1:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if grid[row][column] == 0:
                # Sélectionner la case en dessous pour savoir si elle est jouée
                below = row + 1
                
                if grid[below][column] == 1 or grid[below][column] == 2 or row == 5:
                        grid[row][column] = 1
                        print("PLAYER 1", pos, "Grid coordinates: ", row, column)
                        player = 2

                        # Vérif ligne verticale
                        if grid[row + 2][column] == 1 and grid[row + 3][column] == 1:
                            print("C'EST GAGNÉ")
                            victory = font.render("You WIN", 1, RED)
                            screen.blit(victory, (400, 700))
                            pygame.mixer.init()
                            pygame.mixer.music.load(multiplex)
                            pygame.mixer.music.play()

                        # Vérif ligne Horizontale
                        elif grid[row][column + 1] == 1 and grid[row][column + 2] == 1 and grid[row][column + 3] == 1 or grid[row][column - 1] == 1 and grid[row][column - 2] == 1 and grid[row][column - 3] == 1 or grid[row][column - 1] == 1 and grid[row][column + 1] == 1 and grid[row][column + 2] == 1 or grid[row][column - 2] == 1 and grid[row][column - 1] == 1 and grid[row][column + 1] == 1:
                            print("C'EST GAGNÉ")
                            victory = font.render("You WIN", 1, RED)
                            screen.blit(victory, (400, 700))
                            pygame.mixer.init()
                            pygame.mixer.music.load(multiplex)
                            pygame.mixer.music.play()

                        # Vérif ligne Diagonale
                        elif grid[row - 1][column + 1] == 1 and grid[row - 2][column + 2] == 1 and grid[row - 3][column + 3] == 1 or grid[row + 1][column - 1] == 1 and grid[row - 1][column + 1] == 1 and grid[row - 2][column + 2] == 1 or grid[row + 1][column - 1] == 1 and grid[row + 2][column - 2] == 1 and grid[row - 1][column + 1] == 1 or grid[row + 1][column - 1] == 1 and grid[row + 2][column - 2] == 1 and grid[row + 3][column - 3] == 1 or grid[row + 1][column + 1] == 1 and grid[row + 2][column + 2] == 1 and grid[row + 3][column + 3] == 1 or grid[row - 1][column - 1] == 1 and grid[row + 2][column + 2] == 1 and grid[row + 3][column + 3] == 1 or grid[row - 1][column - 1] == 1 and grid[row - 2][column - 2] == 1 and grid[row + 3][column + 3] == 1 or grid[row - 1][column - 1] == 1 and grid[row - 2][column - 2] == 1 and grid[row - 3][column - 3] == 1:
                            print("C'EST GAGNÉ")
                            victory = font.render("You WIN", 1, RED)
                            screen.blit(victory, (400, 700))
                            pygame.mixer.init()
                            pygame.mixer.music.load(multiplex)
                            pygame.mixer.music.play()

                else:
                    print("Case injouable")

            else:
                print("Case déjà jouée")
            
        elif event.type == pygame.MOUSEBUTTONDOWN and player == 2:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if grid[row][column] == 0:
                # Sélectionner la case en dessous pour savoir si elle est jouée
                below = row + 1
                
                if grid[below][column] == 1 or grid[below][column] == 2 or row == 5:
                        grid[row][column] = 2
                        print("PLAYER 2", pos, "Grid coordinates: ", row, column)
                        player = 1

                        # Vérif ligne verticale
                        if grid[row + 2][column] == 2 and grid[row + 3][column] == 2:
                            print("C'EST GAGNÉ")
                            victory = font.render("You WIN", 1, RED)
                            screen.blit(victory, (400, 700))
                            pygame.mixer.init()
                            pygame.mixer.music.load(multiplex)
                            pygame.mixer.music.play()

                        # Vérif ligne Horizontale
                        elif grid[row][column + 1] == 2 and grid[row][column + 2] == 2 and grid[row][column + 3] == 2 or grid[row][column - 1] == 2 and grid[row][column - 2] == 2 and grid[row][column - 3] == 2 or grid[row][column - 1] == 2 and grid[row][column + 1] == 2 and grid[row][column + 2] == 2 or grid[row][column - 2] == 2 and grid[row][column - 1] == 2 and grid[row][column + 1] == 2:
                            print("C'EST GAGNÉ")
                            victory = font.render("You WIN", 1, RED)
                            screen.blit(victory, (400, 700))
                            pygame.mixer.init()
                            pygame.mixer.music.load(multiplex)
                            pygame.mixer.music.play()

                        # Vérif ligne Diagonale
                        elif grid[row - 1][column + 1] == 2 and grid[row - 2][column + 2] == 2 and grid[row - 3][column + 3] == 2 or grid[row + 1][column - 1] == 2 and grid[row - 1][column + 1] == 2 and grid[row - 2][column + 2] == 2 or grid[row + 1][column - 1] == 2 and grid[row + 2][column - 2] == 2 and grid[row - 1][column + 1] == 2 or grid[row + 1][column - 1] == 2 and grid[row + 2][column - 2] == 2 and grid[row + 3][column - 3] == 2 or grid[row + 1][column + 1] == 2 and grid[row + 2][column + 2] == 2 and grid[row + 3][column + 3] == 2 or grid[row - 1][column - 1] == 2 and grid[row + 2][column + 2] == 2 and grid[row + 3][column + 3] == 2 or grid[row - 1][column - 1] == 2 and grid[row - 2][column - 2] == 2 and grid[row + 3][column + 3] == 2 or grid[row - 1][column - 1] == 2 and grid[row - 2][column - 2] == 2 and grid[row - 3][column - 3] == 2:
                            print("C'EST GAGNÉ")
                            victory = font.render("You WIN", 1, RED)
                            screen.blit(victory, (400, 700))
                            pygame.mixer.init()
                            pygame.mixer.music.load(multiplex)
                            pygame.mixer.music.play()

                else:
                    print("Case injouable")
            else:
                print("Case déjà jouée")
    
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(6):
        for column in range(7):
            color = BLUE
            if grid[row][column] == 1:
                color = RED
            elif grid[row][column] == 2:
                color = YELLOW
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + PADDING,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()