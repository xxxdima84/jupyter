print("У Мэри был маленький барашек.") # печать строки У Мэри был маленький барашек.
print("Его шерсть была белой как {}.". format('снег')) # печать строки  Его шерсть была белой как с добавлением форматированной стоки'снег'
print("И всюду, куда Мэри шла, ") # печать строки "И всюду, куда Мэри шла, "
print("Маленький барашек всегда следовал за ней.") # печать строки Маленький барашек всегда следовал за ней.
print("."*10) # что это могло значить? -- умножение строки "." 10

end1 = "Б"   # объявили переменную end1 = "Б" 
end2 = "а"   # объявили переменную end2 = "а"
end3 = "д"   # объявили переменную end3 = "д" 
end4 = "д"   # объявили переменную end4 = "д" 
end5 = "и"   # объявили переменную end5 = "и"
end6 = "Г"   # объявили переменную end6 = "Г" 
end7 = "а"   # объявили переменную end7 = "а"
end8 = "й"   # объявили переменную end8 = "й" 

# Обратите внимние на запятую в конце строки уберите ее. Что произошло? -- будет ошибка SyntaxError: invalid syntax

print(end1 + end2 + end3 + end4 + end5, end='' ) # Склеивание переменных end1 = "Б" + end2 = "а" end3 = "д" end4 = "д" end5 = "и" 
print(end6 + end7 + end8) # Склеивание переменных  end6 = "Г" end7 = "а" end8 = "й"