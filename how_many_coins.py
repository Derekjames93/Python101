print ('You have 0 coins')
answer = 'yes'
coins = 0

how_many = f"You have {coins} coins"


while answer == 'yes' :

    answer = input('Do you want another?')
    coins = coins + 1
    how_many = f"You have {coins} coins"
    print(how_many)
    
print ('Bye')
