# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."


def calculator(x, oper, y):
    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/":
        if y == 0:
            return None
        else:
            return x / y


is_valid = False

while not is_valid:

    x, oper, y = input(msg_0).split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in "+-*/":
        print(msg_2)
        continue

    result = calculator(x, oper, y)

    if result is None:
        print(msg_3)
        continue
    else:
        is_valid = True
        print(result)


