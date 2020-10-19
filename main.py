# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Strings
#1
print('enter your name')
x=input()
print('hello, '+x)
########################################################################
#2
print ('the name of the first one')
first=input()
print ('the name of the second one')
second=input()

if len(first)>len(second):
    print(first +"longest name")
elif len(second) >len(first):
    print(second + "longest name")
else:
    print('equals name')
###########################################################
# #3
print('Enter your name')
name=input()
if name[0] in ('a','o','i','e','u'):
    print ('congrats,first letter of your name is a vowel')
else:
    print('your name doesnot start with a vowel')
# ######################################################################################
#4 ask the user for his name ,and tell him if the last letter is a vowel or a consonant
print('Enter your name')
name=input()
l_letter=len(name)-1
if name[l_letter] in ('a','o','i','e','u'):
    print ('last letter is a vowel')
else:
    print('last letter is a consonant')
###########################################################################
# #5
print('enter first number')
num1=int(input())
print('enter second number')
num2=int(input())
print('sum ',num1+num2)
#########################################################################
# #6
print("enter a sentence without a")
sentence=input()
if "a" not in sentence.lower():
    print (len(sentence))
else:
    print("try next time")
#####################################################################################
#7 Ask the user for his full name and check the validith of his answer:
print("print your full name ")
f_name=input()
f_l_name=f_name.split(' ')
if len(f_l_name)>2 :
    print("your name is not valid")
elif f_l_name[0].isalpha() and f_l_name[1].isalpha() and  f_l_name[0][0].isupper() and f_l_name[1][0].isupper():
    print("your name is valid")
else:
    print("your name is not valid")
###################################################################################
# #8 ask the user for a sentence,and then tekk him how many words are in it
print("enter a sentence")
sentence=input()
print(len(sentence.split()))
########################################################################################
# #9 first 2 and the last 2 chars
print("enter a string ")
str=input()
if len(str)<3:
    print('""')
else:
    print(str[:2]+str[-2:])
#####################################################################################
#10 birthday How old he turnt /will turn this year
print ("enter your birthdate with the format dd/mm/yyyy")
b_d=input()
bd=b_d.split("/")
y=int(bd[2])
print("your age is",2020-y)
##############################################################
# 11 how old is him today(hard)


