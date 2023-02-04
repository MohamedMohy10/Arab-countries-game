from turtle import Turtle

ALIGN = "center"
FONT = ('arial', 10, 'normal')


class TextOnMap(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")

    def write_name(self, name, x_position, y_position):
        self.goto(int(x_position), int(y_position))
        self.write(arg=name, align=ALIGN, font=FONT)
