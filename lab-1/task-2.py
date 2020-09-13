# This script ask user to enter a name and number of cookies
# script will check the number of cookies and response to the user
name=input("Please enter your name: ")
number=int(input("Please enetr number of your cookies: "))

print(f'Hi {name}!')

if 1<number<10 :
    print('Are you sure it is enough? ')
elif 10<=number<20:
    print('I agree cookies are delicous!')
elif 20<=number<51:
    print('Be careful, it’s getting too much.')
elif number>50:
    print('No way, it’s getting too much’ and modify the value to be 50')
else:
    print('Something must be wrong, I give you 10 cookies')