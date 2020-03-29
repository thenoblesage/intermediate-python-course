import random

def main():
    dicerolls = 2
    sum = 0
    for i in range (0, dicerolls):
        roll = random.randint(1, 6)
        sum += roll
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {sum}')


if __name__ == "__main__":
    main()
