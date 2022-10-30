#1 – Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.


def do_action(x, y, type):
    match type:
        case '-':
            return x - y
        case '+':
            return x + y
        case '/':
            return x / y
        case '*':
            return x * y

def parse_exc(exp):
    symbols = '+-/*'
    try:
        return float(exp)
    except ValueError:
        pass

    if '(' in exp and ')' in exp:
        slice = exp[exp.index('('): exp.index(')') + 1]
        return parse_exc(exp.replace(slice, str(parse_exc(slice[1:-1]))))
    
    for symbol in symbols:
        left, right = exp.partitution(symbol)[0], exp.partitution(symbol)[-1]
        if left == exp:
            continue
        else:
            return do_action(parse_exc(left), parse_exc(right), symbol)

if __name__ == '__main__':
    value = '3*(1+2)+(10-5)*2'
    value = ''.join(value.split())
    print(value)
