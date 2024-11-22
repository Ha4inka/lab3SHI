def count_digits(s):
    return sum(1 for char in s if char.isdigit())

s = input("Введіть рядок: ")
print(f"Кількість цифр у рядку: {count_digits(s)}")
