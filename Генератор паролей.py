from string import printable
from random import choice
all_simbols = list(printable)[:-6]
while True:
    lenpassword = int(input("сколько числел должно быть в пароле:"))
    if lenpassword < 3:
        print("длина пароля слишком маленькая!")
    elif lenpassword > 20:
        print("длина пароля слишком большая!")
    else:

        break

status = False
while status == False:
    password = "".join([choice(all_simbols) for simbol in range(lenpassword)])
    print(password)
    hacker = input("вам нравиться пароль? ")
    if hacker == "да":
        print("Благодарю сударь за столь сладкую лесть!")
        status = True
    elif hacker == "нет":
        print("Сударь вызываю вас на дуэль за ваше сквернословие!")
       
    else:
        print("Сударь не отвести ли вас к лекарю?")
        break
    