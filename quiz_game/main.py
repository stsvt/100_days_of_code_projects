from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

game = QuizBrain(question_bank)

game.next_question()
