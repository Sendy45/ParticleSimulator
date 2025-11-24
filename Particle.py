import pygame


class Particle:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.mass = 1 #9.109 *  10**-31
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.radius = 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def move(self, dt, screen):
        self.velocity[0] += dt*self.acceleration[0]
        self.velocity[1] += dt*self.acceleration[1]

        self.position[0] += dt*self.velocity[0]
        self.position[1] += dt*self.velocity[1]

        self.wall_collision(screen)

    def wall_collision(self, screen):
        if self.position[0] < 0 or self.position[0] > screen.get_width():
            self.velocity[0] *= -1

        if self.position[1] < 0 or self.position[1] > screen.get_height():
            self.velocity[1] *= -1

    def force(self, other, G):

        dx = other.position[0] - self.position[0]
        dy = other.position[1] - self.position[1]

        dist = (dx * dx + dy * dy) ** 0.5
        if dist == 0:
            return

        F = G * self.mass * other.mass #/ dist ** 2

        ax = F * (dx / dist) / self.mass
        ay = F * (dy / dist) / self.mass

        self.acceleration[0] += ax
        self.acceleration[1] += ay

        other.acceleration[0] -= ax
        other.acceleration[1] -= ay
