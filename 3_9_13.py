def change_case(s, mode):
    if mode == "1":
        return s.upper()
    elif mode == "2":
        return s.lower()
    elif mode == "3":
        return s.swapcase()
    else:
        return "Невірний вибір!"

s = input("Введіть рядок: ")
print("1: Перетворити всі маленькі літери на великі")
print("2: Перетворити всі великі літери на маленькі")
print("3: Змінити регістр літер")
mode = input("Оберіть режим (1/2/3): ")
print(change_case(s, mode))
