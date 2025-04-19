import random
def guessnum(n):
    need_to_guess=random.randint(1,n)
    while True:
        num=int(input('The number:  '))
        if num==need_to_guess:
            print('You guessed correctly')
            break

        elif num>need_to_guess:
            print('To big, the number is smaller ')

        else:
            print('To small , the number is bigger')



def main():
    n=random.randint(1,100)
    print(guessnum(n))
if __name__=='__main__':
    main()