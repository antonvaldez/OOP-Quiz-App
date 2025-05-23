from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    question = Question(x["question"],x["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n\nYou have completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")