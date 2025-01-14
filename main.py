import json

def charger_questions(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
            questions = json.load(f)
    return questions

def poser_question(question):
    print(f"\nCategory : {question['category']}\nDifficulty : {question['difficulty']}\nQuestion : {question['question']}")
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")
    
    try:
        reponse = int(input("Your answer (type the number) : "))
        return reponse == question["answer"]
    except ValueError:
        print("Enter a valid number")
        return False
    
def jouer_quiz(fichier_questions):
    print("Welcome in this advance quizz!")
    questions = charger_questions(fichier_questions)
    if not questions:
        return
    score = 0
    total_questions = len(questions)

    import random
    random.shuffle(questions)
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}/{total_questions}")
        if poser_question(question):
            print("Good answer!")
            score += 1
        else:
            print(f"Bad answer. the good answer was {question['options'][question['answer'] - 1]}")

    print("End of quizz!")
    print(f"Your final score is {score}/{total_questions}.")
    if score == total_questions:
        print("Well played, you are an expert!")
    elif score > total_questions / 2:
        print("Well played but you can still progress.")
    else:
        print("Ah, try again to progess!")
    
if __name__ == "__main__":
    jouer_quiz("questions.json")