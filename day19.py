# from turtle import Turtle,Screen

# tim=Turtle()

# screen=Screen()


# def new_forwards():
#     tim.forward(10)


# def new_backwards():

#     tim.backward(10)

# def left():
#     new_heading=tim.heading() +10
#     tim.setheading(new_heading)

# def right():
#     new_heading=tim.heading() -10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(new_forwards,"s")
# screen.onkey(new_backwards,"b")
# screen.onkey(left,"l")
# screen.onkey(right,"r")
# screen.onkey(clear,"c")
# screen.exitonclick()

from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
set=False
user_bet=screen.textinput(title='Make your bet',prompt='bet the color of turtle :')
colors=['red','green','blue','orange','purple','yellow']
y_coordinate=[-70,-40,-10,20,50,80]
all_tim=[]
for index in range(0,6):
    tim=Turtle(shape='turtle')
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230,y=y_coordinate[index])
    all_tim.append(tim)

if user_bet:
    set=True

while set:
    for turtle in all_tim:
        if turtle.xcor() > 230:
            set=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won!, the {winning_color} turtle is won ")
            else:
                print(f"you loss!, the {winning_color} turtle is won ")

        speed=random.randrange(1,10)
        turtle.forward(speed)
    


screen.exitonclick()
