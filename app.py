print('welcome to my first game!')
name = input('what is your name? ')
age = int(input('what is your age? '))
print("hello", name, "you are", age, "years old")
health = 10
print(' you are start with', health, 'health')
if age >= 18:
    print('you are old enough to play')
    wants_to_play = input('do you want to play? ').lower()
    if wants_to_play == 'yes':
        print('lets play')

        left_or_right = input('first choice... left or right?')
        if left_or_right == 'left':
            ans = input('nice.... do you want to go cross or around ?')
            if ans =='around':
                print('you went around reached other side of the lake')


            elif ans == 'cross':
                print(' you manage the cross and bit by fish and lost 5 health')
                health -=5


            ans = input('you notice a house and river. which one you go to?')

            if ans == 'house':
                print('you go to a house and house owner don,t like you, you lose 5 health')
                health -= 5
            else:
                print(' you fell in the river and you lost')

        else:
                print(' you lost..')

    else:
            print('you are fell down and lost')

else:
     print('see you')

if age >= 14:
 print(' you can play with supervision')

else:
 print('you are not old enough to play!')