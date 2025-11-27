# Utility functions for working with lists

def get_even_numbers(numbers):
    """Повертає список парних чисел."""
    return [n for n in numbers if n % 2 == 0]


def get_unique_sorted(numbers):
    """Повертає відсортований список унікальних елементів."""
    return sorted(set(numbers))


def average(numbers):
    """Повертає середнє значення списку."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 5, 5, 6]

    print("Початковий список:", data)
    print("Парні числа:", get_even_numbers(data))
    print("Унікальні відсортовані:", get_unique_sorted(data))
    print("Середнє значення:", average(data))
    print("Кількість елементів:", len(data))
