def extract_numbers_from_string(data):
    numbers = []
    current_number = ""
    for char in data:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                numbers.append(int(current_number))
            current_number = ""
    if current_number:
        numbers.append(int(current_number))
    return numbers

def classify_numbers_as_odd_or_even(numbers):
    odd_numbers = []
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return odd_numbers, even_numbers

user_input = input("Enter numbers separated by spaces: ")
numbers_list = extract_numbers_from_string(user_input)
odd_numbers, even_numbers = classify_numbers_as_odd_or_even(numbers_list)

print("Odd numbers:")
print(odd_numbers)
print("Even numbers:")
print(even_numbers)
