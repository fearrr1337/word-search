text = input('Введите текст: ')
word = input('Введите слово, которое вы хотите найти: ')

index = text.lower().find(word.lower())

if index != -1:
    print(f'Слово {word} находится на позиции: {index}')
else:
    print(f'Слово {word} не найдено в списке')

