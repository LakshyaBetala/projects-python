print("Welcome to my computer quiz!")
print("+4 for each question answered correctly \n -1 for each wrong answer")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
score=0

print("lets play :)")
answer = input("what does cpu stands for? ")

if answer.lower() =="central processing unit":
    print("correct!")
    score+=4
else:
    print('incorrect')
    score=-1

answer = input("what does gpu stands for? ")

if answer.lower() =="graphical processing unit":
    print("correct!")
    score+=4
else:
    print('incorrect')
    score=-1

answer = input("what does spu stands for? ")

if answer.lower() =="supply processing unit":
    print("correct!")
    score+=4
else:
    print('incorrect')
    score=-1

answer = input("what does usb stands for? ")

if answer.lower() =="universal serial bus":
    print("correct!")
    score+=4
else:
    print('incorrect')
    score=-1

answer = input("what does cd stands for? ")

if answer.lower() =="compact disc":
    print("correct!")
    score+=4
else:
    print('incorrect')
    score-=1



print("the most important question!!!!!!!!\n")
answer = input("do you like anime?")

if answer.lower() =="yes":
    print("correct!")
    score +=4
else:
    print('incorrect')
    score-=1


print("your total score:",score)





