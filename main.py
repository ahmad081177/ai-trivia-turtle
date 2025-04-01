import turtle
from shapes import draw_heart, draw_sad_face
from llm import get_trivia_data, ask_negative_feedback_gemini, ask_positive_feedback_gemini

# Function to display score on the screen
def display_score(player):
    player.clear()  # Clear previous score
    player.penup()
    player.goto(-250, 250)  # Top-left corner for the score
    player.pendown()
    player.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))

# Function to create a new turtle for clearing previous content
def create_clear_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    return new_turtle

def setup_screen(screen):
    screen.clear()
    screen.title("Trivia Game")
    screen.setup(width=800, height=600)
    screen.bgcolor("lightblue")

def display_feedback(t, response):
    # Display response message
    t.penup()
    t.goto(0, -160)
    t.pendown()
    t.write(response, align="center", font=("Arial", 14, "normal"))

# Function to display question and options
def display_question():
    global score  # Access the global score variable
    global screen

    setup_screen(screen)

    # Create separate turtles for each part of the content
    question_turtle = create_clear_turtle()
    answer_turtle = create_clear_turtle()
    feedback_turtle = create_clear_turtle()

    # Fetch trivia data
    trivia = get_trivia_data()
    question = trivia["question"]
    options = trivia["options"]
    correct_answer = trivia["correct_answer"]

    # Display question
    question_turtle.goto(0, 200)
    question_turtle.pendown()
    question_turtle.write(question, align="center", font=("Arial", 16, "normal"))

    # Display options
    for idx, option in enumerate(options, 1):
        answer_turtle.penup()
        answer_turtle.goto(0, 150 - (idx * 30))
        answer_turtle.pendown()
        answer_turtle.write(f"{idx}. {option}", align="center", font=("Arial", 14, "normal"))

    # Display score
    display_score(score_turtle)

    # Get user answer
    user_answer = screen.textinput("Trivia Question", "Enter the number of your answer (1-4):")

    # Validate answer input
    if not user_answer or not user_answer.isdigit() or not (1 <= int(user_answer) <= 4):
        screen.clear()
        display_feedback(feedback_turtle, "Great Job and good bye!")
        screen.ontimer(lambda: screen.bye(), 3000)  # Wait 3000 ms (3 seconds)
        return  # Exit if invalid input

    # Draw face based on answer
    feedback_turtle.penup()
    feedback_turtle.goto(0, -120)
    feedback_turtle.pendown()

    #Check answer and update score
    if options[int(user_answer) - 1] == correct_answer:
        draw_heart()
        response = ask_positive_feedback_gemini()
        score += 1  # Increment score for correct answer
    else:
        draw_sad_face()
        response = ask_negative_feedback_gemini()

    
    # Display score
    display_score(score_turtle)

    # Display response message
    display_feedback(feedback_turtle, response)
    
    # Pause for 3-4 seconds before next question
    screen.ontimer(lambda: display_question(), 3000)  # Wait 3000 ms (3 seconds)

    screen.mainloop()


# Initialize variables
score = 0
screen = turtle.Screen()
question_turtle = create_clear_turtle()
answer_turtle = create_clear_turtle()
feedback_turtle = create_clear_turtle()
score_turtle = create_clear_turtle()

# Start the game
display_question()
