print("Введите два числа для анализа диапазона")
x = input("Начало диапазона: ")
y = input("Конец диапазона: ")
if (x).lstrip("-""+").isdigit() == False or (y).lstrip("-""+").isdigit() == False :
   print("Вы должны были ввести числа, а не буквы или еще какую дичь, в следующий раз будьте внимательнее\nошибка программы \nпопробуйте еще раз")
   x = input("Начало диапазона: ")
   y = input("Конец диапазона: ")
x=int(x)
y=int(y)
txt_menu = ("1 - вывести на экран все числа этого диапазона включительно  \n2 - вывести все числа этого диапазона включительно в обратном порядке "
			"\n3 - вывести все числа кратные 7 включительно \n4 - вывести количество чисел кратных 5 включительно\n5 - изменить начало и конец диапазона\n6 - Закончить работу программы"
			" \nвыберите функцию : ")
print(txt_menu)          #Заранее создаем переменную с текстом, чтоб каждый раз не прописывать сам текст к меню
nomer = int(input())
while True:
	while True:
		if nomer >= 1 and nomer <= 6:    #Если хотите добавить функционал, увеличьте максимальное значение nomer и сам функционал
			break
		nomer = int(input("Вы выбрали несуществующий функционал, попробуйте еще раз: "))
	if nomer == 1:
		print("Все числа диапазона:") or print(list(range(x, y + 1)))
		print(txt_menu)
		nomer = int(input())  #Вновь выбираем функционал
	elif nomer == 2:
		print("Все числа диапазона в обратном порядке:") or print(list(range(x, y + 1))[::-1])
		print(txt_menu)
		nomer = int(input())   #Вновь выбираем функционал
	elif nomer == 3:
		print("Числа кратные '7':")
		for i in range(x, y + 1):
			if i % 7 == 0:
				print(i)
		print(txt_menu)
		nomer = int(input())     #Вновь выбираем функционал
	elif nomer == 4:
		print("Количество цифр кратных '5':")
		num = 0
		for i in range(x, y + 1):
			if i % 5 == 0:
				num += 1
		print(num)
		print(txt_menu)
		nomer = int(input())     #Вновь выбираем функционал
	elif nomer == 5:
		x = int(input("Начало диапазона: "))
		y = int(input("Конец диапазона: "))
		print(txt_menu)
		nomer = int(input())        #Вновь выбираем функционал
	elif nomer == 6:
		print("Спасибо что воспользовались моей нелепой программой, всего хорошего BRO\nхотя, постой, друг. Точно хочешь выйти с программы, ничего не забыл?")
		l = input("1 - Спасибо что напомнили, хочу просмотреть еще некоторые диапазоны (запустить программу заново\n"
					  "Любое значение - Очень не хочу покидать на самом деле эту чудесную прорамму, спасибо БОГУ что существуют такие программисты как ты, но к сожалению на этом все\n"
					  ":")
		if l == "1":
			print(txt_menu)
			nomer = int(input())
		else:                                    #Нужно ведь и похвалить пользователя, за использование программы, а вдруг вернется еще))
			i = 0
			while 1 == 1:
				print("Красавичик, ты лучший, молодец, возращайся, у тебя все получится, Life is Good, ты неповторимый")
				i = i + 1
				if i == 300000:
					break
			exit()
