# write your code here

msg_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]

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
        msg = msg + msg_[6]
    if (x == 1 or y == 1) and oper == "*":
        msg = msg + msg_[7]
    if (x == 0 or y == 0) and oper in "*+-":
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


def store_result(value):
    global memory
    msg_index = 10 if is_one_digit(value) else None
    while msg_index is not None:

        print(msg_[msg_index])
        _answer = input()
        if _answer not in "yn":
            continue
        elif _answer == "n":
            return

        msg_index = msg_index + 1 if _answer == "y" and msg_index < 12 else None

    memory = value


finished = False
while not finished:

    print(msg_[0])
    x, oper, y = input().split()

    x, y = assign_var(x), assign_var(y)
    if x is None or y is None:
        print(msg_[1])
        continue

    if oper not in "+-*/":
        print(msg_[2])
        continue

    check(x, oper, y)

    result = calculator(x, oper, y)

    if result is None:
        print(msg_[3])
        continue

    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_[4])
        answer = input()
        if answer == "y":
            store_result(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_[5])
        answer = input()
        if answer == "n":
            finished = True






