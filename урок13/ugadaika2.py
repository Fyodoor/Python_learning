# Загадать случайное число от 1 до 100
# Организовать опрос пользователя
# Ввести число
# Если загаданное число больше, чем введенное число -> больше
# Если загаданное число меньше, чем введенное число -> меньше
# Если загаданное число равно введенному числу -> Меркурий в лунной фазе на вашей стороне
# До скорого, заходите если чё

import random

def is_valid(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1 and user_number <= 100:
            return True
        else:
            return False
    else:
        return False
  
while True:
    
    secret_number = random.randint(1, 100)
    print("Добро пожаловать в игру 'Угадай число'")
    
    total = 0
    
    while True:
        print("Введите число от 1 до 100")
        user_input = input()
        total += 1
        if not is_valid(user_input):
            continue
        
        user_number = int(user_input)
        
        if secret_number > user_number:
            print("Загаданное число больше, чем введенное Вами")
        elif secret_number < user_number:
            print("Загаданное число меньше, чем введенное Вами")
        else:
            print("Ура! Удача на Вашей стороне камрад")
            print("Колличество попыток: ", total)
            break
    
    print("Спасибо за игру. \nЕсли хотите сыграть ещё, введите - Да")
    
    answer = input()
    
    if answer == "Да":
        continue
    else:
        break