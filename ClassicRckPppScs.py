import random

def strike():
    hand = random.choice(['Rock', 'Paper', 'Scissor'])
    return hand

def convert_int(num):
    if num == '1':
        weapon = 'Rock'
    elif num == '2':
        weapon = 'Paper'
    else:
        weapon = 'Scissor'
    return weapon

def who_won(human_weapon, robot):
    if (human_weapon == 'Rock' and robot == 'Rock') or (human_weapon == 'Paper' and robot == 'Paper') or (human_weapon == 'Scissor' and robot == 'Scissor'):
        winner = 'none'
        print('Empate')
    elif (human_weapon == 'Rock' and robot == 'Scissor') or (human_weapon == 'Paper' and robot == 'Rock') or (human_weapon == 'Scissor' and robot == 'Paper'):
        winner = 'human'
        print('Ganó el humano')
    else:
        winner = 'robot'
        print('Ganó el robot')

    return winner

def query_player():
    options = ['1', '2', '3']
    human = 0
    while human not in options:
        human = input('Rock(1), Paper(2), or Scissor(3)? ')
        if human not in options:
            print('You have to type a number between 1 and 3 (1, 2 or 3).')
            print('')
    return human


print('')
print("Let's play the classic random rock paper or scissors.")
print('Whoever reaches 5 points wins.')
print('')

points_robot = 0
points_human = 0
while points_human < 5 and points_robot < 5:
    human = query_player()
    human_weapon = convert_int(human)
    robot = strike()
    print('')
    print('Human:', human_weapon)
    print('Robot:', robot)
    print('')
    winner = who_won(human_weapon, robot)
    if winner == 'human':
        points_human += 1
    elif winner == 'robot':
        points_robot += 1
    print('')
    print('Points:')
    print('Human:', points_human)
    print('Robot:', points_robot)
    print('')
    if points_human == 5:
        print('You won, Human!!')
        # break
    elif points_robot == 5:
        print('You won, Robot!!')
        # break


print('End of the game. See you soon.')
print('')