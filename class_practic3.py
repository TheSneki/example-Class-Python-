class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print("Очень интересный вопрос! Не знаю.")
        print()


class Student(Human):
    def ask_question(self, someone, question):
        print(f"{someone.name}, {question}")
        someone.answer_question(question)


class Curator(Human):
    def answer_question(self, question):
        if "грустненько" in question:
            print("Держись, всё получится. Хочешь видео с котиками?")
            print()
        else:
            super().answer_question(question)
            print()


class Mentor(Human):
    def answer_question(self, question):
        if "грустненько" in question:
            print("Отдохни и возвращайся с вопросами по теории.")
            print()
        elif "питонистом" in question:
            print("Сейчас расскажу.")
        else:
            super().answer_question(question)
            print()


class CodeReviewer(Human):
    def answer_question(self, question):
        if "каникулы" in question:
            print("Очень интересный вопрос! Не знаю.")
            print()
        elif "проект" in question:
            print("О, вопрос про проект, это я люблю.")
            print()
        else:
            super().answer_question(question)
            print()


# Создаем объекты
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

# Задаем вопросы
student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
