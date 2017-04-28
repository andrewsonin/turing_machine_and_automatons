alphabet = list('1234567890qw~ert`yui<op*&:%№@!";[|\]as)(-_d=+fgh>jkl;zxc#vb^nm,./')
output = open('rules_delete_a.txt', 'w', encoding='utf8')
output.write('1 $ 1 1 $\n')
for i in range(len(alphabet)):
    cur = alphabet[i]
    if cur != 'a':
        output.write('1 ' + cur + ' 1 1 ' + cur + '\n')
        output.write('2 ' + cur + ' ' + str(i + 3) + ' 1 $\n')
        output.write(str(i + 3) + ' $ 2 -1 ' + cur + '\n')
        output.write('-1 ' + cur + ' ' + str(-i - 2) + ' 1 $\n')
        output.write(str(-i - 2) + ' $ 2 -1 ' + cur + '\n')
    else:
        output.write('1 a 2 -1 $\n')
output.write('2 $ -1 -1 $\n')
output.write('-1 $ 0 0 $')
