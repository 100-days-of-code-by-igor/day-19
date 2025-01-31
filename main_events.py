from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="space", fun=clear)
screen.exitonclick()