
def reverse(n , num) :

    if n > num :
        return 
    reverse(n+1 , num)
    print(n)


n = int(input("enter a number"))
reverse(1, n)