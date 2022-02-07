import datetime
import random
import json

def getQues():
    fp = open("question.json")
    content = fp.read()
    fp.close()
    questions = json.loads(content)
    return questions

def question():
    queslist = getQues()
    count = 0
    marks = 0
    choiceList=[]
    while True:
        ques = random.choice(queslist)
        quesIndex = queslist.index(ques)
        if quesIndex not in choiceList:
            choiceList.append(quesIndex)
            for q in ques:
                print("Ques:- ",q)
                ans = input("Enter your answer(in a,b,c,d): ")
                if ans == ques[q]:
                    marks+=10
                count+=1
                print()
        if count == 10:
            break
    return marks

def saveResult(name,marks):
    now = datetime.datetime.now().strftime("[%d/%m/%Y | %H:%M:%S]")
    fp = open("resultsHistory.txt",'a+')
    fp.write("\n"+now+"\n\t"+name+ " >>\t Marks obtained "+str(marks)+" out of 100\n")
    fp.close()

def getResult():
    try:
        fp = open("resultsHistory.txt")
        content = fp.read()
        fp.close()
        print(content)
    except Exception:
        print("No Records!\n")

def startingQuiz():
    while True:
        entryInput = input("\n1. Start The Quiz \n2. History \n3. Exit \nChoose either 1, 2 or 3: ")
        if entryInput == '1':
            candidateName = input("Enter Your Full Name: ")
            print("\n>> Please give the answer of each questions...\n")
            result = question()
            saveResult(candidateName,result)
            print("\n Marks Obtained: ",result,"out of 100\n")
            print("\n-----Thank You For Giving The Quiz!-----\n")
        elif entryInput == '2':
            print('\n----Quiz Result History----\n')
            getResult()
        elif entryInput == '3':
            break
        else:
            print('\nWarn - Wrong input! Please try again...\n')

if __name__ == '__main__' :
    print("======QUIZ! A MIND BUSTER======")
    startingQuiz()
    print("\n-----Thank You For Using The Quiz App!-----\n===== Design & Code By - Jatin Sharma =====")