# Функція для зчитування масиву з файлу
def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        array = list(map(int, file.read().split()))
    return array


def find_min_positions(array):
    min_value = min(array)
    min_positions = [i for i, x in enumerate(array) if x == min_value]

    # Перевірка на кількість мінімальних елементів
    if len(min_positions) >= 4:
        return min_positions[2], min_positions[3]  # Третій та четвертий мінімальні елементи
    else:
        print(f"Мінімальних елементів не вистачає. Кількість мінімальних елементів: {len(min_positions)}")
        return None, None

# Зчитування масиву з файлу
array_from_file = read_array_from_file('generated_array.txt')

third_min_pos, fourth_min_pos = find_min_positions(array_from_file)

if third_min_pos is not None and fourth_min_pos is not None:
    print(f"Позиція третього мінімального елемента: {third_min_pos}")
    print(f"Позиція четвертого мінімального елемента: {fourth_min_pos}")
else:
    print("Не вдалося знайти третього та четвертого мінімальних елементів.")