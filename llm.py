import google.generativeai as genai
import os, json
from dotenv import load_dotenv
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel(os.environ['GEMINI_MODEL'])

# Ask Gemini for a response
def ask_negative_feedback_gemini() -> str:
    try:
        query = "Give me one short comforting message for a wrong answer."
        response = model.generate_content(query)
        return response.text.split("\n")[0]  # Limit to the first line
    except Exception as e:
        return f"Error: {str(e)}"

def ask_positive_feedback_gemini() -> str:
    try:
        query = "Give me one short congratulatory message for kids who answer correctly."
        response = model.generate_content(query)
        return response.text.split("\n")[0]  # Limit to the first line
    except Exception as e:
        return f"Error: {str(e)}"

def __ask_gemini_json(request: str) -> str:
    try:
        response = model.generate_content(request)
        return response.text  # Limit to the first line
    except Exception as e:
        return f"Error: {str(e)}"
    
# Function to fetch a trivia question from Gemini
def get_trivia_data():
    prompt = "Generate a simple multiple-choice trivia question for kids aged 10. Provide a JSON format with 'question', 'options' (list of 4), 'correct_answer'."
    try:
        response = __ask_gemini_json(prompt)
        response = response.strip("```json ").strip("```\n")
        trivia_data = json.loads(response)  # Validate JSON format
        return trivia_data
    except:
        return {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris"
        }