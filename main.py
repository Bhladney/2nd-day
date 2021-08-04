import sys, pygame, time
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()


size = (width,height) = (screen_info.current_w, screen_info.current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (60,0,255)

shark = pygame.image.load('images/Shark.png')
shark = pygame.transform.smoothscale(shark, (40,40))
fish_rect = shark.get_rect()
fish_rect.center = (width // 2, height// 2)

speed_x = 0
speed_y = 0
moving = False

def move(x,y):
  global speed_x, speed_y
  speed_x += x
  speed_y += y
  fish_rect.move_ip(speed_x, speed_y)

def reset():
  global speed_x, speed_y
  speed_x = 0
  speed_y = 0


def main():
  global moving
  while True:
    clock.tick(60)
    screen.fill(color)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_w:
          move(0,-5)
          reset()
        if event.key == K_s:
          move(0,5)
          reset()
        if event.key == K_d:
          move(5,0)
          reset()
        if event.key == K_a:
          move(-5,0)
          reset()
    screen.blit(shark, fish_rect)
    pygame.display.flip()

if __name__ == '__main__':
   main()
