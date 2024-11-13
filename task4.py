import matplotlib.pyplot as plt

# Функція для зчитування масиву з файлу
def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        array = list(map(int, file.read().split()))
    return array

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

# Виведення зчитаного масиву на екран
print("Зчитаний масив:", array_from_file)

# Візуалізація масиву
visualize_array(array_from_file)
