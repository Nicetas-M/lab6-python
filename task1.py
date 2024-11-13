import random


def generate_array():
    # Генерація масиву з 50 елементів, значення яких від -99 до 99
    array = [random.randint(-99, 99) for _ in range(50)]

    # Додавання мінімальних елементів (від 3 до 4 однакових мінімальних елементів)
    min_value = min(array)
    min_count = random.randint(3, 4)
    for _ in range(min_count):
        array[array.index(min_value)] = min_value

    # Додавання 20% нульових елементів
    num_zeros = int(len(array) * 0.2)
    zero_positions = random.sample(range(len(array)), num_zeros)
    for pos in zero_positions:
        array[pos] = 0

    # Повертаємо отриманий масив
    return array


# Генерація масиву
array = generate_array()

# Збереження масиву в файл
with open('generated_array.txt', 'w') as file:
    file.write(' '.join(map(str, array)))
