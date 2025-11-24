import pygame

class Particle:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.velocity = [0, 0]
        self.radius = 5

    # Draw particle
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    # Handle wall collision - prevent out of bounds coordinates
    def wall_collision(self, screen):
        if self.position[0] < 0 or self.position[0] > screen.get_width():
            self.velocity[0] *= -1

        if self.position[1] < 0 or self.position[1] > screen.get_height():
            self.velocity[1] *= -1