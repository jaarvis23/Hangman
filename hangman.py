import random
answerlist=['hello','world','anushka']
random.shuffle(answerlist)
answer=list(answerlist[0])
display=[]
display.extend(answer)
for i in range(len(display)):
    display[i]='_'
print(" ".join(display))
print()
count=0
while count<len(answer):
    print("count =",count)
    guess=input("enter a character")
    for i in range(len(answer)):
        if answer[i]==guess:
            display[i]=guess
            count=count+1
    print(" ".join(display))
    print()
print("wll done!!! you guessed the word succesfully")     
     
     
     
    

               
