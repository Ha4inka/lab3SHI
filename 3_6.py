def print_letters(n):
    letters = [print_letter_r(i) for i in range(1, n + 1)]
    for row in zip(*letters):
        print("  ".join(row))

def print_letter_r(n):
    return [
        " ___   ",
        f"|    \\ ",
        f"|  {n}  |",
        "| ___/ ",
        "|      ",
        "|      "
    ]

n = int(input("Введіть число від 1 до 9: "))
print_letters(n)
