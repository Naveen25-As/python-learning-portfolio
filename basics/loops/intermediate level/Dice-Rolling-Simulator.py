# Dice Rolling Simulator.

import random

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)

    print("🎲 You rolled:", dice)

    again = input("Roll again? (y/n): ")

    if again.lower() != "y":
        break