class QuizGame:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct = 0
    
    def new_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.question} (true/false) : ")
        if answer == str(current_question.answer).lower():
            print("Great job!")
            self.correct += 1
        else:
            print("Maybe next time..")
        print("Answer: " + str(current_question.answer))
        print(f"Your score: {self.correct}/{self.question_number}" )
        print()
        
    
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"Final score: {self.correct}/{self.question_number}")
            return False