import random
# '⛀' = 1  '⛂' = 2  "⬜️" = 4  "⬛️" = 0

a = random.randint(1,2)
if a == 1:
    stol = [["⛂","⬜️"]*4,["⬜️","⛂"]*4,["⛂","⬜️"]*4,["⬜️","⬛️"]*4,["⬛️","⬜️"]*4,["⬜️","⛀"]*4,["⛀","⬜️"]*4,["⬜️","⛀"]*4]
    vrag_fishka = '⛀'
    fishka = '⛂'
else:
    stol = [["⛀","⬜️"]*4,["⬜️","⛀"]*4,["⛀","⬜️"]*4,["⬜️","⬛️"]*4,["⬛️","⬜️"]*4,["⬜️","⛂"]*4,["⛂","⬜️"]*4,["⬜️","⛂"]*4]
    fishka = '⛂'
    vrag_fishka = '⛀'

def print_stol(shashki):
    print("   ", end="")
    for i in range(8):
        print(f'{chr(1072+i)}  ', end='')
    print()
    for i in range(len(shashki)):
        print(i + 1, end=" ")
        for j in shashki[i]:
            print(j, end=" ")
        print()
    return ''

while True:
    print(print_stol(stol))
    move = input("ходят белые, Выбери шашку которой будешь ходить:     ").lower()
    if len(move) != 2:
        print('Должно быть 2 символа')
        continue
    if not move[1].isdigit():
        print('второй символ должен быть цифрой')
        continue
    x = int(move[1]) - 1
    y = ord(move[0]) - 1072
    if 0 <= x < 8 and 0 <= y < 8:
        if stol[x][y] == fishka:
            movetwo = input("Выбери куда ходить:     ").lower()
            if len(movetwo) != 2:
                print('Должно быть 2 символа')
                continue
            if not movetwo[1].isdigit():
                print('второй символ должен быть цифрой')
                continue
            x2 = int(movetwo[1]) - 1
            y2 = ord(movetwo[0]) - 1072
            if 0 <= x2 < 8 and 0 <= y2 < 8:
                try:
                    if stol[x][y] == stol[x2+1][y2-1]:
                        try:
                            if stol[x2][y2] == fishka and stol[x2-1][y2+1] == '⬛':
                                stol[x][y] = '⬛'
                                stol[x2][y2] = '⬛'
                                stol[x2 - 1][y2 + 1] = fishka
                        except IndexError:
                            stol[x][y] = "⬛️"
                            stol[x2][y2] = fishka
                except IndexError:
                    try:
                        if stol[x][y] == stol[x2+1][y2+1]:
                            try:
                                if stol[x2][y2] == fishka and stol[x2-1][y2-2] == '⬛':
                                    stol[x][y] = '⬛'
                                    stol[x2][y2] = '⬛'
                                    stol[x2-1][y2-2] = fishka
                            except IndexError:
                                stol[x][y] = "⬛️"
                                stol[x2][y2] = fishka
                    except IndexError:
                        print('может ходить только на и скосок')
        else:
            print("Не правильно выбрана пешка попробуй ещё раз:")
    else:
        print("Не правильно выброна пешка попробуй ещё раз:")