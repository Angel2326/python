n = int(input('Введите количество элементов списка'))
my_list = []
for i in range(n):
    my_list.append(int(input(f'Введите {i + 1}-й элемент списка')))
print(my_list)
k = 0
while k < len(my_list):
    my_list.insert(k + 2, my_list[k])
    my_list.pop(k)
    k += 2
print(my_list)
