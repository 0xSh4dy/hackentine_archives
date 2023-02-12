print("!Welcome to Att4ck_on_tit4n!")
print("Are you just an Anime fan? Or are you even smart as Erwin Smith!!!")
print("Here's a small quiz for you!!! (PRESS ENTER TO CONTINUE!!!)")
ans=input()
print("-----------------------------------------------------------------------------------------------------")

print("1. What is the username of the current secretary of InfoSecIITR?")
ans1 = input()
if(ans1!="tit4n"):
    print("Wrong answer!!! Restart the quiz, Bye!!!")
    exit(0)

print("2. Write is his original first name ?")
ans2 = input().lower()
if(ans2!="aryaman"):
    print("Wrong answer!!! Restart the quiz, Bye!!!")
    exit(0)

print("3. What other clubs has he been a part of ?")
ans3 = input().lower()
if(ans3!="sdslabs"):
    print("Wrong answer!!! Restart the quiz, Bye!!!")
    exit(0)

print("4. He is working on a startup and is the Co-founder of the company. Write the domain name of the company")
ans4 = input().lower()
if(ans4!="strello.co"):
    print("Wrong answer!!! Restart the quiz, Bye!!!")
    exit(0)

print("5. When is his birthday? (write like this: 31February)")
ans5 = input()
if(ans5!="30January"):
    print("Wrong answer!!! Restart the quiz, Bye!!!")
    exit(0)

print("6. tit4n is too talented. He has also worked as an intern in a big company. Name that company")
ans6 = input().lower()
if(ans6!="microsoft"):
    print("Wrong answer!!! Restart the quiz, Bye!!!")
    exit(0)

print("Hmm you seem to be quite a keen detective, here's a flag for you from tit4n himself")
print("Vulntine{few_tit4ns_work_for_humanity}")