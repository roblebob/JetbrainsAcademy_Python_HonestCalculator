# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0.0


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


def assign_var(s):
    global memory
    if s == "M":
        return memory
    try:
        return float(s)
    except ValueError:
        return None


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

    result = calculator(x, oper, y)

    if result is None:
        print(msg_3)
        continue

    print(result)

    while True:
        print(msg_4)
        answer = input()

        if answer == "y":
            memory = result
            break
        elif answer == "n":
            break

    while True:
        print(msg_5)
        answer = input()

        if answer == "y":
            break
        elif answer == "n":
            finished = True
            break




