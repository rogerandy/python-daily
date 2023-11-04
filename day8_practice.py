# import math

# def cans(height,weight,coverage):
#     totally=(height*weight)/coverage
#     round_up=math.ceil(totally)
#     print(f"you will need to{round_up}")

# height_H=int(input("高度多少"))
# weight_W=int(input("高度多少"))
# cover=5


# cans(height=height_H,weight=weight_W,coverage=cover)

def hello(number):
    is_num=True
    for i in range(2,number):
        if number % i ==0:
            is_num=False
    if is_num:
        print("YES")
    else:
        print("nono")

hello(53) 

