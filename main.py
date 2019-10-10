from phi import phi

x = (4*(10**3))

k = int

n = int


def suchn(k):
    counter=0
    n=0
    list = []
    while(n<=x):
        if phi(n) == phi(n+k):
            counter = counter+1
            list.append(n)
        n=n+1

    return counter, #list

def  after6(k):
    print("this is for upper limit x=",x," k=",k)
    i=0
    #the i in the for loop decides for how many values after k you want to compute
    while(i <=5):
        mod=(k+i)%6
        print (k+i," :",mod,"(mod 6):", suchn(k+i))

        i=i+1

#in the below function, replace 20 by whatever value of k you want to start from
after6(20)