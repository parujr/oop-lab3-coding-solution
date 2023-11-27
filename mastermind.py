class MasterMind:

    def __get_puzzle(self, num_color, num_pos):
        import random
        answer = ''

        for i in range(0, num_pos):
            x = random.randint(1, num_color)
            answer += str(x)
        return str(answer)
    
    def __sanitize_input(self, num_color, num_pos):
        try:
            x = int(num_color)
        except ValueError:
            print(num_color, ": not valid as a value for number for colors")

        if x < 0:
            x = 1
        elif x > 8:
            x = 8

        try:
            y = int(num_pos)
        except ValueError:
            print(num_pos, ": not valid as a value for number of postions")
        
        if y < 0:
            y = 1
        elif y > 10:
            y = 10
        
        return [x, y]

    def __init__(self, num_color, num_pos):
        [self.num_color, self.num_pos] = self.__sanitize_input(num_color, num_pos)
        self.puzzle = self.__get_puzzle(self.num_color, self.num_pos)
        self.ans_list = []
        self.game_end = False

    def __get_clue(self, guess, ans):
        black = 0
        ans_list = list(ans)
        orig_len = len(ans_list)
        for i in range(len(guess)):
            if guess[i] == ans[i]:
                black += 1
        for char in guess:
            if char in ans_list:
                ans_list.remove(char)
        white = orig_len - len(ans_list)
        white -= black
        return [black, white]
    
    def __str_clue(self, hint):
        s = ""
        for i in range(0, hint[0]):
            s += '* '
        for i in range(0, hint[1]):
            s += 'o '
        return s[0:-1]

    def play(self):
        print("Here is the puzzle:", self.puzzle)
        print("Playing MM with", self.num_color, "colors and", self.num_pos, "positions")
        while (not self.game_end):
            print("What is your guess?: ", end='')
            your_try = input()
            print("Your guess is", your_try[0:self.num_pos])
            hint = self.__get_clue(your_try[0:self.num_pos], self.puzzle)
            print(self.__str_clue(hint))
            print()
            self.ans_list.append([your_try, hint])
            if hint[0] == self.num_pos:
                self.game_end = True
                print("You solve the puzzle after", len(self.ans_list), "rounds")
    
    def summarize(self):
        if not self.game_end:
            return
        for item in self.ans_list:
            print(item[0], self.__str_clue(item[1]))
    
my_game = MasterMind(10, 20)
my_game.play()
my_game.summarize()
