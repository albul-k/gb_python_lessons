print("""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
""")


def user_info(first_name: str, second_name: str, birthdate: str, current_city: str, email: str, phone_number: str) -> str:
    """[summary]

    Arguments:
        first_name {str} -- Имя
        second_name {str} -- Фамилия
        birthdate {str} -- Дата рождения
        current_city {str} -- Город проживания
        email {str} -- Электронная почта
        phone_number {str} -- Номер телефона

    Returns:
        str -- Данные пользователя
    """
    return f'{first_name} {second_name} {birthdate} {current_city} {email} {phone_number}'


params = {
    'first_name': 'Имя',
    'second_name': 'Фамилия',
    'birthdate': 'Дата рождения',
    'current_city': 'Город проживания',
    'email': 'Электронная почта',
    'phone_number': 'Номер телефона',
}

params_input = {}
for key, value in params.items():
    params_input[key] = input(f'{value}: ')

info = user_info(
    phone_number=params_input['phone_number'],
    email=params_input['email'],
    current_city=params_input['current_city'],
    birthdate=params_input['birthdate'],
    second_name=params_input['second_name'],
    first_name=params_input['first_name']
)

print(info)
