# Average of n input numbers
count=int(input("How many number do you want to enter: "))

sum=0

for i in range(count):
    sum=sum+int(input(f"Please enter {i+1}. number: "))
average=sum/count

print(f'{average:.2f}')
