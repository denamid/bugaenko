print("Введите два числа для анализа диапазона")
x = int(input("Начало диапазона: "))
y = int(input("Конец диапазона: "))
for i in range ( x, y + 1):
   if i % 3 == 0 and i %5 != 0:
      print("Fizz")
   elif i % 5 == 0:
         print("Buzze")
   elif i % 3 == 0 and i % 5 == 0:
         print("Fizz Buzz")
   else:
      print(i)