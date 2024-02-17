import pygame
from pygame.locals import *
import random

size = width, height = (1280, 720)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.init()
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Dauntae's first game")
screen.fill((67, 88, 69))
clock = pygame.time.Clock()
running = True

pygame.display.update()


# load images
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

# load enemy vehicle
oil = pygame.image.load("oil.png")
oil_loc = oil.get_rect()
oil_loc.center = left_lane, height * 0.2

counter = 0

# game loop
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("Level up", speed)

    oil_loc[1] += speed

    if oil_loc[1] > height:
        if random.randint(0, 1) == 0:
            oil_loc.center = right_lane, -200
        else:
            oil_loc.center = left_lane, -200

    if car_loc[0] == oil_loc[0] and oil_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])
    # road
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))

    # yellow line
    pygame.draw.rect(
        screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
    )
    # white line 1
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height),
    )
    # white line 2
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height),
    )
    screen.blit(car, car_loc)
    screen.blit(oil, oil_loc)
    pygame.display.update()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


# link for car
# <a href="https://www.flaticon.com/free-icons/car" title="car icons">Car icons created by Freepik - Flaticon</a>
# link for oil spill
# <a href="https://www.flaticon.com/free-icons/oil-spill" title="oil spill icons">Oil spill icons created by Khoirul Huda - Flaticon</a>
