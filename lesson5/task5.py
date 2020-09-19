# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce
import random
import string

def buildblock(size):
    return ' '.join(random.choice(string.digits) for _ in range(size))


with open('text_5.txt','w+', encoding='utf-8') as f:  # открытие в режиме чтения
    f.write(buildblock(10)) # формируем случайную строку с числами через пробел
    f.seek(0)  # указываем начальную позицию для чтения
    str_ =''.join(f.readlines()) # считываем из файла и переводим в строку
    print('Сумма строки = : ',reduce(lambda x,y: int(x) + int(y), list(str_.replace(' ',''))))