# Strings
word = " Hello world"
# Changes all words in var to uppercase
word.upper

# List
#Iterable and mutated
programming_languages = ["bash", "Python" ,"HTML", "CSS", "Javascript"] #list literal
programming_languages [2] # Calls Python in the list
# whenever you give negative index[-1] it goes from the opposite end of the list

#Tuple. They cannot change.
# Iterabke abd immutable
# In order to slice a tupple you would use gps_coordinate[1:4]
    # This break it down by tge commas. Empty space infront [:4] will make it assume its starting from the 
    # of list
gps_coordinates = (33.836843 , -75.483944)

# range
numbers_from_zero_to_a_million = range (100,70,2) #range (start,stop,step(incriments)) #list literal
programming_languages [2] # Calls Python in the list

#Tuple. They cannot change.
gps_coordinates = (33.836843 , -75.483944)

# range
numbers_from_zero_to_a_million = range (100,70,2) #range (start,stop,step(incriments))

#Example 1
programming_languages = ["bash", "Python" ,"HTML", "CSS", "Javascript"]


while True :
    try:
        user_index = int(input('Number: " '))
        break
    except ValueError :
        print ('Try again!')
        
try:
    print(programming_languages[3])
except IndexError :
    print('That doesnt exist')
#Example 2
programming_languages = ["bash", "Python" ,"HTML", "CSS", "Javascript"]

n = 1

output = programming_languages[n+2]
#This will set the [3] because 1+2=[3] which will choose CSS
print(output)
