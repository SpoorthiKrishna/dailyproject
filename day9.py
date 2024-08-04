# # student_scores={
# #     "spoorthi":88,
# #     "ramya":99,
# #     "sinchana":92,
# #     "kruthika":100,
# # }
# # student_grades={}
# # # student_grades={
# # #     95-100:"outstanding",
# # #     90-94:"very good",
# # #     85-89:"good",
# # #     1-84:"better",
# # # }
# # for student in student_scores:
# #     if student_scores[student]>=95:
# #         student_grades[student]="outstanding"
# #     elif student_scores[student]>=90 and student_scores[student]<=94:
# #         student_scores[student]="very good"
# #     elif student_scores[student]>=85 and student_scores[student]<=89:
# #         student_scores[student]=" good"
# #     elif student_scores[student]<85:
# #         student_scores[student]=" not better"

# # # print(student_grades)
# # travel={
# #     "france":{"visited":["paris","delta","alpha"],"not visited":["sigma","constant"]},
# #     "germany":{"hype","light,"}
# # }
# travel_log=[
#     {
#         "city":"France",
#         "visited":5,
#         "to_visit":['Paries','dolis','taven']
#      },
#      {
#          "city":"German",
#          "visited":3,
#          "to_visit":['san francs','berlin','stattgur']
#      },
# ]

# def add_to_country(city,visited,list_of_cities):
#     new_country={}
#     new_country[city]=name
#     new_country[visited]=times
#     new_country[list_of_cities]=addlist
#     travel_log.append(new_country)

# name=input()
# times=input()
# addlist=input().split(",")


# add_to_country(city=name,visited=times,list_of_cities=addlist)
res={}
def participate(high_bid):
    high=0
    winner=""
    for bidder in high_bid:
        amount=high_bid[bidder]
        if amount > high:
            high=amount
            winner=bidder
    print(f"the winner is {winner} by bid of {high}")



check=True
while check:
    name=input("enter your name ")
    bid=int(input("your bid : $ "))
    res[name]=bid
    final=input("is there any other person to bid 'yes' or 'no' :")
    if final == 'no':
        check=False
        participate(res)
    
        

    
