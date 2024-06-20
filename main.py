from turtle import Turtle, Screen
import random

in_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color")
colors = ["blue","green","yellow","orange","red"]
turtles = []
# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230,y=-100)
y = -120
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=y)
    y += 50
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You have won! The winning color is {winning_color}")
            else:
                print(f"You have lost! The winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()