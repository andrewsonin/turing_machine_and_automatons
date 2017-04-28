class Tape():
    def __init__(self):
        self.cur_state = '1'
        self.cursor = 0
        self.rules = {}

    def turing(self, input_file, output_file, rule_file):
        seq = list('$' + open(input_file, 'r', encoding='utf8').read() + '$')
        self.read_rules(rule_file)
        while self.cur_state != '0':
            self.iteration(seq)
        open(output_file, 'w', encoding='utf8').write(''.join(map(str, seq)).strip('$'))

    def iteration(self, seq):
        self.cur_state, add, seq[self.cursor] = self.rules[(self.cur_state, seq[self.cursor])]
        self.cursor += int(add)

    def read_rules(self, rule_file):
        for elem in open(rule_file, 'r', encoding='utf8').readlines():
            line = elem.split()
            self.rules[(line[0], line[1])] = line[2], line[3], line[4]

my_tape = Tape()
my_tape.turing('input.txt', 'output.txt', 'rules_clearance.txt')
