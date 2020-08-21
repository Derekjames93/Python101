#height = input('What is the height of the box? ')
#width = input('what is the width of the box? ')
num = 0
while True :
    height = input('What is the height of the box? ')
    width = input('what is the width of the box? ')
    try :   
        num = int(input('Give me a number please:'))
        height = int(height)
        width = int(width)
        break
    except ValueError :
        print('Please enter a value number!')
    except :
        print ('Something')



count = 0
print('*' * width)


while count < height - 2:

    print('*' + (' ' * (width - 2)) + '*')
    count = count + 1
    

print('*' * width)