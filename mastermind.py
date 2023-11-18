import random
import copy

class Mastermind:
    def __init__(self, x:int = 6, y:int = 4):
        self.color = x
        self.position = y
        self.original = self.ramdom_original()

    def ramdom_original(self):
        original = [random.randint(1, self.color) for _ in range(self.position)]
        return original
    
    def play(self):
        print(self.original)
        print(f"Playing Mastermind with {color} colors and {position} positions")
        i = 1
        while i <= 10:
            clue = []
            guess = input("What is your guess?: ")
            print(f"Your guess is {guess}")
            temp_list = list(guess)
            num_list = [int(x) for x in temp_list]
            origin = copy.copy(self.original)
            print(num_list)
            _ = 0
            for j in range(4):
                if num_list == self.original:
                    print("correct")
                    return "correct"
                elif num_list[_] == self.original[j]:
                    clue.append('*')
                    num_list.remove(num_list[_])
                    origin.remove(origin[_])
                else:
                    if len(num_list) == 1:
                        _ = 0
                    elif _ < (len(num_list) - 1):
                        _ += 1
            for k in num_list:
                if k in origin:
                    clue.append('o')
            clue = ''.join(clue)
            print(clue)
            i += 1
        print(self.original)

color = int(input("How many color: "))
position = int(input("How many position: "))
game = Mastermind(color, position)
game.play()
