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
    if a > 4:
        maze_painter.left(90)
        maze_painter.fd(10)
        maze_painter.pu()
        maze_painter.fd(width*2)
        maze_painter.pd()
        maze_painter.fd(40)
        maze_painter.left(90)
        maze_painter.forward(width*2)
        maze_painter.bk(width*2)
        maze_painter.right(90)
        maze_painter.forward(a*width - 10)





wn = trtl.Screen()

wn.mainloop()