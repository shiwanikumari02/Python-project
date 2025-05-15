import random
import time

# Define a list of questions and answers
questions = [
    {
        "question": "What does the 'self' keyword refer to in Python?", 
        "answers": ["It refers to the instance of the class", "It refers to a global variable", "It refers to the current function", "It refers to an object in memory"],
        "correct": "It refers to the instance of the class"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "answers": ["int", "list", "float", "character"],
        "correct":  "character"
    },
    {   
        "question": "What does the 'len()' function do in Python?",
        "answers": ["Returns the length of a string", "Returns the largest number", "Returns the number of items in a list", "Both a and c"],
        "correct": "Both a and c"
    },
    {
        "question": "Which method can be used to add an element to the end of a list?",
        "answers": [".insert()", ".append()", ".extend()", ".add()"],
        "correct": ".append()"
    },
    {
        "question": "Which of the following is used to define a function in Python?",
        "answers": ["def", "function", "fun", "define"],
        "correct": "def"
    },
    {
        "question": "Which of the following is a correct way to write a Python comment?",
        "answers": ["# This is a comment", "// This is a comment", "/* This is a comment */", "-- This is a comment"],
        "correct":  "# This is a comment"
    },
    {
        "question": "How do you handle exceptions in Python?",
        "answers": ["try...catch", "try...except", "catch...finally", "try...finally"],
        "correct": "try...except"     
    },
    {
        "question": "What is the purpose of the raise statement in Python?",
        "answers": ["It is used to handle exceptions", "It is used to suppress exceptions", "It is used to create custom exception classes", "It is used to print exception messages"],
        "correct": "It is used to create custom exception classes"
    },
    {
        "question": "Which of the following statements is true about Python dictionaries?",
        "answers": ["Keys must be unique", "Values must be unique", "Dictionaries are ordered", "Dictionaries can contain duplicate keys"],
        "correct": "Keys must be unique"
    },
    {
        "question": "Which exception is raised when an index is out of range in a list?", 
        "answers": ["RangeError", "IndexOutOfRange", "IndexError", "ListException"], 
        "correct": "IndexError"
    },
]

# Shuffle questions to randomize their order
random.shuffle(questions)

# Function to display a question
def display_question(q):
    print("\n" + q["question"])
    for i, answer in enumerate(q["answers"], 1):
        print(f"{i}. {answer}")

# Function to start the quiz
def start_quiz():
    score = 0
    total_questions = len(questions)
    
    # Start a timer
    start_time = time.time()
    
    # Loop through the questions
    for q in questions:
        display_question(q)
        
        # Get user's answer
        user_answer = input("Your answer (1/2/3/4): ")
        
        # Check if the answer is correct
        try:
            if q["answers"][int(user_answer) - 1] == q["correct"]:
                score += 1
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
    
    # Calculate elapsed time
    elapsed_time = round(time.time() - start_time, 2)
    
    # Provide feedback at the end of the quiz
    print(f"\nQuiz Complete! You answered {score} out of {total_questions} questions correctly.")
    print(f"Time taken: {elapsed_time} seconds.")
    
    # Score feedback
    if score > 8:
        print("\nGreat job! You have excellent Python knowledge!")
    elif score >= 5:
        print("\nGood attempt! Keep practicing and you'll get even better.")
    else:
        print("\nKeep practicing! You're on your way to mastering Python!")

# Run the quiz
if __name__ == "__main__":
    start_quiz()

