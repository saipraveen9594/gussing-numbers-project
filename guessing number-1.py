while True:
#importing random module
    import random

    #choose an upper limit and a lower limit.
    #use the int function to ensure the value entered is an integer.
    lower_limit =int(input('Enter the lower limit value:'))
    upper_limit = int(input('Enter the upper limit value:'))

    #select a random numbers between the upper and lower limit.
    #the function takes the upper limit and lower limit as parameters and picks a number between the two numbers
    #in python, variables can be declared and assigned at the same time
    random_number=random.randint(lower_limit,upper_limit)
    print('you will have to choose a number between:',upper_limit,'and',lower_limit)
    #we assign a variable 'chances' that will act as the counter for a loop
    #the user will have to input his guess so we assign his guess into a variable
    chances=0
    while chances<5:
        chances+=1
        guess=int(input('Enter your guess:'))
        if random_number==guess:
            print('guessed correctly. the number was',random_number)
            break
        elif guess<random_number:
            print('you guessed smaller number...')
        elif guess>random_number:
            print('you guessed larger number...')
        if chances==4:
            print('\n you have no chances...')
            print('\n the number was',random_number)
            print('better luck nxt time')
            break
        print('\n')
        break
