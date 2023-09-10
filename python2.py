num=int(input('enter the number here :-'))
factorial=1
if num<0:
    print("the factorial does not exist")
elif num==0:
    print("the factorial of 0 is",1)
elif num>0:
    for i in range(1,num+1):
        factorial=factorial*i
        print("the factorial of the given number is :-",factorial)
    else:
        print("invalid number")