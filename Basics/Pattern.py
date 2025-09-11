import turtle
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
colors = ["white", "grey", "olive", "white", "grey", "olive"]
for i in range(150):
    pen.color(colors[i % 6])
    for _ in range(6):
        pen.forward(100)
        pen.left(60)
    pen.left(10)

screen.mainloop()