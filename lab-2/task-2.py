'''
ACIT4420-Problem_solving_with_scripting
Lab-2 Task-2
Student: Meraj Mostmand Kashi,s356478
'''

file="python.txt"

# Reading the file
text=open(file,"rt")
line=text.read()

new_text=""
word=""
dic={}

for chr in line:     
    if chr in ",:;.'!?/*()\"&\r\n[]":      #removing special characters
        chr=" "
    new_text+=chr

for chr in new_text:        #reading characters from new text
    if chr!=" ":      #reading word
        word+=chr
    elif chr==" ":      #end of the word. put the word in the dictionary
        if word in dic:
            dic[word]+=1        #increase count of the word
        else:
            dic.update({word:1})        #put new word in the dictionary 
        word=""

for key in dic:     #print the result
    if dic[key]>3:
        print(f"{key} : {dic[key]}")


        



