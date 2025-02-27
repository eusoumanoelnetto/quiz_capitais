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

def show_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    while True:
        answer = input("Digite o número da resposta correta: ")
        if answer.isdigit() and 1 <= int(answer) <= 4:
            return answer
        else:
            print("Entrada inválida. Por favor, escolha um número entre 1 e 4.")

def check_answer(question, answer):
    return question["options"][int(answer) - 1] == question["correct_answer"]

def ask_until_correct(question):
    attempts = 0
    max_attempts = 2
    while attempts < max_attempts:
        user_answer = show_question(question)
        if check_answer(question, user_answer):
            print("Correto!\n")
            return True
        else:
            attempts += 1
            if attempts < max_attempts:
                attempts_left = max_attempts - attempts
                print(f"Errado! A resposta correta é {question['correct_answer']}. Tentativas restantes: {attempts_left}. Tente novamente.\n")
            else:
                print(f"Errado! A resposta correta é {question['correct_answer']}.\n")
    return False

def run_quiz(quiz, name):
    score = 0
    for q in quiz:
        if not ask_until_correct(q):
            print(f"{name}, você errou a mesma pergunta duas vezes. O quiz foi encerrado.")
            return
        score += 1
    print(f"{name}, você acertou {score} de {len(quiz)} perguntas.")
    if score == len(quiz):
        print(f"Parabéns, {name}! Você acertou todas as questões!")

if __name__ == "__main__":
    name = input("Qual é o seu nome? ").strip()
    ready = input(f"{name}, está pronto para testar seus conhecimentos? (SIM/NÃO): ").strip().upper()
    if ready == "SIM":
        run_quiz(quiz, name)
    else:
        print("Quiz cancelado.")