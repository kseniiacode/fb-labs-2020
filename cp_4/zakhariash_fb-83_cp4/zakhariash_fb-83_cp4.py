import random
import math


def isPrime(p):
    b = 10
    for i in [2, 3, 5, 7, 11]:
        if math.gcd(i, p) > 1:
            #print('Divisible by {}'.format(i))
            return 0
    d = p - 1
    s = 0
    while d%2 == 0:
        s += 1
        d /= 2
    d = int(d)
    for i in range(5):
        x = random.randint(2, p-1)
        if math.gcd(x, p) > 1:
            #print('MillerRabin test is failed')
            return 0
        else:
            if pow(x, d, p) != 1 and pow(x, d, p) != p-1:
                isprimenum = 0
                for r in range(1, s):
                    xr = pow(x, d*(2**r), p)
                    if xr == 1:
                        #print('MillerRabin test is failed')
                        return 0
                    if xr == p-1:
                        isprimenum = 1
                        break
                if not isprimenum:
                    #print('MillerRabin test is failed')
                    return 0
    return 1


def findPrime (amountbits):
    p, m0 = 0, 0
    used_x = []
    n0 = int(('0b1' + '0'*(amountbits - 2) + '1'), 2)
    n1 = int(('0b' + '1'*amountbits), 2)
    while (p == 0):
        x = random.randint(n0, n1)
        while x in used_x:
            x = random.randint(n0, n1)
        used_x.append(x)
        print(len(used_x))
        if(x%2 == 0):
            m0 = x+1
        else:
            m0 = x
        for i in range(int((n1 - m0)/2)):
            if isPrime(m0 + 2*i):
                p = m0 + 2*i
                break
    print(p)
    return p

findPrime(80)


print('finished')

