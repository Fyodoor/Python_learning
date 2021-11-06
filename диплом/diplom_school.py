import os
import jsonpickle

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
    
    def writelines(self, path, data):
        file = open(path, "w")
        data = file.writelines(data)
        file.close
        
    def clear(self, path):
        file = open(path, "w")
        data = file.write("")
        file.close()    
        
    def exists(self, path):
        return os.path.exists(path)

class School:
    def __init__(self, number_school, adress_school):
        self.number_school = number_school
        self.adress_school = adress_school
        
        


class Students:
    def __init__(self, first_name_student, last_name_student, age_student,
                 number_class):
        self.first_name_student = first_name_student
        self.last_name_student = last_name_student
        self.age_student = age_student
        self.number_class = number_class        
    
class StudentsStorage:
    def __init__(self):
        
        self.file_name = "students.json"
        
    def get_all(self):
        if not file_provider.exists(self.file_name):
            students = []
            self.safe_students(students)
            
        data = file_provider.get(self.file_name)
        students = jsonpickle.decode(data)
        return students
    
    def safe_students(self, students):
        json_data = jsonpickle.encode(students)
        file_provider.writelines(self.file_name, json_data)
            
    def add(self, student):
        students = self.get_all()
        students.append(student)
        self.safe_students(students)
        
    def remove(self, index):
        students = self.get_all()
        students.pop(index)
        self.safe_students(students)
        

def print_students():
    first_name_student = "Имя"
    last_name_student = "Фамилия"
    age_student = "Возраст"
    number_class = "Номер класса"
    
    
    print(f'{first_name_student:15}{last_name_student:15}{age_student:15}{number_class:15}')
    
    students = studentsStorage.get_all()
    for i in range(len(students)):
        for student in students:
            print(f'{i + 1}.{student.first_name_student:15}{student.last_name_student:15}{student.age_student:15}{student.number_class:15}')


def add_new_student():
    
    print("Введите Имя, Фамилию, Возраст, Номер класса")
    first_name_student = input("введите имя ученика: ")
    last_name_student = input("введите фамилию ученика: ")
    age_student = input("введите возраст ученика: ")   
    number_class = input("введите класс ученика: ")
    new_student = Students(first_name_student, last_name_student, age_student,
                 number_class)
    studentsStorage.add(new_student)

def get_user_answer():
    user_input = input()
    
    while not user_input.isdigit():
        print("Введите число")
        user_input = input()
    
    return int(user_input)
    
def remove_student():
    students = studentsStorage.get_all()
    while True:
        print("Выберите номер ученика которого надо удалить.")
        
        print_students(students)
        user_answer = get_user_answer()
        
        if user_answer < 1 or user_answer > len(students):
            continue
            
        studentsStorage.remove(user_answer - 1)
        
        print(f"{user_answer} успешно удален")
        break


    
file_provider = FileProvider()
studentsStorage = StudentsStorage()



while True:
    
    students = studentsStorage.get_all()
    count_students = len(students)   
    
    
    print("Показать список учащихся? Нажмите 1")
    user_answer = int(input())
    if user_answer == 1:
        print_students()    
        
    print("Хотите добавить нового ученика? Для этого отправтье 1")
    user_answer = int(input())
    if user_answer == 1:
        add_new_student()    
    
    print("Хотите удалить ученика? Для этого отправтье 1")
    user_answer = int(input())
    if user_answer == 1:
        remove_student()
        
    print("Вернуться к меню? Для этого отправтье 1")
    user_answer = int(input())
    
    if user_answer != 1:
        break    