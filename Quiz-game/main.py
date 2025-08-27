from data import questions
from question import Question
from quiz_game import QuizGame

question_list = []
for item in questions:
    question_task = item["question"]
    question_answer = item["answer"]
    new_question = Question(question_task, question_answer)
    question_list.append(new_question)

quizGame = QuizGame(question_list)

while(quizGame.still_has_question()):
    quizGame.new_question()
