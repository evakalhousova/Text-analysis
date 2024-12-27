"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Eva Kalhousová
email: eva.kalhousova@gmail.com
discord: evakalhousova
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

username = input('Username: ')
password = input('Password: ')
print('-' * 40)

registered_users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

if registered_users.get(username) == password:
    print(f'Welcome to the app, {username}!')
    print('We have 3 texts to be analyzed.')
    print('-' * 40)
else:
    print('Unregistered user, terminating the program.')
    exit()

text_number = input('Enter a number btw. 1 and 3 to select: ')
print('-' * 40)

text_number_correct = [1, 2, 3]

if not text_number.isnumeric():
    print('Entered data is not a number, terminating the program.')
    exit()
elif int(text_number) not in text_number_correct:
    print('There is no text with such a number, terminating the program.')
    exit()

analyzed_text = TEXTS[int(text_number)-1]

analyzed_text_stripped = analyzed_text.replace('.', '').replace(',', '')            # Odstranění čárek a teček.

analyzed_text_list = analyzed_text_stripped.split()

title_list = []
for word in analyzed_text_list:
    if word.istitle():
        title_list.append(word)

upper_list = []
for word in analyzed_text_list:
    if word.isupper() and word.isalpha():           # isalpha aby to nepočítalo slovo '30N'.
        upper_list.append(word)

lower_list = []
for word in analyzed_text_list:
    if word.islower() and word.isalpha():
        lower_list.append(word)

numeric_list = []
for word in analyzed_text_list:
    if word.isnumeric():
        numeric_list.append(int(word))

print(f'There are {len(analyzed_text_list)} words in the selected text.')
print(f'There are {len(title_list)} titlecase words.')
print(f'There are {len(upper_list)} uppercase words.')
print(f'There are {len(lower_list)} lowercase words.')
print(f'There are {len(numeric_list)} numeric strings.')
print(f'The sum of all the numbers: {sum(numeric_list)}.')
print('-' * 40)

word_length = []
for word in analyzed_text_list:
    length = len(word)
    word_length.append(length)

print('LEN|', '{:^18}'.format('OCCURRENCES'), '|NR.')
print('-' * 40)

counts = {}
for number in word_length:
    if number not in counts:
        counts[number] = 1
    else:
        counts[number] = counts[number] + 1
for key, value in sorted(counts.items()):
    print(f"{key:>3}|{'*' * value:<20}|{value}")
