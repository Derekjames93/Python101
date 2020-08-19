# Prompt user for total bill then convert bill to an int
bill_user = input("What was your total bill? ")
bill_user = int(bill_user)
number_people = input(" How many people will you split with ")
number_people=int(number_people)
#Prompt user for the level of service
level_of_service = input("Was the service good, fair, or bad? ")
#tip amounts
good_tip = .20 
fair_tip = .15
bad_tip = .10 
# create a function to decide the tip amount. Make sure to use return statement in functions
def tip_amount ():
    if level_of_service == "good" :
        return(good_tip * bill_user)
    elif level_of_service == "fair" :
        return(fair_tip * bill_user)
    elif level_of_service == "bad" :
        return(bad_tip * bill_user)
    else :
        return("No tip")
# Create a new variable tip to store the function
tip = tip_amount()
total_amount = (tip + bill_user) / number_people
print(total_amount)

