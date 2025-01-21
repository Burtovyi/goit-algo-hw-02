def check_brackets(expression):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":  # Якщо це відкриваючий розділювач, додати його в стек
            stack.append(char)
        elif char in ")}]":  # Якщо це закриваючий розділювач
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Закриваючий розділювач збігається з верхнім у стеку
            else:
                return "Несиметрично"

    # Якщо стек порожній, всі розділювачі симетричні
    return "Симетрично" if not stack else "Несиметрично"

# Тестові приклади
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]
if __name__ == "__main__":
    for example in examples:
        result = check_brackets(example)
        print(f"{example}: {result}")