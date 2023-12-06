import random
import copy

class Mastermind:
    def __init__(self, x: int = 6, y: int = 4):
        # Initialize Mastermind game with specified color and position parameters
        self.color = x
        self.position = y
        # Generate a random original code for the player to guess
        self.original = self.random_original()

    def random_original(self):
        # Generate a random list of numbers representing the original code
        original = [random.randint(1, self.color) for _ in range(self.position)]
        return original

    def play(self):
        # Display the original code (for debugging purposes)
        print(self.original)
        # Inform the player about the game settings
        print(f"Playing Mastermind with {self.color} colors and {self.position} positions")
        i = 1
        while i <= 10:
            clue = []
            # Get the player's guess
            guess = input("What is your guess?: ")
            # Check if the guess has the correct number of positions
            if len(guess) != self.position:
                raise ValueError(f'Guess must have {self.position} positions')
            temp_list = list(guess)
            # Convert the guess into a list of integers
            num_list = [int(x) for x in temp_list]
            # Validate that each number in the guess is within the valid range
            for num in num_list:
                if num not in range(1, self.color + 1):
                    raise ValueError('Invalid color')
            print(f"Your guess is {guess}")
            # Create a copy of the original code for comparison
            origin = copy.copy(self.original)
            print(num_list)
            _ = 0
            for j in range(self.position):
                # Check if the entire guess is correct
                if num_list == self.original:
                    print("Correct!")
                    return "Correct"
                # Check for correct color and position
                elif num_list[_] == self.original[j]:
                    clue.append('*')
                    num_list.remove(num_list[_])
                    origin.remove(origin[_])
                else:
                    # Adjust the index for the next iteration
                    if len(num_list) == 1:
                        _ = 0
                    elif _ < (len(num_list) - 1):
                        _ += 1
            # Check for correct color but wrong position
            for k in num_list:
                if k in origin:
                    clue.append('o')
            # Combine the clue symbols and display
            clue = ''.join(clue)
            print(clue)
            i += 1
        # Inform the player about the correct code if they run out of turns
        print("Sorry, you're out of turns. The correct answer was:", self.original)

# Main loop for playing the game
while True:
    color = int(input("How many colors: "))
    position = int(input("How many positions: "))
    # Create a new instance of the Mastermind game
    game = Mastermind(color, position)
    # Start the game
    game.play()
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing! Goodbye!")
        break
