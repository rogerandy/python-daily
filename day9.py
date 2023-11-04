bids = {}

is_bid_finished = False

while not is_bid_finished:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = float(price)  # 將出價轉換為浮點數
    should_again = input("Do you want to enter another bid? (yes/no) ")
    if should_again.lower() == "no":
        is_bid_finished = True

# 找到最高出價者
highest_bid = 0
winner = ""
for bidder, bid_amount in bids.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The highest bidder is {winner} with a bid of ${highest_bid}")
