import sys

import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WIDTH = 800
HEIGHT = 600

# Create the windowimport sys

import pygame


class Player:
    def __init__(self, image_path, dim: pygame.Vector2, pos: pygame.Vector2, grappleSpeed, playerSpeed):
        self.image = pygame.transform.scale(pygame.image.load(image_path), dim)
        self.width = dim[0]
        self.height = dim[1]
        self.pos = pos
        self.vel = pygame.Vector2(0, 0)
        self.playerSpeed = playerSpeed
        self.grappleSpeed = grappleSpeed
        self.grappleAttached = False
        self.grapplePos = [float, float]
        self.grappleTarget = None


    def draw(self, screen):
        self.drawCharacter(screen)

    def drawCharacter(self, screen):
        screen.blit(self.image, (self.pos[0], self.pos[1]))

    def grapple(self, screen):
        mousePos = pygame.mouse.get_pos()
        if self.grappleAttached:

            # Move stick figure towards grappling hook

            self.pos[0] += (self.grapplePos[0] - self.pos[0]) * 0.1

            self.pos[1] += (self.grapplePos[1] - self.pos[1]) * 0.1

            # Check if stick figure has reached grappling hook
            if abs(self.pos[0] - self.grapplePos[0]) < 50 and abs(self.pos[1] - self.grapplePos[1]) < 50:
                self.grappleAttached = False
        else:
            # Check if mouse is clicked
            if pygame.mouse.get_pressed()[0]:
                self.grapplePos[0] = mousePos[0]
                self.grapplePos[1] = mousePos[1]
                self.grappleAttached = True

            # Apply gravity
            # self.pos[1] += 10

        # Clear screen
        screen.fill((255, 255, 255))

        # Draw stick figure
        screen.blit(self.image, (self.pos[0], self.pos[1]))

        # Draw grappling hook
        if not self.grappleAttached:
            pygame.draw.line(screen, (0, 0, 0), (self.pos[0], self.pos[1]), (mousePos[0], mousePos[1]), 2)

        else:
            pygame.draw.line(screen, (0, 0, 0), (self.pos[0], self.pos[1]), (self.grapplePos[0], self.grapplePos[1]),
                             2)

        # Update display
        pygame.display.update()


class Window:
    def __init__(self, width, height):
        # Initialize Pygame
        pygame.init()
        self.width = width
        self.height = height
        self.running = True;
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.screen.fill((255, 255, 255))

    def run(self, loop):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()
            loop()

    def runClock(self):
        # Set clock
        self.clock.tick(60)

        # Update Display
        pygame.display.update()


window = Window(0, 0)
player = Player("octopus_sprite.png", pygame.Vector2(100, 100), pygame.Vector2(15.0, 10.0), 2, 2)
player.draw(window.screen)


def game():
    player.grapple(window.screen)
    window.runClock()


window.run(game)
pygame.quit()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Load stick figure sprite
    stick_figure = pygame.image.load("octopus_sprite.png")
    stick_figure = pygame.transform.scale(stick_figure, (100, 100))

    # Set stick figure starting position
    stick_figure_x = WIDTH // 2
    stick_figure_y = HEIGHT // 2

    # Set grappling hook starting position
    grappling_hook_x = stick_figure_x-100
    grappling_hook_y = stick_figure_y - 1000
    grappling_hook_attached = False

    # Create a list of platforms
    # Define a list to store platforms
    platforms = []

    # Add platforms to the list
    platforms.append((0, HEIGHT - 40, WIDTH, 40))
    platforms.append((WIDTH // 4, HEIGHT // 2, WIDTH // 2, 20))
    platforms.append((WIDTH // 2, HEIGHT * 3 // 4, WIDTH // 4, 20))

    # Define clock for setting game speed
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if grappling_hook_attached:
            # Move stick figure towards grappling hook
            stick_figure_x += (grappling_hook_x - stick_figure_x) * 0.1
            stick_figure_y += (grappling_hook_y - stick_figure_y) * 0.1

            # Check if stick figure has reached grappling hook
            if abs(stick_figure_x - grappling_hook_x) < 5 and abs(stick_figure_y - grappling_hook_y) < 5:
                grappling_hook_attached = False
        else:
            # Check if mouse is clicked
            if pygame.mouse.get_pressed()[0]:
                grappling_hook_x = mouse_x
                grappling_hook_y = mouse_y
                grappling_hook_attached = True

            # Apply gravity
            stick_figure_y += 4

            # Check for collisions with platforms
            for platform in platforms:
                if stick_figure_y + stick_figure.get_height() > platform[1] and stick_figure_y + stick_figure.get_height() < \
                        platform[1] + platform[3]:
                    if stick_figure_x > platform[0] and stick_figure_x < platform[0] + platform[2]:
                        stick_figure_y = platform[1] - stick_figure.get_height()
                        break

        # Clear screen
        screen.fill((255, 255, 255))

        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(screen, (0, 0, 0), platform)

        # Draw stick figure
        screen.blit(stick_figure, (stick_figure_x, stick_figure_y))

        # Draw grappling hook
        if not grappling_hook_attached:
            pygame.draw.line(screen, (0, 0, 0), (stick_figure_x, stick_figure_y), (mouse_x, mouse_y), 2)
        else:
            pygame.draw.line(screen, (0, 0, 0), (stick_figure_x, stick_figure_y), (grappling_hook_x, grappling_hook_y), 2)

        # Update display
        pygame.display.update()

        # Set clock
        clock.tick(60)

        #Update Display
        pygame.display.update()

        # set clock
        clock.tick(60)

    pygame.quit()



