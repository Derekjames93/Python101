
# Cat_day var ask for input number from user
cat_day = input('Whats the name of the day of the week?')
# Set Cat_day var that translates the user string number input to integer
cat_day = int(cat_day)

if cat_day == 1:
    print('It is Monday')
elif cat_day == 2:
    print('It is Tuesday')
elif cat_day == 3:
    print('It is Wednesday')
elif cat_day == 4:
    print('It is Thursday')
elif cat_day == 5:
    print('It is Friday')
elif cat_day == 6:
    print('It is Saturday')
elif cat_day == 7 :
    print('It is Sunday')
else:
    print('This is not a day')


