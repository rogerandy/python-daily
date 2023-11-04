from game import data
import random



score=0
roger_is_handsome=True
account_b=random.choice(data)




while roger_is_handsome:
    def compare(account):
        account_name=account['name']
        account_description=account['description']
        account_country=account['country']
        return f"{account_name},{account_description}  form  {account_country}"

    def check_answer(guess,a_followers,b_followers):
        if a_followers>b_followers:
            if guess == "a":
                return "a"
            else:
                return "b"



    account_a=account_b
    account_b=random.choice(data)

    while account_a==account_b:
        account_b=random.choice(data)

    print(f"compare A {compare(account_a)}")
    print("-----------")
    print("vs")
    print("-----------")
    print(f"against B {compare(account_b)}")

    guess=input("what is your answer??'a','b'")

    a_followers=account_a['follower_count']
    b_followers=account_b['follower_count']

    is_correct=check_answer(guess,a_followers,b_followers)





    if is_correct :
        score+=1
        print(f"you are right   {score}")
    else:
        print(f"yor are wrong,  {score}")
        break

