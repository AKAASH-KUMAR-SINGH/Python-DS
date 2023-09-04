import random
n=random.randint(0,10)
guess=0
while True:
    print("I am thinking of a number(1 to 10),can you guess what it is ?")
    guess+=1
    q=int(input())
    if q==n:
        print("Yaa!,You got it",q)
        break
    elif n > q:
        print("Too Low")
    else:
        print("Too High")
print(f"GAME OVER,'You took' {guess} guesses")