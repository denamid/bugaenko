print("Увеличивымем слова/буквы в тексте:")
string = input("Текст: ")
edit = input("Введите слова или символы которые нужно увеличить(Перевести в верхний регистр): ").lower()

words_list = edit.split()

for x in words_list:
    string=string.replace(x, x.upper())
print(string)