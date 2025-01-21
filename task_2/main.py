from collections import deque

def is_palindrome(s: str) -> bool:
    # Приводимо рядок до нижнього регістру та видаляємо всі пробіли
    sanitized_string = ''.join(char.lower() for char in s if char.isalnum())

    # Створюємо двосторонню чергу і додаємо до неї всі символи
    char_deque = deque(sanitized_string)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Приклад використання
if __name__ == "__main__":
    test_string = "A man a plan a canal Panama"
    print(f"'{test_string}' є паліндромом: {is_palindrome(test_string)}")
