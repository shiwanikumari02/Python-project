import random
import time
import threading

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

# Countdown timer for 20 seconds
def countdown_timer(seconds, stop_event):
    for remaining in range(seconds, -1, -1):
        if stop_event.is_set():
            break
        print(f"\rTime Duration: {remaining} seconds", end="")
        time.sleep(1)
    if not stop_event.is_set():  # Check if time is up
        print("\nTime's up!")

# Function to start the quiz
def start_quiz():
    score = 0
    total_questions = len(questions)
    
    for q in questions:
        display_question(q)
        print("\nYou have 20 seconds to answer this question...")
        # Timer setup
        stop_event = threading.Event()
        timer_thread = threading.Thread(target=countdown_timer, args=(20, stop_event))
        timer_thread.start()
        
        # Get user input with a timer
        user_answer = None
        try:
            user_answer = input("\n                             Your answer (1/2/3/4):")
        finally:
            # Stop the timer after user input or if time is up
            stop_event.set()
            timer_thread.join()
        
        # If time's up, don't process the answer and just show the correct answer
        if not stop_event.is_set():  # If time's up
            print(f"The correct answer is: {q['correct']}")
        else:
            # Check if the answer is correct
            try:
                if q["answers"][int(user_answer) - 1] == q["correct"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer is: {q['correct']}")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 4.")
        
        # Automatically move to the next question after the time is up or after answer
        time.sleep(1)  # Short pause before the next question to give feedback

    # Calculate percentage
    percentage = (score / total_questions) * 100

    # Provide feedback at the end of the quiz
    print(f"\nQuiz Complete! You answered {score} out of {total_questions} questions correctly.")
    print(f"Your score: {percentage:.2f}%")  # Display the percentage score
    
    # Provide personalized feedback based on the percentage
    if percentage > 80:
        print("\nGreat job! You have excellent Python knowledge!")
    elif percentage >= 50:
        print("\nGood attempt! Keep practicing and you'll get even better.")
    else:
        print("\nKeep practicing! You're on your way to mastering Python!")

# Run the quiz
if __name__ == "__main__":
    start_quiz()
