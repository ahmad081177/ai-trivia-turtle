import turtle


# Function to display score on the screen
def draw_heart():
    turtle.setheading(0)  # Reset heading to default (right)

    turtle.penup()
    turtle.goto(0, -130)
    turtle.pendown()
    
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(100)
    turtle.circle(-50, 200)
    turtle.left(120)
    turtle.circle(-50, 200)
    turtle.forward(100)
    turtle.end_fill()

def draw_sad_face(y=-30):
    turtle.setheading(0)  # Reset heading to default (right)

    turtle.speed(3)
    turtle.color("black")

    # Draw face outline
    turtle.penup()
    turtle.goto(0, y-50)
    turtle.pendown()
    turtle.circle(50)

    # Draw left eye
    turtle.penup()
    turtle.goto(-20, y+10)
    turtle.pendown()
    turtle.circle(5)

    # Draw right eye
    turtle.penup()
    turtle.goto(20, y+10)
    turtle.pendown()
    turtle.circle(5)

    # Draw sad mouth (downward curve)
    turtle.penup()
    turtle.goto(20, y-30)  # Start lower for a frown
    turtle.pendown()
    turtle.setheading(-220)  # Reverse the arc direction
    turtle.circle(30, 100)  # Negative arc for sad expression

    # Hide turtle and display
    turtle.hideturtle()
