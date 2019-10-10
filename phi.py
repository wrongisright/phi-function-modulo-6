from math import gcd




def phi(n):
    counter = 0
    checkint = 1

    #no. integers less than n and relatively prime to n
    while(checkint <= n):

        val = gcd(checkint,  n)

        if val==1 :
            counter=counter + 1


        checkint = checkint + 1


    return int(counter)




