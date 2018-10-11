# 实现一个带括号的四则运算，用栈

from structures.stack import Stack


def calculate(equation):
    number_stack = Stack()
    action_stack = Stack()
    res = None

    return res


if __name__ == "__main__":
    while True:
        equation = input('请输入算式:')
        if equation is 'exit':
            break
        print('结果为：', calculate(equation))


