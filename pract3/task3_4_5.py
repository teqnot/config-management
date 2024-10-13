import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

# Задание 3
BNF = '''
E = B | B E
B = 0 | 1
'''

# Задание 4
# BNF = '''
# E = P | C
# P = (E) | ()
# C = {E} | {}
# '''

# Задание 5
# BNF = '''
# E = T | E "|" T
# T = F | T "&" F
# F = "~" F | "(" E ")" | VAR
# VAR = x | y | z
# '''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))