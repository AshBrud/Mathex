from formater import init_formating, color
from controler import init_control_by_setp



# exp = input('Your expression : ')

# Long test

# exp_list = [['x=3=0'],
#             ['2x+3-=0', '2x+3+=0', '2x+3*=0', '2x+3/=0'],
#             ['2x+3=-0', '2x+3=+0', '2x+3=*0', '2x+3=/0'],
#             ['2x+-3=0', '2x++3=0', '2x+*3=0', '2x+/3=0'],
#             ['2x--3=0', '2x-+3=0', '2x-*3=0', '2x-/3=0'],
#             ['2x*-3=0', '2x*+3=0', '2x**3=0', '2x*/3=0'],
#             ['2x/-3=0', '2x/+3=0', '2x/*3=0', '2x//3=0']]

exp_list = [['x=3=0'],
            ['2x*-3=0'],
            ['2x/-3=0']]

# Quick test

# exp_list = [['x*/9=0']]

for row in exp_list:
    for exp in row:
        while True:
            print(color('***************************', 'HEADER'))
            print('->', color(exp, ['BOLD', 'HEADER']))           
            exp_controls = init_control_by_setp(exp)

            if exp_controls['result']:
                # print(exp_controls['feedback'])
                print('-> ', init_formating(exp_controls['exp']))
                break
            else:
                if exp_controls['feedback'] == 'restart':
                    print('The program', color('restarted', 'FAIL'))

                elif exp_controls['feedback']== 'abort':
                    print(color('out of the program', 'FAIL'))
                    break

                else:
                    print(exp_controls['feedback'])
                    break
    continuation = input('\n\n' + color('Press any key to continue', ['HEADER', 'ITALIC']) + ' > ')