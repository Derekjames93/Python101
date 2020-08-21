count = 0

starback =  ' ' * 4

starother = ' ' * 4


while count < 10 :
    
    print(' ' * (10- count)  + ('*' * count) + ('*' * (count -1)))
    
    count = count + 1
    
    starother = starother + '*'
   
    starback = (' ' * (5- count)) + starback + '*'
    