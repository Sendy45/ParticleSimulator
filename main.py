import sys
import random
import pygame
from Particle import Particle

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    fps = 60

    N = 100  # number of particles
    particles = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "red")
        for _ in range(N)
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        dt = clock.tick(fps) / 1000

        for particle in particles:
            particle.move(dt, screen)
            others = [p for p in particles if p != particle]
            for other in others:
                particle.force(other)

        for particle in particles:
            particle.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    run_simulation()