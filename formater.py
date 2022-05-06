

# Module for formqting the expression

# --- Formatinf for control ----
#  

def number_of_operator(exp): # return the number of operators found in a mathematical expression
    operator = '+-*/='
    count = 0
    for c in exp:
        if operator.find(c) != -1:
            count += 1
    return count

def operator_isolator(exp): # Isolate operator operators with a specific charactor
    operator = '+-*/='
    returned_exp = []
    part = ''
    operator_number = number_of_operator(exp)
    operator_number_count = 0
    
    for i in range(len(exp)):
        c = exp[i]
        part += c

        if operator.find(c) != -1:
            returned_exp.append(part[:-1])
            returned_exp.append(c)
            operator_number_count += 1
            part = ''
        elif i == (len(exp) - 1) and operator_number_count == operator_number:
            returned_exp.append(part)
            continue

    return returned_exp

def space_deleter(term, c = ' '): # Delete space in form an expression
    return term.replace(c, '')

def exp_space_deleter(exp_splited):
    for i in range(len(exp_splited)):
        exp_splited[i] = space_deleter(exp_splited[i])
    return exp_splited

# ----

def init_formating(exp):
    return exp_space_deleter(operator_isolator(exp))

# ------

exp = input('Your expression please : ')

print(init_formating(exp))