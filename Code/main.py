import sys

import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WIDTH = 800
HEIGHT = 600

# Create the windowimport sys

screenInfo = pygame.display.Info()


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

    def moveTowardsGrapple(self):
        # Move stick figure towards grappling hook

        self.pos[0] += (self.grapplePos[0] - self.pos[0]) * 0.1

        self.pos[1] += (self.grapplePos[1] - self.pos[1]) * 0.07

        # Check if stick figure has reached grappling hook
        if abs(self.pos[0] - self.grapplePos[0]) < 50 and abs(self.pos[1] - self.grapplePos[1]) < 50:
            self.grappleAttached = False

    def setGrapplePos(self, pos):
        self.grapplePos[0] = pos[0]
        self.grapplePos[1] = pos[1]
        self.grappleAttached = True

    def drawGrapple(self, screen, mousePos):
        # Draw grappling hook

        XOFfset = 8
        YOffset = 60
        if not self.grappleAttached:
            pygame.draw.line(screen, (0, 0, 0), (self.pos[0] + XOFfset, self.pos[1] + YOffset),
                             (mousePos[0], mousePos[1]), 2)

        else:
            pygame.draw.line(screen, (0, 0, 0), (self.pos[0] + XOFfset, self.pos[1] + YOffset),
                             (self.grapplePos[0], self.grapplePos[1]),
                             2)

    def drawChar(self, screen):
        # Draw stick figure
        screen.blit(self.image, (self.pos[0], self.pos[1]))

    def collideWithPlatform(self, platform):
        if self.pos[1] + self.height < platform.rect.top:
            return False
        if self.pos[1] > platform.rect.bottom:
            return False
        if self.pos[0] + self.width < platform.rect.left:
            return False
        if self.pos[0] > platform.rect.right:
            return False
        return True

    def main(self, screen, platform):
        mousePos = pygame.mouse.get_pos()
        if self.grappleAttached:
            self.moveTowardsGrapple()

        else:
            # Check if mouse is clicked
            if pygame.mouse.get_pressed()[0]:
                self.setGrapplePos(mousePos)
            if (self.pos[0] > screenInfo.current_w):
                self.pos[0] = screenInfo.current_w
            elif (self.pos[0] < 0):
                self.pos[0] = 0
            if (self.pos[1] < 0):
                self.pos[1] = 0
            elif (self.pos[1] > screenInfo.current_h - 100):
                self.pos[1] = screenInfo.current_h - 100
            for platform in platforms:
                if self.collideWithPlatform(platform):
                    player.pos[1] = platform.rect.top - player.height

            # Apply gravity
            self.pos[1] += 5

        # Clear screen

        self.drawChar(screen)

        self.drawGrapple(screen, mousePos)

        #


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
        BLUE = (255, 125, 0)

        pygame.draw.rect(self.screen, BLUE, pygame.Rect(100, 100, 60, 60))

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


class Platform:
    def __init__(self, color, size, solid):
        self.rect = pygame.Rect(size)
        self.color = color
        self.solid = solid
        self.surface = window.screen

    def drawRect(self):
        pygame.draw.rect(self.surface, self.color, self.rect, self.solid)


window = Window(screenInfo.current_w, screenInfo.current_h)
player = Player("octopus_sprite.png", pygame.Vector2(100, 100), pygame.Vector2(15.0, 10.0), 2, 2)

platform1 = Platform((65, 85, 210), (100, 400, 800, 300), 0)
platform2 = Platform((128, 10, 155), (screenInfo.current_w - 900, screenInfo.current_h - 100, 600, 60), 3)

platforms = [platform1, platform2]
player.main(window.screen, platforms)


def game():
    window.screen.fill((255, 255, 255))
    player.main(window.screen, platforms)
    for platform in platforms:
        platform.drawRect()
    window.runClock()


window.run(game)
pygame.quit()
