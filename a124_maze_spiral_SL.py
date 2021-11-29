import turtle as trtl

walls = 50
width = 10
color = "red"

maze_painter = trtl.Turtle() 
maze_painter.ht()
maze_painter.pu()
maze_painter.color(color)
maze_painter.speed(0)
maze_painter.goto(0,0)




maze_painter.pd()
for a in range(walls):
    maze_painter.left(90)
    maze_painter.forward(a*width)


wn = trtl.Screen()

wn.mainloop()