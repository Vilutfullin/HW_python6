from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # Переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = current_time.hour >= 22 or current_time.hour < 6

    assert is_dark_theme is True

def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    # Переключите темную тему в зависимости от времени суток,
    # но учтите что темная тема может быть включена вручную
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        # Если пользователь не выбрал тему, то проверяем время
        if time(22, 0) <= current_time <= time(6, 0):
            is_dark_theme = True  # Включаем темную тему после 18:00 и до 6:00
        else:
            is_dark_theme = False  # Светлая тема в остальное время

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]


    for user in users:
        print(user)
        if user["name"]== "Olga":
            user_olga = user



    #  найдите пользователя с именем "Olga"
    assert user_olga == {"name": "Olga", "age": 45}

    #  найдите всех пользователей младше 20 лет
    suitable_users = [i for i in users if i['age'] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def print_function_info(func, *args, **kwargs):
    function_name = func.__name__.replace("_", " ").title()
    arguments = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"{function_name} [{arguments}]")

def open_browser(browser_name):
    print_function_info(open_browser, browser_name=browser_name)

def go_to_companyname_homepage(page_url):
    print_function_info(go_to_companyname_homepage, page_url=page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_function_info(find_registration_button_on_login_page, page_url=page_url, button_text=button_text)

