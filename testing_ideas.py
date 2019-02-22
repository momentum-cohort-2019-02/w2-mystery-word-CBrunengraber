running = True

while running:
    x = input('Please select your level of difficulty - easy, medium, or hard: ')
    print('You selected: ', x)
    if x == 'easy':
        running = False
        print("let's play!")
    if x == 'medium':
        running = False
        print("let's play!")
    if x == 'hard':
        running = False
        print("let's play!")
    if x not in ['easy', 'medium', 'hard']:     
        print('you must enter easy, medium, or hard')
