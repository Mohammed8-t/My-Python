from turtle import*
shape("turtle")

penup()
goto(-300, 0)
pendown()

var1 = var2 = var3 = 1

begin_fill()
color("black", "blue")
while(var1 <= 2):
	forward(520)
	left(90)
	forward(400)
	left(90)
	var1 += 1
end_fill()

penup()
goto(-230, 50)
left(90)
pendown()

begin_fill()
color("black", "white")
while(var2 <= 2):
	forward(300)
	right(90)
	forward(50)
	right(90)
	var2 += 1
end_fill()


penup()
goto(-60, 50)
pendown()

begin_fill()
color("black", "white")
forward(200)
left(45)
forward(150)
right(135)
forward(60)
right(45)
forward(80)
left(45)
forward(20)
left(45)
forward(80)
right(45)
forward(60)
right(135)
forward(150)
left(45)
forward(200)
right(90)
forward(50)
end_fill()

penup()
goto(150, 50)
right(90)
pendown()

begin_fill()
color("black", "white")
while(var3 <= 2):
	forward(300)
	left(90)
	forward(50)
	left(90)
	var3 += 1
end_fill()

hideturtle()
exitonclick()