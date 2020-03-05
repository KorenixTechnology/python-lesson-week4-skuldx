def hw_week4(name, age):
    # Your code here
    
    # For interactive input
    #name = input('Please input your name:')
    #age = input('Please input your age:')

    if name == 'Alice':
        print('Hi,Alice.')
    elif int(age) < 12:
        print('You are not Alice, kiddo.')
    
    elif int(age) > 2000:
        print('Unlike you, Alice is not an undead, imortal vampire.')
    
    elif int(age) > 100:
        print('You are not Alice, grannie.')
    else:
        print('No suitable result, program ends')


if __name__ == '__main__':
    hw_week4('Alice', 200)
