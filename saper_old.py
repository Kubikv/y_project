import random


def saper():
    print('Добро пожаловать в игру - Сапер' + '\n'
          'Выберете уровень сложности:' + '\n'
          '1 - легкий(6*6 и 5 мин)' + '\n'
          '2 - средний(10*8 и 10 мин)' + '\n'
          '3 - сложный(18*14 и 20 мин)')
    dif = int(input())
    print('Игра очень проста.' + '\n'
          'Вам нужно открыть все клетки,где нет мин.' + '\n'
          'Если вы открываете клетку с миной,то вы проиграли.' + '\n'
          'При нажатии на клетку, среди соседей которой нет мин,'
          ' открываются также все соседние с ней клетки.' + '\n'
          'при открытии пустой клетки,все пустые клетки расположенные'
          ' рядом будут открыты, процесс продолжается рекурсивно.' + '\n'
          'И последнее - вы можете оставлять отметки:' + '\n'
          'Флаг - flag x y.' + '\n'
          'Вопрос - question x y или q x y.' + '\n'
          'И убирать их:' + '\n'
          'Флаг - flag_d x y.' + '\n'
          'Вопрос - question_d x y или q_d x y' + '\n'
          'Приятной игры!' + '\n'
          '-----------------------------------------' + '\n'
          'Выберете клетку с которой хотите начать.'
          'Чтобы выбрать клетку введите команду "open x y",'
          'где x - это координата клетки по горизонтали,'
          'а y - по вертикали')
    hidden_field(dif)


def hidden_field(difficulty):
    first_coords = input().split()
    global kolvo_v, kolvo_g, kolvo_mines
    if difficulty == 1:
        kolvo_v = 6
        kolvo_g = 6
        kolvo_mines = 5
    elif difficulty == 2:
        kolvo_v = 8
        kolvo_g = 10
        kolvo_mines = 10
    elif difficulty == 3:
        kolvo_v = 14
        kolvo_g = 18
        kolvo_mines = 20
    spisok = list(map(lambda x: 'm' if x < kolvo_mines else '0', range(
        kolvo_v * kolvo_g)))
    sxd = list(map(lambda x: 'f', range(kolvo_v * kolvo_g)))
    spisok_show = list(map(lambda x: ' ', range(kolvo_v * kolvo_g)))
    flag = True
    while flag:
        random.shuffle(spisok)
        if spisok[(int(first_coords[2]) - 1) * kolvo_g + int(
                first_coords[1]) - 1] == 'm':
            continue
        else:
            flag = False
    for i in range(1, kolvo_v + 1):
        for g in range(kolvo_g):
            if spisok[(i - 1) * kolvo_g + g] == 'm':
                for n in range(-1, 2):
                    for m in range(-1, 2):
                        if m == 0 and n == 0:
                            continue
                        if spisok[(abs((i - 1 + n)) % kolvo_v) * kolvo_g + (
                                abs(g + m)) % kolvo_g] != 'm':
                            if (i - 1 + n) >= kolvo_v or (g + m) >= kolvo_g:
                                continue
                            if (g + m) < 0:
                                continue
                            if i - 1 + n < 0:
                                continue
                            spisok[(abs((i - 1 + n)) % kolvo_v) * kolvo_g + (
                                abs(g + m)) % kolvo_g] = \
                                str(int(spisok[(abs((i - 1 + n)) % kolvo_v) *
                                    kolvo_g + (abs(g + m)) % kolvo_g]) + 1)
    # for i in range(1, kolvo_v + 1):
        # for g in range(kolvo_g):
            # print('[' + spisok[(i - 1) * kolvo_g + g] + ']', end='')
        # print()
    if spisok[(int(first_coords[2]) - 1) * kolvo_g + int(
            first_coords[1]) - 1] != 'm':
        spisok_show[(int(first_coords[2]) - 1) * kolvo_g + int(
            first_coords[1]) - 1] = 'empty'
        if spisok[(int(first_coords[2]) - 1) * kolvo_g + int(
                first_coords[1]) - 1] == '0':
            spisok_show = set_clear(spisok, first_coords, spisok_show, sxd)
    for i in range(1, kolvo_v + 1):
        for g in range(kolvo_g):
            if spisok_show[(i - 1) * kolvo_g + g] == 'empty':
                print(' ' + spisok[(i - 1) * kolvo_g + g], end=' ')
            else:
                print('[' + spisok_show[(i - 1) * kolvo_g + g] + ']', end='')
        print()
    flag = True
    while flag:
        command = input().split()
        if command[0].lower() == 'open':
            first_coords = command
            if spisok[(int(first_coords[2]) - 1) * kolvo_g + int(
                    first_coords[1]) - 1] != 'm':
                spisok_show[(int(first_coords[2]) - 1) * kolvo_g + int(
                    first_coords[1]) - 1] = 'empty'
                if spisok[(int(first_coords[2]) - 1) * kolvo_g + int(
                        first_coords[1]) - 1] == '0':
                    spisok_show = set_clear(spisok,
                                            first_coords, spisok_show, sxd)
            else:
                flag = False
                game_end()
                break
        if command[0].lower() == 'flag':
            spisok_show[(int(command[2]) - 1) * kolvo_g + int(
                command[1]) - 1] = 'f'
        if command[0].lower() == 'q' or command[0].lower() == 'question':
            spisok_show[(int(command[2]) - 1) * kolvo_g + int(
                command[1]) - 1] = '?'
        if command[0].lower() == 'flag_d':
            spisok_show[(int(command[2]) - 1) * kolvo_g + int(
                command[1]) - 1] = ' '
        if command[0].lower() == 'q_d' or command[0].lower() == 'question_d':
            spisok_show[(int(command[2]) - 1) * kolvo_g + int(
                command[1]) - 1] = ' '
        for i in range(1, kolvo_v + 1):
            for g in range(kolvo_g):
                if spisok_show[(i - 1) * kolvo_g + g] == 'empty':
                    print(' ' + spisok[(i - 1) * kolvo_g + g], end=' ')
                else:
                    print('[' + spisok_show[(
                          i - 1) * kolvo_g + g] + ']', end='')
            print()
        if check_win(spisok_show, spisok):
            flag = False


def set_clear(s, f_c, s_s, sxd):
    if s[(int(f_c[2]) - 1) * kolvo_g + int(f_c[1]) - 1] != 'm':
        s_s[(int(f_c[2]) - 1) * kolvo_g + int(f_c[1]) - 1] = 'empty'
        sxd[(int(f_c[2]) - 1) * kolvo_g + int(f_c[1]) - 1] = 'x'
        if s[(int(f_c[2]) - 1) * kolvo_g + int(f_c[1]) - 1] == '0':
            for n in range(-1, 2):
                for m in range(-1, 2):
                    if m == 0 and n == 0:
                        continue
                    if s[(abs((int(f_c[2]) - 1 + n)) % kolvo_v) * kolvo_g +
                         (abs(int(f_c[1]) + m - 1)) % kolvo_g] != 'm':
                        if (int(f_c[2]) - 1 + n) >= kolvo_v or (
                           int(f_c[1]) + m - 1) >= kolvo_g:
                            continue
                        if (int(f_c[1]) + m - 1) < 0:
                            continue
                        if int(f_c[2]) - 1 + n < 0:
                            continue
                        s_s[(abs((int(f_c[2]) - 1 + n)) % kolvo_v) * kolvo_g +
                            (abs(int(f_c[1]) + m) - 1) % kolvo_g] = 'empty'
            for n in range(-1, 2):
                for m in range(-1, 2):
                    if m == 0 and n == 0:
                        continue
                    if s[(abs((int(f_c[2]) - 1 + n)) % kolvo_v) * kolvo_g +
                         (abs(int(f_c[1]) + m - 1)) % kolvo_g] != 'm':
                        if (int(f_c[2]) - 1 + n) >= kolvo_v or (int(
                           f_c[1]) + m - 1) >= kolvo_g:
                            continue
                        if (int(f_c[1]) + m - 1) < 0:
                            continue
                        if int(f_c[2]) - 1 + n < 0:
                            continue
                        if s[(abs((int(
                            f_c[2]) - 1 + n)) % kolvo_v) * kolvo_g + (
                                abs(int(f_c[1]) + m - 1)) % kolvo_g] == '0':
                            if sxd[(abs((int(
                                f_c[2]) - 1 + n)) % kolvo_v) * kolvo_g + (
                                    abs(int(
                                        f_c[1]) + m - 1)) % kolvo_g] != 'x':
                                f_c = ['open', str(
                                    int(f_c[1]) + m), str(int(f_c[2]) + n)]
                                s_s = flag(s, f_c, s_s, sxd)
            return s_s


def flag(s, f_c, s_s, sxd):
    b = set_clear(s, f_c, s_s, sxd)
    return b


def game_end():
    print('THE END' + "\n"
          'Вы проиграли:(' + "\n"
          'Хотите сыграть еще раз?')
    answer = input()
    if answer.lower() == 'yes' or answer.lower() == 'да':
        game_restart()
    else:
        print('Было приятно поиграть,до встречи:)')


def check_win(s_s, s):
    flag_check = True
    for i in range(len(s_s)):
        if s_s[i] == ' ':
            if s[i] != 'm':
                flag_check = False
                break
            flag_check = False
            break
        elif s_s[i] == '?':
            if s[i] != 'm':
                flag_check = False
                break
        elif s_s[i] == 'f':
            if s[i] != 'm':
                flag_check = False
                break
    if flag_check:
        print('ПОООООООООООООББББББЕЕЕЕЕЕЕЕЕЕДДДДДДАААААААААА!!!!!!!' + "\n"
              'Хочешь сыграть еще раз?')
        answer = input()
        if answer.lower() == 'yes' or answer.lower() == 'да':
            game_restart()
        else:
            print('Было приятно поиграть,до встречи:)')
        return True


def game_restart():
    print('Выберете сложность.')
    dif = int(input())
    hidden_field(dif)


saper()
