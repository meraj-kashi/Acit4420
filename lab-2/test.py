file="python.txt"

# Reading the file
text=open(file,"rt")
line=text.read()

word=""
dic={}
count=0 #to calculate the total words

for chr in line:     
    if chr in ",:;.'!?/*()\"&\r\n[]":      #removing special characters
        chr=" "
    word+=chr


print(word)