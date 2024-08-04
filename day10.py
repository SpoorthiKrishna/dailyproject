# # # # capitalize the name
# # # def cap(f_letter, l_letter):
# # #     first=f_letter.title()
# # #     last=l_letter.title()
# # #     return f"{first} {last}"

# # # print(cap("spOOrtHi","KriSHna"))

# # def leap_year(year):
# #     if year%4==0:
# #         if year%100==0:
# #             if year%400==0:
# #                 return True
# #             else:
# #                 return False
# #         else:
# #             return True
# #     else:
# #         return False


# # def day_in_month(year,month):
# #     list_month=[31,28,31,30,31,30,31,31,30,31,30,31]
# #     if month==2 and leap_year(year):
# #         return 29
# #     else:
# #         return list_month[month-1]



# # year=int(input())
# # month=int(input())
# # days=day_in_month(year,month)
# # print(days)
# def calci(num1,num2):
#     if prefer== '+':
#         return num1 + num2
#     elif prefer == '-':
#         return num1-num2
#     elif prefer == '*':
#         return num1*num2
#     elif prefer == '%':
#         return num1%num2
#     elif prefer == '/':
#         return num1/num2
#     else:
#         print("None")
    
# first=int(input("enter first number : "))
# choose=True
# while choose:
    
#     prefer=input("+\n -\n * \n % \n /\n choose operation :")
#     second=int(input("enter second number : "))
#     ret=calci(first,second)
#     print(ret)
#     chance=input(f"would you like to do operation with {ret}, type 'y' to continue, 'n' for no :")
#     if chance=='n':
#         choose=False
#     else:
#         calci(ret,second)
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

operation={'+':add,
           '-':sub,
           '*':mul,
           '/':div,}

def calculation():
    num1=float(input("enter the first number :"))

    for oper in operation:
        print(oper)
    flag=True
    while flag:
        choose=input("enter an operator to be perform : ")

        num2=float(input("enter your second number ; "))

        opertion_result=operation[choose]
        res=opertion_result(num1,num2)
        print(res)
        print(f"{num1} {choose} {num2} = {res}")
        chance2=input(f"would you like to do operation with {res}, type 'y' to continue, 'n' for no :")
        if chance2 == "y":
            num1=res
        elif chance2=='n':
            flag=False
            calculation()
        

calculation()
    



