# This game has 1 player, 3 enemies and 1 prize

import pygame
import random

# Initialize the pygame modules to get everything started.

pygame.init()

# Specifying the width and height of the screen that will be created when the program runs

screen_width = 1050
screen_height = 680

# Creating a screen
screen = pygame.display.set_mode((screen_width,screen_height))

# Creating a player,prize and enemies
player_big = pygame.image.load("player.jpg")
enemy1_big = pygame.image.load("monster.jpg")
enemy2_big = pygame.image.load("monster.jpg")
enemy3_big = pygame.image.load("monster.jpg")
prize_big = pygame.image.load("prize.jpg")

# Reducing the size of the images used for the player, enemies and prize
player = pygame.transform.scale(player_big,(30,30))
enemy1 = pygame.transform.scale(enemy1_big,(50,50))
enemy2 = pygame.transform.scale(enemy2_big,(50,50))
enemy3 = pygame.transform.scale(enemy3_big,(50,50))
prize = pygame.transform.scale(prize_big,(80,40))



# Getting the height and width of the images
player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

print("This is the height of the enemy image: " +str(enemy1_height))
print("This is the width of the enemy image: " +str(enemy1_width))

print("This is the height of the prize image: " +str(prize_height))
print("This is the width of the prize image: " +str(prize_width))

# Storing the position of the player as variables

playerXPosition = 100
playerYPosition = 50

# Making the enemy and prize start off screen and at a random y position.

enemy1_XPosition =  screen_width
enemy1_YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2_XPosition =  screen_width
enemy2_YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3_XPosition =  screen_width
enemy3_YPosition =  random.randint(0, screen_height - enemy3_height)

prize_XPosition =  screen_width
prize_YPosition =  random.randint(0, screen_height - prize_height)


# This checks if the up, down, left or right key is pressed.
# Right now they are not so make them equal to the boolean value of False.

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play.

while 1:

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the position specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1_XPosition, enemy1_YPosition))
    screen.blit(enemy2, (enemy2_XPosition, enemy2_YPosition))
    screen.blit(enemy3, (enemy3_XPosition, enemy3_YPosition))
    screen.blit(prize, (prize_XPosition, prize_YPosition))

    pygame.display.flip()# This updates the screen.

    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False


    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1


    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemy and prize:
    
    enemy1_Box = pygame.Rect(enemy1.get_rect())
    enemy1_Box.top = enemy1_YPosition
    enemy1_Box.left = enemy1_XPosition

    enemy2_Box = pygame.Rect(enemy2.get_rect())
    enemy2_Box.top = enemy2_YPosition
    enemy2_Box.left = enemy2_XPosition

    enemy3_Box = pygame.Rect(enemy3.get_rect())
    enemy3_Box.top = enemy3_YPosition
    enemy3_Box.left = enemy3_XPosition

    prize_Box = pygame.Rect(prize.get_rect())
    prize_Box.top = prize_YPosition
    prize_Box.left = prize_XPosition

    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1_Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2_Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3_Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prize_Box):
    
        # Display winning status to the user: 
        
        print("You win!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    # If the prize is off the screen the user loses the game:
    
    if prize_XPosition < 0 - prize_width:
    
        # Display wining status to the user: 
        
        print("You didn't get the prize, you lose!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)    


    # Make enemy and prize approach the player.
    
    enemy1_XPosition -= 0.15
    enemy2_XPosition -= 0.15
    enemy3_XPosition -= 0.15
    prize_XPosition -= 0.15
    
    # ================The game loop logic ends here. =============    



        
            


                





