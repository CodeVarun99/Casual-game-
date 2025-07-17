'''
game to play

'''

def game(a):
    import random
    b = random.randint(1,1000)
    c = random.randint(1,1000)
    
    if b>a>c or c>a>b:
        d = random.randint(1,100)
        print(f'You WON, your new score is {d}')
        return d
    else:
        print('You LOSE, new no score generated')
        return 0

num = int(input('Enter a number between 1 to 1000 to play the game: '))
s = game(num)
print(f'current score is {s}')
with open('project1.txt', 'a+') as ps:
    ps.seek(0)
    k = ps.read().strip()
    
    if k:
        l = int(k)
        print(f'Previous high score is {l}')
    else:
        l = 0
        print(f'Previous high score is {l}')
    
if s > l :
    print(f'New high score {s} is achieved')
    with open('project1.txt','w') as file:
        file.write(str(s))


