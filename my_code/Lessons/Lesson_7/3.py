str =input("Введите текст:")
Str = str.replace("...",".")
num_pred = Str.count(".") + Str.count("!") + Str.count("?")
print(num_pred)