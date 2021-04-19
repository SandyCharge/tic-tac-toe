def change_str(number, string, letter):  # Редактирование строки
    game[number[0]] = string[:number[1] * 2] + letter + string[number[1] * 2 + 1:]
    return 0


def control(user):  # Проверка выигрышных комбинаций
    for i in winner:
        if i == user.intersection(
                i):  # Сравниваем два множества с использованием intersection - пересечения двух множеств
            print("Игрок ", 1 if id(user) == id(user_1) else 2, "победил")
            return 1
    return 0


def enter(user):  # Ввод нового значения X или O
    number = input("Введите числа без пробелов - ")
    number_tuple = tuple(map(int, number))

    if (number_tuple[0] > 3 or number_tuple[1] > 3) or (
            number_tuple[0] <= 0 or number_tuple[1] <= 0):  # Проверка на корректное значение
        print("Значение  должно быть от 1 до 3")
        return 0

    user.add(number)
    change_str(number_tuple, game[number_tuple[0]], 'x' if id(user) == id(user_1) else 'o')
    for i in game:
        print(i)
    return 0


def step(user):  # Ход игроком
    if len(user) < 2:
        enter(user)
    else:
        enter(user)
        if control(user):
            print("Игра окончена")
            return 1
    return 0


def start():  # Стартовая функция выбирает игрока
    if len(user_1) <= len(user_2):
        print("Ходит игрок - 1 ")
        if step(user_1):
            return 1
    else:
        print("Ходит игрок - 2 ")
        if step(user_2):
            return 1
    return 0


game = ["  1 2 3", "1 - - -", "2 - - -", "3 - - -"]
winner = [{"11", "12", "13"}, {"21", "22", "23"}, {"31", "32", "33"}, {"11", "21", "31"}, {"12", "22", "32"},
          {"31", "32", "33"}, {"11", "22", "33"}, {"13", "22", "31"}]
user_1 = set()
user_2 = set()

for i in game:
    print(i)
print("Ввестии пару цифр без пробелов где первая цифра это горизонталь(строка) а вторая цифра это вертикаль(столбец)")
print("Пример: 21, после чего нажмите  кнопку Enter")
i = 0

while i <= 8:
    if start():
        break
    elif i == 8:
        print("Победила дружба")
        break
    i += 1
