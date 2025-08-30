from collections import deque

def is_palindrom(s: str) -> bool:
    ''' Перевіряє чи вхідний рядок є паліндромом '''

    # Видаляємо пробіли та переводимо в нижній регістр
    normalized_str = ''.join(s.split()).lower()

    # Створюємо двосторонню чергу
    char_deque = deque(normalized_str)

    # Якщо начальна довжина черги менше або рівна 1 то це не паліндром 
    if len(char_deque) <= 1:
        return False

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        first_char = char_deque.popleft()
        last_char = char_deque.pop()

        if first_char != last_char:
            return False
        
    return True

if __name__ == "__main__":
    test_strings = [
        "A man a plan a canal Panama",
        "Аргентина манит негра",
        "Radar",
        "level",
        "hello",
        "No lemon no melon",
        "12321",
        "",
        "a"
    ]

    print("Перевірка на паліндром:")
    for text in test_strings:
        if is_palindrom(text):
            print(f"Рядок '{text}' є паліндромом")
        else:
            print(f"Рядок '{text}' не є паліндромом")