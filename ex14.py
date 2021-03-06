from sys import argv

script, user_name, first = argv
print("Моя первая программа называется:",first)
promt = '>'

print(f"Привет, {user_name}, я сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я тебе нравлюсь, {user_name}?")
likes = input(promt)

print(f"Где ты живешь, {user_name}?")
lives = input(promt)

print("На каком компютере ты работаешь?")
computer = input(promt)

print(f"""
Итак ты ответил {likes} На вопрос нравлюсь ли я тебе.
Ты живешь{lives}. Не представляю где это.
И у тебя есть компютер {computer}. И это Прекрасно!
 """)
