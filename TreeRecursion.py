
def reverse(n , num) :

    if n<1 or n>num :
       return
    
    print(n)
    reverse(n-1 ,num)
    print(n)

n = int(input("enter a number"))
reverse(n, n)