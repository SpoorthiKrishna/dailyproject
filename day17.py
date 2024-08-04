from moduless import Question # type: ignore
from data2 import question_data  # type: ignore
from quizbrain import Quizbrain # type: ignore

questionbank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    questionbank.append(new_question)

quiz=Quizbrain(questionbank)

while quiz.still_question(): # type: ignore
    quiz.next_question()
