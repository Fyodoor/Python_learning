import pygame
import random
import time

class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color("red")
        self.center_x = 100
        self.center_y = 100
        self.radius = 30
        self.inz = False
        
        self.vx = 2
        self.vy = 2
    
    def show(self):
        pygame.draw.circle(self.display, self.color, (self.center_x, self.center_y), self.radius)
    
    
    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy
        
    def clear(self):
        pygame.draw.circle(self.display, pygame.Color("white"), (self.center_x, self.center_y), self.radius)
        
    def move(self):
        self.clear()
        self.go()
        self.show()
    
    
    def stop(self):
        self.vx = 0
        self.vy = 0
        
    def in_zone(self, width, height):
        if self.center_x <= self.radius or self.center_x >= width - self.radius:
            return True
        if self.center_y <= self.radius or self.center_y >= height - self.radius:
            return True
        return False
          
    def outzone(self):
        if self.center_x >= self.radius or self.center_x <= width - self.radius:
            return True
        if self.center_y >= self.radius or self.center_y <= height - self.radius:
            return True
        return False        
    
class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        
        self.color = pygame.Color("blue")
        
        width, height = display.get_size()
        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)

    
class PointBall(Ball):
    def __init__(self, display, x, y):
        super().__init__(display)
        
        self.color = pygame.Color("yellow")

        self.center_x = x
        self.center_y = y
              

class RandomPointMovableBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)
        
        while True:
            self.vx = random.randint(-3, 3)
            self.vy = random.randint(-3, 3)
            if not self.vx == 0 or self.vy == 0:
                break      

class Scoreboard:
    
    def __init__(self, font, center_x, center_y):
        self.font = font
        self.xy = center_x
        self.yx = center_y
    
    def text(self,display, str):
        red = (255, 0, 0)
        yellow = (239, 228, 176)
    
        text = font.render(str, True, red, yellow)
        textRect = text.get_rect()
        textRect.center = (self.xy, self.yx)        
        display.blit(text, textRect)               
            
    
pygame.init()
pygame.display.set_caption("Catchme")
width = 700
height = 400
display = pygame.display.set_mode((width, height))
display.fill(pygame.Color("white")) # or display.fill((255,255,255))

RED = (255, 0, 0)

font = pygame.font.SysFont("arial", 24)
display_text = font.render("Шаров на экране: ", 1, RED)
score = Scoreboard(font, width//2, 25)

balls= []
for i in range(10):
    ball = RandomPointMovableBall(display)
    ball.show()
    balls.append(ball)

pygame.display.flip()


time.sleep(1)

clock = pygame.time.Clock()
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.in_zone(width, height):
                    continue
                ball.in_zone = True
                ball.stop()

    count = 0
    for ball in balls:
        if ball.in_zone == True:
            count += 1
    score.text(display, f'поймали = {count}')    
    
    for ball in balls:
        ball.move()
        
    pygame.display.flip()
    clock.tick(30)