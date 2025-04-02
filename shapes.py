import turtle

def create_clickable_button(text, x, y, callback):
    """Creates a clickable button turtle.

    Args:
        text: The text to display on the button.
        x: The center x-coordinate of the button.
        y: The center y-coordinate of the button.
        callback: The function to call on click. This function MUST accept
                  two arguments (x_coord, y_coord), even if it ignores them.
    """
    button_turtle = turtle.Turtle()
    button_turtle.hideturtle()
    button_turtle.speed(0)
    button_turtle.penup()

    # Simple rectangular button example
    button_width = 150
    button_height = 40
    # Position turtle at the bottom-left corner for drawing the rectangle
    button_turtle.goto(x - button_width / 2, y - button_height / 2)
    button_turtle.fillcolor("lightgrey")
    button_turtle.pencolor("black") # Add border color
    button_turtle.pensize(1)      # Add border thickness
    button_turtle.begin_fill()
    button_turtle.pendown()
    for _ in range(2):
        button_turtle.forward(button_width)
        button_turtle.left(90)
        button_turtle.forward(button_height)
        button_turtle.left(90)
    button_turtle.end_fill()
    button_turtle.penup()

    # Write text on the button
    # Go to a position slightly adjusted for vertical centering of text
    button_turtle.goto(x, y - button_height / 4 - 4) # Adjust Y for text baseline
    button_turtle.pencolor("black")
    button_turtle.write(text, align="center", font=("Arial", 12, "normal"))

    # --- Click Handling ---
    # Move the turtle back to the button center to define the clickable area
    button_turtle.goto(x, y)
    # Use an existing shape like 'square' and resize it to cover the button area
    # This invisible shape will capture the click
    button_turtle.shape("square")
    # stretch_wid is N/S stretch, stretch_len is E/W stretch (based on default heading 0)
    button_turtle.shapesize(stretch_wid=button_height / 20, stretch_len=button_width / 20)
    # Make the shape invisible but clickable
    button_turtle.color("") # No color or outline for the clickable shape itself
    # Alternatively, make it semi-transparent for debugging:
    # button_turtle.color("red")
    # button_turtle.fillcolor("")
    button_turtle.showturtle() # Show the (invisible) clickable shape

    # --- Directly assign the prepared callback ---
    # The 'callback' passed to this function MUST accept (x, y)
    button_turtle.onclick(callback)

    return button_turtle # Return the turtle that handles the click


def draw_heart(heart_turtle, x, y):
    """Draws a heart using the provided turtle instance."""
    heart_turtle.clear() # Clear previous drawing by this turtle
    heart_turtle.hideturtle()
    heart_turtle.speed(0) # Fastest speed
    heart_turtle.penup()
    heart_turtle.goto(x, y) # Use the provided y coordinate
    heart_turtle.pendown()
    heart_turtle.setheading(0)

    heart_turtle.color("red")
    heart_turtle.begin_fill()
    heart_turtle.left(140)
    heart_turtle.forward(112) # Size of heart sides
    heart_turtle.circle(-56, 200) # Radius 56, extent 200 deg
    heart_turtle.setheading(60) # Turn to draw the second half
    heart_turtle.circle(-56, 200) # Radius 56, extent 200 deg
    heart_turtle.forward(112) # Size of heart sides
    heart_turtle.end_fill()



def draw_sad_face(face_turtle, center_x, center_y): # Accept turtle instance
    """Draws a sad face using the provided turtle instance."""
    face_turtle.clear() # Clear previous drawing by this turtle
    face_turtle.hideturtle()
    face_turtle.speed(0) # Fastest speed
    face_turtle.pensize(2)
    face_turtle.penup()

    radius = 50

    # Draw face outline (yellow fill, black border)
    face_turtle.goto(center_x, center_y - radius) # Go to bottom of circle
    face_turtle.setheading(0)
    face_turtle.pendown()
    face_turtle.color("black", "yellow")
    face_turtle.begin_fill()
    face_turtle.circle(radius)
    face_turtle.end_fill()
    face_turtle.penup()

    # Draw left eye (dot)
    eye_x_offset = 20
    eye_y_offset = 15
    eye_size = 10
    face_turtle.goto(center_x - eye_x_offset, center_y + eye_y_offset)
    face_turtle.dot(eye_size, "black")

    # Draw right eye (dot)
    face_turtle.goto(center_x + eye_x_offset, center_y + eye_y_offset)
    face_turtle.dot(eye_size, "black")

    
    # Calculate start position: Left side of the mouth arc
    mouth_start_x_offset = -25 
    mouth_start_y_offset = 25 

    # Go to the calculated starting point
    face_turtle.penup()
    face_turtle.goto(center_x - mouth_start_x_offset, center_y - mouth_start_y_offset)
    face_turtle.pendown()

    # Set the heading to point generally UP and LEFT (e.g., 120 degrees)
    face_turtle.setheading(120)

    #Draw sad mouth (downward arc)
    mouth_radius = 30
    mouth_extent = 120 # Degrees of arc
    face_turtle.circle(mouth_radius, mouth_extent)
    face_turtle.penup()