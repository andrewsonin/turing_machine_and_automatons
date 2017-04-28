from time import sleep


class Wolfram():
    def __init__(self, arg=0):
        arg = bin(arg)[2:][-1::-1] + '0' * 7
        self.rules = {}
        p = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    self.rules[(i, j, k)] = int(arg[p])
                    p += 1

    def iterate(self, seq):
        len_seq = len(seq)
        new_states = [0] * len_seq
        while True:
            print(' '.join(map(str, seq)))
            for i in range(len_seq):
                j = (lambda x: -1 if x == len_seq - 1 else x + 1)(i)
                new_states[i] = self.rules[seq[i-1], seq[i], seq[j]]
            seq = new_states
            sleep(0.3)

automaton = Wolfram(110)
automaton.iterate(list(map(int, '00000000000100000000000')))
