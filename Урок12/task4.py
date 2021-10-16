def cost(number):
    delivery = 0
    while number > 0:
        if number == 1:
            delivery = 100
        if number > 1:
            delivery = 100
            while number > 1:
                delivery += 50
                number -= 1 
        number -= 1
    return delivery

volume = int(input())
print(cost(volume))            