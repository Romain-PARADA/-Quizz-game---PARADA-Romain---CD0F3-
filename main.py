import json

def charger_questions(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        print("Le fichier de questions est introuvable.")
        return []

def poser_question(question):
    print(f"\nCatégorie : {question['category']}\nDifficulté : {question["difficulty"]}\nquestion : {question["question"]}")
    for i,option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")
    
    try:
        reponse = int(input("Votre réponse (entrez le numéro) : "))
        return reponse == question["answer"]
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return False
    