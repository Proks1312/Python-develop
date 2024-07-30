def personal_sum(numbers):
    """
    Функция подсчета суммы чисел в коллекции и количества некорректных данных.

    :param numbers: Коллекция чисел
    :return: Кортеж (result - сумма чисел, incorrect_data - количество некорректных данных)
    """
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += float(item)  # Преобразуем в float, чтобы обработать int и float
        except (ValueError, TypeError):
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    """
    Функция вычисления среднего арифметического чисел в коллекции.

    :param numbers: Коллекция чисел
    :return: Среднее арифметическое всех чисел или 0 при делении на 0 или None при некорректных данных
    """
    if not isinstance(numbers, (list, tuple)):
        print('В numbers записан некорректный тип данных')
        return None

    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0:
            return 0
        average = total_sum / (len(numbers) - incorrect_data)  # Учтем только корректные данные
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
