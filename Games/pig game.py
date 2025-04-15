import random
def pig():
    print("Welcome to the game of PIG!")

    begin=input('To start the game, press "Enter"').strip()
    if begin=="":
        print("Let's play!")

        target=30

        my_score=0
        computer_score=0

        while my_score<target and computer_score<target:


            print('----------------------------------------------')
            my_roll=random.randint(1,10)
            print(f"You rolled a {my_roll}")
            if my_roll==1:
                my_score=0
                print(f'You rolled a 1 , now your score is {my_score}')
            else:
                my_score+=my_roll

            computer_roll=random.randint(1,10)
            print(f"Computer rolled a {computer_roll}")
            if computer_roll==1:
                computer_score=0
                print(f'Computer score is {computer_score}')
            else:
                computer_score+=computer_roll

            print('----------------------------------------------')
            print(f'Your score is {my_score} ')
            print(f'Computer score is {computer_score}')







            if my_score>=target and my_score>computer_score:
                print('----------------------------------------------')
                print("You win!")
                break

            if computer_score>=target and computer_score>my_score:
                print('----------------------------------------------')
                print("Computer wins!")
                break







pig()