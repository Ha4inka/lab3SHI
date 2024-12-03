def find_frequent_chars(s, chars):
    char_counts = {char: s.count(char) for char in chars}
    max_count = max(char_counts.values())
    return [char for char, count in char_counts.items() if count == max_count]

s = input("Введіть рядок: ")
chars = set(input("Введіть символи множини через пробіл: ").split())
print("Символи, які зустрічаються найчастіше:", find_frequent_chars(s, chars))
