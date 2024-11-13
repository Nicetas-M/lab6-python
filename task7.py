import matplotlib.pyplot as plt

# Функція для зчитування масиву з файлу
def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        array = list(map(int, file.read().split()))
    return array

def rearrange_and_sort(array):
    even_positions = [array[i] for i in range(0, len(array), 2)]
    odd_positions = [array[i] for i in range(1, len(array), 2)]

    even_positions.sort()
    odd_positions.sort()

    return even_positions + odd_positions

# Функція для візуалізації масиву
def visualize_array(array):
    min_value = min(array)
    plt.bar(range(len(array)), array, color=['red' if x == min_value else 'blue' for x in array])
    for i, value in enumerate(array):
        if value == min_value:
            plt.text(i, value, str(value), ha='center', va='bottom', color='black')
    plt.xlabel("Індекс")
    plt.ylabel("Значення")
    plt.title("Візуалізація масиву")
    plt.show()

# Зчитування масиву з файлу
array_from_file = read_array_from_file('generated_array.txt')

sorted_array = rearrange_and_sort(array_from_file)
print("Отриманий масив після сортування:", sorted_array)

# Візуалізація отриманого масиву
visualize_array(sorted_array)
