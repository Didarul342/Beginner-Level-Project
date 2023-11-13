import random

while True:
    print("Rolling Dice...")

    print(f"The value is ", random.randint(1,6))

    repeat = input("Roll Dice again? 'y' for yes & 'n' for no: ")

    if repeat == 'n':
        break
