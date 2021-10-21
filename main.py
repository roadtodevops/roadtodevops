# country = {4: 3}
# country = {True: 3}
# country = {(5, 6): 3}
# print(country[4])
# print(country[(5, 6)])


# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# country = dict(code='RU', name='Russian', population=144)

# print(country)
# print(country.items())

# for key, value in country.items():
#     print(key, '-', value)

# country.clear()

# print(country.get('name'))
# country.popitem()
# print(country.items())
# print(country.values())
# print(country.keys())
# country.pop('name')

# country.update()

# country['code'] = 'None'
#
# print(country.items())

person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Marley',
        'age': 45,
        'address': ('г. Москва', 'ул. Какая-то', '45'),
        'grades': {'math': 5, 'physics': 3}
    },
    'user_2': {

    }
}



print(person['user_1']['grades']['physics'])