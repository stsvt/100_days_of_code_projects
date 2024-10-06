class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer, question_answer):
        self.question_number += 1
        if answer.strip().lower() == question_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()
        self.next_question()

    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            answer = input(f"Q{self.question_number + 1}: {current_question.text} (True/False): ")
            self.check_answer(answer, current_question.answer)
        else:
            print("You've completed the quiz!")
            print(f"Your final score is: {self.score}/{self.question_number}")

