
# Global variables
operator = '+-*/='
# Module for formqting the expression

## ******************* COLOR FORMATING *******************
def color(text, styles):

    ENDC = '\033[0m'

    style_dict = {'HEADER' : '\033[95m',
                  'BLUE' : '\033[94m',
                  'GREEN' : '\033[90m',
                  'WARNING' : '\033[93m',
                  'FAIL' : '\033[91m',
                  'BOLD' : '\033[1m',
                  '2' : '\033[2m',
                  'ITALIC' : '\033[3m',
                  'UNDERLINE' : '\033[4m',
                  'GREYBG' : '\033[100m',
                  'REDBG' : '\033[101m',
                  'GREENBG' : '\033[102m',
                  'YELLOWBG' : '\033[103m',
                  'BLUEBG' : '\033[104m',
                  'PINKBG' : '\033[105m',
                  'CYANBG' : '\033[106m'}

    returned_style = ''
    styles_type = type(styles)

    if styles_type is str:
        returned_style += style_dict[styles] if styles in style_dict else ''
    elif styles_type is list or styles_type is tuple:
        for style in styles:
            returned_style += style_dict[style] if style in style_dict else ''
    else:
        return text

    return returned_style + text + ENDC

# ---- Formatinf for control ----
#  

def number_of_operator(exp): # return the number of operators found in a mathematical expression
    # operator = '+-*/='
    count = 0
    for c in exp:
        if operator.find(c) != -1:
            count += 1
    return count

def operator_isolator(exp): # Isolate operator operators with a specific charactor
    # operator = '+-*/='
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

def operator_joiner(exp_splited): # Join operators with numbers
    # operator = '+-*/='
    i = 0
    while i < len(exp_splited):
        if operator.find(exp_splited[i]) != -1 and len(exp_splited[i]) == 1:
            exp_next = exp_splited[i + 1] if exp_splited[i] != '=' else ''
            exp_previous = exp_splited[i - 1] if i != 0 and exp_splited[i] == '*' or exp_splited[i] == '/' else ''
    
            if i + 1 < len(exp_splited):
                if exp_splited[i] == '+' or exp_splited[i] == '-':
                    exp_splited[i] = exp_previous + exp_splited[i] + exp_next
                    del exp_splited[i + 1]
                    
                elif exp_splited[i] == '*' or exp_splited[i] == '/':
                    exp_splited[i] = exp_previous + exp_splited[i] + exp_next
                    del exp_splited[i + 1]
                    if i != 0:
                        del exp_splited[i - 1]
        i += 1
    return exp_splited

def space_deleter(term, c = ' '): # Delete space in form an expression
    return term.replace(c, '')

def exp_space_deleter(exp_splited): # Delete space in term in the splited format of exp
    for i in range(len(exp_splited)):
        exp_splited[i] = space_deleter(exp_splited[i])
    return exp_splited

def empty_term_deleter(exp_splited):
    i = 0
    while i < len(exp_splited):
        if exp_splited[i] == '':
            del exp_splited[i]
        i += 1
    return exp_splited

#
# ------

def init_formating(exp): 
    # Isolate operators -> 
    # delete spaces in terms -> 
    # delete empty terms -> 
    # join operators with terms except equal operator -> 
    # return the list in string format using join() function
    return ' '.join(operator_joiner(empty_term_deleter(exp_space_deleter(operator_isolator(exp)))))
#
# ------