# Импортируйте необходимые модули
from datetime import datetime as dt

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if len(data) ==2 and data[0]!=None and data[1]!=None:
        result = True
    else:
        result = None
    return result

def check_correct_time(time):
    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True
    if storage_data!={}:
        if time<=max(storage_data):
            result=False
        else:
            result=True
    else:
        result=False
    return result

def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    result=sum(storage_data.values())+steps
    return result

def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    result=(sum(storage_data.values())+steps)*STEP_M/1000
    return result

def get_currenttime(time):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    result=(sum(storage_data.values())+time)
    return result

def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени;
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.
    hours=current_time.hour+current_time.minute/60
    mean_speed=dist/hours
    result=(K_1*WEIGHT+(mean_speed**2/HEIGHT)*K_2*WEIGHT)*hours*60

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.
    pass

# Место для функции show_message.


def accept_package(data):
    """Обработать пакет данных."""

    if  not check_correct_data(data):# Если функция проверки пакета вернет False
        return 'Некорректный пакет'

    # Распакуйте полученные данные.
    pack_time = dt.strptime(data[0],FORMAT).time() # Преобразуйте строку с временем в объект типа time.

    if check_correct_time(pack_time): # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1]) # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(data[1]) # Запишите результат расчёта пройденной дистанции.
    current_time=get_currentime(data[0]) #
    spent_calories = get_spent_calories (dist,current_time) # Запишите результат расчёта сожжённых калорий.
    # achievement =  # Запишите выбранное мотивирующее сообщение.
    # Вызовите функцию show_message().
    # Добавьте новый элемент в словарь storage_data.
    storage_data.update(data)
    # Верните словарь storage_data.
    return storage_data


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)