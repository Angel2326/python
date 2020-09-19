# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_dict = {1 :'один',2:'два',3:'три', 4:'четыре'}
with open('text_4_1.txt', 'w', encoding='utf-8') as f1:
    with open('text_4.txt', 'r', encoding='utf-8') as f:  # открытие в режиме чтения
        textlines = f.readlines()
        for line in textlines:
            line_list = line.split()
            line_list[0] = my_dict[int(line_list[2])]
            new_str = ' '.join(line_list)
            f1.write(new_str+'\n')