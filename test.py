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
screen.fill("green")
clock = pygame.time.Clock()
running = True

pygame.display.update()


# load images
car = pygame.image.load("car2.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

# load enemy vehicle
car2 = pygame.image.load("car1.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

counter = 0

# game loop
while running:
    counter += 1
    if counter == 1024:
        speed += 0.25
        counter = 0
        print("Level up", speed)
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
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
    screen.blit(car2, car2_loc)
    pygame.display.update()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


# link for car 1
# <a href="https://www.flaticon.com/free-icons/car" title="car icons">Car icons created by Freepik - Flaticon</a>
# lik for car 2
# <a href="https://www.flaticon.com/free-icons/racing-car" title="racing car icons">Racing car icons created by Freepik - Flaticon</a>
