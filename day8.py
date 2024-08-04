# # # def do_things(a,b):
# # #     sum=a+b
# # #     print(sum)
    

# # # do_things(2,5)
# # import math
# # def paint_calc(height,width,cover):
# #     res=(height*width)/cover
# #     final_res=math.ceil(res)
# #     print(f"you need {final_res} cans of paints")


# # test_h=int(input("enter the height of the wall : "))
# # test_w=int(input("enter the width of the wall : "))
# # coverage=5
# # paint_calc(height=test_h,width=test_w,cover=coverage)

# # check prime number
# def prime(num):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#     if is_prime:
#         print("it's prime number")
#     else:
#         print("it's not prime number")

# n=int(input("enter a number : "))
# prime(num=n)

# caeser cipher
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# def encrypt(plain_text,plain_shift):
#     cipher=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position+plain_shift
#         new_letter=alphabet[new_position]
#         cipher+=new_letter
#     print(cipher)
# def decrypt(plain_text,plain_shift):
#     caeser=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position-plain_shift
#         new_letter=alphabet[new_position]
#         caeser+=new_letter
#     print(caeser)
def ceaser(choices,plain_text,plain_shift):
    empty=""
    for letter in plain_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            if choices=="encode":
                new_position=position+plain_shift
            else:
                new_position=position-plain_shift
            new_letter=alphabet[new_position]
            empty+=new_letter 
        else:
            empty+=letter
           
    print(f"your {choices} is {empty} ")

check=True        
while check:
    user_choice=input("type 'encode' to encrypt 'decode' to decrypt :")
    text=input("your message : ").lower()
    shift=int(input("Type the shift number : "))
    shift=shift%26
    ceaser(choices=user_choice,plain_text=text,plain_shift=shift)
    res=input("do you want to continue yes or no : ")
    if res=="no":
        check=False
        print("ok, good bye ")
# if user_choice == "encode":
#     encrypt(plain_text=text,plain_shift=shift)
# else:
#     decrypt(plain_text=text,plain_shift=shift)



