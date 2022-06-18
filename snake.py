from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle('square')
        tim.penup()
        tim.color('white')
        tim.goto(position)
        self.all_turtles.append(tim)

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def move(self):
        for tur_num in range(len(self.all_turtles) - 1, 0,
                             -1):  # here we did not take range(2,-1) but (2,0) because 2nd and 3rd have to move to
            # 0th position if we would put range (2,-1) then in the below code, turtle num in  new_x and new_y will
            # become -1 and there is nothing on -1 in the list and it will show up the error.
            new_x = self.all_turtles[tur_num - 1].xcor()
            new_y = self.all_turtles[tur_num - 1].ycor()
            self.all_turtles[tur_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
