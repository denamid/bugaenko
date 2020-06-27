print("Введите текст, для проверки полиморфности")
string = input("Текст для проверки: ").replace(' ', '').lower()
back_string = string[::-1]
if back_string == string:
    print("Полиморф")
else:
    print("Не полиморф")