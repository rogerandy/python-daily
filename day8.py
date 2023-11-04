alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caser(start_text, shift_amount, end_direction):
    end_text = ""
    if end_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet: 
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text+= char
     
    print(f"這是{end_direction}的結果: {end_text}")

 
messger_box=True

while messger_box:
    direction = input("你要 'encode' 還是 'decode': ")
    text = input("請輸入內容: ").lower()
    shift = int(input("請輸入移位數: "))
    # shirt= shift%26
    caser(start_text=text, shift_amount=shift, end_direction=direction)

    result=input("do you want to again?")
    if result == "no":
        messger_box=False
        print("bye")
