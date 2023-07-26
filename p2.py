from turtle import *

# color('red')
# width(13)
# forward(120)
# left(60)
# forward(120)
# left(60)
# forward(120)
# left(60)
# forward(120)
# left(60)
# forward(120)
# left(60)
# forward(120)

# color('blue')

# right(60)
# backward(120)
# right(60)
# forward(120)
# right(120)
# forward(120)
# left(60)
# backward(120)

# right(60)
# forward(120)
# left(60)
# backward(120)
# right(120)
# backward(120)
# right(60)
# forward(120)
# down()

# home()


# pos()
# color('blue')
# clearscreen()

for steps in range(100):
    for c in ('blue','red','green'):
        color(c)
        forward(steps)
        right(30)
        color('red')
        fillcolor('yellow')


# for star in range(20):
#     for c in ('blue','green','red'):
#         circle(star)
#         color(c)

# Turtle.forward(25)

hideturtle()
mainloop()