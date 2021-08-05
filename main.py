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
  global speed_x, speed_y, moving
  speed_x += x
  speed_y += y
  fish_rect.move_ip(speed_x, speed_y)

def reset():
  global speed_x, speed_y
  speed_x = 0
  speed_y = 0


def main():
  global moving, speed_x, speed_y
  x = 0
  y = 0
  while True:
    clock.tick(30)
    screen.fill(color)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_w:
          x = 0
          y = -1
          moving = True
        if event.key == K_s:
          x = 0
          y = 1
          moving = True
        if event.key == K_d:
          x = 1
          y = 0
          moving = True
        if event.key == K_a:
          x = -1
          y = 0
          moving = True
      elif event.type == KEYUP:
        if event.key == K_w:
          reset()
          moving = False
        if event.key == K_s:
          reset()
          moving = False
        if event.key == K_d:
          reset()
          moving = False
        if event.key == K_a:
          reset()
          moving = False
    if moving:
      print(speed_x)
      move(x, y)
    screen.blit(shark, fish_rect)
    pygame.display.flip()

if __name__ == '__main__':
   main()