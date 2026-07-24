quiz_list = []
quiz_list.append("건이는 어떤 파일에 다른사람에게도 모든 권한을 주고싶어한다 터미널에 어떤 명령어를 써야할까?")
good1 = ["chmod 777","CHMOD 777 ","Chmod 777"] #1번 문제
quiz_list.append("건이는 현재 자신이 어떤 파일에 있는지 알고싶어 한다 어떤 명령어를 써야할까?")
good2 = ["pwd","PWD"]    #2번 문제
quiz_list.append("건이는 계정을 새로 만들려고 한다 어떤 명령어를 써야할까?")
good3 = ["adduser","Adduser","ADDUSER"]   #3번 문제
quiz_list.append("건이는 전에 자신이 어떤 명령어를 써왔는지 알아보려고 한다 어떤 명령어를 써야할까?")
good4 = ["history","History","HISTORY"] #4번 문제
quiz_list.append("건이는 메모장에 쓰고싶은걸 다 쓴다음 저장하고 나가고 싶어한다 어떤 명령어를 써야할까?")
good5 = [":wq", ":WQ", "Wq"]#5번 문제



def printquiz(x):
    if x == 0:
        print(quiz_list[0])
        y = input("정답을 적어주세요 :")
        if y in good1 :
            print("정답!")
            return True
        else :
            print(f"정답은{good1} 이였습니다!")
            return False
    elif x == 1:
        print(quiz_list[1])
        y = input("정답을 적어주세요 :")
        if y in good2 :
            print("정답!")
            return True
        else :
            print(f"정답은{good2} 이였습니다!")
            return False
    elif x == 2:
        print(quiz_list[2])
        y = input("정답을 적어주세요 :")
        if y in good3 :
            print("정답!")
            return True
        else :
            print(f"정답은{good3} 이였습니다!")
            return False
    elif x == 3:
        print(quiz_list[3])
        y = input("정답을 적어주세요 :")
        if y in good4 :
            print("정답!")
            return True
        else :
            print(f"정답은{good4} 이였습니다!")
            return False
    elif x == 4:
        print(quiz_list[4])
        y = input("정답을 적어주세요 :")
        if y in good5 :
            print("정답!")
            return True
        else :
            print(f"정답은{good5} 이였습니다!")
            return False
