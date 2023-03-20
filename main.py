# Импортируйте необходимые модули
import datetime
import string

FORMAT = '%H:%M:%S'
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(package):
    """
    Проверка корректности полученного пакета.

    :param package: time and steps
    :type package: tuple

    """
    if len(package) != 2 or None in package:
        return False
    else:
        return True


def check_correct_time(time) -> bool:
    """
    Проверка корректности параметра времени.

    :param time: description
    :type time: int

    :return description
    :rtype: str
    """
    if len(storage_data) != 0 and time <= max(storage_data):
        return False
    else:
        return True


def get_step_day(data) -> int:
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.

    steps = sum(list(data.values()))
    return steps


def get_distance(steps) -> int:
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    dist = steps * STEP_M
    return dist


def get_spent_calories(dist, current_time) -> float:
    """Получить значения потраченных калорий."""
    time = float(datetime.datetime.strptime(current_time, '%H,%M'))
    mean_speed = dist / time
    minutes = time * 60
    spent_calories = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * minutes
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.
    return spent_calories


def get_achievement(dist) -> str:
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return f'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return f'Неплохо! День был продуктивный'
    elif dist >= 2:
        return f'Завтра наверстаем!'
    else:
        return f'Лежать тоже полезно. Главное — участие, а не победа!'


# Место для функции show_message.


def accept_package(data):
    """Обработать пакет данных."""

    if not check_correct_data(data):
        return 'Некорректный пакет'
    else:

        # Распакуйте полученные данные.
        pack_time = data[0]
        # Преобразуйте строку с временем в объект типа time.
        pack_time = datetime.datetime.strptime(pack_time, FORMAT)

        if not check_correct_time(pack_time):
            return 'Некорректное значение времени'
        else:

            day_steps = get_step_day(storage_data)
            dist = get_distance(day_steps)
            spent_calories = get_spent_calories(dist, data[0])
            achievement = get_achievement(day_steps)
            storage_data[pack_time] = day_steps
            show_message(storage_data)
            # Вызовите функцию show_message().
            # Добавьте новый элемент в словарь storage_data.
            # Верните словарь storage_data.
            return storage_data


def show_message(data):
    ...


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
