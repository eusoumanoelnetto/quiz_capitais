import pytest

from quiz import check_answer, show_question

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
]

def test_check_answer_correct():
    question = quiz[0]
    assert check_answer(question, "1") == True

def test_check_answer_incorrect():
    question = quiz[0]
    assert check_answer(question, "2") == False

if __name__ == "__main__":
    pytest.main()
