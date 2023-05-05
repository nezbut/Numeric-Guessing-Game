from random import randint
import sys


# Эта функция вызывается если пользователь в конце ввёл "Конец" и там где надо было нажать Enter он вводит число "1979"
def easter_egg():
    da = input('Вы уверены что хотите продолжить?: ').strip().lower()
    if da not in ['да', 'нет']:
        while da not in ['да', 'нет']:
            da = input('Да или Нет!!!!: ').strip().lower()
    if da in ["да", "нет"]:
        if da == 'нет':
            print('Увы выхода нет.')
        if da == 'да' or da == 'нет':
            print('Игроку приготовиться!')
            input('Нажмите что-нибудь: ')
            da = 0
            while da < 800:
                print('vzlom by Warren Robinett')
                input('chtonibut nazmite(xaxaxaxaxaxaxaaxaxaxaxaxaxax): ')
                if da == 200:
                    print('''Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, '
                          'Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, '
                          'Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo,
                          Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo
                          Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo
                          Ne nadoelo? , Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?, Ne nadoelo?''')
                if da == 500:
                    print('''vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, '
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, '
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        ' vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, '
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,'
                        'vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4, vzlom$^#&$#^$&*$^@#&^$@4,''')
                if da == 700:
                    print('''Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11,'
                        ' Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11,'
                        ' Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11
                        Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11,'
                        Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11,'
                        Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11,'
                        Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11, Yжe skoro!!!11,''')
                da += 1
            da = 0
            while da < 500:
                print('?!3%№"№#%#' * 50)
                input(
                    'chtonibut nazmite, chtonibut nazmite, chtonibut nazmite, chtonibut nazmite, chtonibut nazmitechtonibut nazmitechtonibut nazmitechtonibut nazmite: ')
                da += 1
            print('''Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            Вас взломал Warren Robinett!
            ''')
            konec = input('napishi "1979": ').strip().lower()
            if konec not in ['1979']:
                while konec not in ['1979']:
                    konec = input('napishi 1979!!!!: ').strip().lower()
            if konec == '1979':
                sys.exit()


# Функция на проверку цифр.
def number_check(one_number, two_number):
    if not one_number.isdigit() or not two_number.isdigit() or int(one_number) >= int(two_number):
        if not one_number.isdigit() or not two_number.isdigit():
            while True:
                print('Введите числа согласно условию -> (a < b (b включительно!), число должно быть положительное!)!')
                one_number = input('Какое будет первое число?: ').strip()
                two_number = input('Какое будет второе число?: ').strip()
                if one_number.isdigit() and two_number.isdigit():
                    break
        if int(one_number) >= int(two_number):
            while True:
                print('Читайте внимательно условие -> "a < b (b включительно!), число должно быть положительное!"')
                one_number = input('Какое будет первое число?: ').strip()
                two_number = input('Какое будет второе число?: ').strip()
                if one_number.isdigit() and two_number.isdigit() and int(one_number) < int(two_number):
                    break
    return one_number, two_number


# Функция выполняется, если игрок захотел поиграть снова.
def Game_replay():
    one_number_1 = input('Какое будет первое число?: ').strip()
    two_number_2 = input('Какое будет второе число?: ').strip()
    one_number_1, two_number_2 = number_check(one_number_1, two_number_2)
    one_number_1, two_number_2 = int(one_number_1), int(two_number_2)
    random_number_random = randint(one_number_1, two_number_2)
    print(f'{name_gamer}, мы загадали для вас случайное число от {one_number_1} до {two_number_2}(включительно!).')
    gamer_number_gamer = gamer_number_check(one_number_1, two_number_2)
    attempt_counter_attempt = 0
    while True:
        if gamer_number_gamer > random_number_random:
            print('Надо ввести число поменьше🙃')
            gamer_number_gamer = gamer_number_check(one_number_1, two_number_2)
            attempt_counter_attempt += 1
        if gamer_number_gamer < random_number_random:
            print('Надо ввести число побольше🙂')
            gamer_number_gamer = gamer_number_check(one_number_1, two_number_2)
            attempt_counter_attempt += 1
        if gamer_number_gamer == random_number_random:
            print(f'Поздравляю {name_gamer}, вы угадали число!🤩')
            print(f'Количество ваших попыток = {attempt_counter_attempt}💣')
            if attempt_counter_attempt == 0:
                print('Вы довольно везучий😄')
            print("-" * 55)
            end_ = input(
                'Вы желаете закончить игру? или можете начать игру заново😉(Введите "Конец" или же "Заново"): ').strip().lower()
            if end_ in ['конец', 'заново']:
                if end_ == 'конец':
                    print(f'''{name_gamer}, было очень приятно что вы поиграли в мою игру💖
            обязательно заходите еще!''')
                    print("-" * 55)
                    egg_ = input('            Для выхода нажмите Enter: ')
                    if egg_ == '1979':
                        easter_egg()
                    else:
                        sys.exit()
                if end_ == 'заново':
                    Game_replay()
            if end_ not in ['конец', 'заново']:
                while True:
                    end_ = input('введите "Конец" или "Заново": ')
                    if end_ in ['конец', 'заново']:
                        if end_ == 'конец':
                            print(f'''{name_gamer}, было очень приятно что вы поиграли в мою игру💖
            обязательно заходите еще!''')
                            print("-" * 55)
                            egg_ = input('            Для выхода нажмите Enter: ')
                            if egg_ == '1979':
                                easter_egg()
                            else:
                                sys.exit()
                        if end_ == 'заново':
                            Game_replay()


# Функция, которая проверяет число введенное игроком.
def gamer_number_check(one_number_11, two_number_22):
    number = input('Попробуйте его угадать🎲: ').strip()
    if not number.isdigit() or int(number) > two_number_22 or int(number) < one_number_11:
        if not number.isdigit():
            while not number.isdigit():
                print('Вы ввели не число!')
                number = input('Попробуйте его угадать снова🎲: ').strip()
                if number.isdigit():
                    break
        if int(number) > two_number_22 or int(number) < one_number_11:
            while True:
                print(
                    f'Вы ввели не число или же вы ввели число не в диапазоне от {one_number_11} до {two_number_22}(включительно!)')
                number = input('Попробуйте его угадать снова🎲: ').strip()
                if number.isdigit() and one_number_11 <= int(number) <= two_number_22:
                    break
    return int(number)


# Начало и настройка игры.
print(r'''                  /\_/\ 
                  >^,^< 
                   / \  
                  (|_|)_/''')
print('Добро пожаловать в игру "Числовая Угадайка"🧐')
print('           Итак давайте начнем!')
input('           Нажмите Enter: ')
print("-" * 55)
name_gamer = input('Введите ваше имя: ').strip().capitalize()
if not name_gamer.isalpha():
    while not name_gamer.isalpha():
        print('Мне кажется у вас имя не из цифр и пробелов😉')
        name_gamer = input('Введите ваше имя: ').strip().capitalize()
print(
    f'''Итак {name_gamer} для начала игры введите числа в диапазоне котором будет загадано число: a < b (b включительно!), число должно быть положительное!''')
one_number = input('Какое будет первое число?: ').strip()
two_number = input('Какое будет второе число?: ').strip()
one_number, two_number = number_check(one_number, two_number)
print(f'{name_gamer} ваши числа {one_number} и {two_number}. Желаем вам удачной игры!😊')
print('-' * 55)
# Условия игры.
print('            Давайте объясним вам условия игры:')
print()
print(f'''Игра генерирует случайное число в диапазоне от {one_number} до {two_number}(включительно!)
и просит вас угадать это число. Также если введенное вами число больше или меньше загаданного числа, 
то игра даст вам подсказку. И в конце игры будет выведено количество попыток за которые вы пытались угадать число.
                Желаем вам приятной игры!😇''')
print("-" * 55)
# Начало игры.
one_number, two_number = int(one_number), int(two_number)
random_number = randint(one_number, two_number)  # Игра генерирует случайное число
print(f'{name_gamer}, мы загадали для вас случайное число от {one_number} до {two_number}(включительно!).')
gamer_number = gamer_number_check(one_number,
                                  two_number)  # Игрок вводит своё число, и программа проверяет с помощью функции правильное ли оно.
attempt_counter = 0
while True:  # сама игра
    if gamer_number > random_number:
        print('Надо ввести число поменьше🙃')
        gamer_number = gamer_number_check(one_number, two_number)
        attempt_counter += 1
    if gamer_number < random_number:  # игра даёт подсказки, если пользователь ввёл число больше загаданного или меньше.
        print('Надо ввести число побольше🙂')
        gamer_number = gamer_number_check(one_number, two_number)
        attempt_counter += 1
    if gamer_number == random_number:
        print(f'Поздравляю {name_gamer}, вы угадали число!🤩')
        print(
            f'Количество ваших попыток = {attempt_counter}💣')  # если пользователь угадал число, то выводится поздравление и количество попыток
        if attempt_counter == 0:
            print('Вы довольно везучий😄')
        print("-" * 55)
        end = input(
            'Вы желаете закончить игру? или можете начать игру заново😉(Введите "Конец" или же "Заново"): ').strip().lower()  # тут у игрока есть 2 выбора либо закончить игру, либо начать заново.
        if end in ['конец', 'заново']:
            if end == 'конец':
                print(f'''{name_gamer}, было очень приятно что вы поиграли в мою игру💖
            обязательно заходите еще!''')
                print("-" * 55)
                egg = input('            Для выхода нажмите Enter: ')
                if egg == "1979":
                    easter_egg()  # Тут находиться пасхалка. Если пользователь ввёл 'конец' и потом написал '1979' это отсылка на самую первую пасхалку в играх.
                else:
                    sys.exit()
            if end == 'заново':
                Game_replay()
        if end not in ['конец', 'заново']:  # тут находиться проверка если пользователь ввёл не 'конец' или 'заново'
            while True:
                end = input('введите "Конец" или "Заново": ')
                if end in ['конец', 'заново']:
                    if end == 'конец':
                        print(f'''{name_gamer}, было очень приятно что вы поиграли в мою игру💖
            обязательно заходите еще!''')
                        print("-" * 55)
                        egg = input('            Для выхода нажмите Enter: ')
                        if egg == '1979':
                            easter_egg()
                        else:
                            sys.exit()
                    if end == 'заново':
                        Game_replay()
