def count_substring(s, sub):
    count = 0
    index = 0
    while index < len(s):
        index = s.find(sub, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

s = input("Введіть рядок: ")
sub = input("Введіть підрядок: ")
print(f"Кількість входжень підрядка: {count_substring(s, sub)}")
