print("Вывести все числа кратные 7 в выбраном диапазоне")
x = int(input(("Введите начало диапазона:")))
y  = int(input(("Введите конец диапазона:")))
for i in range(x,y+1):
   if i % 7 == 0:
      print(i)