# Simulate a sports tournament
# Taken and adapted from CS50x (David J. Malan)

import csv
import sys
import random
import argparse

# Number of simulations to run
N = 1000


def main(arguments):

    teams = []
    # TODO: Read teams into memory from file
    # maybe use csv reader (try google)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="csv file with team ratings to use, must contain 2^k teams")
    return parser.parse_args()


if __name__ == "__main__":
    # args = parse_command_line()
    # main(args)
    winner = simulate_round([{
        'rating': 100,
        'name': 'Australia'
    }, {
        'rating': 500,
        'name': 'England'
    }, {
        'rating': 100,
        'name': 'China'
    }, {
        'rating': 500,
        'name': 'Germany'
    }])
    print(winner)

