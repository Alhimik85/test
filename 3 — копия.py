#исходная строка asdxfghyxyx
#заменить буквы х на у
x="asdxfghyxyxx"
y=""
for	x in x:
	if x == "x":
		y +="y"
	else:
		y +=x

print('Исходная строка:',x)
print('Измененная строка:',y)

#замена строк х на у без дополнительной
str1 = 'asdxfghyxyxx'
str2 = str1.replace('x','y')
print(str1, str2)
