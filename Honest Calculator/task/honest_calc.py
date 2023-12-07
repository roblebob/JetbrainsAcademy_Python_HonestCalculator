# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
digits = "0123456789"
opers = "+-*/"

is_valid = False

while not is_valid:

    calc = input(msg_0)

    x, oper, y = calc.split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in opers:
        print(msg_2)
        continue

    is_valid = True
