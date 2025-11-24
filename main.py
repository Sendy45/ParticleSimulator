import sys
import random

import pygame
from Particle import Particle

def rule(particles1, particles2, g):
    for p1 in particles1:
        for p2 in particles2:
            p1.force(p2, g)

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    fps = 30

    reds = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "red")
        for _ in range(100)
    ]
    yellows = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "blue")
        for _ in range(300)
    ]
    greens = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "green")
        for _ in range(300)
    ]

    particles = reds + yellows + greens

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        for particle in particles:
            particle.acceleration = [0, 0]

        screen.fill((0, 0, 0))
        dt = clock.tick(fps) / 1000

        rule(reds, reds, 1)
        rule(yellows, yellows, -0.01)
        rule(reds, yellows, -0.01)

        rule(greens, greens, -0.1)
        rule(greens, yellows, 0.01)
        rule(reds, greens, -0.01)

        for particle in particles:
            particle.move(dt, screen)
            particle.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    run_simulation()