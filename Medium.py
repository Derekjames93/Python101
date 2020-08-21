# take an input
leet = input('Enter Phrase from 21 Jump Street:')

# A -> 4
# E -> 3
# G -> 6
# I -> 1
# O -> 0
# S -> 5
# T -> 7

#convert to uppercase
leet= leet.upper()


#define an output

translation = ''

#loop over each character in input
for phrase in leet :

#replace letters if they are leet
    if phrase == 'A':
        translation += '4'
    elif phrase == 'E' :
        translation += '3'
    elif phrase == 'G' :
        translation += '6'
    elif phrase == 'I' :
        translation += '1'
    elif phrase == 'O' :
        translation += '0'
    elif phrase == 'S' :
        translation += '5'
    elif phrase == 'T' :
        translation += '7'
    else :
        translation += phrase
    






#print the translation
print(translation)