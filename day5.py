# # # #print average height

# # # heights=input().split(",")
# # # length=len(heights)
# # # sum=0
# # # for i in range(0,length):
# # #     sum+=int(heights[i])
# # # print("the number of student is: ",length)
# # # print("the sum of the total students is ",sum)
# # # avg=sum/length
# # # print("the average height of total student is : ",avg)
# # # print maximum number only using for loop
# # number=input().split(",")
# # for n in range(0,len(number)):
# #     number[n]=int(number[n])
# # high=0
# # for i in number:
# #     if i > high :
# #         high=i

# # print(f"the highest score is {high}")
# num=input()
# sum=0
# for i in range(0,int(num)+1):
#     if i%2==0:
#         print(i)
#         sum+=i
# # print("the even number is :", sum)
# num=int(input())
# for i in range(1,num+1):
#     if i%3==0 :
#         print("FUZZ")
#     elif i%5==0:
#         print("BUZZ")
#     elif i%3==0 and i%5==0:
#         print("FUZZ BUZZ")
#     else:
#         print(i)
import random
l=['a','b','c','d','e','f','g',]
s=['@','#','$','&']
n=['1','2','3','4']
print("Welcome to the pypassword Generator ")

# letter=int(input('how many letter would you like to choose :'))
# symbol=int(input("how many symbol would you like to choose :"))
# number=int(input("how many number would you like to choose :"))
# password=''
# for i in range(1,letter+1):
#     password+=random.choice(l)
# for i in range(1,symbol+1):
#     password+=random.choice(s)
# for i in range(1,number+1):
#     password+=random.choice(n)
# print(password)

# hard level
letter=int(input("how many letter would you like to choose :"))
symbol=int(input("how many symbol would you like to choose :"))
number=int(input("how many number would you like to choose :"))
password_list=[]
for i in range(1,letter+1):
    password_list+=random.choice(l)
for i in range(1,symbol+1):
    password_list+=random.choice(s)
for i in range(1,number+1):
    password_list+=random.choice(n)

random.shuffle(password_list)

password=""
for i in password_list:
    password+=i
print(password)






        