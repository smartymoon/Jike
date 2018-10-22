import re
from structures.stack import Stack


def action_weight(action):
    actions = [
        ('+', 1),
        ('-', 1),
        ('*', 2),
        ('/', 2),
        ('(', 0),
    ]
    for item in actions:
        if item[0] == action:
            return item[1]


def FullToHalf(s):
    n = []
    for char in s:
        num = ord(char)
        if num == 0x3000:
            num = 32
        elif 0xFF01 <= num <= 0xFF5E:
            num -= 0xfee0
        num = chr(num)
        n.append(num)
    return ''.join(n)


def reform_equation(equation):
    # clean equation
    equation = re.sub('\s', '', FullToHalf(equation))

    # reform equation
    if equation.startswith('-'):
        equation = '0' + equation

    equation = equation.replace('(-', '(0-')
    return equation


def make_equations(equation):
    # split equation
    equations = re.split('([\+\-\*\/\(\)])', equation)
    equations = [it for it in equations if it is not '']
    equations.reverse()
    return equations


def calculator(equation):
    error = "算式不合法"
    number_stack = Stack()
    action_stack = Stack()

    equation = reform_equation(equation)
    equations = make_equations(equation)

    def do_cal():
        one = number_stack.pop()
        two = number_stack.pop()

        res = 0
        action = action_stack.pop()
        if action == '*':
            res = two * one
        if action == '-':
            res = two - one
        if action == '+':
            res = two + one
        if action == '/':
            res = two / one

        number_stack.push(res)

    def got_number(number):
        number_stack.push(number)

    def got_action(action):
        # 非常复杂
        if action == ')':
            # 直到遇到 '(' 才停止计算,遇不到则报错
            while action_stack.last() is not '(':
                do_cal()
            action_stack.pop()
            return
        if action == '(' or action_stack.if_empty() or action_weight(action) > action_weight(action_stack.last()):
            action_stack.push(action)
            return

        do_cal()
        action_stack.push(action)

    while len(equations) is not 0:
        item = equations.pop()
        if item in ['*', '-', '(', '+', ')', '/']:
            try:
                got_action(item)
            except IndexError:
                return error
            except ZeroDivisionError:
                return '错误，除数出现 0'
            except Exception as E:
                return str(E)
        else:
            try:
                got_number(float(item))
            except ValueError:
                return error

    # 把列表中的内容全部弹出，返回最后一个数
    while action_stack.len() > 0:
        try:
            do_cal()
        except IndexError:
            return error
        except ZeroDivisionError:
            return '错误，除数出现'

    if number_stack.len() is not 1:
        return error
    return number_stack.pop()


if __name__ == "__main__":
    while True:
        equation = input('请输入算式: ')
        if equation == 'exit':
            break
        print(calculator(equation))
