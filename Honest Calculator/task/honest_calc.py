# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

memory = 0.0


def assign_var(s):
    global memory
    if s == "M":
        return memory
    try:
        return float(s)
    except ValueError:
        return None


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
        return x / y


def is_one_digit(x):
    return x.is_integer() and -10 < x < 10


def check(x, oper, y):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg = msg + msg_7
    if (x == 0 or y == 0) and oper in "*+-":
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


finished = False
while not finished:

    print(msg_0)
    x, oper, y = input().split()

    x, y = assign_var(x), assign_var(y)
    if x is None or y is None:
        print(msg_1)
        continue

    if oper not in "+-*/":
        print(msg_2)
        continue

    check(x, oper, y)

    result = calculator(x, oper, y)

    if result is None:
        print(msg_3)
        continue

    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            finished = True






