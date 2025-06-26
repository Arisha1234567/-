
def check_letters(s: str):
    simbols = ['0' for x in range(26)]
    for letter in s:
        if 97 <= ord(letter.lower()) <= 122:
            index_letter = ord(letter.lower()) - 97
            simbols[index_letter] = '1'

    return ''.join(simbols)

print(check_letters('ABcd'))
print(check_letters('A-Z'))
print(check_letters('b*e*e*g*e*e*k'))
print(check_letters('a'))
print(check_letters('Привет!'))
print(check_letters('abcdefghijklmnopqrstuvwxyz'))