types_of_people = 10 # переменной types_of_people присвоили значение 10
x = f"Существует {types_of_people} типов людей" # в строку Существует (добавлена переменная types_of_people) типов людей

binary = "Python" # в переменной binary присваиваем значение "Python"
do_not = "нет" # в переменной do_not присваиваем значение "нет"
y = f"Те, кто понимает {binary}, и те, кто - {do_not}." #  в форматированную стоку вводим переменную (binary - Python)

print(x) # выводим на печать значение переменной x в строку Существует 10 типов людей
print(y) # выводим на печать значение переменной y  -Те, кто понимает Python, и те, кто - нет.

print(f"Я сказал: {x}")   # выводим на печать форматированную строку - Я сказал: Существует 10 типов людей
print(f"А еще я сказал: '{y}'")  # выводим на печать форматированную строку - А еще я сказал: 'Те, кто понимает Python, и те, кто - нет.'

hilarius = False  # переменной hilarius присвоили значение False
joke_evaluation = "Разве это не смешно ?!{}" # переменной присвоили значение - Разве это не смешно ?!{}

print(joke_evaluation.format(hilarius)) # выводим на печать значение форматированной строки hilarius Разве это не смешно ?!False ( хочу применить форматирование к уже созданной строке)

w = "Это часть строки слева..."  # переменной w присвоили значение "Это часть строки слева"
e = "а это часть строки справа." # переменной e рисвоили значение а это часть строки справа

print(w+e) # выводим на печать склиные строки w + e