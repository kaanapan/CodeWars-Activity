def without_para(exp):
    numbers = []
    ops = []
    exp = "".join(exp.split())
    i = 0
    while i < len(exp):
        num = ""
        while i < len(exp) and exp[i] not in "+-*/":
            num += exp[i]
            i+=1
        numbers.append(num)
        if i != len(exp):
            ops.append(exp[i])
            i+=1
    print(numbers)
    print(ops)
    #Complete double minuses
    j = 0
    while j < len(numbers):
        if numbers[j] == "":
            numbers.pop(j)
            a = numbers.pop(j)
            ops.pop(j)
            minus = True
            while a == "":
                minus = not minus
                a = numbers.pop(j)
                ops.pop(j)
            if minus:
                numbers.insert(j,-float(a))
            else:
                numbers.insert(j, float(a))
        j+=1
    print(numbers)
    print(ops)
    #Finish * and /
    while "*" in ops or "/" in ops:
        count_star = find_index(ops,"*")
        count_div = find_index(ops, "/")
        if count_star < count_div:
            ops.pop(count_star)
            operand_a = numbers.pop(count_star)
            operand_b = numbers.pop(count_star)
            numbers.insert(count_star, float(operand_a) * float(operand_b))
        else:
            ops.pop(count_div)
            operand_a = numbers.pop(count_div)
            operand_b = numbers.pop(count_div)
            numbers.insert(count_div, float(operand_a) / float(operand_b))

    while "+" in ops or "-" in ops:
        count_plus = find_index(ops,"+")
        count_minus = find_index(ops, "-")
        if count_plus < count_minus:
            ops.pop(count_plus)
            operand_a = numbers.pop(count_plus)
            operand_b = numbers.pop(count_plus)
            numbers.insert(count_plus, float(operand_a) + float(operand_b))
        else:
            ops.pop(count_minus)
            operand_a = numbers.pop(count_minus)
            operand_b = numbers.pop(count_minus)
            numbers.insert(count_minus, float(operand_a) - float(operand_b))
    return float(numbers[0])

def find_index(l, op):
    for i in range(len(l)):
        if l[i] == op:
            return i
    return 10000

def with_para(exp):
    if "(" not in exp:
        return without_para(exp)
    else:
        exp = "".join(exp.split())
        start = exp.find("(")
        i = start + 1
        opener_count = 1
        while opener_count != 0:
            if exp[i] == ")":
                opener_count -=1
                i +=1
            elif exp[i] == "(":
                opener_count += 1
                i +=1
            else:
                i +=1
        print("start : ", start, " end : ", i-1)
        a = with_para(exp[start+1:i-1])
        return with_para(exp[:start] + str(a) + exp[i:])

def calc(exp):
    print(exp)
    return with_para(exp)