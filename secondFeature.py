"""Расчет арифмитических выражений через обратную польскую нотацию"""

OPS = ["+", "-", "*", "/", "(", ")"]


def prior(op):
    """Получить приоритет операции"""
    if op in ["+", "-"]:
        return 1
    elif op in ["*", "/"]:
        return 2
    elif op == "(":
        return -1
    elif op == ")":
        return 0


def toPostfix(s):
    """Преобразовать инфиксную нотацию в постфиксную"""
    operations = []
    result = []
    for symbol in s:
        if symbol not in OPS:
            result.append(symbol)
        else:
            if operations:
                if prior(symbol) == 0:
                    while operations[-1] != "(":
                        result.append(operations.pop(-1))
                    operations.pop(-1)
                elif prior(symbol) == -1:
                    operations.append(symbol)
                elif prior(operations[-1]) >= prior(symbol):
                    result.append(operations.pop(-1))
                    operations.append(symbol)
                else:
                    operations.append(symbol)
            else:
                operations.append(symbol)
    while operations:
        result.append(operations.pop(-1))

    return result


def calcPostfix(s):
    """Расчитать значение выражения в постфиксной нотации"""
    numbers = []
    for el in s:
        if el in OPS:
            a, b = numbers.pop(-2), numbers.pop(-1)
            if el == "+":
                numbers.append(a + b)
            elif el == "-":
                numbers.append(a - b)
            elif el == "/":
                numbers.append(a / b)
            elif el == "*":
                numbers.append(a * b)

        else:
            numbers.append(int(el))
    return numbers[0]


def strToInfixList(s):
    """Преобразовать строку в список операндов и операций"""
    s = s.replace(" ", "")
    result = []
    buff = ''
    for symbol in s:
        if symbol in OPS:
            if buff:
                result.append(buff)
                buff = ''
            result.append(symbol)
        else:
            buff += symbol
    if buff:
        result.append(buff)

    return result


def calculate(s):
    try:
        s = strToInfixList(s)
        s = toPostfix(s)
        s = calcPostfix(s)
        return f"Значение: {s}"
    except Exception as error:
        print(error)
        return "Упс, что то пошло не так"


if __name__ == "__main__":
    while True:
        s = input("Выражение:")
        if s == "-1":
            break
        print("Значение:", calculate(s))
