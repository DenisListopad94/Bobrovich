# 1. Вам дана последовательность строк. Выведите строки, содержащие "cat".

import re

text = """
       doctor cat!
       categories 1
       dog and cat
       manufactured
       *caterpillar$
       cartridge
       Catalonia center
       'catalog' Otto
       certification  
       """

print(re.findall(r'\S*cat\S*', text))

# 2. Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

text = """
       fghjdzoijbfofz rfjev
       zfjgzoprjop
       jgh;zg5Fz
       86hgg9Hzg6@zHGohu6
       byuizfghzzihzih;o
       """
print(re.findall(r'\S*z\S{3}z\S*', text))

# 3. Номер должен быть длиной 10 знаков и начинаться с 8 или 9.
# Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python.

phone_numbers = """
                '456789123'
                '834 45 64 343'
                '9-1-2-3-4-5-6-7-84'
                '9876543214'
                '855-55-66-884'
                '+375 777 77 77'
                """
print(re.findall(r'\'[89](?:\S*\s*\d\S*){9}\'', phone_numbers))

# 4. Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.

text = """
       Карл у Клары украл кораллы,
       а Клара у Карла украла кларнет
       """
print([e.strip() for e in re.findall(r'\s[АЕЁИОУЫЭЮЯаеёиоуыэюя]\w*', text)])

# 5. Дана строка. Вывести все числа этой строки, как отрицательные, так и положительные.

text = """
       3456 kgffg456y57u5kh65 -45 difjv-67dfjnv 5$$$
       """
print(re.findall(r'-*\d+', text))

# 6. В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

print(re.sub(r'\shuman\s', ' computer ', 'A human is the most clever on the Earth. The human can think very fast.'))

# 7. Извлечь дату из строки. Формат даты dd–mm-yyyy.

text = """
       Today is 20-09-2023. 
       Yesterday was 19-09-2023. 
       Tomorrow will be 21-09-2023.
       """
print(re.findall(r'\d\d-\d\d-\d{4}', text))

# 8. Найти все слова, в которых есть хотя бы одна буква ‘b’.

text = """
       area, barber, bonus, fabric, python, computer, b&b
       """
print([e.strip() for e in re.findall(r'\s\S*b+\S*', text)])

# 9. В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.

text = """
       dkjfjjjosaek operwfkkkkkwpwed 930t4jf77gbmjjjdlfv
       """
print(re.sub(r'\w{2,}', '*', text))
