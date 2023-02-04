from turtle import Turtle

# text style
ALIGN = "center"
FONT = ('arial', 10, 'normal')


class TextOnMap(Turtle):  # a class to create turtle objects to write on screen
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")

    def write_name(self, name, x_position, y_position):  # parameters: name, x-cor, y-cor of the country
        """ Go to the required location and write the name on screen """
        self.goto(int(x_position), int(y_position))
        self.write(arg=name, align=ALIGN, font=FONT)
