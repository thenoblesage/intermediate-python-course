import random

def main():
    dicerolls = 2
    sum = 0
    for i in range (0, dicerolls):
        roll = random.randint(1, 6)
        sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == 6:
            print(f'You rolled a {roll}! Critical Success')
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {sum}')


if __name__ == "__main__":
    main()
