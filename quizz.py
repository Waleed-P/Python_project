import time
time_remaining=60
score=0
questions=['Is python  is high level language','list is immutable','Is set has duplicate values']
answers=['yes','no','no']
print('There are 3 questions \nAnswer the qustions in the form of "yes" and "no" \nEach answer carries 10 score')
print("Total time is 60 seconds \n")
Decesion=input('Are you  ready to start :').lower()
if Decesion=='yes':
    for i in range(0,len(questions)):
        print()
        print(i+1,':',questions[i])
        starting_time=time.time()
        ans=input("Enter your answer :").lower()
        ending_time=time.time()
        time_taken=int(ending_time-starting_time)
        print('Time taken to answer=',time_taken,' seconds')
        time_remaining=time_remaining-time_taken
        
        if time_remaining<=0:
            print(" \nTIME OUT ")
            total_score=score/30*100
            print("\nYour score=",int(total_score),'%')
            exit()
        print("Remaining time=",time_remaining,'seconds')

        if ans==answers[i]:
            print("Correct answer")
            score=score+10
        else:
            print("Wrong answer",', correct answer is',answers[i])

    total_score=score/30*100
    print("\nYour score=",int(total_score),'%')

else:
    exit()