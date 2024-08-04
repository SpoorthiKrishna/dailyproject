def mutate(a_list):
    b_list=[]
    for i in a_list:
        new_item=i *2
        b_list.append(new_item)
    print(b_list)



mutate([1,3,4,5,6])