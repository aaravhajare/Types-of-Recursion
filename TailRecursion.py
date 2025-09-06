
def print1(n , num) :

    if n > num :
        return

    print(n)
    print1(n + 1 , num)


n = int(input("Enter a number"))
print1(1, n)