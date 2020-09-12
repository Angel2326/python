def user_info(name, lastname, birth_year,city_living,e_mail,phone_number):
    return [f'Информация о пользователе: Имя - {name},Фамилия - {lastname}, Год рождения - {birth_year}',
            f'Город проживания - {city_living}, Почта - {e_mail}, Номер телефона - {phone_number}']
print (user_info(phone_number = '8(999)9999999',e_mail= 'Ivanov@mail.ru',city_living='Париж',birth_year = 1980,
                 lastname = 'Ivanov', name = 'Ivan' ))