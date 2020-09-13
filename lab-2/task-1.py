'''
ACIT4420-Problem_solving_with_scripting
Lab-2 Task-1
Student: Meraj Mostmand Kashi,s356478
'''
print("Welcome to My Calender!")

week_days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
dic={}      #Define a clean dictionary

while True:
    print("s - Store Program\r\nl - List daily program\r\nx - Exit")
    action=input("Select from list: ")
    if action=="s":     #Storing procedure
        day=input("Which day? ").lower()        #normalize input 
        if day not in week_days:
            print("Invalid week day")
            day=input("Which day? ").lower()
        time=int(input("Which time: "))
        if time<0 or time>24:
            print("Invalid time")
            time=int(input("Which time: "))
        if time==24:        #clock 00:00 and 24:00 are same!
            time=0
        program=input("What is your program?")
        if day in dic:      #update dictionary if a day planned before
            dic[day][time]=program
        else:       #create new key/value for new day
            dic.update({day:{time:program}})
       
    elif action=="l":       #Loading plan procedure
        day=input("Which day? ").lower()
        if day not in week_days:
            print("Invalid week day")
            day=input("Which day? ").lower()
        if day in dic:
            for i in range(24):     #loop to find plan from the dictionary and print out
                if i in dic[day]:
                    print(f"{i}:00 : {dic[day][i]}")
                else:
                    print(f"{i}:00")
        else:       #If no plan found for the day:
            print(f"No Plan found for {day}.")

    elif action=="x":       #Procedute to exit the program
        break

print("Thank you and Goodbye!")

        
