
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

## **************** DELETE SPACES *****************

def space_off(exp):
    return ''.join(exp.split())

def operator_simple_separator(exp):
    exp = space_off(exp)
    exp_splited = []
    exp_splited_term = ''
    count = 0

    while True:
        
        if count < len(exp):
            if exp[count] == '-' or exp[count] == '+' or exp[count] == '=':
                exp_splited.append(exp_splited_term)
                exp_splited.append(exp[count])
                exp_splited_term = ''
                count += 1

            else:
                if exp[count] == '*' or exp[count] == '/':
                    next = 0
                    while True:
                        if count < len(exp):
                            exp_splited_term += exp[count]
                            count += 1
                            if next == 1:
                                break
                            next += 1
                        else:
                            break
                else:
                    exp_splited_term += exp[count]
                    if count == len(exp) - 1:
                        exp_splited.append(exp_splited_term)
                    count += 1

        else:
            break
    
    return exp_splited

def init_formating(exp): 
    # Isolate operators -> 
    # delete spaces in terms -> 
    # delete empty terms -> 
    # join operators with terms except equal operator -> 
    # return the list in string format using join() function
    return ' '.join(operator_simple_separator(exp))
#
# ------