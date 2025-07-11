from turtle import *

speed(10)
#we want to paint a house

#step1:make a square
width(7)
color("blue")
begin_fill()







forward(200)



left(90)     
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
end_fill()
#end of square
#drawing a door
begin_fill()

left(90)


forward(70)
color("yellow")




left(90)


forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#drawing the roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
begin_fill()
color("green")
penup()
goto(10,140)
pendown()
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#მეორე ფანჯარა
begin_fill()
color("green")
penup()
goto(190,140)
pendown()

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
    











    
exitonclick()