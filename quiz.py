import json
import random


class Question:
    """Определяем класс, его методы и поля"""
    def __init__(self, question_text, question_dif, right_answer, is_asked=False, user_answer=None):
        self.question_text = question_text
        self.question_dif = question_dif
        self.right_answer = right_answer
        self.is_asked = is_asked
        self.user_answer = user_answer
        self.question_points = 0

    def get_points(self):
        if self.question_dif == "1":
            self.question_points = 10
        elif self.question_dif == "2":
            self.question_points = 20
        elif self.question_dif == "3":
            self.question_points = 30
        elif self.question_dif == "4":
            self.question_points = 40
        elif self.question_dif == "5":
            self.question_points = 50

    def is_correct(self):
        if self.user_answer == self.right_answer:
            return True
        else:
            return False

    def build_question(self):
        return f"Вопрос: {self.question_text}\nСложность {self.question_dif}/5\n"

    def build_positive_feedback(self):
        print(f"Ответ верный, получено {self.question_points} баллов\n")

    def build_negative_feedback(self):
        print(f"Ответ неверный, верный ответ {self.right_answer}\n")

def output_results():
    """Выводим итоги"""
    print(f"Вот и всё!\nОтвечено {total_right_answers} вопроса из {len(questions_list)}\nНабранно баллов: {total_points}")

def read_file():
    """Считываем данные из файла"""
    with open("questions.json") as file:
        questions_list = file.read()
    return json.loads(questions_list)

questions_list = read_file()

#основное тело программы
total_points = 0
total_right_answers = 0

random.shuffle(questions_list)
for question_dic in questions_list:
    question = Question(question_dic["q"], question_dic["d"], question_dic["a"])
    quest_output = question.build_question()
    question.is_asked = True
    question.user_answer = input(quest_output)

    if question.is_correct():
        question.get_points()
        total_points += question.question_points
        question.build_positive_feedback()
        total_right_answers += 1
    else:
        question.build_negative_feedback()

output_results()
