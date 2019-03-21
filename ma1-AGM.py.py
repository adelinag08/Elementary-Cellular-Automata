
class CA:

    def __init__(self, rule, init_state='0'*20+'1'+'0'*20):

        self.rule = format(rule, '08b')
        self.current_state = init_state

    def state(self):

        return self.current_state
        pass

    def next(self):

        rules = {
            "111": self.rule[0],
            "110": self.rule[1],
            "101": self.rule[2],
            "100": self.rule[3],
            "011": self.rule[4],
            "010": self.rule[5],
            "001": self.rule[6],
            "000": self.rule[7]
        }
        self.current_state = '0' + self.current_state + '0'
        self.c_state = ''
        for i in range(len(self.current_state)-1):
            if self.current_state[i:i+3] in rules:
                self.c_state = self.c_state + rules[self.current_state[i:i+3]]
        self.current_state = self.c_state

        return self.c_state

    def run(self, num=18):

        print(self.current_state.replace("0", " ").replace("1", "*"))
        while num <=18 and num>=1:
            print(self.next().replace("0", " ").replace("1", "*"))
            num -=1
ca = CA(90)
ca
