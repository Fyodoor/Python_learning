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
    def __init__(self, display , walls):
        super().__init__(display)
        
        # self.left_wall , self.right_wall , self.top_wall , self.bottom_wall = None
        for wall in walls:
            if wall.name == 'top': self.top_wall = wall
            elif wall.name == 'left' : self.left_wall = wall
            elif wall.name == 'bottom' :self.bottom_wall = wall
            elif wall.name == 'right' : self.right_wall = wall
            else: print('unknow wall')

        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)        

class BillyardBall(RandomPointMovableBall):
    def __init__(self, display , walls):
        super().__init__(display ,walls)
        self.color = pygame.Color("green")
        self.walls = walls
    
    def go(self):
        super().go()
        
        
        

        width, height = self.display.get_size()
        if self.center_x <= self.radius or self.center_x >= width - self.radius:
            if self.center_x <= self.radius:
                self.left_wall.interceptCollision(self.center_x)
            else:
                self.right_wall.interceptCollision(self.center_x)

            self.vx = -self.vx

        if self.center_y <= self.radius or self.center_y >= height - self.radius:
            if self.center_y <= self.radius:
                self.top_wall.interceptCollision(self.center_y)
            else:
                self.bottom_wall.interceptCollision(self.center_y)

            self.vy = -self.vy


class CollisionTracker:
    def __init__(self , threshold , condition):
        self.threshold = threshold
        self.condition = condition
        self.collision_count = 0

    def interceptCollision(self , coords):
        if self.condition(coords , self.threshold):
            self.collision_count += 1

# region
        # for _ , tuple in enumerate(thresholds):
        #     self.collision_count.append((tuple[0] , tuple[1] , 0))
   

    # def interceptCollision(self , coords , name):

    #     for index , tuple in enumerate(self.collision_count):
    #         if tuple[0] == name:
    #             print(coords , ' treshold - ' , tuple[1])
    #             if name == 'top' or name == 'right':
    #                 if coords > tuple[1] :
    #                     self.collision_count[index] = (tuple[0] , tuple[1] , tuple[2] + 1)
    #                     print( tuple[0] ,  'COLLAPSED')
    #             elif coords < tuple[1]:
    #                     self.collision_count[index] = (tuple[0] , tuple[1] , tuple[2] + 1)
    #                     print( tuple[0] ,  'COLLAPSED')
               
        #   region  

       

class Wall(CollisionTracker):
    def __init__(self , threshold , condition , font ,  display , name ,   xMarker , yMarker):
        super().__init__(threshold , condition)
        self.xMarker = xMarker ; self.yMarker = yMarker
        self.display = display
        self.font = font
        self.name = name
        
       
        
    def draw(self):
        pygame.draw.rect(self.display , (255,255,255) , (self.xMarker,self.yMarker , 100 ,50))
        textsurface = self.font.render(str(self.collision_count), False, (0, 0, 0))
        self.display.blit(textsurface,(self.xMarker,self.yMarker))
 
    



    

pygame.init()

width = 700
height = 400
display = pygame.display.set_mode((width, height))
temp_ball = Ball(display)
display.fill(pygame.Color("white")) # or display.fill((255,255,255))
isLess = lambda a , b : a <= b
isMore = lambda a , b : a >= b
walls = [
      ( height - height + 100 , isLess , 350 , 0 , 'top') ,
      ( width  - temp_ball.center_x , isMore   , 650 , 200 , 'right') ,
      ( height -  10 , isLess , 350 , 350 , 'bottom') ,
      ( width - width + temp_ball.center_x  / 4  , isMore , 0 , 200 , 'left')
      ]

balls= []

pygame.font.init() 
game_font = pygame.font.SysFont('Comic Sans MS', 30)

for i , tuple in enumerate(walls):
    wall = Wall(tuple[0] , tuple[1] , game_font , display , tuple[4] , tuple[2] , tuple[3] )
    wall.draw()
    walls[i] = wall

for i in range(6):
    ball = RandomPointMovableBall(display , walls)
    ball.show()
    balls.append(ball)

    ball = BillyardBall(display , walls)
    ball.show()
    balls.append(ball)
    
    

pygame.display.flip()

time.sleep(2)

clock = pygame.time.Clock()
while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                ball.stop()

    for wall in walls:
        wall.draw()

    
    for ball in balls:
        ball.move()
    
    pygame.display.flip()
    clock.tick(80)