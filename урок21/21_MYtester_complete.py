# -*- coding: utf8 -*-

import random
import os

class FileProvider:
    def get(self, path):
        file = open(path, "r")
        data = file.read()
        file.close()
        return data
    
    def append(self, path, data):
        file = open(path, "a")
        data = file.write(data)
        file.close()
    
    def clear(self, path):
        file = open(path, "w")
        data = file.write("")
        file.close()    
        
    def exists(self, path):
        return os.path.exists(path)
        
        
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuestionsStorage:
    def get_all(self):
        file_name = "questions.txt"
        if not file_provider.exists(file_name):
            questions = [Question("Сколько будет два плюс два умноженное на два?", 6),
                         Question("Бревно нужно распилить на 10 частей, сколько надо сделать распилов?", 9),
                         Question("На двух руках 10 пальцев. Сколько пальцев на 5 руках", 25),
                         Question("Укол делают каждые полчаса, сколько нужно минут для трёх уколов?", 60),
                         Question("Пять свечей горело, две потухли. Сколько свечей осталось?", 2)]
            self.safe_questions(questions)
            
        data = file_provider.get(file_name).strip("\n")
        data = data.split("\n")
        questions = []
        for line in data:
            values = line.split("#")
            question = Question(values[0], int(values[1]))
            questions.append(question)
            
        return questions
    
    def safe_questions(self, questions):
        for question in questions:
            self.add(question)
            
    def add(self, question):
        file_name = "questions.txt"
        data = f"{question.text}#{question.answer}\n"
        file_provider.append(file_name, data)
        
    def remove(self, index):
        questions = self.get_all()
        questions.pop(index)
        
        file_name = "questions.txt"
        file_provider.clear(file_name)
        
        self.safe_questions(questions)
        

class User:
    def __init__(self, name, count_right_answers=0, result="Неизвестно"):
        self.name = name
        self.count_right_answers = count_right_answers
        self.result = result
        
    def accept_right_answer(self):
        self.count_right_answers += 1
        
    def set_result(self, result):
        self.result = result

class UserResultStorage:
    def safe(self, user):
        file_name = "results.txt"
        data = f"{user.name}#{user.count_right_answers}#{user.result}\n"
        
        file_provider.append(file_name, data)
        
        
    def get_all(self):
        file_name = "results.txt"
        
        data = file_provider.get(file_name).strip("\n")
        data = data.split("\n")        
        users = []
        
        for line in data:
            values = line.split("#")
            user = User(values[0], values[1], values[2])
            users.append(user)
            
        return users
          
def calculate_result(count_right_answers, count_questions):
    right_answers_precent = count_right_answers * 100 // count_questions
    results = [ "Идиот", "Кретин", "Дурак", "Нормальный", "Талант", "Гений"]
    return results[right_answers_precent // 20]


def get_user_answer():
    user_input = input()
    
    while not user_input.isdigit():
        print("Введите число")
        user_input = input()
    
    return int(user_input)


def show_user_results():
    name = "Имя"
    count_right_answers = "Кол-во правильных ответов"
    result = "Результат"
    print(f'{name:15}{count_right_answers:30}{result:15}')
    
    users = usersResultStorage.get_all()
    
    for user in users:
        print(f"{user.name:15}{user.count_right_answers:30}{user.result:15}")

def add_new_question():
    print("Введите текст вопроса")
    text = input()
    print("Введите ответ на вопрос")
    answer = get_user_answer()
    new_question = Question(text, answer)
    questionsStorage.add(new_question)
    
def print_questions(questions):
    print("------------------------------------------")
    for i in range(len(questions)):
        print(f"{i+1}.{questions[i].text}")
        
    print("------------------------------------------")
    
def remove_question():
    questions = questionsStorage.get_all()
    while True:
        print("Выберите номер вопроса который надо удалить.")
        
        print_questions(questions)
        
        user_answer = get_user_answer()
        if user_answer < 1 or user_answer > len(questions):
            continue
        
        questionsStorage.remove(user_answer - 1)
        
        print(f"Ура.Вопрос под номером {user_answer} успешно удален")
        break
    
file_provider = FileProvider()
questionsStorage = QuestionsStorage()
usersResultStorage = UserResultStorage()
while True:
    
    questions = questionsStorage.get_all()
    count_questions = len(questions)
    
    print("Как Вас зовут?")
    user_name = input()
    user = User(user_name)
    for i in range(len(questions)):
        print(f"Вопрос №{i + 1}")
        
        random_index = random.randint(0, len(questions) -1)
        print(questions[random_index].text)
        
        user_answer = get_user_answer()
        
        right_answer = questions[random_index].answer
        if user_answer == right_answer:
            user.accept_right_answer()
            
        questions.pop(random_index)
                
        
    print("Количество правильных ответов ", user.count_right_answers)
    
    result = calculate_result(user.count_right_answers, count_questions)
    user.set_result(result)
    print(f"{user_name}, Ваш результат: {result}")
    
    usersResultStorage.safe(user)
    
    print("Хотите посмотреть результаты предыдущих игр? Для этого отправтье слово ДА")
    user_answer = input()
    if user_answer.upper() == "ДА":
        show_user_results()
    
    print("Хотите добавить новый вопрос? Для этого отправтье слово ДА")
    user_answer = input()
    if user_answer.upper() == "ДА":
        add_new_question()    
    
    print("Хотите удалить вопрос? Для этого отправтье слово ДА")
    user_answer = input()
    if user_answer.upper() == "ДА":
        remove_question()      
    
    print("Хотите сыграть заново? Для этого отправтье слово ДА")
    user_answer = input()
    
    if user_answer.upper() != "ДА":
        break