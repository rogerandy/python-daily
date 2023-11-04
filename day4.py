# import random
 
# random.seed(10)
 
# # Get the state of the generator
# state = random.getstate()
 
# print('Generating a random sequence of 3 integers...')
# for i in range(3):
#     print(random.randint(1, 1000))
 
# # Restore the state to a point before the sequence was generated
# random.setstate(state)
# print('Generating the same identical sequence of 3 integers...')
# for i in range(3):
#     print(random.randint(1, 1000))

# import random

# data = "apple, banana, orange"  # 去掉额外的空格
# data_parts = data.split(", ")  # 使用逗号和空格作为分隔符

# datas = len(data_parts)  # 计算子字符串的数量

# pay_money = random.randint(0, datas - 1)  # 随机生成一个索引
# will_pay = data_parts[pay_money]  # 使用索引访问随机选择的子字符串

# print(will_pay)
import random

paper='''
-------------   
              )
              )
              )
              )
___________ _)
'''

sissors='''

---------------
                )
    ________   _ )
    ____ )
    _____)
    )
            
'''
rock='''
--------)
        )
        )
        )
------- )

'''

# paper = "布"
# sissors = "剪刀"
# rock = "石頭"

game_image=[rock,paper,sissors]

user = int(input("你要出什麼,0=rock,1=paper,2=sissors :"))
if user>=3 or user<0:
  print("....")
else:
 print(game_image[user])
# //電腦出
 computer = random.randint(0, 2)
 print(f"電腦出:{computer}")
 print(game_image[computer])

 if user == 0 and computer == 2:
        print("you win")
 elif user == 0 and computer == 1:
        print("you are lose")
 elif user == computer:
        print("it is a draw!")
 elif user == 1 and computer == 0:
        print("you win")
 elif user == 1 and computer == 2:
        print("you are lose")
 elif user == 2 and computer == 1:
        print("you win")
 elif user == 2 and computer == 0:
        print("you are lose")

   






