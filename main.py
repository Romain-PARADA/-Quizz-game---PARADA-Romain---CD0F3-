import json

def charger_questions(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
            questions = json.load(f)
    return questions

def poser_question(question):
    print(f"\nCategory : {question['category']}\nDifficulty : {question["difficulty"]}\nquestion : {question["question"]}")
    for i,option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")
    
    try:
        reponse = int(input("Your answer (type the number) : "))
        return reponse == question["answer"]
    except ValueError:
        print("Enter a valid number")
        return False
    
    