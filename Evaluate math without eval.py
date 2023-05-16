from operator import add, sub, mul, truediv


class Calc:

    def __init__(self) -> None: pass

    @staticmethod
    def __call__(exp: str) -> int | float:
        '''
        Функтор
        :param exp:
        :return:
        '''
        res1 = Calc.calc_all(Calc.remove_minus(Calc.remove_parentheses(Calc.space(exp))))[0]
        try:
            return int(res1) if int(res1) - float(res1) == 0 else float(res1)
        except ValueError:
            return float(res1)

    @staticmethod
    def space(expression: str) -> list:
        '''
        разделяет все элементы проблемами
        :param expression:
        :return:
        '''
        expression = expression.replace(' ', '')  # убираем пробелы уже присутсвующие в выражении
        tmp_lst = ''
        tmp = ''
        for i in expression:
            if i in '+-*/()':  # добавляем число в список если находим знак или скобку
                tmp_lst = tmp_lst + tmp + ' '
                tmp = i
                tmp_lst = tmp_lst + tmp + ' '
                tmp = ''
            elif i.isdigit() or i == '.':  # собираем целое или вещественно число
                tmp = tmp + i
        return (tmp_lst + tmp).split()

    @staticmethod
    def remove_minus(expression: list) -> list:
        '''
        Проверка на дубликаты '-' либо на отрицательные числа
        :param expression:
        :return:
        '''
        for k, v in enumerate(expression):
            #  проверяем есть ли дубликаты знаков
            if v in {'+', '-', '*', '/'} and expression[k + 1] in '-':
                if expression[k + 2] in '-':
                    expression[k + 1] = None
                    expression[k + 2] = None
                else:
                    expression[k + 2] = str('-' + str(expression[k + 2])).replace('--', '+')
                    expression[k + 1] = None
        expression = list(filter(lambda z: z, [i for i in expression if i != '--']))
        # ищем отрицательные числа
        if expression[0] == '-':
            expression[0] = None
            expression[1] = str('-' + expression[1]).replace('--', '')
        # Исключаем пустые значения и дубликаты '-'
        expression = list(filter(lambda z: z, [i for i in expression if i != '--']))
        return expression

    @staticmethod
    def calc_exp(args: list) -> str:
        '''
        считает фрагмент выражения
        :param args:
        :return:
        '''
        operation = {'+': add,
                     '-': sub,
                     '*': mul,
                     '/': truediv}
        return operation.get(args[1])(float(args[0]), float(args[2]))

    @staticmethod
    def calc_all(expression):
        '''
        Считает все выражение
        :param expression:
        :return:
        '''
        while len(expression) > 1:
            if '*' in expression or '/' in expression:  # очередность действий
                if '*' not in expression:
                    k = expression.index('/')
                elif '/' not in expression:
                    k = expression.index('*')
                else:
                    k = min([expression.index('*'), expression.index('/')])
                expression[k - 1] = Calc.calc_exp(expression[k - 1: k + 2])
                expression.pop(k)
                expression.pop(k)
            else:
                res = Calc.calc_exp(expression)
                expression = [res, *expression[3:]]
        return expression

    @staticmethod
    def remove_parentheses(expression):
        '''
        Вычесление выражения в скобках
        :param expression:
        :return:
        '''
        if {'(', ')'}.isdisjoint(expression):  # проверяем на наличие скобок
            return expression
        left_pos = 0  # Позиция последней открывающей скобки
        for k, v in enumerate(expression):
            left_pos = k if v == '(' else left_pos
            if v == ')':
                tmp1 = expression[left_pos + 1:k]  # содержимое скобок
                if len(tmp1) > 2:  # Если в скобках выражение вычисляем его.
                    tmp1 = Calc.calc_all(Calc.remove_minus(tmp1))
                expression = list(map(str, expression[:left_pos] + tmp1 + expression[k + 1:]))
                if not {'(', ')'}.isdisjoint(expression):
                    expression = Calc.remove_parentheses(expression)
                return expression


calc = Calc()