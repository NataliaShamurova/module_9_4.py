#Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: x == y, first, second))
print(res)


#Замыкание:
def get_advanced_writer(file_name):
    #with open(file_name, 'w', encoding='utf-8')
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:

        #Записываем в файл
                file.writelines(str(i) + '\n')
    return write_everything

write = get_advanced_writer('1.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())