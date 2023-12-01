import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

def generate_random_vector(elements):
    return [random.randint(1, 20) for _ in range(elements)]

def multiply_matrix_and_vector(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("The number of columns in the matrix should be equal to the number of elements in the vector")

    result = []
    for row in matrix:
        row_sum = sum(row[j] * vector[j] for j in range(len(vector)))
        result.append(row_sum)

    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

def write_list_to_file(filename, content):
    try:
        with open(filename, 'w') as txt_file:
            for item in content:
                txt_file.write(f"{item}\n")
    except FileNotFoundError:
        print("Error: The new file could not be created.")

random_matrix = generate_random_matrix(4, 7)
random_vector = generate_random_vector(7)

print("The matrix:")
display_matrix(random_matrix)

print("Vector:")
print(random_vector)

result_vector = multiply_matrix_and_vector(random_matrix, random_vector)
print("Result:")
print(result_vector)

write_list_to_file("output_file.txt", result_vector)
