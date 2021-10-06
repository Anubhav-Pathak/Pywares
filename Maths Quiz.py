print("-"*28,"       Easy Math Quiz","-"*28,"Press 1 for Addition","Press 2 for Subtraction","Press 3 for Multiplication","Press 4 for Division",sep="\n",end="\n"+"-"*28+"\n")
import random
def Calculate(n):
    if n == 1: return lambda a,b: a+b
    elif n == 2: return lambda a,b: a-b
    elif n == 3: return lambda a,b: a*b
    else: return lambda a,b: a//b
Questions,Correct = 0,0
Operation = ("+","-","*","//")
while True: 
    try:
        n = int(input("Enter your choice: "))
        if n <= 4 and n > 0: 
            Questions += 1
            a,b = random.randint(0,100), random.randint(0,100)
            if n == 4: 
                while b == 0: a,b = random.randint(0,100), random.randint(0,100)
            Result = Calculate(n)(a,b)
            Answer = int(input(f"{a} {Operation[n-1]} {b} = "))
            if Result == Answer: 
                print("Correct")
                Correct += 1
            else: print("Incorrect")
        elif n == 5: break
        else: raise ValueError
    except ValueError: 
        print("Wrong Input")
        continue
    except KeyboardInterrupt: 
        print("Keyboard Interruption occured")
        continue
if Questions > 0:
    print(f"\nYou answered {Correct} out of {Questions} Questions correctly")
    print(f"Your Score: {round((Correct/Questions) * 100, 2)}%")
else: print("\nThanks for Wasting Time")