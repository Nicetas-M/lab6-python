def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        array = list(map(int, file.read().split()))
    return array

# Зчитування масиву
array_from_file = read_array_from_file('generated_array.txt')
print("Зчитаний масив:", array_from_file)
