#Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить,
# кто будет делать очередной модуль нового курса.

# Формат входных данных
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.

# Формат выходных данных
# Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.

def start_game():
    timur = input()
    ruslan = input()

    if timur == ruslan:
        print("ничья")
    else:
        if timur == "ножницы":
            if ruslan == "камень":
                print("Руслан")
            else:
                print("Тимур")
        elif timur == "камень":
            if ruslan == "бумага":
                print("Руслан")
            else:
                print("Тимур")
        else:
            if ruslan == "ножницы":
                print("Руслан")
            else:
                print("Тимур")