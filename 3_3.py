def unique_words(sentence):
    words = set(sentence.split())
    return list(words)

sentence = input("Введіть речення: ")
print("Унікальні слова:", unique_words(sentence))
