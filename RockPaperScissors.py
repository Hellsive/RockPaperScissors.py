#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

# List of all Player types both human and robots.
class Player():
    my_move = None
    their_move = None

    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

# Human player with input.
    class HumanPlayer(Player):

        def move(self):
            show = input("Select your move: Rock, Paper, or Scissors? ")
            while show != 'rock' and show != 'paper' and show != 'scissors':
                print("Wrong input. Please select your move")
                show = input("rock, paper, scissors?")

            return (show)

#Random player that changes choice every time.
    class RandomPlayer(Player):

        def move(self):
            return random.choice(moves)

# Player that always plays rock, no matter what.
    class RockPlayer(Player):
        def move(self):
            return 'rock'

# Player that always copies the last move input by the human player.
    class ReflectPlayer(Player):
        def move(self):
            if their_move == "paper":
                return "paper"

            elif their_move == "scissors":
                return "scissors"

            else:
                return "rock"

        def learn(self, my_move, their_move):
            self.their_move = my_move

# Player that cycles through the 'moves' list in order.
    class CyclePlayer(Player):
        def move(self):
            if self.my_move == 'rock':
                return 'paper'
            elif self.my_move == 'paper':
                return 'scissors'
            elif self.my_move == 'scissors':
                return 'rock'


# Sets the win conditions of rock, paper, and scissors.
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
        (one == 'scissors' and two == 'paper') or
        (one == 'paper' and two == 'rock'))

# Game flow and input conditions.
class Game():

    def __init__(self, my_move, their_move):
        self.p1 = my_move
        self.p2 = their_move
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1_score += 1
            print (["You won!"])
        elif beats(move2, move1):
            self.p2_score += 1
            print (["You lose!"])
        elif beats(move2, move1):
            self.p2_score += 1
            print (["You lose!"])

    def play_game(self):
        print("Game start!")
        rounds = int(input("How many rounds would you like to play?"))
        for round in range (rounds):
            print ([f"The score is {self.p1_score} to {self.p2_score}"])

        if self.p1_score > self.p2_score:
            print("You win!")

        elif self.pl_score < self.p2_score:
            print("You lose!")

        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    player_types = {
        "Normal Player": Player.lower(),
        "Random Player": RandomPlayer.lower(),
        "Cycle Player": CyclePlayer.lower(),
        "Mirror Player" ReflectPlayer.lower()
    }
    game = Game(Player(), Player())
    game.play_game()