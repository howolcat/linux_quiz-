import random
from quizpro import printquiz
score = 0



# 퀴즈목록


print('''
Linux! Quiz Time!
''')

while True:
    ans = input("What would you like to quiz? (y/n)")
    while ans in ["y","Y"]:
        qustion1 = random.randint(0,4)
        qustion2 = random.randint(0,4)
        qustion3 = random.randint(0,4)
        if len({qustion1, qustion2, qustion3}) == 3:
            for q in [qustion1, qustion2, qustion3]:
                result = printquiz(q)
                if result == True :
                    score += 1
            print(f"{score}맞추셨습니다!")
            if score == 3 :
                print("등급 A")
            elif score == 2 :
                print("등급 B")
            elif score == 1 :
                print("등급 C")
            else  :
                print("등급 F")
            break
    else :
        print("Bye bye ~")
        break







