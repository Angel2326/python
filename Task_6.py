# for i in range(2):
my_dict_var = {}
my_dict1 = {}
my_dict2 = {}
my_dict3 = {}
my_list1 = ()
my_list_res = []
user_key = ('название', 'цена', 'количество', 'ед')

user_1 = input(f'Введите через пробел: название товара №{1}, цену, количество, ед:     ')
user_2 = input(f'Введите через пробел: название товара №{2}, цену, количество, ед:     ')
user_3 = input(f'Введите через пробел: название товара №{2}, цену, количество, ед:     ')

user_1_value = list(user_1.split())
user_2_value = list(user_2.split())
user_3_value = list(user_3.split())

for i in range(len(user_key)):
    my_dict1[user_key[i]] = user_1_value[i]
    my_dict2[user_key[i]] = user_2_value[i]
    my_dict3[user_key[i]] = user_3_value[i]

my_dict_var_1 = (1, my_dict1)
my_dict_var_2 = (2, my_dict2)
my_dict_var_3 = (3, my_dict3)
my_list_res.append(my_dict_var_1)
my_list_res.append(my_dict_var_2)
my_list_res.append(my_dict_var_3)
print(my_list_res)
print(my_list_res[0][1].values())
print(my_list_res[1][1].values())
print(my_list_res[2][1].values())

new_list=list(zip(my_list_res[0][1].values(),my_list_res[1][1].values(),my_list_res[2][1].values()))
new_dict =dict(zip(my_list_res[0][1].keys(),new_list))
print(new_dict)
#print(new_dict)













































