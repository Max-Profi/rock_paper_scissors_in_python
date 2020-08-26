import random

print("Make your chose: rock, paper or scissors")

user_input = input('> ')

options = ['rock', 'paper', 'scissors']

comp_input = random.choice(options)

if user_input == comp_input:
    print(f'There is a draw. Player chose {user_input} and computer chose {comp_input}')
    
elif (user_input == 'rock' and comp_input == 'scissors') or (user_input == 'paper' and comp_input == 'rock') or (user_input == 'scissors' and comp_input == 'paper'):
         print(f'You won. The computer chose {comp_input} and lost')
         
else:
    print(f'You lost, the computer chose {comp_input}')
