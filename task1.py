s = 'Дом, в котором мы живём, — это не просто дом. В доме живут люди, и люди эти делают дом домом. Без людей дом — просто стены, а стены без дома и без людей — уже не дом, а коробка.'

alf = 'ёйцукенгшщзхъфывапролджэячсмитьбю'   # приводим в порядок текст  
ALF = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
for i in range(len(s)):
	if s[i] in ALF: 
		s = s[:i] +  alf[ALF.index(s[i])] + s[i+1:]
	elif s[i] not in alf and s[i] not in ALF and s[i] != ' ':
		if i == len(s) - 1:
			s = s[:-1] + ' '
		else:
			s = s[:i]+' ' +s[i+1:]
s = s[:-1]
s = s.replace('  ', ' ').replace('  ', ' ')

ss = s.split(' ')    # преобразуем сторку в список слов
kol_words = len(ss)
kol_unik_words = len(list(set(ss)))
print(f"Всего слов: {kol_words}, из них уникальных: {kol_unik_words}")


# создаем словарь, считающий количесвто поторов
chastota = {}
for i in ss:
	key = i
	if key not in chastota: chastota[key] = 1
	else: chastota[key] +=1

# сортируем словаь
chastota1 = chastota      # в будущем понадобиться копия изначальног словаря
chastota = dict(sorted(chastota.items()))
chastota = dict(sorted(chastota.items(), key = lambda item: -item[1]))   #сортируем по уменьшению словарь

# находим топ-5 и сращу записываем в строку для вывода
ans_chas = 'Топ-5 слов:'
n = 0    # выводим топ-5 самых частых слов с нумерацией
for word, col in chastota.items():
    n += 1
    if n<=5: ans_chas += f" {word} ({col}),"
ans_chas = ans_chas[:-1]

print(ans_chas)

# сортируем список по длине слов
chastota1 = dict(sorted(chastota1.items(), key = lambda item: len(item[0]), reverse = True))
bol_dlina = len(next(iter(chastota1)))
dlin = ''
for word, kol in chastota1.items():
	if len(word) == bol_dlina: dlin += word +  ', ' 
dlin = dlin[:-2]
print(f"Самое длинное слово: {dlin}")

# перезаписываем наш список - вместо слов, их длина
for i in range(len(ss)): 
	ss[i] = len(ss[i])

# создаем новый словарь по длине слов
dlina = {}
for i in ss:
	key = i
	if key not in dlina: dlina[key] = 1
	else: dlina[key] += 1
dlina = dict(sorted(dlina.items()))
print(f"Слова по длинам: {dlina}")
