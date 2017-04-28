alphabet = list('1234567890qwertyuiop[]asdfghjkl;zxcvbnm,./')
output = open('rules_transfer.txt', 'w', encoding='utf8')
for i in range(len(alphabet)):
    output.write('1 ' + str(alphabet[i]) + ' ' + str(i + 2) + ' ' + '1 $\n')
    for elem in alphabet:
        output.write(str(i + 2) + ' ' + elem + ' ' + str(i + 2) + ' ' + '1' + ' ' + elem + '\n')
    output.write(str(i + 2) + ' ' + '$ ' + '0 0 ' + alphabet[i] + '\n')
output.write('1 $ 1 1 $')
