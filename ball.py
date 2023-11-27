import turtle

class Ball:
    def __init__(self, size, x, y, vx, vy, color):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def draw(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()
    
    def move(self):
        self.x += self.vx
        self.y += self.vy

        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]

        if abs(self.x + self.vx) > (canvas_width - self.size):
            self.vx = -self.vx

        if abs(self.y + self.vy) > ( canvas_height- self.size):
            self.vy = -self.vy            
