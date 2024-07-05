import json
import random
import time

def load_questions_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data['questions']
    except FileNotFoundError:
        print(f"Fișierul {filename} nu a fost găsit.")
        return []
    except json.JSONDecodeError:
        print("Eroare la parsarea fișierului JSON.")
        return []
    except KeyError:
        print("Structura fișierului JSON nu conține cheia 'questions'.")
        return []

def save_score_to_text_file(player_name, score, total_questions, filename="scores.txt"):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"Nume: {player_name}, Scor: {score}/{total_questions}\n")
    except Exception as e:
        print(f"Eroare la salvarea scorului în fișier: {e}")

def quiz_trivia(questions, player_name):
    score = 0
    random.shuffle(questions)
    
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        start_time = time.time()
        while True:
            response = input("Răspunsul tău (a/b/c/d sau q pentru a ieși): ").lower()
            if response in ['a', 'b', 'c', 'd', 'q']:
                break
            else:
                print("Opțiune invalidă! Te rog să alegi a, b, c, d sau q pentru a ieși.")
        
        if response == 'q':
            print(f"Te-ai oprit. Scorul tău final este: {score} din {len(questions)}")
            save_score_to_text_file(player_name, score, len(questions))
            return
        
        end_time = time.time()
        if end_time - start_time > 10:
            print("Timpul a expirat!")
            continue
        
        if response == question["correct"]:
            score += 1
            print("Corect!")
        else:
            print(f"Greșit! Răspunsul corect este {question['correct']}.")
        print()
    
    print(f"Scorul tău final este: {score} din {len(questions)}")
    save_score_to_text_file(player_name, score, len(questions))

if __name__ == "__main__":
    #Calea fisierului JSON
    filename = ''
    #•
    questions = load_questions_from_file(filename)
    if questions:
        player_name = input("Introdu numele tău: ")
        quiz_trivia(questions, player_name)
    else:
        print("Nu s-au putut încărca întrebările.")
