import random
choice=['rock','paper','scissors']
def user():

    user_choise=input('choose your choise(rock,paper,scissors)').lower()
    if user_choise not in choice:
        return None
    else:
        return user_choise




def computer():
    computer_choise=random.choice(choice)
    print(computer_choise)
    return computer_choise



def game():
    me=user()
    comp=computer()

    if me==comp:

         print ('draw')
    elif (me == 'rock' and comp =='scissors') or \
            (me == 'scissors' and comp =='paper') or \
            (me == 'paper' and comp =='rock'):

         print( 'win')
    else:

         print('lose')




game()
