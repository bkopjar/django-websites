if __name__ == '__main__':

    birthdays = {
        'Albert Einstein': '14/03/1879',
        'Benjamin Franklin': '17/01/1706',
        'Ada Lovelace': '10/12/1815',
        'Donald Trump': '14/06/1946',
        'Rowan Atkinson': '06/01/1955'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))