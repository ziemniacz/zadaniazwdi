def zadanie32(n: int)->bool:
    if n%2 == 0: return True
    an0 = 2
    an1 = an0 * 3 + 1
    while an1 <= n:
        if n % an1 == 0: return True
        an0 = an1
        an1 = an0 * 3 + 1
    return False

def zadanie33(n: int)->bool:
    while n > 9:
        j = n % 10
        n //= 10
        d = n % 10
        if d >= j: return False
    return True

def zadanie34(n: int)->bool:
    r = ((n%100)//10) / (n%10)
    while n > 9:
        j = n % 10
        n //= 10
        d = n % 10
        if not r == d/j: return False
        r = d/j
    return True

def zadanie35(n: int)->bool:
    n_copy = n
    length = 0
    while n_copy > 0:
        n_copy //= 10
        length += 1

    while n > 0:
        r = n % 10
        if r == length: return True
        n //= 10

    return False

def zadanie36(n: int)->bool:
    last = n % 10
    n //= 10
    while n > 0:
        if n % 10 == last: return False
        n //= 10
    return True

def zadanie27(a,b,n):
    dec = 0.1
    w = a//b
    t = w
    c,d = a,b
    while n>0:
        c = (c - d)*10
        t = c // b
        w += t*dec
        dec *= 0.1
        d = t*b
        n -= 1

    return w

def dec_to_hex(n):
    match (n):
        case 10: return 'A'
        case 11: return 'B'
        case 12: return 'C'
        case 13: return 'D'
        case 14: return 'E'
        case 15: return 'F'
        case _: return n

def zadanie66(n):
    counter = 1
    div = 1
    ncopy = n
    while ncopy // (div*16) > 0:
        ncopy //= div
        div *= 16
        counter += 1
    a = [0]*(counter)

    while counter > 0:
        smallcounter = 0
        while n - div >= 0:
            n -= div
            smallcounter+=1

        s = dec_to_hex(smallcounter)
        a[counter-1] = s
        div //= 16
        counter -= 1
    return a

def zadanie68(n):
    a = [True]*n
    a[0], a[1] = False, False
    i = 2
    while i*i < n:
        if a[i] == True:
            j = i**2
            while j < n:
                a[j] = False
                j += i
            i += 1
    return a

def silnia(n):
    if n == 0: return 1
    w = 1
    for i in range(0, n):
        w *= n-i
    return w

def kreator_tablic(pod, n):
    if pod == 1:
        a = [0] * (n+2)
        a[0] = 1
        a[1] = ','
        return a
    a = [None] * (n+2)
    a[0] = 0
    a[1] = ','
    j = 2
    dzielnik = 1
    dzielna = 0
    for i in range(n):
        dzielnik *= 10
        r = dzielnik // pod
        a[j] = r
        j += 1
        if j-2 >= n: break
        dzielna = r*pod
        dzielnik -= dzielna
    return a

def dodawanie_tablic(a, b, n):
    suma = [0] * (n+2)
    suma[1] = ','
    for i in range(0, n+2):
        if not i == 1:
            w = suma[i]+a[i]+b[i]
            if w >= 10:
                j = i
                dod = w
                k = j-1
                while True:
                    if k == 1: k = 0
                    suma[j] = dod%10
                    if suma[k] + 1 < 10:
                        suma[k] += 1
                        break
                    else:
                        j -= 1
                        k -= 1
                        dod = 10

            else: suma[i] = w
    return suma

def zadanie69(n):
    e = []
    poprzednia_tablica = dodawanie_tablic(kreator_tablic(silnia(0), n), kreator_tablic(silnia(1), n), n)
    i = 2
    for j in range(n):
        nowa_tablica = kreator_tablic(silnia(i), n)
        e = dodawanie_tablic(poprzednia_tablica, nowa_tablica, n)
        poprzednia_tablica = e
        i+=1
    return e
print(zadanie69(40))