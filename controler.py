from formater import color

enable_operators = '+-*/='
enable_parameters = 'abcdefghijklmnopqrstuvwxyz'
enable_numbers = '0123456789'
# Control function

## **************** PERSONAL INPUT *****************

def controled_input(message):
    while True:
        try:
            response = input(message)
            if response == 'y':
               break

            elif response == 'n':
                break

            elif response == 's':
               break

            else:
                print('Please make sure to enter y or n.\nIf you want to quit the program entre s.\n')
        
        except KeyboardInterrupt:
            print('Something went wrong !')
            response = 's'
            break

    return response

## **************** STRANGE OPERATOR FOUND ******************

def strange_operator_checker(exp):
    for c in exp.lower():
        if c == ' ':
            continue

        if enable_operators.find(c) == -1 and enable_parameters.find(c) == -1 and enable_numbers.find(c) == -1:
            return {'result' : True,
                    'element' : c}
    
    return {'result' : False}

def strange_operator_reporter(exp):
    if strange_operator_checker(exp)['result']:
        return {'message' : color('-> ERROR >> ', 'FAIL') + "I don't understand this operator : " + color(strange_operator_checker(exp)['element'], 'FAIL')}
    return {'message' : 'Nothing suspect !'}

## **************** EQUALITY REDUNDANT ******************

def equal_redundant_checker(exp):
    count = 0
    for c in exp:
        if c == '=':
            count += 1
    
    return {'result' : True, 'count' : count} if count > 1 else {'result' : False, 'count' : count}

def equal_redundant_reporter(exp):
    #-----------------------------------------------------------------------------
    # This function is complete and is aware to make a comment whatever 
    # the number of equal operator found is.

    # equal_operator_count = equal_redundant_checker(exp)['count']
    # comment_extension = ' equal operator found.'.replace('equal operator', 'equal operators') if equal_operator_count > 1 else ' equal operator found.'
    
    # return {'message' : color('\n-> ', 'FAIL') + 'Your expression has ' + color(str(equal_operator_count) + comment_extension, 'FAIL') + ' Please correct it !' \
    #         if equal_redundant_checker(exp)['result'] else 'No equal operator found.' \
    #             if equal_operator_count == 0 else 'All is clean.' \
    #                 if equal_operator_count == 1 else 'Something went wrong !'}
    #
    #-----------------------------------------------------------------------------
    #
    # This part of the function is aware to make a simple comment of the redundant checker function
    return {'message' : color('\n-> ERROR >> ', 'FAIL') + 'Your expression has ' + color(str(equal_redundant_checker(exp)['count']) + ' equal operators found.', 'FAIL') + ' Please correct it !'}
    
## **************** OPERATORS REDUNDANT ERRORS ******************

def redundant_operators_error_checker(exp): # Return a tuple bool, and term
    operators_ref = ['+-', '++', '+*', '+/',
                     '--', '-+', '-*', '-/',
                     '*-', '*+', '**', '*/',
                     '/-', '/+', '/*', '//',
                     '=-', '=+', '=*', '=/',
                     '-=', '+=', '*=', '/=']

    term_found = ()
    for term in operators_ref:
        if exp.find(term) != -1 and term not in term_found:
            term_found += (term, )

    return {'result' : False, 'element' : term_found} if len(term_found) == 0 else {'result' : True, 'element' : term_found}

def redundant_operator_error_reducer(exp, tuple_terms): # Reduces in operator scope
    
    # ----------------------------------------------------
    # 0 -> -
    # 1 -> +
    # 2 -> * Except : '*-' (1), '*/' (2),
    # 3 -> / Except : '/-' (1), '/*' (2),
    # 4 -> = Except : '=-' (1),

    reducable_operator_terms = (['+-', '-+'],
                                ['--', '++'],
                                ['*+', '**', '+*', '-*'],
                                ['/+', '//', '+/', '-/'],
                                ['=+', '=*', '=/', '-=', '+=', '*=', '/='])

    # Note number :
    # '->' means 'is reduced to' or 'is resolved to'
    # (1) The program can progress
    # (2) The anbiguity has to be raised. The user has to make a joice between '*' and  '/' operators
    # ----------------------------------------------------

    for terms in tuple_terms:
        if terms in reducable_operator_terms[0]:
            exp = exp.replace(terms, '-')
        elif terms in reducable_operator_terms[1]:
            exp = exp.replace(terms, '+')
        elif terms in reducable_operator_terms[2]:
            exp = exp.replace(terms, '*')
        elif terms in reducable_operator_terms[3]:
            exp = exp.replace(terms, '/')
        elif terms in reducable_operator_terms[4]:
            exp = exp.replace(terms, '=')
    return exp

def redundant_operators_error_reporter(exp):
    return {'message' : color('\n-> ERROR >> ', 'FAIL') + 'Strange term found : ' + color(', '.join(list(redundant_operators_error_checker(exp)['element'])), 'FAIL') + \
             color('\n\n-> correction required. ', ['ITALIC', 'BLUE'])}

def redundant_operator_error_reducer_reporter(exp):
    if redundant_operators_error_checker(exp)['result'] and exp != redundant_operator_error_reducer(exp, redundant_operators_error_checker(exp)['element']):
        return {'message' : redundant_operators_error_reporter(exp)['message'] + \
                '\n   Is this expression what you meant ? ' + color(redundant_operator_error_reducer(exp, redundant_operators_error_checker(exp)['element']), 'BLUE') + '\n',
                'exp' : redundant_operator_error_reducer(exp, redundant_operators_error_checker(exp)['element'])}
    
    elif redundant_operators_error_checker(exp)['result'] and exp == redundant_operator_error_reducer(exp, redundant_operators_error_checker(exp)['element']):
        return {'message' : redundant_operators_error_reporter(exp)['message'],
            'exp' : exp}

    return {'message' : ' -> All is perfect !\n',
            'exp' : exp}

#-----------------------------------------

# def init_control_all_once(exp):
#     message_error = ''
#     for test_number in range(3):
#         if test_number == 0:
#             if equal_redundant_checker(exp)['result']:
#                 message_error += '\n' + equal_redundant_reporter(exp)['message']
#         elif test_number == 1:
#             if strange_operator_checker(exp)['result']:
#                 message_error += '\n' + strange_operator_reporter(exp)['message']
#         elif test_number == 2:
#             if redundant_operators_error_checker(exp)['result']:
#                 message_error += '\n' + 'I don\'t know.'
    
#     return {'result' : True if len(message_error) == 0 else False,
#             'message_error' : 'Configuration required' if len(message_error) == 0 else message_error}

def init_control_by_setp(exp):

    for test_number in range(3):
        if test_number == 0:
            if equal_redundant_checker(exp)['result']:
                return {'result' : False,
                        'feedback' : equal_redundant_reporter(exp)['message'],
                        'exp' : exp}

        elif test_number == 1:
            if strange_operator_checker(exp)['result']:
                return {'result' : False,
                        'feedback' : strange_operator_reporter(exp)['message'],
                        'exp' : exp} 

        elif test_number == 2:
            if redundant_operators_error_checker(exp)['result'] and exp != redundant_operator_error_reducer(exp, redundant_operators_error_checker(exp)['element']):
                print(redundant_operator_error_reducer_reporter(exp)['message'])
                
                response = controled_input(color('->', 'BLUE') + ' y - yes / n - no / s - to stop : ')
                if response == 'y':
                    return {'result' : True,
                            'feedback' : redundant_operator_error_reducer_reporter(exp)['message'],
                            'exp' : redundant_operator_error_reducer_reporter(exp)['exp']}

                elif response == 'n':
                    return {'result' : False,
                            'feedback' : 'restart',
                            'exp' : redundant_operator_error_reducer_reporter(exp)['exp']}

                elif response == 's':
                    return {'result' : False,
                            'feedback' : 'abort',
                            'exp' : redundant_operator_error_reducer_reporter(exp)['exp']}

            elif redundant_operators_error_checker(exp)['result'] and exp == redundant_operator_error_reducer(exp, redundant_operators_error_checker(exp)['element']):
                return {'result' : True,
                        'feedback' : redundant_operator_error_reducer_reporter(exp)['message'],
                        'exp' : exp}
    
    return {'result' : True,
            'feedback' : 'All is ok !',
            'exp' : exp}