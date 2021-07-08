"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import sys

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# parent class for other player classes
class Player:
    my_move = None
    their_move = None

    def move(self):
        # this sets the index of the moves to 0
        return moves[0]

    def learn(self, my_move, their_move):
        pass


# computer class for randomized moves
class RandomPlayer(Player):
    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
        return self.my_move


# users player class
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, or scissors? > ").lower()
            if move in moves:
                return move
            print("Yikes! Please try again. ")


# computer class to reflect user class input
class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


# computer class that cycles through the move list in order
class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def valid_input(prompt):  # input validation
    while True:
        response = input(prompt)
        if response in ["y", "n"]:
            break
        else:
            print("Sorry, I don't understand.\n")


class Game:
    """
    Sets the players scores
    Args:
        0 = score is none
    Objects:
            Represent the players
    """
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")
        """ this if statement stores the
            players scores and increments it
            after each win in a round
        """
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1_score += 1
            print("PLayer 1 won! \n")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 won! \n")
        else:
            print("A tie!\n")
        """ these print funtions return players scores
            after each win/lose """
        print(f"PLayer 1 score: {self.p1_score}")
        print(f"Player 2 score: {self.p2_score}\n")

    def play_game(self):
        print("Game start!")
        for round in range(1, 6):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!\n")
        print(f"Your score: {self.p1_score} Opponents score: {self.p2_score} ")
        if self.p1_score > self.p2_score:
            print("Yay! You're the winner.\n ")
        elif self.p1_score < self.p2_score:
            print("Oh no...  You lost.\n ")
        else:
            print("It's a tie! There's no winner.")

        response = valid_input("Would you like to again?\n"
                               "Enter 'y' for yes.\n"
                               "Enter 'n' for no .\n")
        if response == 'y' in response:
            print("Awesome! Restarting game now.")
            game.play_game()

        elif response == 'n' in response:
            print("That's OK. Thank you for playing!")
            sys.exit()


def startGame():
    players = {
        '1': RandomPlayer(),
        '2': ReflectPlayer(),
        '3': CyclePlayer()
    }

    p1 = HumanPlayer()
    p2 = None

    while True:
        opponent = input("""Select opponent:
            1 - Random Player:
            2 - Reflect Player:
            3 - Cycle Player: \n""")

        if opponent in players:
            p2 = players[opponent]
            break
        print("Invalid opponent, please try again. \n")

    game = Game(p1, p2)
    game.play_game()


if __name__ == '__main__':
    startGame()
