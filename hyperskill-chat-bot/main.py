def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I am a chat bot.')
    print('I was created by Ankush in ' + birth_year + '.')


def remind_name():
    print()
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')
    print()


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")
    print()


def count():
    print('Now I will prove to you that I can count to any number you want.')
    print("Enter any number.")

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1
    print()


def test():
    print("Let's test your programming knowledge.")
    print()
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    print()
    print("Chose the correct option.")
    print()

def ans():
    while input() != '2':
        print("Oops! That's not the right answer. Keep trying.")
        print()



def end():
    print('Yayy!!! You got the right answer.')
    print()
    print('Congratulations, have a nice day!')


greet('Silent', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
ans()
end()
