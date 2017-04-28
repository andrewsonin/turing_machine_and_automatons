alphabet = list('1234567890qw~ert`yui<op*&:%№@!";[|\]as)(-_d=+fgh>jkl;zxc#vb^nm,./')
output = open('rules_clearance.txt', 'w', encoding='utf8')
output.write('1 $ 1 1 $\n')
for i in range(len(alphabet)):
    cur = i + 2
    output.write('1 ' + alphabet[i] + ' ' + str(cur) + ' 1 ' + alphabet[i] + '\n')
    for j in range(len(alphabet)):
        output.write(str(cur) + ' ' + alphabet[j] + ' ' + str(cur) + ' 1 ' + alphabet[j] + '\n')
        if i == j:
            output.write('r' + str(cur) + ' ' + alphabet[j] + ' ' + 'c' + ' -1 $\n')
        else:
            output.write('r' + str(cur) + ' ' + alphabet[j] + ' 0 0 ' + alphabet[j] + '\n')
    output.write(str(cur) + ' $ ' + 'r' + str(cur) + ' -1 $\n')
    output.write('c ' + alphabet[i] + ' c -1 $\n')
output.write('c $ 0 0 $')
