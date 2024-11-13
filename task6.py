# Функція для зчитування масиву з файлу
def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        array = list(map(int, file.read().split()))
    return array

def after_seventh_zero(array):
    zero_positions = [i for i, x in enumerate(array) if x == 0]

    if len(zero_positions) >= 7:
        seventh_zero_pos = zero_positions[6]
        after_elements = array[seventh_zero_pos + 1:]
        return len(after_elements), sum(after_elements)
    else:
        return 0, 0

# Зчитування масиву з файлу
array_from_file = read_array_from_file('generated_array.txt')

count, total_sum = after_seventh_zero(array_from_file)
print(f"Кількість елементів після 7-го нульового елемента: {count}")
print(f"Сума елементів після 7-го нульового елемента: {total_sum}")
