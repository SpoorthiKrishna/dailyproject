# # import turtle as tim 


# # # on_screen=Turtle()
# # # on_screen.shape("turtle")
# # # on_screen.forward(100)
# # # on_screen.right(90)
# # # on_screen.forward(100)
# # # on_screen.right(90)
# # # on_screen.forward(100)
# # # on_screen.right(90)
# # # on_screen.forward(100)

# # # screen=Screen()
# # # screen.exitonclick
# # # h=Turtle()
# # # h.color('red')
# # # for _ in range(1,10):
# # #     h.forward(10)
# # #     h.penup()
# # #     h.forward(10)
# # #     h.pendown
    
# # # screen=Screen()
# # # screen.exitonclick
# # # t=Turtle()
# # # def shapes(new_size):
# # #     angle=360/new_size
# # #     for _ in range(new_size):
# # #         t.forward(100)
# # #         t.right(angle)

# # # for size in range(3,11):
# # #     shapes(size)

# # import random
# # t=tim.Turtle()
# # tim.colormode(255)
# # def colors():
# #     r=random.randint(0,255)
# #     g=random.randint(0,255)
# #     b=random.randint(0,255)
# #     return (r,g,b)

# # # direction=[0,90,180,270]
# # t.speed("fastest")
# # def print_circle(size_gap):
# #     for _ in range(int(360/size_gap)):
# #         t.color(colors)
# #         t.circle(100)
# #         t.setheading(t.heading() + size_gap)
# # # t.pensize(15)
# # print_circle(5)

# # # for _ in range(200):
# # #     t.color(colors())
# # #     t.forward(30)
# # #     t.setheading(random.choice(direction))
# # screen=tim.Screen()
# # screen.exitonclick
# import turtle
# import random

# turtle.colormode(255)
# t = turtle.Turtle()
# t.speed("fastest")

# def colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# def print_circle(size_gap):
#     for _ in range(int(360 / size_gap)):
#         t.color(colors())
#         t.circle(100)
#         t.setheading(t.heading() + size_gap)

# print_circle(5)
# turtle.done()
# import colorgram
# rgb_colors=[]
# colors=colorgram.extract('sam.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_tuple=(r,g,b)
#     rgb_colors.append(new_tuple)

# print(rgb_colors)
import turtle as t
import random
tim=t.Turtle()

t.colormode(255)
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list=[(228, 226, 223), (243, 243, 245), (245, 234, 241), (232, 167, 61), (52, 110, 156), (211, 122, 163), (119, 148, 202), (17, 128, 95), (149, 20, 59), (4, 176, 143), (177, 45, 85), (223, 202, 119), (224, 77, 115), (160, 165, 36), (40, 164, 209), (28, 34, 83), (226, 90, 44), (119, 172, 116), (235, 242, 240), (215, 63, 34), (124, 107, 161), (80, 20, 45), (41, 54, 98), (17, 96, 70), (225, 172, 190), (158, 212, 200), (30, 62, 56), (11, 88, 104), (227, 174, 168), (182, 188, 208)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num=100
for inter in range(1,num+1):
        
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if inter %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen=t.Screen()
screen.exitonclick