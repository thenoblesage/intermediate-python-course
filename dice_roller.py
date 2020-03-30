import random

def main():
    dicerolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    sum = 0
    for i in range (0, dicerolls):
        roll = random.randint(1, dice_size)
        sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success')
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {sum}')


if __name__ == "__main__":
    main()
