import random
from datetime import datetime

def get_random_number():
    return random.randint(5873,100000)

def addn_qs():
    num1 = get_random_number()
    num2 = get_random_number()
    print(f"What is the sum of {num1} and {num2}?")
    answer = int(input())
    if answer != (num1+num2):
        return False
    else:
        return True

def run():
    sta
    for i in range(1000):
        status = addn_qs()
        if status==False:
            print("Wrong answer, mate")
            exit(0)
        

main()