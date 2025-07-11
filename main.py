from turtle import Screen, Turtle

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("snake gaym")

seg1 = Turtle("square")
seg1.color("white")

seg2 = Turtle("square")
seg2.color("white")
seg2.goto(-20,0)

seg3 = Turtle("square")
seg3.color("white")
seg3.goto(-40,0)









window.exitonclick()