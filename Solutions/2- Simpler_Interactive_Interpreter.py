import re

##From Math expression kata
def without_para(exp):
    numbers = []
    ops = []
    exp = "".join(exp.split())
    i = 0
    while i < len(exp):
        num = ""
        while i < len(exp) and exp[i] not in "+-*/%":
            num += exp[i]
            i+=1
        numbers.append(num)
        if i != len(exp):
            ops.append(exp[i])
            i+=1
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
    while "*" in ops or "/" in ops or "%" in ops:
        count_star = find_index(ops,"*")
        count_div = find_index(ops, "/")
        count_mod = find_index(ops, "%")
        if count_star < count_div and count_star < count_mod:
            ops.pop(count_star)
            operand_a = numbers.pop(count_star)
            operand_b = numbers.pop(count_star)
            numbers.insert(count_star, float(operand_a) * float(operand_b))
        elif count_div < count_star  and count_div < count_mod:
            ops.pop(count_div)
            operand_a = numbers.pop(count_div)
            operand_b = numbers.pop(count_div)
            numbers.insert(count_div, float(operand_a) / float(operand_b))
        else:
            ops.pop(count_mod)
            operand_a = numbers.pop(count_mod)
            operand_b = numbers.pop(count_mod)
            numbers.insert(count_mod, float(operand_a) % float(operand_b))
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
        a = with_para(exp[start+1:i-1])
        return with_para(exp[:start] + str(a) + exp[i:])

def calc(exp):
    #Added modulo to Math exp kata
    return with_para(exp)



def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        if re.match(r"^ *$", expression):
            return ""
        if re.match(r"^(\d+ *)*$", expression):
            raise ValueError("error")
        tokens = tokenize(expression)
        expression = expression.replace(" ", "")
        reg_valid = re.compile(r"^(\d+[+\-*/%])+\d+$")
        if re.match(reg_valid, expression):
            return calc(expression)

        elif len(tokens) == 1 and tokens[0] in self.vars:
            return self.vars[tokens[0]]

        elif len(tokens) == 1 and tokens[0] not in self.vars:
            # Should give an error
            return self.vars[tokens[0]]

        elif tokens[1] == "=":
            tmp = expression[2:]
            for i in self.vars:
                tmp = tmp.replace(i,str(int(self.vars[i])))
            self.vars[tokens[0]] = int(calc(tmp))
            return self.vars[tokens[0]]

        else:
            tmp = expression
            for i in self.vars:
                tmp = tmp.replace(i, str(int(self.vars[i])))
            return calc(tmp)
