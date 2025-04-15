import random
def guessnum(n):
    need_to_guess=random.randint(1,n)
    while True:
        num=int(input('numarul de ghicit : '))
        if num==need_to_guess:
            print('Ai ghicit numarul corect')
            break

        elif num>need_to_guess:
            print('Prea mare , numarul este mai mic ')

        else:
            print('Prea mic , numarul este mai mare')



def main():
    print(guessnum(100))
if __name__=='__main__':
    main()