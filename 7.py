import re

def is_identifier(word):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, word))

word = input("Введіть слово: ")
if is_identifier(word):
    print("Це валідний ідентифікатор.")
else:
    print("Це не є валідним ідентифікатором.")
