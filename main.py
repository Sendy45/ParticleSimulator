import sys
import random
import pygame
from Particle import Particle

# Particle forces - attraction or repelling forces
def rule(particles1, particles2, g, screen):
    for p1 in particles1:
        fx = 0
        fy = 0
        for p2 in particles2:
            # distance between particles
            dx = p1.position[0] - p2.position[0]
            dy = p1.position[1] - p2.position[1]
            d = (dx * dx + dy * dy) ** 0.5
            if 0 < d < 80: # disregarding small forces
                F = g * (1/d) # non accurate force calculation
                # per axis force
                fx += F * dx
                fy += F * dy

        # Update velocities per axis and position
        # cut velocity by half - smoother animation
        p1.velocity[0] = (p1.velocity[0] + fx) * 0.5
        p1.velocity[1] = (p1.velocity[1] + fy) * 0.5
        p1.position[0] += p1.velocity[0]
        p1.position[1] += p1.velocity[1]

        # Handle wall collision
        p1.wall_collision(screen)

# Main  simulation function
def run_simulation():
    # Initialization
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True

    # Particle groups - sizes and colors
    reds = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "red")
        for _ in range(200)
    ]
    blues = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "blue")
        for _ in range(200)
    ]
    greens = [
        Particle([random.randint(0, 800), random.randint(0, 600)], "green")
        for _ in range(200)
    ]

    particles = reds + blues + greens

    while running:
        # Exist handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        # Set of rules - changeable
        rule(greens, greens, -0.32, screen)
        rule(greens, reds, -0.17, screen)
        rule(greens, blues, 0.34, screen)

        rule(reds, reds, -0.10, screen)
        rule(reds, greens, -0.34, screen)

        rule(blues, blues, 0.15, screen)
        rule(blues, greens, -0.20, screen)

        # Draw particles
        for particle in particles:
            particle.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    run_simulation()