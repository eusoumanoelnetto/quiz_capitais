quiz = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Paris", "Londres", "Berlim", "Madri"],
        "correct_answer": "Paris"
    },
    {
        "question": "Qual é a capital do Japão?",
        "options": ["Pequim", "Seul", "Tóquio", "Bangkok"],
        "correct_answer": "Tóquio"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
        "correct_answer": "Brasília"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "correct_answer": "Canberra"
    },
    {
        "question": "Qual é a capital do Canadá?",
        "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
        "correct_answer": "Ottawa"
    }
]

def run_quiz(quiz):
    score = 0
    for q in quiz:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        answer = input("Escolha a resposta correta (1-4): ")
        if q["options"][int(answer) - 1] == q["correct_answer"]:
            score += 1
            print("Correto!\n")
        else:
            print(f"Errado! A resposta correta é {q['correct_answer']}.\n")
    print(f"Você acertou {score} de {len(quiz)} perguntas.")

if __name__ == "__main__":
    run_quiz(quiz)

    # Escreva uma função que recebe a questão e as exibe uma a uma para o usuário.
    # Ela retorna a resposta do usuário e valida se a resposta é valida ou se ela é um erro.
    
def show_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    answer = input("Escolha a resposta correta (1-4): ")
    return answer

# Escreva uma função que recebe a resposta do usuário e a compare com a resposta correta.

def check_answer(question, answer):
    return question["options"][int(answer) - 1] == question["correct_answer"]



def main():
    score = 0
    for q in quiz:
        user_answer = show_question(q)
        if check_answer(q, user_answer):
            score += 1
            print("Correto!\n")
        else:
            print(f"Errado! A resposta correta é {q['correct_answer']}.\n")
    print(f"Você acertou {score} de {len(quiz)} perguntas.")