for_11_16 = {'10': 'A',
             '11': 'B',
             '12': 'C',
             '13': 'D',
             '14': 'E',
             '15': 'F'}

eror_response = 'Не верно число или его система'
NeedSyst = 'Введите нужную вам систему:'
SystInfo = 'Введите систему этого числа:'


def checking_the_number(numder_or_letter):
    # Возвращает число из числа или буквы
    if numder_or_letter.isdigit() and int(numder_or_letter) < 10:
        return int(numder_or_letter)
    else:
        for number, letter in for_11_16.items():
            if numder_or_letter == letter:
                return int(number)


def per_v_des(chislo, sistem):
    for one in chislo:
        if checking_the_number(one) >= sistem:
            return eror_response
    if len(chislo) > 1:
        otv = checking_the_number(chislo[0]) * sistem
        for i in chislo[1:len(chislo) - 1]:
            checking = checking_the_number(i)
            otv += checking
            otv = otv * sistem
        otv += checking_the_number(chislo[len(chislo) - 1])
        return str(otv)
    else:
        return str(checking_the_number(chislo))


def per_iz_des(chislo, sist):
    if chislo.isdigit():
        chislo = int(chislo)
        otv = ''
        while chislo >= sist:
            last = chislo % sist
            if last < 10:
                otv += str(last)
            else:
                for number, letter in for_11_16.items():
                    if str(last) == number:
                        otv += letter
            chislo = chislo // sist

        if chislo < 10:
            otv += str(chislo)
        else:
            for number, letter in for_11_16.items():
                if str(chislo) == number:
                    otv += letter
        return otv[::-1]
    else:
        return eror_response


while True:
    print('Выберете действие:\n'
          '1.Перевод из одной системы в другую-\n'
          '2.Сложение(+)\n'
          '3.Вычетание(-)\n'
          '4.Умножение(*)\n'
          '5.Деление(:)\n'
          '6.Stop-')

    inf_response = str(input('Введите цифру действия из списка:'))

    if inf_response == '1':
        # перевод
        number_in_dec = per_v_des(str(input('Ведите число:')),
                                  int(input(SystInfo)))
        if number_in_dec == eror_response:
            print(eror_response)
            continue
        print(per_iz_des(number_in_dec,
              int(input(NeedSyst))))

    elif inf_response == '2':
        # сложение
        firstnum = per_v_des(str(input('Ведите 1ое число:')),
                             int(input(SystInfo)))
        sekondnum = per_v_des(str(input('Ведите 2ое число:')),
                              int(input(SystInfo)))

        sum = int(firstnum) + int(sekondnum)
        print(per_iz_des(str(sum), int(input(NeedSyst))))

    elif inf_response == '3':
        # вычетание
        firstnum = per_v_des(str(input('Ведите 1ое (большее) число:')),
                             int(input(SystInfo)))
        sekondnum = per_v_des(str(input('Ведите 2ое число:')),
                              int(input(SystInfo)))

        difference = int(firstnum) - int(sekondnum)
        print(per_iz_des(str(difference), int(input(NeedSyst))))

    elif inf_response == '4':
        # умножение
        firstnum = per_v_des(str(input('Ведите 1ое число:')),
                             int(input(SystInfo)))
        sekondnum = per_v_des(str(input('Ведите 2ое число:')),
                              int(input(SystInfo)))

        multiplication = int(firstnum) * int(sekondnum)
        print(per_iz_des(str(multiplication), int(input(NeedSyst))))

    elif inf_response == '5':
        # деление
        firstnum = per_v_des(str(input('Ведите 1ое (большее) число:')),
                             int(input(SystInfo)))
        sekondnum = per_v_des(str(input('Ведите 2ое число:')),
                              int(input(SystInfo)))

        multiplication = int(firstnum) // int(sekondnum)
        print(per_iz_des(str(multiplication), int(input(NeedSyst))))

    elif inf_response == '6':
        break
