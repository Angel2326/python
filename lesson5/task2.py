# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

#first variant
count = 0
with open('text_3.txt',encoding='utf-8') as f:  # открытие в режиме чтения
    for line in f:
        print (f'{count+1} строка: {len(line.split())} слова')
        count += 1
    print ('Количество строк: ', count)
    print('')

#second variant
count = 0
with open('text_3.txt', 'r', encoding='utf-8') as f:
    textlines = f.read()
    for line in textlines:
        print(f'{count + 1} строка: {len(line.split())} слова')
        count += 1
    print ('Количество строк: ', count)


