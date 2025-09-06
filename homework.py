
def negative(n) :
    n = int(input("enter a number"))

    if n > 0 :
        print("positive") 
        negative(n)

    elif n == 0 :
        print("Zero")
        negative(n)

    elif n < 0 :
        print("Negative")

negative(5)