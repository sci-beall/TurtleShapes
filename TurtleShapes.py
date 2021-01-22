import turtle as tr

#############################################################
# IDEAS:
# control number of sides
# control size
# control location
# control color
# control border color
# control boarder thinkness
# FUNCTIONS:
# user_interface, draw, get_sides, get_size, get_location, get_color, get_b_color, get thickness
# turtle screen inside extra tkinter screen? Part of user_interface?
#############################################################



def draw(sides, x, y, size, fill, border, thickness):
    '''Set to draw the shape given based on a number of sides.'''

    tr.penup()
    tr.goto(x,y)
    tr.pendown()

    if sides < 2:
        tr.forward(size)
    elif sides == 2:
        tr.left(90)
        tr.forward(size/2)
        tr.right(90)
        tr.forward(size/2)
    elif sides == 3:
        tr.penup()
        tr.goto(x-size/2, y-size/2)
        tr.pendown()
        tr.left(60)
        tr.color(border, fill)
        tr.begin_fill()
        for _ in range(3):
            tr.forward(size)
            tr.right(120)
        tr.end_fill()
    
    tr.mainloop()


def user_interface():
    '''Get information from a user'''
    n_sides = 3
    size = 100
    location = (0,0)
    color = 'black'
    b_color = 'black'
    thickness = 1

    draw(n_sides, location[0], location[1], size, color, b_color, thickness)


if __name__ == "__main__":
    user_interface()