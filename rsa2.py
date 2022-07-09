#Josue Francisco Carpio Peña
#Marcia Luigina Montenegro Cavagnaro 
#Joaquin Muñoz


import random
from hashlib import sha1


S=40
def EUCLIDES(a, b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a % b)


def EUCLIDES_EXTEND(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, dx, dy) = EUCLIDES_EXTEND(b, a % b)
        (x, y) = (dy, dx - a // b * dy)
        return (d, x, y)


def INVERSA(a, n):
    (mcd, x, y) = EUCLIDES_EXTEND(a, n)
    if mcd == 1:
        return x % n
    else:
        return None

def RANDOM(min, max):
    return random.randint(min, max)

def EXP_MOD(a, x, n):
    c = a % n
    r = 1
    while x > 0:
        if x % 2 == 1:
            r = (r * c) % n
        c = (c * c) % n
        x = x // 2
    return r


def RANDOMBITS(b):
    max = pow(2, b) - 1
    n = RANDOM(0, max)
    m = pow(2, b - 1) + 1
    n = n | m
    return n

def EXP_MODBITS(x, y, z):
    c = 0
    d = 1
    n = y.bit_length()
    for i in range(n):
        c = 2 * c
        d = (d * d) % z
        if y & 2 ** (n - 1):
            c += 1
            d = (d * x) % z
        y = y << 1
    return d        

def POW_MOD(a, x, n):
    c = a % n
    r = 1
    
    while(x > 0):
        if((x % 2) != 0):
            r = (r * c) % n
        
        c = (c * c) % n
        x = int(x / 2)
    
    return r

def ES_COMPUESTO(a, n, t, u):
    x = POW_MOD(a, u, n)

    if (x == 1 or x == n - 1):
        return False

    for i in range(1,t,1):
        x = POW_MOD(x, 2, n)
        if (x == n - 1):
            return False

    return True



def random_primos(b):
    s = S
    n = RANDOMBITS(b)
    while (not MILLER_RABIN(n, s)):
        n += 2
  
    return n


def MILLER_RABIN(n, s):
    t = 0
    u = n - 1
    while (u % 2 == 0):
        u = u / 2
        t = t + 1

    j = 1
    while (j < s):
        a = RANDOM(2, n - 1)
        if (ES_COMPUESTO(a, n, t, u)):
            return False
            
        j += 1

    return True



#---------------------RSA----------

def RSA_KEY_GENERATOR(bits):
    arg = bits // 2
    p = random_primos(arg)
    q = random_primos(arg)
    while p == q:
        q = random_primos(arg)

    n = p * q
    phiN = (p - 1) * (q - 1)
    
    e = RANDOMBITS(bits)
    while EUCLIDES(e, phiN) != 1:
        e = RANDOMBITS(bits)
    
    d = INVERSA(e, phiN)
    return (e, n), (d, n)

def cifrado(m, k: tuple):
    arg1, arg2 = k
    return EXP_MOD(m, arg1, arg2)


#-------------------------ATAQUES----------

#----ataque 1---------
def primos(n):
    primes = ()
    for i in range(1, n):
        if EUCLIDES(i, n) != 1 and MILLER_RABIN(i, 500):
            primes += (i,)
            if len(primes) == 2:
                break

    return primes

def primer_ataque():
    e = 65537
    n = 999630013489
    P = e, n
    c = 747120213790

    first, second = primos(n)
    
    phiN = (first - 1) * (second - 1)
    S = INVERSA(e, phiN), n

    m = cifrado(c, S)
    cx = cifrado(m, P)

    print("m: ",m)
    print("c: ",cx)
    print("P(m):c= ",c==cx)

#---------ataque 2--------


def segundo_ataque():
    e = 7
    n = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
    P = e, n
    c = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
    
    e_ = 11
    P_ = (e_, n)
    c_ = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

    if (EUCLIDES(e, e_ == 1) and EUCLIDES(c_, n)):
        

        z, x, y = EUCLIDES_EXTEND(e, e_)

        a = EXP_MOD(INVERSA(c, n), -x, n) if x < 0 else EXP_MOD(c, x, n)
        b = EXP_MODBITS(INVERSA(c_, n), -y, n) if y < 0 else EXP_MODBITS(c_, y, n)

        m = (a * b) % n
        cx = cifrado(m, P)

        
        print("m: ",m)
        print("cx: ",cx)
        print("c: ",c)
        print("cx=c",cx==c)
    else:
        print("useless!")

#---------------ataque 3-------------
def tercer_ataque():
    k = 32
    P, S = RSA_KEY_GENERATOR(k)
    _, n = P
    M =b'Hello World!'

    h = sha1()
    h.update(M)
    m = int(h.hexdigest(), 16)
    m %= n

    senal = cifrado(m, S)
    u = cifrado(senal, P)

    
    print("M: ",M)
    print("m: ",m)
    print("Senal: ",senal)
    print("u: ",u)
    print("u=m: ",u==m)


print("Este es el primer ataque!--------------")
primer_ataque()
print()
print("Este es el segundo ataque!--------------")
print()
segundo_ataque()
print()
print("Este es el tercer ataque!--------------")
tercer_ataque()
