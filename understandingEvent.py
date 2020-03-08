# Import a library of functions called 'pygame'
import pygame,sys
from pygame.locals import *
# Initialize the game engine
pygame.init()
pygame.key.set_repeat(1000,100)
clock = pygame.time.Clock()
# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [800, 300]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)
pygame.display.set_caption('understanding about event')

# print text function
def printText(msg, color='BLACK', pos=(0, 50)):
    textSurface = font.render(msg, True, pygame.Color(color))
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

def main():
    # Loop until the user clicks the close button.
    flag = None

    while True:

        # Main Event Loop
        a = pygame.event.get()
        for event in a:  # User did something
            if event.type == pygame.KEYDOWN:  # If user release what he pressed.
                pressed = pygame.key.get_pressed()#get the list of the state of pushed key buttons
                buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                flag = True
            elif event.type == pygame.KEYUP:  # If user press any key.
                pressed = pygame.key.get_pressed()
                buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v]
                flag = False
            elif event.type == pygame.QUIT:  # If user clicked close.
                pygame.quit()
                sys.exit()



        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Print red text if user pressed any key.
        if flag == True:
            b = ''
            keyCode = ''
            for i in range(len(buttons)):
                b +=buttons[i]+','
            for key in range(len(pressed)):
                if pressed[key]:
                    keyCode += str(key)+','
            printText('you just key down!!', 'BLUE', (0, 70))
            printText('ASCII code of the pressed key : ' + b, 'RED', (0, 90))
            printText('# of the pressed key : ' + str(len(buttons)), 'RED', (0, 110))
            printText('length of the list of the state of the pushed key buttons : ' \
                      + str(len(pressed)), 'RED', (0, 130))
            printText('length of event : ' + str(len(a)), 'RED', (0, 150))
            printText('Pressed KeyCode : ' + keyCode, 'RED', (0, 170))
            printText('event.type Code : ' + str(event.type), 'RED', (0, 190))
            printText('event.key Code : ' + str(event.key), 'RED', (0, 210))
        # Print blue text if user released any key.
        elif flag == False:
            printText('you just key up!!', 'BLUE')
            printText('--> released what you pressed.', 'BLUE', (0, 70))
            printText('# of Pressed Key : ' + str(len(buttons)), 'RED', (0, 110))
            printText('length of Pressed : ' + str(len(pressed)), 'RED', (0, 130))
            printText('length of event : ' + str(len(a)), 'RED', (0, 150))
            printText('event.type Code : ' + str(event.type), 'RED', (0, 170))
            printText('event.key Code : ' + str(event.key), 'RED', (0, 190))

        # Print default text if user do nothing.
        else:
            printText('Please press any key.')
            printText('length of event : ' + str(len(a)), 'RED', (0, 150))
            printText('event typeCode : ' + str(event.type), 'RED', (0, 170))

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

if __name__=='__main__':
    main()





