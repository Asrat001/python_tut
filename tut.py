def mytutorial(n):
    """ trying to display a fabinach sequense of n """
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a+b


mytutorial(9)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('do you like to quit ?', 1)
