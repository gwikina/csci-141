import turtle, math, random 
pond = 500
MAX_RAINDROPS = 100
def drawPond():
    """
    sets up the pond in and then goes to the middle
    """
    turtle.setup(1000, 1000)
    turtle.setworldcoordinates(-400, -400, 400,400)
    turtle.up()
    turtle.back(200)
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.down()
    turtle.color('light blue')
    turtle.begin_fill()
    turtle.forward(pond)
    turtle.right(90)
    turtle.forward(pond)
    turtle.right(90)
    turtle.forward(pond)
    turtle.right(90)
    turtle.forward(pond)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(50, 50)
    turtle.down()
def drawDrop(rad):
    """
    Draws a raindrop by drawing a circle

    Fills in circle with a random rgb value

    Returns the circumference of the circle
    
    """
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    turtle.color(r,g,b)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
    return(math.pi*(r**2))
def drawRec(c,r):
    """
    Draws a circle with an increasing radius recursively

    Returns the circumference of all the circles 
    """
    if c < 1:
        return 0
    elif c ==1:
        turtle.circle(r)
    else:
        turtle.color('black')
        turtle.circle(r+1)
    return((math.pi*(r**2)) + drawRec(c-1, r+10))
def drawIter(n,r):
    """
    Draws a circle with an increasing radius iteratively

    Picks penup and moves it by distance of the radius

    returns circumference 
    """
    orig_r = r
    c = (math.pi*r*2)
    drawDrop(r)
    while n > 0:
        turtle.color('black')
        turtle.circle(r)
        turtle.up()
        turtle.right(90)
        turtle.forward(orig_r)
        turtle.left(90)
        turtle.down()
        r = orig_r + r
        n = n-1
    return c
def numOfDrops(number, n, r):
    """
    Gives a random position for the x and y (based on initialization)

    draws the iterative rain drop function base case is reached

    else it will continue to call itself while drawing another iterative raindrop 
    """
    c = 0
    x = random.randint(-(pond/2) + r + 200, (pond/2) - r-100)
    y = random.randint(-(pond/2) + r + 150 , (pond/2) - r - 200)
    if number == 1:
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        c = c + drawIter(n,r)
        return c
    elif number > 1:
        n = random.randint(3,8)
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        drawIter(n,r)
        return 2 * math.pi* r + numOfDrops(number-1, n, r)
def main():
    """
    Asks for a number of raindrops

    randomly selects a number of ripples

    calls function

    color mode is needed as the color was stuck on 1 which produces bad color combinations

    Iniatilizes the setting 
    """
    rainDrops = int(input('How many raindrops do you wish to  draw? '))
    if rainDrops > MAX_RAINDROPS:
        print('Too large, try agin')
        main()
    turtle.colormode(255)
    drawPond()
    print(numOfDrops(rainDrops,random.randint(3,8), 10))
main()
