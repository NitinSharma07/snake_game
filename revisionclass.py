from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.creation()
        self.head = self.all_turtles[0]

    def creation(self):
        for position in positions:
            tim = Turtle('square')
            tim.color('white')
            tim.penup()
            tim.goto(position)
            self.all_turtles.append(tim)

    def move(self):
        for tur_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[tur_num - 1].xcor()
            new_y = self.all_turtles[tur_num - 1].ycor()
            self.all_turtles[tur_num].goto(new_x, new_y)
        self.all_turtles[0].forward(20)

    def up(self):
        if self.all_turtles[0].heading() != 270:
            self.all_turtles[0].setheading(90)

    def down(self):
        if self.all_turtles[0].heading() != 90:
            self.all_turtles[0].setheading(270)

    def right(self):
        if self.all_turtles[0].heading() != 180:
            self.all_turtles[0].setheading(0)

    def left(self):
        if self.all_turtles[0].heading() != 0:
            self.all_turtles[0].setheading(180)



