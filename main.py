import turtle
from shapes import draw_heart, draw_sad_face, create_clickable_button
from llm import get_trivia_data, ask_negative_feedback_gemini, ask_positive_feedback_gemini


def display_score():
    # Ensure score turtle is properly handled after screen clear
    score_turtle.clear()
    score_turtle.penup()
    score_turtle.hideturtle() # Hide it while moving
    score_turtle.goto(-350, 250) # Adjusted position slightly left
    score_turtle.pendown()
    score_turtle.write(f"Score: {score} / {total_questions}", align="left", font=("Arial", 14, "normal"))


def setup_screen():
    # Clear previous drawings before setting up the new screen
    heart_left_turtle.clear()  # Clear left heart
    heart_right_turtle.clear() # Clear right heart
    sad_face_left_turtle.clear() # Clear left face
    sad_face_right_turtle.clear()# Clear right face
    feedback_turtle.clear()

    screen.clear() # Clears all drawings and turtles from the screen
    screen.tracer(0)
    screen.title("Trivia Game")
    screen.setup(width=800, height=600)
    screen.bgcolor("lightblue")

    # Re-initialize persistent turtles after screen.clear()
    # Set properties like hidden, penup, speed again
    for t in [question_turtle, feedback_turtle, score_turtle,
              heart_left_turtle, heart_right_turtle,
              sad_face_left_turtle, sad_face_right_turtle]:
        t.hideturtle()
        t.penup()
        t.speed(0) # Ensure speed is reset if needed


def display_feedback(response):
    feedback_turtle.clear()
    feedback_turtle.penup()
    feedback_turtle.goto(0, -160) # Y-coordinate for feedback text
    feedback_turtle.pendown()
    feedback_turtle.write(response, align="center", font=("Arial", 14, "normal"))
    # No screen.update() here, let answer_selected handle the update after drawing shapes

def answer_selected(answer_idx):
    global score, total_questions
    global current_trivia

    for btn_turtle in buttons:
         btn_turtle.onclick(None) # Disable button clicks

    trivia = current_trivia
    correct_answer = trivia["correct_answer"]
    user_answer = trivia["options"][answer_idx]

    screen.tracer(0) # Turn off updates for drawing

    feedback_turtle.clear() # Clear previous feedback text
    feedback_turtle.penup()
    feedback_turtle.goto(0, -160) # Position for feedback text
    feedback_turtle.pendown()

    if user_answer == correct_answer:
        draw_heart(heart_left_turtle, -270, -50)

        response = ask_positive_feedback_gemini()
        feedback_turtle.write(response, align="center", font=("Arial", 14, "normal")) # Write text
        
        draw_heart(heart_right_turtle, 270, -50)
        score += 1
    else:
        draw_sad_face(sad_face_left_turtle, -270, 0)

        response = ask_negative_feedback_gemini()
        feedback_turtle.write(response, align="center", font=("Arial", 14, "normal")) # Write text
        
        draw_sad_face(sad_face_right_turtle, 270, 0)

    total_questions += 1
    display_score() # Update score display
    screen.update() # Show all changes at once

    screen.ontimer(display_question, 3000) # Wait before next question


def quit_game():
    """Closes the turtle graphics window."""
    screen.bye()


def display_question():
    global current_trivia, buttons
    setup_screen() # Clears screen, redraws background, hides turtles

    current_trivia = get_trivia_data()
    if not current_trivia: # Handle case where trivia data fails
        question_turtle.write("Failed to load trivia!", align="center", font=("Arial", 16, "normal"))
        screen.update()
        return

    question = current_trivia.get("question", "N/A")
    options = current_trivia.get("options", [])

    # Display Question
    question_turtle.penup()
    question_turtle.goto(0, 200)
    question_turtle.pendown()
    # Use write method correctly
    question_turtle.clear() # Clear previous question text just in case
    question_turtle.write(question, align="center", font=("Arial", 16, "normal"))

    buttons.clear() # Clear the list of button turtles from previous question
    button_y = 100
    button_gap = 60 # Spacing between buttons

    # Display Options (Answer Buttons)
    for idx, option in enumerate(options):
        # Create a lambda that accepts x, y (required by onclick)
        # but calls answer_selected with the current index 'idx'.
        # The 'i=idx' part captures the current value of 'idx' for this specific lambda.
        answer_handler = lambda x_coord, y_coord, i=idx: answer_selected(i)
        clickable_turtle = create_clickable_button(option, 0, button_y - (idx * button_gap), answer_handler)
        if clickable_turtle:
             buttons.append(clickable_turtle) # Store the clickable turtle

    # Create Quit button
    # Create a lambda that accepts x, y (required by onclick) but calls quit_game.
    quit_handler = lambda x_coord, y_coord: quit_game()
    quit_button_turtle = create_clickable_button("Quit", 0, -200, quit_handler)
    if quit_button_turtle:
        buttons.append(quit_button_turtle) # Also track quit button if needed

    display_score()
    screen.update() # Update screen once all elements are drawn
    screen.tracer(1) # Turn screen updates back on

# --- Global Variables ---
score = 0
total_questions = 0

screen = turtle.Screen()

# --- Create turtles ONCE ---
question_turtle = turtle.Turtle()
feedback_turtle = turtle.Turtle()
score_turtle = turtle.Turtle()

# Create separate turtles for left and right icons
heart_left_turtle = turtle.Turtle()
heart_right_turtle = turtle.Turtle()
sad_face_left_turtle = turtle.Turtle()
sad_face_right_turtle = turtle.Turtle()

# Initial setup for all turtles
all_turtles = [question_turtle, feedback_turtle, score_turtle,
               heart_left_turtle, heart_right_turtle,
               sad_face_left_turtle, sad_face_right_turtle]
for t in all_turtles:
    t.hideturtle()
    t.penup()
    t.speed(0) # Set fastest speed

current_trivia = {}
buttons = [] # List to keep track of button turtles

# --- Start Game ---
display_question()
screen.mainloop()