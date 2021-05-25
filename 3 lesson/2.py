def person_info(name, surname, year, city, email, telephone):
    result = f'{surname} {name}, {year} года рождения проживает в городе {city}. Контактные данные: {email}, {telephone}'
    return result

print(person_info(name = 'Иван', surname = 'Иванов', year = '1900', city = 'Иваново', email = 'mail@mail.ru', telephone = '89001234567'))