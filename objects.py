import random as rnd

WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

Colors=[WHITE, RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    "фишечка"
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.live = True
        self.type="ball"

    def draw(self):
        "Рисуем шарик"
        pass

class wave:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Field:
    def __init__(self, n, w, h):
        self.n = n+1
        self.w=w
        self.h=h
        self.massive=[]
        self.score=0
        global Colors
        for i in range(n+1):
            self.massive[i]+=[Ball(i*self.w+self.w//2,self.h//2,self.h//2,BLACK)]
            for j in range(1,n+1):
                t=rnd.randint(0,7)
                if self.massive[i][j-1]==Colors[t] or self.massive[i-1][j]==Colors[t]:
                    j-=1
                    continue
                self.massive[i]+=[Ball(i*self.w+self.w//2,j*self.h+self.h//2,self.h//2,Colors[t])]

    def update(self):

        pass

    def check(self):
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if self.massive[i][j].live:
                    self.walk_the_line(i,j)
        self.update()


    def walk_the_line(self,x0,y0):
        vol=[wave(x0,y0)]
        current_color=self.massive[x0][y0].color
        current_sum=0
        go=[wave(1,0),wave(-1,0),wave(0,1),wave(0,1),]
        for v in vol:
            for g in go:
                if self.massive[v.x+g.x][v.y+g.y].color==current_color and self.massive[v.x+g.x][v.y+g.y].live:
                    vol+=wave(v.x+g.x,v.y+g.y)
                    current_sum+=1

        if current_sum>=3:
            self.score+=current_sum
            for v in vol:
                self.massive[v.x][v.y].live=False















